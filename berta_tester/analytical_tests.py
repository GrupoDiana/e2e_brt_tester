from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import time

from berta_tester.audio_io import AudioReadError, read_stereo_wav_float
from berta_tester.audio_metrics import ComparisonStatus, StereoComparisonResult, compare_stereo_audio
from berta_tester.console_output import print_key_values, print_section
from berta_tester.console_style import format_status
from berta_tester.paths import project_root
from berta_tester.test_definition import TestDefinition
from berta_tester.test_runner import TestSession


@dataclass(frozen=True)
class OscActionResult:
    action_command: str
    target_id: str
    success: bool
    description: str


@dataclass(frozen=True)
class AnalyticalImpulseResponseResult:
    status: ComparisonStatus
    action_result: OscActionResult | None
    comparison: StereoComparisonResult | None
    reason: str
    generated_path: Path
    reference_path: Path


def _resolve_project_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return project_root() / path


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "ok", "success"}
    return bool(value)


def _parse_action_result(arguments: tuple[Any, ...]) -> OscActionResult:
    if len(arguments) < 3:
        raise RuntimeError(
            "/control/actionResult received with too few arguments: "
            f"{arguments!r}"
        )

    action_command = str(arguments[0])
    target_id = str(arguments[1])
    success = _as_bool(arguments[2])
    description = " ".join(str(argument) for argument in arguments[3:])
    return OscActionResult(
        action_command=action_command,
        target_id=target_id,
        success=success,
        description=description,
    )


def _wait_for_action_result(
    session: TestSession,
    action_command: str,
    target_id: str,
    timeout: float,
) -> OscActionResult:
    def predicate(message: Any) -> bool:
        args = message.arguments
        if len(args) < 3:
            return False
        return str(args[0]) == action_command and str(args[1]) == target_id

    reply = session.osc_client.wait_for_message(
        "/control/actionResult",
        timeout=timeout,
        predicate=predicate,
    )
    return _parse_action_result(reply.arguments)


def _wait_for_file_ready(path: Path, timeout_seconds: float = 100.0) -> None:
    """Wait until a newly generated file is visible, non-empty and stable.

    BeRTA sends /control/actionResult when the recording has finished, but on
    Windows the filesystem/antivirus/lower-level writer may still need a short
    moment before another process can open the file reliably. This is not used
    as the primary synchronisation mechanism; it is only a post-confirmation
    file-readiness guard.
    """
    deadline = time.monotonic() + max(0.1, timeout_seconds)
    last_size: int | None = None
    last_mtime_ns: int | None = None
    stable_observations = 0
    last_error: Exception | None = None

    while time.monotonic() < deadline:
        try:
            if path.exists() and path.is_file():
                stat = path.stat()
                # A valid WAV header is at least 44 bytes. Be conservative and
                # require the file to be larger than the minimum header.
                if stat.st_size > 44:
                    with path.open("rb") as file:
                        file.read(12)

                    if stat.st_size == last_size and stat.st_mtime_ns == last_mtime_ns:
                        stable_observations += 1
                    else:
                        stable_observations = 1
                        last_size = stat.st_size
                        last_mtime_ns = stat.st_mtime_ns

                    if stable_observations >= 2:
                        return
        except Exception as error:
            last_error = error

        time.sleep(0.1)

    if last_error is not None:
        raise RuntimeError(f"Generated file is not ready for reading: {path}: {last_error}")
    raise RuntimeError(f"Generated file is not ready for reading: {path}")


def _validate_analytical_test_config(test: TestDefinition) -> list[str]:
    errors: list[str] = []
    if not test.generated_wav_path:
        errors.append("Generated WAV path is empty.")
    if not test.reference_wav_path:
        errors.append("Reference WAV path is empty.")
    if test.nrmse_margin_percent <= 0:
        errors.append("NRMSE margin must be greater than zero.")
    if test.osc_action_timeout_seconds <= 0:
        errors.append("OSC action timeout must be greater than zero.")
    if test.ir_duration_seconds <= 0:
        errors.append("Impulse response duration must be greater than zero.")
    if test.ir_period_samples < 0:
        errors.append("Impulse period samples must be greater than or equal to zero.")
    if test.ir_delay_samples < 0:
        errors.append("Impulse delay samples must be greater than or equal to zero.")
    return errors


def _make_result(
    *,
    status: ComparisonStatus,
    action_result: OscActionResult | None,
    comparison: StereoComparisonResult | None,
    reason: str,
    generated_path: Path,
    reference_path: Path,
) -> AnalyticalImpulseResponseResult:
    return AnalyticalImpulseResponseResult(
        status=status,
        action_result=action_result,
        comparison=comparison,
        reason=reason,
        generated_path=generated_path,
        reference_path=reference_path,
    )


def _format_percent(value: float | None) -> str:
    if value is None:
        return "undefined"
    return f"{value:.6f}%"


