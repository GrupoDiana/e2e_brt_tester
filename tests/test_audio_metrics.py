from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from berta_tester.audio_io import AudioReadError, read_stereo_wav_float
from berta_tester.audio_metrics import ComparisonStatus, compare_stereo_audio


SAMPLE_RATE = 48000


def write_wav(path: Path, data: np.ndarray, sample_rate: int = SAMPLE_RATE) -> None:
    sf.write(str(path), data, sample_rate, subtype="FLOAT")


def stereo(left: np.ndarray, right: np.ndarray | None = None) -> np.ndarray:
    if right is None:
        right = left.copy()
    return np.column_stack([left, right]).astype(np.float64)


def impulse(length: int = 128, index: int = 8, amplitude: float = 1.0) -> np.ndarray:
    data = np.zeros(length, dtype=np.float64)
    data[index] = amplitude
    return data


def compare_from_arrays(tmp_path: Path, generated: np.ndarray, reference: np.ndarray):
    generated_path = tmp_path / "generated.wav"
    reference_path = tmp_path / "reference.wav"
    write_wav(generated_path, generated)
    write_wav(reference_path, reference)
    return compare_stereo_audio(
        read_stereo_wav_float(generated_path),
        read_stereo_wav_float(reference_path),
        margin_percent=1.0,
        detect_channel_swap=True,
    )


def test_identical_files_pass(tmp_path: Path) -> None:
    signal = stereo(impulse(), impulse(index=12, amplitude=0.5))
    result = compare_from_arrays(tmp_path, signal, signal)

    assert result.status is ComparisonStatus.PASS
    assert result.passed is True
    assert result.left is not None
    assert result.left.nrmse_percent == pytest.approx(0.0)
    assert result.right is not None
    assert result.right.nrmse_percent == pytest.approx(0.0)


def test_gain_change_fails_with_nrmse(tmp_path: Path) -> None:
    reference = stereo(impulse(), impulse(index=12, amplitude=0.5))
    generated = reference * 0.5
    result = compare_from_arrays(tmp_path, generated, reference)

    assert result.status is ComparisonStatus.FAIL
    assert result.left is not None
    assert result.left.nrmse_percent == pytest.approx(50.0)
    assert result.right is not None
    assert result.right.nrmse_percent == pytest.approx(50.0)


def test_temporal_shift_is_reported_but_strict_comparison_fails(tmp_path: Path) -> None:
    reference_left = impulse(index=20)
    generated_left = impulse(index=23)
    reference = stereo(reference_left, reference_left)
    generated = stereo(generated_left, generated_left)
    result = compare_from_arrays(tmp_path, generated, reference)

    assert result.status is ComparisonStatus.FAIL
    assert result.left is not None
    assert result.left.detected_lag_samples == 3
    assert result.left.nrmse_percent is not None
    assert result.left.nrmse_percent > 1.0
    assert result.left.aligned_nrmse_percent == pytest.approx(0.0)


def test_channel_swap_is_detected_but_not_marked_pass(tmp_path: Path) -> None:
    left = impulse(index=8, amplitude=1.0)
    right = impulse(index=24, amplitude=0.25)
    reference = stereo(left, right)
    generated = stereo(right, left)
    result = compare_from_arrays(tmp_path, generated, reference)

    assert result.status is ComparisonStatus.FAIL
    assert result.possible_channel_swap is True
    assert result.cross_left_to_right_nrmse_percent == pytest.approx(0.0)
    assert result.cross_right_to_left_nrmse_percent == pytest.approx(0.0)


def test_length_mismatch_is_strict_failure_with_common_diagnostic(tmp_path: Path) -> None:
    reference = stereo(impulse(length=128, index=8))
    generated = stereo(impulse(length=130, index=8))
    result = compare_from_arrays(tmp_path, generated, reference)

    assert result.status is ComparisonStatus.FAIL
    assert result.strict_length_match is False
    assert result.generated_samples == 130
    assert result.reference_samples == 128
    assert "Strict length mismatch" in result.reason


def test_silent_reference_channel_makes_nrmse_undefined(tmp_path: Path) -> None:
    reference = stereo(np.zeros(128), impulse(index=10))
    generated = stereo(np.zeros(128), impulse(index=10))
    result = compare_from_arrays(tmp_path, generated, reference)

    assert result.status is ComparisonStatus.FAIL
    assert result.left is not None
    assert result.left.nrmse_percent is None
    assert "Reference RMS" in result.reason


def test_audio_reader_rejects_mono_wav(tmp_path: Path) -> None:
    mono_path = tmp_path / "mono.wav"
    sf.write(str(mono_path), np.zeros(128), SAMPLE_RATE, subtype="FLOAT")

    with pytest.raises(AudioReadError, match="exactly two channels"):
        read_stereo_wav_float(mono_path)


def test_audio_reader_rejects_sample_rate_mismatch_in_comparison(tmp_path: Path) -> None:
    generated_path = tmp_path / "generated.wav"
    reference_path = tmp_path / "reference.wav"
    signal = stereo(impulse())
    write_wav(generated_path, signal, sample_rate=48000)
    write_wav(reference_path, signal, sample_rate=44100)

    result = compare_stereo_audio(
        read_stereo_wav_float(generated_path),
        read_stereo_wav_float(reference_path),
        margin_percent=1.0,
    )

    assert result.status is ComparisonStatus.ERROR
    assert "Sample rates do not match" in result.reason


def test_audio_comparison_reports_timing_stages(tmp_path: Path) -> None:
    signal = stereo(impulse(), impulse(index=12, amplitude=0.5))
    generated_path = tmp_path / "generated.wav"
    reference_path = tmp_path / "reference.wav"
    write_wav(generated_path, signal)
    write_wav(reference_path, signal)
    timing_messages: list[str] = []

    compare_stereo_audio(
        read_stereo_wav_float(generated_path),
        read_stereo_wav_float(reference_path),
        margin_percent=1.0,
        detect_channel_swap=True,
        timing_callback=timing_messages.append,
    )

    assert timing_messages == [
        "Audio comparison: left-channel metrics started",
        "Audio comparison: left-channel metrics completed",
        "Audio comparison: right-channel metrics started",
        "Audio comparison: right-channel metrics completed",
        "Audio comparison: cross-channel diagnostic started",
        "Audio comparison: cross-channel diagnostic completed",
    ]
