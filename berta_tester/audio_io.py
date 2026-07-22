from __future__ import annotations

import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np

try:
    import soundfile as sf
except ImportError as error:  # pragma: no cover - depends on local environment
    raise ImportError(
        "Missing dependency 'soundfile'. Install it with: pip install soundfile"
    ) from error


@dataclass(frozen=True)
class StereoAudio:
    path: Path
    sample_rate: int
    samples: np.ndarray
    subtype: str

    @property
    def num_channels(self) -> int:
        if self.samples.ndim == 1:
            return 1
        return int(self.samples.shape[1])

    @property
    def num_samples(self) -> int:
        return int(self.samples.shape[0])

    @property
    def duration_seconds(self) -> float:
        if self.sample_rate <= 0:
            return 0.0
        return self.num_samples / self.sample_rate

    @property
    def left(self) -> np.ndarray:
        return self.samples[:, 0]

    @property
    def right(self) -> np.ndarray:
        return self.samples[:, 1]


class AudioReadError(RuntimeError):
    pass


def _windows_extended_path(path: Path) -> str:
    r"""Return a Windows long-path compatible representation.

    libsndfile/soundfile may fail with opaque "System error" messages on long
    Windows paths. The \\?\ prefix asks the Windows API to bypass MAX_PATH
    normalisation for absolute local paths. UNC paths need the \\?\UNC\ form.
    On non-Windows platforms this function is not used.
    """
    path_text = str(path.resolve(strict=False))
    if path_text.startswith("\\\\?\\"):
        return path_text
    if path_text.startswith("\\\\"):
        return "\\\\?\\UNC\\" + path_text.lstrip("\\")
    return "\\\\?\\" + path_text


def _soundfile_path_candidates(path: Path) -> list[str]:
    candidates = [str(path)]
    if os.name == "nt":
        candidates.append(_windows_extended_path(path))

    unique_candidates: list[str] = []
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
    return unique_candidates


def _read_with_soundfile(path: Path) -> tuple[object, np.ndarray, int]:
    errors: list[str] = []

    for candidate in _soundfile_path_candidates(path):
        try:
            info = sf.info(candidate)
            data, sample_rate = sf.read(candidate, dtype="float64", always_2d=True)
            return info, data, int(sample_rate)
        except Exception as error:
            errors.append(f"{candidate}: {error}")

    # Final fallback for Windows path-length issues: copy the file to a short
    # temporary path and let libsndfile read that path. This does not alter the
    # samples; it only avoids path handling limitations in lower-level libraries.
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_path = Path(temp_file.name)
        shutil.copyfile(path, temp_path)
        info = sf.info(str(temp_path))
        data, sample_rate = sf.read(str(temp_path), dtype="float64", always_2d=True)
        return info, data, int(sample_rate)
    except Exception as error:
        errors.append(f"temporary copy fallback: {error}")
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except Exception:
                pass

    raise AudioReadError(
        "Could not read WAV with soundfile. Tried direct path, Windows extended "
        "path when available, and temporary-copy fallback. Errors: "
        + " | ".join(errors)
    )


def read_stereo_wav_float(path: Path | str) -> StereoAudio:
    """Read a stereo WAV file as float64 without independent normalization.

    Integer PCM conversion is delegated to libsndfile via soundfile, which applies
    the standard full-scale conversion consistently for all files. Floating-point
    WAV files are returned as their stored amplitudes. No per-file or per-channel
    normalization is performed.
    """
    wav_path = Path(path).resolve(strict=False)

    if not wav_path.exists():
        raise AudioReadError(f"WAV file does not exist: {wav_path}")
    if not wav_path.is_file():
        raise AudioReadError(f"WAV path is not a file: {wav_path}")

    try:
        info, data, sample_rate = _read_with_soundfile(wav_path)
    except AudioReadError:
        raise
    except Exception as error:
        raise AudioReadError(f"Could not read WAV file: {wav_path}: {error}") from error

    if info.format != "WAV":
        raise AudioReadError(f"File is not a WAV file: {wav_path} (format: {info.format})")
    if info.channels != 2:
        raise AudioReadError(
            f"WAV file must contain exactly two channels: {wav_path} "
            f"(channels: {info.channels})"
        )

    if data.ndim != 2 or data.shape[1] != 2:
        raise AudioReadError(
            f"WAV data must be stereo after decoding: {wav_path} "
            f"(shape: {data.shape})"
        )
    if not np.all(np.isfinite(data)):
        raise AudioReadError(f"WAV contains NaN or infinite samples: {wav_path}")

    # Values outside [-1, 1] are valid for floating-point WAV. They are reported
    # by the comparison diagnostics, but they are not a read failure.
    return StereoAudio(
        path=wav_path,
        sample_rate=sample_rate,
        samples=np.asarray(data, dtype=np.float64),
        subtype=info.subtype,
    )