def _format_float(value: float | None, suffix: str = "") -> str:
    if value is None:
        return "undefined"
    return f"{value:.6f}{suffix}"


def _left_nrmse(result: AnalyticalImpulseResponseResult) -> float | None:
    comparison = result.comparison
    if comparison is None or comparison.left is None:
        return None
    return comparison.left.nrmse_percent


def _right_nrmse(result: AnalyticalImpulseResponseResult) -> float | None:
    comparison = result.comparison
    if comparison is None or comparison.right is None:
        return None
    return comparison.right.nrmse_percent


def print_analytical_summary(
    session: TestSession,
    result: AnalyticalImpulseResponseResult,
) -> None:
    print_section("Analytical test summary")
    print_key_values(
        (
            ("Test", session.test.name),
            (
                "Connection with BeRTA",
                "active" if session.is_berta_process_running() else "not running",
            ),
            ("Settings file", f"Settingsfiles/{session.test.settings_file}"),
            ("Generated file", result.generated_path),
            ("Reference file", result.reference_path),
            ("Allowed margin", f"{session.test.nrmse_margin_percent:.6f}%"),
        )
    )

    if result.action_result is not None:
        print(f"OSC action: {result.action_result.action_command}")
        print(f"OSC action success: {result.action_result.success}")
        print(f"OSC description: {result.action_result.description}")

    comparison = result.comparison
    if comparison is not None:
        print_section("Audio comparison")
        print(f"Sample rate: {comparison.sample_rate} Hz")
        print(f"Generated samples: {comparison.generated_samples}")
        print(f"Reference samples: {comparison.reference_samples}")
        if comparison.sample_rate:
            duration = comparison.common_samples / comparison.sample_rate
            print(f"Compared duration: {duration:.6f} s")
        print(f"Strict length match: {comparison.strict_length_match}")

        if comparison.left is not None:
            print()
            print("Left channel:")
            print(f"  NRMSE: {_format_percent(comparison.left.nrmse_percent)}")
            print(f"  Correlation: {_format_float(comparison.left.correlation)}")
            print(f"  Max abs error: {_format_float(comparison.left.max_abs_error)}")
            print(f"  Generated RMS: {_format_float(comparison.left.generated_rms)}")
            print(f"  Reference RMS: {_format_float(comparison.left.reference_rms)}")
            print(f"  Level difference: {_format_float(comparison.left.level_difference_db, ' dB')}")
            print(
                "  Detected lag: "
                f"{comparison.left.detected_lag_samples} samples "
                f"({comparison.left.detected_lag_ms:.6f} ms)"
            )
            print(
                "  Aligned NRMSE diagnostic: "
                f"{_format_percent(comparison.left.aligned_nrmse_percent)}"
            )

        if comparison.right is not None:
            print()
            print("Right channel:")
            print(f"  NRMSE: {_format_percent(comparison.right.nrmse_percent)}")
            print(f"  Correlation: {_format_float(comparison.right.correlation)}")
            print(f"  Max abs error: {_format_float(comparison.right.max_abs_error)}")
            print(f"  Generated RMS: {_format_float(comparison.right.generated_rms)}")
            print(f"  Reference RMS: {_format_float(comparison.right.reference_rms)}")
            print(f"  Level difference: {_format_float(comparison.right.level_difference_db, ' dB')}")
            print(
                "  Detected lag: "
                f"{comparison.right.detected_lag_samples} samples "
                f"({comparison.right.detected_lag_ms:.6f} ms)"
            )
            print(
                "  Aligned NRMSE diagnostic: "
                f"{_format_percent(comparison.right.aligned_nrmse_percent)}"
            )

        if session.test.detect_channel_swap:
            print()
            print("Cross-channel diagnostic:")
            print(
                "  Generated L vs Reference R NRMSE: "
                f"{_format_percent(comparison.cross_left_to_right_nrmse_percent)}"
            )
            print(
                "  Generated R vs Reference L NRMSE: "
                f"{_format_percent(comparison.cross_right_to_left_nrmse_percent)}"
            )
            print(f"  Possible channel swap: {comparison.possible_channel_swap}")

    print_section("Final result")
    print_key_values(
        (("Status", format_status(result.status)), ("Reason", result.reason))
    )


def print_analytical_compact_summary(result: AnalyticalImpulseResponseResult) -> None:
    """Print the compact report used by the non-verbose menu action."""
    print_section("Test result")
    print_key_values(
        (
            ("Status", format_status(result.status)),
            ("Left channel NRMSE", _format_percent(_left_nrmse(result))),
            ("Right channel NRMSE", _format_percent(_right_nrmse(result))),
            ("Reason", result.reason),
        )
    )


