from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from berta_tester.audio_io import StereoAudio

EPSILON_RMS = 1.0e-12


class ComparisonStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"


@dataclass(frozen=True)
class ChannelMetrics:
    nrmse_percent: float | None
    correlation: float | None
    max_abs_error: float
    generated_rms: float
    reference_rms: float
    level_difference_db: float | None
    detected_lag_samples: int
    detected_lag_ms: float
    aligned_nrmse_percent: float | None
    reason: str | None = None


@dataclass(frozen=True)
class StereoComparisonResult:
    status: ComparisonStatus
    passed: bool
    strict_length_match: bool
    sample_rate: int | None
    generated_samples: int
    reference_samples: int
    common_samples: int
    margin_percent: float
    left: ChannelMetrics | None
    right: ChannelMetrics | None
    cross_left_to_right_nrmse_percent: float | None
    cross_right_to_left_nrmse_percent: float | None
    possible_channel_swap: bool
    reason: str


@dataclass(frozen=True)
class LengthMismatchDiagnostic:
    generated_samples: int
    reference_samples: int
    difference_samples: int
    difference_ms: float | None


def rms(signal: np.ndarray) -> float:
    if signal.size == 0:
        return 0.0
    return float(np.sqrt(np.mean(np.square(signal.astype(np.float64)))))


def nrmse_percent(generated: np.ndarray, reference: np.ndarray) -> float | None:
    reference_rms = rms(reference)
    if reference_rms <= EPSILON_RMS:
        return None
    return 100.0 * rms(generated - reference) / reference_rms


def pearson_correlation(generated: np.ndarray, reference: np.ndarray) -> float | None:
    if generated.size == 0 or reference.size == 0:
        return None
    generated_centered = generated - np.mean(generated)
    reference_centered = reference - np.mean(reference)
    denominator = np.linalg.norm(generated_centered) * np.linalg.norm(reference_centered)
    if denominator <= EPSILON_RMS:
        return None
    return float(np.dot(generated_centered, reference_centered) / denominator)


def level_difference_db(generated: np.ndarray, reference: np.ndarray) -> float | None:
    generated_rms = rms(generated)
    reference_rms = rms(reference)
    if generated_rms <= EPSILON_RMS or reference_rms <= EPSILON_RMS:
        return None
    return float(20.0 * np.log10(generated_rms / reference_rms))


def detect_lag_samples(generated: np.ndarray, reference: np.ndarray) -> int:
    """Estimate lag using cross-correlation.

    Positive lag means the generated signal appears delayed relative to the
    reference. Negative lag means the generated signal appears earlier.
    """
    if generated.size == 0 or reference.size == 0:
        return 0

    generated_centered = generated - np.mean(generated)
    reference_centered = reference - np.mean(reference)
    if np.linalg.norm(generated_centered) <= EPSILON_RMS or np.linalg.norm(reference_centered) <= EPSILON_RMS:
        return 0

    correlation = np.correlate(generated_centered, reference_centered, mode="full")
    lag_index = int(np.argmax(np.abs(correlation)))
    return lag_index - (reference.size - 1)


def aligned_vectors_for_lag(generated: np.ndarray, reference: np.ndarray, lag: int) -> tuple[np.ndarray, np.ndarray]:
    if lag > 0:
        return generated[lag:], reference[: generated.size - lag]
    if lag < 0:
        return generated[: generated.size + lag], reference[-lag:]
    return generated, reference


def compute_channel_metrics(
    generated: np.ndarray,
    reference: np.ndarray,
    sample_rate: int,
) -> ChannelMetrics:
    generated = np.asarray(generated, dtype=np.float64)
    reference = np.asarray(reference, dtype=np.float64)
    reference_rms = rms(reference)
    generated_rms = rms(generated)
    nrmse = nrmse_percent(generated, reference)
    lag = detect_lag_samples(generated, reference)
    lag_ms = 1000.0 * lag / sample_rate if sample_rate > 0 else 0.0
    aligned_generated, aligned_reference = aligned_vectors_for_lag(generated, reference, lag)
    aligned_nrmse = None
    if aligned_generated.size > 0 and aligned_reference.size > 0:
        aligned_nrmse = nrmse_percent(aligned_generated, aligned_reference)

    reason = None
    if nrmse is None:
        reason = "Reference RMS is zero or practically zero; NRMSE is undefined."

    return ChannelMetrics(
        nrmse_percent=nrmse,
        correlation=pearson_correlation(generated, reference),
        max_abs_error=float(np.max(np.abs(generated - reference))) if generated.size else 0.0,
        generated_rms=generated_rms,
        reference_rms=reference_rms,
        level_difference_db=level_difference_db(generated, reference),
        detected_lag_samples=lag,
        detected_lag_ms=lag_ms,
        aligned_nrmse_percent=aligned_nrmse,
        reason=reason,
    )


