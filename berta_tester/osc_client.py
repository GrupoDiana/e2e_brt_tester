from __future__ import annotations

import os
import queue
import subprocess
import threading
import time
from contextlib import AbstractContextManager
from dataclasses import dataclass
from typing import Any, Callable

try:
    from pythonosc import dispatcher, osc_message_builder, osc_server
except ImportError as error:  # pragma: no cover - depends on local environment
    raise ImportError(
        "Missing dependency 'python-osc'. Install it with: pip install python-osc"
    ) from error

from berta_tester.app_config import (
    BERTA_OSC_IP_ENV_VAR,
    BERTA_OSC_PORT_ENV_VAR,
    DEFAULT_BERTA_OSC_IP,
    DEFAULT_BERTA_OSC_PORT,
    DEFAULT_OSC_CONNECT_MAX_ATTEMPTS,
    DEFAULT_OSC_CONNECT_RETRY_WAIT_SECONDS,
    DEFAULT_OSC_STARTUP_TIMEOUT_SECONDS,
    DEFAULT_TESTER_OSC_IP,
    DEFAULT_TESTER_OSC_PORT,
    OSC_CONNECT_MAX_ATTEMPTS_ENV_VAR,
    OSC_CONNECT_RETRY_WAIT_SECONDS_ENV_VAR,
    OSC_STARTUP_TIMEOUT_ENV_VAR,
    TESTER_OSC_IP_ENV_VAR,
    TESTER_OSC_PORT_ENV_VAR,
)


@dataclass(frozen=True)
class OscEndpoint:
    ip: str
    port: int


@dataclass(frozen=True)
class OscMessage:
    address: str
    arguments: tuple[Any, ...]

    def __str__(self) -> str:
        if not self.arguments:
            return self.address
        return f"{self.address} {' '.join(map(str, self.arguments))}"


@dataclass(frozen=True)
class OscVerificationResult:
    connected: bool
    version: str
    connect_reply: OscMessage
    ping_reply: OscMessage
    version_reply: OscMessage
    berta_endpoint: OscEndpoint
    tester_endpoint: OscEndpoint


def _read_int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"Environment variable {name} must be an integer") from error


def _read_float_env(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"Environment variable {name} must be a number") from error


def get_berta_endpoint_from_env() -> OscEndpoint:
    return OscEndpoint(
        ip=os.getenv(BERTA_OSC_IP_ENV_VAR, DEFAULT_BERTA_OSC_IP),
        port=_read_int_env(BERTA_OSC_PORT_ENV_VAR, DEFAULT_BERTA_OSC_PORT),
    )


def get_tester_endpoint_from_env() -> OscEndpoint:
    return OscEndpoint(
        ip=os.getenv(TESTER_OSC_IP_ENV_VAR, DEFAULT_TESTER_OSC_IP),
        port=_read_int_env(TESTER_OSC_PORT_ENV_VAR, DEFAULT_TESTER_OSC_PORT),
    )


def get_startup_timeout_from_env() -> float:
    return _read_float_env(
        OSC_STARTUP_TIMEOUT_ENV_VAR, DEFAULT_OSC_STARTUP_TIMEOUT_SECONDS
    )


def get_connect_retry_wait_from_env() -> float:
    retry_wait_seconds = _read_float_env(
        OSC_CONNECT_RETRY_WAIT_SECONDS_ENV_VAR,
        DEFAULT_OSC_CONNECT_RETRY_WAIT_SECONDS,
    )
    if retry_wait_seconds <= 0:
        raise ValueError(
            f"Environment variable {OSC_CONNECT_RETRY_WAIT_SECONDS_ENV_VAR} must be > 0"
        )
    return retry_wait_seconds


def get_connect_max_attempts_from_env() -> int:
    max_attempts = _read_int_env(
        OSC_CONNECT_MAX_ATTEMPTS_ENV_VAR,
        DEFAULT_OSC_CONNECT_MAX_ATTEMPTS,
    )
    if max_attempts < 1:
        raise ValueError(
            f"Environment variable {OSC_CONNECT_MAX_ATTEMPTS_ENV_VAR} must be >= 1"
        )
    return max_attempts


MessagePredicate = Callable[[OscMessage], bool]


