from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
from scipy.signal import choose_conv_method
from scipy.signal import correlate as signal_correlate
from scipy.signal import correlation_lags

from berta_tester.audio_io import read_stereo_wav_float
from berta_tester.audio_metrics import detect_lag_samples


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("generated_length", "reference_length"),
    ((31, 19), (128, 128), (2048, 1536)),
)
def test_scipy_fft_correlation_matches_numpy_direct(
    generated_length: int,
    reference_length: int,
) -> None:
    rng = np.random.default_rng(20260901)
    generated = rng.standard_normal(generated_length)
    reference = rng.standard_normal(reference_length)

    direct = np.correlate(generated, reference, mode="full")
    fft = signal_correlate(generated, reference, mode="full", method="fft")

    np.testing.assert_allclose(fft, direct, rtol=1.0e-11, atol=1.0e-11)


@pytest.mark.parametrize("expected_lag", (-23, 0, 17))
def test_auto_correlation_preserves_positive_and_negative_lags(
    expected_lag: int,
) -> None:
    rng = np.random.default_rng(42)
    reference = rng.standard_normal(512)
    generated = np.zeros_like(reference)

    if expected_lag > 0:
        generated[expected_lag:] = reference[:-expected_lag]
    elif expected_lag < 0:
        generated[:expected_lag] = reference[-expected_lag:]
    else:
        generated[:] = reference

    direct = np.correlate(
        generated - np.mean(generated),
        reference - np.mean(reference),
        mode="full",
    )
    direct_lag = int(np.argmax(np.abs(direct))) - (reference.size - 1)

    assert direct_lag == expected_lag
    assert detect_lag_samples(generated, reference) == direct_lag


def test_fft_correlation_matches_direct_for_real_reference_audio() -> None:
    audio = read_stereo_wav_float(
        PROJECT_ROOT / "Referencefiles" / "analytical_test_49_reference.wav"
    )
    generated = audio.left[:4096]
    reference = audio.right[:4096]

    direct = np.correlate(generated, reference, mode="full")
    fft = signal_correlate(generated, reference, mode="full", method="fft")

    np.testing.assert_allclose(fft, direct, rtol=1.0e-10, atol=1.0e-10)


def test_fft_peak_for_ambiguous_signal_is_one_of_the_direct_maxima() -> None:
    generated = np.zeros(256)
    reference = np.zeros(256)
    generated[[40, 120]] = 1.0
    reference[[20, 100]] = 1.0

    direct = np.correlate(generated, reference, mode="full")
    fft = signal_correlate(generated, reference, mode="full", method="fft")
    lags = correlation_lags(generated.size, reference.size, mode="full")
    direct_maximum = np.max(np.abs(direct))
    valid_lags = set(
        int(lag)
        for lag in lags[
            np.isclose(np.abs(direct), direct_maximum, rtol=1.0e-12, atol=1.0e-12)
        ]
    )
    fft_lag = int(lags[int(np.argmax(np.abs(fft)))])

    np.testing.assert_allclose(fft, direct, rtol=1.0e-11, atol=1.0e-11)
    assert fft_lag in valid_lags


def test_scipy_auto_selects_fft_for_one_second_audio() -> None:
    signal = np.zeros(48000, dtype=np.float64)

    assert choose_conv_method(signal, signal, mode="full") == "fft"
