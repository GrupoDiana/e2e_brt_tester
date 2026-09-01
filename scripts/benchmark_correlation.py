from __future__ import annotations

import time
from pathlib import Path

import numpy as np
from scipy.signal import choose_conv_method
from scipy.signal import correlate as signal_correlate

from berta_tester.audio_io import read_stereo_wav_float
from berta_tester.paths import project_root


REFERENCE_CASES = (
    ("1 second", "Referencefiles/analytical_test_49_reference.wav"),
    ("2 seconds", "Referencefiles/analytical_test_4_reference.wav"),
)


def _measure_case(label: str, relative_path: str) -> None:
    audio = read_stereo_wav_float(project_root() / Path(relative_path))
    signal = audio.left - np.mean(audio.left)
    selected_method = choose_conv_method(signal, signal, mode="full")

    started_at = time.perf_counter()
    direct = np.correlate(signal, signal, mode="full")
    direct_seconds = time.perf_counter() - started_at

    started_at = time.perf_counter()
    automatic = signal_correlate(signal, signal, mode="full", method="auto")
    automatic_seconds = time.perf_counter() - started_at

    maximum_difference = float(np.max(np.abs(direct - automatic)))
    speedup = direct_seconds / automatic_seconds

    print(f"Case: {label}")
    print(f"Samples: {signal.size}")
    print(f"Method selected by SciPy: {selected_method}")
    print(f"NumPy direct: {direct_seconds:.6f} s")
    print(f"SciPy auto: {automatic_seconds:.6f} s")
    print(f"Speedup: {speedup:.1f}x")
    print(f"Maximum absolute difference: {maximum_difference:.3e}")
    print()


def main() -> None:
    for label, relative_path in REFERENCE_CASES:
        _measure_case(label, relative_path)


if __name__ == "__main__":
    main()