def compare_stereo_audio(
    generated: StereoAudio,
    reference: StereoAudio,
    margin_percent: float,
    detect_channel_swap: bool = True,
) -> StereoComparisonResult:
    if margin_percent <= 0:
        return StereoComparisonResult(
            status=ComparisonStatus.ERROR,
            passed=False,
            strict_length_match=False,
            sample_rate=None,
            generated_samples=generated.num_samples,
            reference_samples=reference.num_samples,
            common_samples=0,
            margin_percent=margin_percent,
            left=None,
            right=None,
            cross_left_to_right_nrmse_percent=None,
            cross_right_to_left_nrmse_percent=None,
            possible_channel_swap=False,
            reason="Margin percent must be greater than zero.",
        )

    if generated.sample_rate != reference.sample_rate:
        return StereoComparisonResult(
            status=ComparisonStatus.ERROR,
            passed=False,
            strict_length_match=False,
            sample_rate=None,
            generated_samples=generated.num_samples,
            reference_samples=reference.num_samples,
            common_samples=0,
            margin_percent=margin_percent,
            left=None,
            right=None,
            cross_left_to_right_nrmse_percent=None,
            cross_right_to_left_nrmse_percent=None,
            possible_channel_swap=False,
            reason=(
                "Sample rates do not match: "
                f"generated={generated.sample_rate} Hz, reference={reference.sample_rate} Hz."
            ),
        )

    common_samples = min(generated.num_samples, reference.num_samples)
    strict_length_match = generated.num_samples == reference.num_samples

    if common_samples == 0:
        return StereoComparisonResult(
            status=ComparisonStatus.ERROR,
            passed=False,
            strict_length_match=strict_length_match,
            sample_rate=generated.sample_rate,
            generated_samples=generated.num_samples,
            reference_samples=reference.num_samples,
            common_samples=common_samples,
            margin_percent=margin_percent,
            left=None,
            right=None,
            cross_left_to_right_nrmse_percent=None,
            cross_right_to_left_nrmse_percent=None,
            possible_channel_swap=False,
            reason="One of the WAV files contains no samples.",
        )

    generated_common = generated.samples[:common_samples, :]
    reference_common = reference.samples[:common_samples, :]

    left = compute_channel_metrics(
        generated_common[:, 0], reference_common[:, 0], generated.sample_rate
    )
    right = compute_channel_metrics(
        generated_common[:, 1], reference_common[:, 1], generated.sample_rate
    )

    cross_left_right = None
    cross_right_left = None
    possible_channel_swap = False
    if detect_channel_swap:
        cross_left_right = nrmse_percent(generated_common[:, 0], reference_common[:, 1])
        cross_right_left = nrmse_percent(generated_common[:, 1], reference_common[:, 0])
        if (
            left.nrmse_percent is not None
            and right.nrmse_percent is not None
            and cross_left_right is not None
            and cross_right_left is not None
        ):
            correct_average = (left.nrmse_percent + right.nrmse_percent) / 2.0
            crossed_average = (cross_left_right + cross_right_left) / 2.0
            possible_channel_swap = crossed_average < correct_average * 0.5

    reasons: list[str] = []
    if not strict_length_match:
        diff_samples = generated.num_samples - reference.num_samples
        diff_ms = 1000.0 * diff_samples / generated.sample_rate
        reasons.append(
            "Strict length mismatch: "
            f"generated={generated.num_samples} samples, "
            f"reference={reference.num_samples} samples, "
            f"difference={diff_samples} samples ({diff_ms:.3f} ms)."
        )

    for channel_name, metrics in (("left", left), ("right", right)):
        if metrics.nrmse_percent is None:
            reasons.append(f"{channel_name} channel NRMSE is undefined: {metrics.reason}")
        elif metrics.nrmse_percent >= margin_percent:
            reasons.append(
                f"{channel_name} channel NRMSE {metrics.nrmse_percent:.6f}% "
                f"is not below margin {margin_percent:.6f}%."
            )

    if possible_channel_swap:
        reasons.append("Cross-channel comparisons are clearly better; channels may be swapped.")

    passed = (
        strict_length_match
        and left.nrmse_percent is not None
        and right.nrmse_percent is not None
        and left.nrmse_percent < margin_percent
        and right.nrmse_percent < margin_percent
    )

    return StereoComparisonResult(
        status=ComparisonStatus.PASS if passed else ComparisonStatus.FAIL,
        passed=passed,
        strict_length_match=strict_length_match,
        sample_rate=generated.sample_rate,
        generated_samples=generated.num_samples,
        reference_samples=reference.num_samples,
        common_samples=common_samples,
        margin_percent=margin_percent,
        left=left,
        right=right,
        cross_left_to_right_nrmse_percent=cross_left_right,
        cross_right_to_left_nrmse_percent=cross_right_left,
        possible_channel_swap=possible_channel_swap,
        reason="; ".join(reasons) if reasons else "Both channels are below the configured NRMSE margin.",
    )