class OscClient(AbstractContextManager["OscClient"]):
    def __init__(self, berta_endpoint: OscEndpoint, tester_endpoint: OscEndpoint) -> None:
        self.berta_endpoint = berta_endpoint
        self.tester_endpoint = tester_endpoint
        self._messages: queue.Queue[OscMessage] = queue.Queue()
        self._dispatcher = dispatcher.Dispatcher()
        self._dispatcher.set_default_handler(self._handle_message)
        self._server = osc_server.ThreadingOSCUDPServer(
            (tester_endpoint.ip, tester_endpoint.port), self._dispatcher
        )
        self._server_thread = threading.Thread(
            target=self._server.serve_forever,
            name="berta-osc-listener",
            daemon=True,
        )

    def __enter__(self) -> "OscClient":
        self.start()
        return self

    def start(self) -> None:
        if not self._server_thread.is_alive():
            self._server_thread.start()

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()

    def close(self) -> None:
        self._server.shutdown()
        self._server.server_close()
        if self._server_thread.is_alive():
            self._server_thread.join(timeout=1.0)

    def disconnect_safely(self, timeout: float = 1.0) -> None:
        """Best-effort unsubscribe from BeRTA updates before closing."""
        try:
            self.request_reply(
                "/control/disconnect",
                "/control/disconnect",
                timeout=timeout,
                retry_interval=timeout,
            )
        except Exception:
            return

    def _handle_message(self, address: str, *arguments: Any) -> None:
        self._messages.put(OscMessage(address=address, arguments=tuple(arguments)))

    def drain_messages(self) -> None:
        """Remove stale messages so a new request cannot be satisfied by old data."""
        while True:
            try:
                self._messages.get_nowait()
            except queue.Empty:
                return

    def send(self, address: str, *arguments: Any) -> None:
        """Send an OSC message from the same UDP port used for replies."""
        builder = osc_message_builder.OscMessageBuilder(address=address)
        for argument in arguments:
            builder.add_arg(argument)
        message = builder.build()
        self._server.socket.sendto(
            message.dgram,
            (self.berta_endpoint.ip, self.berta_endpoint.port),
        )

    def wait_for_message(
        self,
        address: str,
        timeout: float,
        predicate: MessagePredicate | None = None,
    ) -> OscMessage:
        deadline = time.monotonic() + timeout

        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError(f"Timed out waiting for OSC message: {address}")

            try:
                message = self._messages.get(timeout=remaining)
            except queue.Empty as error:
                raise TimeoutError(f"Timed out waiting for OSC message: {address}") from error

            if message.address != address:
                continue
            if predicate is not None and not predicate(message):
                continue
            return message

    def _raise_if_process_exited(self, process: subprocess.Popen | None) -> None:
        if process is None:
            return

        return_code = process.poll()
        if return_code is not None:
            raise RuntimeError(
                "BeRTA Renderer exited before OSC verification completed. "
                f"Return code: {return_code}"
            )

    def request_reply(
        self,
        request_address: str,
        reply_address: str,
        *arguments: Any,
        timeout: float,
        process: subprocess.Popen | None = None,
        retry_interval: float = 0.5,
        reply_predicate: MessagePredicate | None = None,
    ) -> OscMessage:
        """Send an OSC request until the expected real reply arrives or timeout expires."""
        deadline = time.monotonic() + timeout
        last_error: TimeoutError | None = None

        self.drain_messages()

        while True:
            self._raise_if_process_exited(process)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                if last_error is not None:
                    raise last_error
                raise TimeoutError(f"Timed out waiting for OSC message: {reply_address}")

            self.send(request_address, *arguments)

            try:
                return self.wait_for_message(
                    reply_address,
                    timeout=min(retry_interval, remaining),
                    predicate=reply_predicate,
                )
            except TimeoutError as error:
                last_error = error

    def connect_with_retries(
        self,
        retry_wait_seconds: float,
        max_attempts: int,
        process: subprocess.Popen | None = None,
    ) -> OscMessage:
        """Try /control/connect multiple times until BeRTA answers."""
        last_error: TimeoutError | None = None
        self.drain_messages()

        for attempt in range(1, max_attempts + 1):
            self._raise_if_process_exited(process)
            print(
                f"OSC connect attempt {attempt}/{max_attempts}: "
                f"waiting {retry_wait_seconds}s before /control/connect..."
            )

            if retry_wait_seconds > 0:
                time.sleep(retry_wait_seconds)

            self.send(
                "/control/connect",
                self.tester_endpoint.ip,
                self.tester_endpoint.port,
            )
            print(
                "Sent /control/connect "
                f"{self.tester_endpoint.ip} {self.tester_endpoint.port}; waiting reply..."
            )

            try:
                reply = self.wait_for_message(
                    "/control/connect",
                    timeout=retry_wait_seconds,
                )
                print(f"Received {reply}")
                return reply
            except TimeoutError as error:
                last_error = error
                print("No /control/connect reply received for this attempt.")

        raise TimeoutError(
            "Timed out waiting for /control/connect after "
            f"{max_attempts} attempts with {retry_wait_seconds}s wait per attempt"
        ) from last_error

    def verify_berta_is_ready(
        self,
        connect_retry_wait_seconds: float,
        connect_max_attempts: int,
        version_timeout: float,
        process: subprocess.Popen | None = None,
    ) -> OscVerificationResult:
        """Verify BeRTA startup using /control/connect first."""
        connect_reply = self.connect_with_retries(
            retry_wait_seconds=connect_retry_wait_seconds,
            max_attempts=connect_max_attempts,
            process=process,
        )

        print("Sending /control/ping and waiting for /control/ping...")
        ping_reply = self.request_reply(
            "/control/ping",
            "/control/ping",
            timeout=version_timeout,
            process=process,
        )
        print(f"Received {ping_reply}")

        print("Sending /control/version and waiting for /control/version...")
        version_reply = self.request_reply(
            "/control/version",
            "/control/version",
            timeout=version_timeout,
            process=process,
        )
        print(f"Received {version_reply}")
        version = " ".join(str(argument) for argument in version_reply.arguments)

        if not version:
            raise RuntimeError("BeRTA replied to /control/version but did not return a version")

        return OscVerificationResult(
            connected=True,
            version=version,
            connect_reply=connect_reply,
            ping_reply=ping_reply,
            version_reply=version_reply,
            berta_endpoint=self.berta_endpoint,
            tester_endpoint=self.tester_endpoint,
        )
