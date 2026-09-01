from __future__ import annotations

from berta_tester.app_config import TIMINGS_ENV_VAR
from berta_tester.timing_trace import TimingTrace, timings_enabled


def test_timings_are_disabled_by_default(monkeypatch) -> None:
    monkeypatch.delenv(TIMINGS_ENV_VAR, raising=False)

    assert timings_enabled() is False


def test_timings_can_be_enabled_with_environment_variable(monkeypatch) -> None:
    monkeypatch.setenv(TIMINGS_ENV_VAR, "1")

    assert timings_enabled() is True


def test_disabled_trace_prints_nothing(capsys) -> None:
    trace = TimingTrace(enabled=False)

    trace.mark("This must stay hidden")

    assert capsys.readouterr().out == ""


def test_enabled_trace_prints_elapsed_and_stage_times(capsys) -> None:
    trace = TimingTrace(enabled=True)

    trace.mark("WAV ready")

    output = capsys.readouterr().out
    assert "[TIMING +" in output
    assert "| stage" in output
    assert "WAV ready" in output
