from __future__ import annotations

import os
import time

from berta_tester.app_config import TIMINGS_ENV_VAR
from berta_tester.console_style import yellow


_ENABLED_VALUES = {"1", "true", "yes", "on"}


def timings_enabled() -> bool:
    """Return whether detailed execution timings are enabled."""
    return os.getenv(TIMINGS_ENV_VAR, "").strip().lower() in _ENABLED_VALUES


class TimingTrace:
    """Print elapsed and stage durations when timing diagnostics are enabled."""

    def __init__(self, *, enabled: bool | None = None) -> None:
        self.enabled = timings_enabled() if enabled is None else enabled
        self._started_at = time.perf_counter()
        self._last_mark_at = self._started_at

    def mark(self, message: str) -> None:
        if not self.enabled:
            return

        now = time.perf_counter()
        elapsed = now - self._started_at
        stage_duration = now - self._last_mark_at
        self._last_mark_at = now
        print(
            yellow(
                f"[TIMING +{elapsed:8.3f}s | stage {stage_duration:8.3f}s] "
                f"{message}"
            )
        )