def execute_analytical_impulse_response_test(
    session: TestSession,
    *,
    show_progress: bool = False,
) -> AnalyticalImpulseResponseResult:
    """Execute the analytical IR test and return its result without printing a report."""
    test = session.test
    trace = session.timing_trace
    trace.mark(f"Analytical action started: [{test.id}] {test.name}")
    generated_path = _resolve_project_path(test.generated_wav_path)
    reference_path = _resolve_project_path(test.reference_wav_path)

    config_errors = _validate_analytical_test_config(test)
    if config_errors:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=None,
            comparison=None,
            reason="; ".join(config_errors),
            generated_path=generated_path,
            reference_path=reference_path,
        )

    if show_progress:
        print()
        print(f"Running: {test.name}")
        print(test.description)
        print("Checking active OSC connection with BeRTA using /control/ping...")

    trace.mark("OSC ping started")
    try:
        session.ping(timeout=test.osc_action_timeout_seconds)
    except Exception as error:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=None,
            comparison=None,
            reason=f"OSC connection is not active: {error}",
            generated_path=generated_path,
            reference_path=reference_path,
        )
    trace.mark("OSC ping completed")

    generated_path.parent.mkdir(parents=True, exist_ok=True)
    if generated_path.exists():
        generated_path.unlink()

    if show_progress:
        print("OSC connection is active.")
        print("Sending /recordIR and waiting for /control/actionResult /recordIR ...")

    action_target = str(generated_path)
    x, y, z = test.ir_position
    session.osc_client.drain_messages()
    session.osc_client.send(
        "/recordIR",
        action_target,
        "wav",
        float(test.ir_duration_seconds),
        int(test.ir_period_samples),
        int(test.ir_delay_samples),
        float(x),
        float(y),
        float(z),
    )
    trace.mark("/recordIR sent; waiting for /control/actionResult")

    try:
        action_result = _wait_for_action_result(
            session,
            action_command="/recordIR",
            target_id=action_target,
            timeout=test.osc_action_timeout_seconds,
        )
    except Exception as error:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=None,
            comparison=None,
            reason=f"Timeout or error waiting for /control/actionResult /recordIR: {error}",
            generated_path=generated_path,
            reference_path=reference_path,
        )
    trace.mark("/control/actionResult received")

    if not action_result.success:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=action_result,
            comparison=None,
            reason=f"BeRTA rejected /recordIR: {action_result.description}",
            generated_path=generated_path,
            reference_path=reference_path,
        )

    if not generated_path.exists():
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=action_result,
            comparison=None,
            reason=f"BeRTA reported success but generated WAV was not found: {generated_path}",
            generated_path=generated_path,
            reference_path=reference_path,
        )

    trace.mark("Generated WAV readiness wait started")
    try:
        _wait_for_file_ready(generated_path)
    except Exception as error:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=action_result,
            comparison=None,
            reason=f"Generated WAV exists but is not ready for reading: {error}",
            generated_path=generated_path,
            reference_path=reference_path,
        )
    trace.mark(
        f"Generated WAV ready: {generated_path} "
        f"({generated_path.stat().st_size} bytes)"
    )

    try:
        trace.mark("Generated WAV read started")
        generated_audio = read_stereo_wav_float(generated_path)
        trace.mark(
            "Generated WAV read completed: "
            f"{generated_audio.num_samples} samples at {generated_audio.sample_rate} Hz"
        )
        trace.mark("Reference WAV read started")
        reference_audio = read_stereo_wav_float(reference_path)
        trace.mark(
            "Reference WAV read completed: "
            f"{reference_audio.num_samples} samples at {reference_audio.sample_rate} Hz"
        )
    except AudioReadError as error:
        return _make_result(
            status=ComparisonStatus.ERROR,
            action_result=action_result,
            comparison=None,
            reason=f"Audio read/validation error: {error}",
            generated_path=generated_path,
            reference_path=reference_path,
        )

    trace.mark("Audio comparison started")
    comparison = compare_stereo_audio(
        generated_audio,
        reference_audio,
        margin_percent=test.nrmse_margin_percent,
        detect_channel_swap=test.detect_channel_swap,
        timing_callback=trace.mark,
    )
    trace.mark("Audio comparison completed")
    return _make_result(
        status=comparison.status,
        action_result=action_result,
        comparison=comparison,
        reason=comparison.reason,
        generated_path=generated_path,
        reference_path=reference_path,
    )


def run_analytical_impulse_response_test(
    session: TestSession,
    *,
    verbose: bool = True,
) -> AnalyticalImpulseResponseResult:
    """Execute the analytical IR test and print either a verbose or compact report.

    Both modes execute the same OSC commands, WAV validation and mathematical
    comparisons. The only difference is the report printed to the console.
    """
    result = execute_analytical_impulse_response_test(
        session,
        show_progress=verbose,
    )
    if verbose:
        print_analytical_summary(session, result)
    else:
        print_analytical_compact_summary(result)
    return result
