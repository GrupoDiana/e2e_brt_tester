from __future__ import annotations

from dataclasses import dataclass
from subprocess import TimeoutExpired
from typing import Iterable

from berta_tester.analytical_tests import (
    AnalyticalImpulseResponseResult,
    execute_analytical_impulse_response_test,
)
from berta_tester.audio_metrics import ComparisonStatus
from berta_tester.test_definition import TestDefinition
from berta_tester.test_runner import TestSession, start_test_session


@dataclass(frozen=True)
class AnalyticalBatchEntry:
    """Compact result for one analytical test executed in a batch."""

    test: TestDefinition
    status: ComparisonStatus
    left_nrmse_percent: float | None
    right_nrmse_percent: float | None
    reason: str


@dataclass(frozen=True)
class AnalyticalBatchResult:
    """Result of running a list of analytical tests."""

    entries: tuple[AnalyticalBatchEntry, ...]

    @property
    def total(self) -> int:
        return len(self.entries)

    @property
    def passed(self) -> int:
        return sum(1 for entry in self.entries if entry.status is ComparisonStatus.PASS)

    @property
    def failed(self) -> int:
        return sum(1 for entry in self.entries if entry.status is ComparisonStatus.FAIL)

    @property
    def errors(self) -> int:
        return sum(1 for entry in self.entries if entry.status is ComparisonStatus.ERROR)


def _nrmse_values(
    result: AnalyticalImpulseResponseResult,
) -> tuple[float | None, float | None]:
    comparison = result.comparison
    if comparison is None:
        return None, None

    left = comparison.left.nrmse_percent if comparison.left is not None else None
    right = comparison.right.nrmse_percent if comparison.right is not None else None
    return left, right


def _format_percent(value: float | None) -> str:
    if value is None:
        return "undefined"
    return f"{value:.6f}%"


def _entry_from_result(
    test: TestDefinition,
    result: AnalyticalImpulseResponseResult,
) -> AnalyticalBatchEntry:
    left_nrmse, right_nrmse = _nrmse_values(result)
    return AnalyticalBatchEntry(
        test=test,
        status=result.status,
        left_nrmse_percent=left_nrmse,
        right_nrmse_percent=right_nrmse,
        reason=result.reason,
    )


def _entry_from_error(test: TestDefinition, error: Exception) -> AnalyticalBatchEntry:
    return AnalyticalBatchEntry(
        test=test,
        status=ComparisonStatus.ERROR,
        left_nrmse_percent=None,
        right_nrmse_percent=None,
        reason=str(error),
    )


def _close_session(session: TestSession, timeout_seconds: float = 5.0) -> None:
    """Close OSC and make sure the BeRTA process used by this batch item exits."""
    close_error: Exception | None = None
    try:
        session.close()
    except Exception as error:
        close_error = error

    process = session.launch_result.process
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=timeout_seconds)
        except TimeoutExpired:
            process.kill()
            process.wait(timeout=timeout_seconds)

    if close_error is not None:
        raise close_error


def run_all_analytical_tests(
    tests: Iterable[TestDefinition],
    *,
    show_progress: bool = True,
) -> AnalyticalBatchResult:
    """Run every analytical test in an isolated BeRTA session.

    Each test launches BeRTA with its own settings file, verifies OSC, executes
    the same analytical action used by the compact menu option, and then closes
    the session before the next test starts. A failing test does not stop the
    batch; its result is recorded and the next test is attempted.
    """
    entries: list[AnalyticalBatchEntry] = []

    for index, test in enumerate(tuple(tests), start=1):
        if show_progress:
            print()
            print(f"Running analytical test {index}: [{test.id}] {test.name}")

        session: TestSession | None = None
        try:
            session = start_test_session(test)
            result = execute_analytical_impulse_response_test(
                session,
                show_progress=False,
            )
            entry = _entry_from_result(test, result)
        except Exception as error:
            entry = _entry_from_error(test, error)
        finally:
            if session is not None:
                try:
                    _close_session(session)
                except Exception as close_error:
                    if entry.status is not ComparisonStatus.ERROR:
                        entry = AnalyticalBatchEntry(
                            test=test,
                            status=ComparisonStatus.ERROR,
                            left_nrmse_percent=entry.left_nrmse_percent,
                            right_nrmse_percent=entry.right_nrmse_percent,
                            reason=f"Test completed, but closing the BeRTA session failed: {close_error}",
                        )

        entries.append(entry)

        if show_progress:
            print(f"Test result: {entry.status.value}")
            print(f"Left channel NRMSE: {_format_percent(entry.left_nrmse_percent)}")
            print(f"Right channel NRMSE: {_format_percent(entry.right_nrmse_percent)}")
            if entry.status is ComparisonStatus.ERROR:
                print(f"Reason: {entry.reason}")

    return AnalyticalBatchResult(entries=tuple(entries))


def print_analytical_batch_summary(result: AnalyticalBatchResult) -> None:
    """Print the final compact summary for a completed analytical batch."""
    print()
    print("Analytical batch results")
    print("------------------------")

    if not result.entries:
        print("No analytical tests were executed.")
        print()
        return

    for entry in result.entries:
        print()
        print(f"[{entry.test.id}] {entry.test.name}")
        print(f"Test result: {entry.status.value}")
        print(f"Left channel NRMSE: {_format_percent(entry.left_nrmse_percent)}")
        print(f"Right channel NRMSE: {_format_percent(entry.right_nrmse_percent)}")
        if entry.status is not ComparisonStatus.PASS:
            print(f"Reason: {entry.reason}")

    print()
    print("Summary")
    print("-------")
    print(f"Total: {result.total}")
    print(f"PASS: {result.passed}")
    print(f"FAIL: {result.failed}")
    print(f"ERROR: {result.errors}")
    print()
