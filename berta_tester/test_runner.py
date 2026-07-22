from __future__ import annotations

from dataclasses import dataclass
from subprocess import TimeoutExpired

from berta_tester.berta_launcher import LaunchResult, launch_berta
from berta_tester.osc_client import (
    OscClient,
    OscVerificationResult,
    get_berta_endpoint_from_env,
    get_connect_max_attempts_from_env,
    get_connect_retry_wait_from_env,
    get_startup_timeout_from_env,
    get_tester_endpoint_from_env,
)
from berta_tester.paths import resolve_settings_file
from berta_tester.test_definition import TestDefinition


@dataclass(frozen=True)
class TestRunResult:
    test: TestDefinition
    launch_result: LaunchResult
    osc_verification: OscVerificationResult


@dataclass
class TestSession:
    """A live BeRTA test session.

    The session keeps the BeRTA process and the Python OSC listener alive after
    startup verification. This is the object that future test actions should use
    to send OSC commands and wait for results.
    """

    test: TestDefinition
    launch_result: LaunchResult
    osc_client: OscClient
    osc_verification: OscVerificationResult
    closed: bool = False

    def close(
        self,
        disconnect: bool = True,
        close_berta_process: bool = True,
        terminate_timeout_seconds: float = 5.0,
    ) -> None:
        """Close the live test session.

        This closes both sides of the session:
        - the OSC subscription/listener used by the Python tester;
        - the BeRTA Renderer process launched for this test.

        BeRTA currently has no dedicated OSC command to quit the application, so
        the renderer process is terminated through subprocess. If it does not
        exit within terminate_timeout_seconds, it is killed as a fallback.
        """
        if self.closed:
            return

        try:
            if disconnect:
                self.osc_client.disconnect_safely()
        finally:
            self.osc_client.close()

        if close_berta_process:
            self.close_berta_process(terminate_timeout_seconds)

        self.closed = True

    def close_berta_process(self, timeout_seconds: float = 5.0) -> None:
        """Terminate the BeRTA Renderer process if it is still running."""
        process = self.launch_result.process
        if process.poll() is not None:
            return

        process.terminate()
        try:
            process.wait(timeout=timeout_seconds)
        except TimeoutExpired:
            process.kill()
            process.wait(timeout=timeout_seconds)

    def ping(self, timeout: float | None = None) -> bool:
        timeout = timeout if timeout is not None else get_startup_timeout_from_env()
        self.osc_client.request_reply(
            "/control/ping",
            "/control/ping",
            timeout=timeout,
            process=self.launch_result.process,
        )
        return True

    def get_version(self, timeout: float | None = None) -> str:
        timeout = timeout if timeout is not None else get_startup_timeout_from_env()
        version_reply = self.osc_client.request_reply(
            "/control/version",
            "/control/version",
            timeout=timeout,
            process=self.launch_result.process,
        )
        return " ".join(str(argument) for argument in version_reply.arguments)

    def is_berta_process_running(self) -> bool:
        return self.launch_result.process.poll() is None


class TestSessionContext:
    """Context manager wrapper for TestSession."""

    def __init__(self, session: TestSession) -> None:
        self.session = session

    def __enter__(self) -> TestSession:
        return self.session

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.session.close()


def _raise_if_berta_exited(launch_result: LaunchResult) -> None:
    return_code = launch_result.process.poll()
    if return_code is not None:
        raise RuntimeError(
            "BeRTA Renderer exited before OSC verification completed. "
            f"Return code: {return_code}"
        )


def start_test_session(test: TestDefinition) -> TestSession:
    """Launch BeRTA, verify OSC, and keep the live session open."""
    settings_file = resolve_settings_file(test.settings_file)
    launch_result = launch_berta(settings_file)

    berta_endpoint = get_berta_endpoint_from_env()
    tester_endpoint = get_tester_endpoint_from_env()
    version_timeout = get_startup_timeout_from_env()
    connect_retry_wait_seconds = get_connect_retry_wait_from_env()
    connect_max_attempts = get_connect_max_attempts_from_env()

    _raise_if_berta_exited(launch_result)

    osc_client = OscClient(berta_endpoint, tester_endpoint)
    try:
        osc_client.start()
        osc_verification = osc_client.verify_berta_is_ready(
            connect_retry_wait_seconds=connect_retry_wait_seconds,
            connect_max_attempts=connect_max_attempts,
            version_timeout=version_timeout,
            process=launch_result.process,
        )
    except Exception:
        osc_client.close()
        raise

    return TestSession(
        test=test,
        launch_result=launch_result,
        osc_client=osc_client,
        osc_verification=osc_verification,
    )


def run_test(test: TestDefinition) -> TestRunResult:
    """Compatibility helper: launch, verify, and close the OSC session.

    The CLI now uses start_test_session() so BeRTA remains available for test
    actions. This function is kept for callers that only need a launch check.
    """
    session = start_test_session(test)
    try:
        return TestRunResult(
            test=session.test,
            launch_result=session.launch_result,
            osc_verification=session.osc_verification,
        )
    finally:
        session.close()
