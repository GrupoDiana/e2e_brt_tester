from __future__ import annotations

import os
import platform
import subprocess
from dataclasses import dataclass
from pathlib import Path

from berta_tester.app_config import (
    BERTA_EXECUTABLE_ENV_VAR,
    DEFAULT_MACOS_BERTA_EXECUTABLE,
    DEFAULT_WINDOWS_BERTA_EXECUTABLE,
)


@dataclass(frozen=True)
class LaunchResult:
    executable: Path
    working_directory: Path
    settings_file: Path
    process: subprocess.Popen


def get_default_berta_executable() -> Path:
    override = os.getenv(BERTA_EXECUTABLE_ENV_VAR)
    if override:
        return Path(override).expanduser().resolve()

    current_os = platform.system()

    if current_os == "Windows":
        return Path(DEFAULT_WINDOWS_BERTA_EXECUTABLE)

    if current_os == "Darwin":
        return Path(DEFAULT_MACOS_BERTA_EXECUTABLE)

    raise RuntimeError(
        f"Unsupported operating system: {current_os}. "
        f"Set {BERTA_EXECUTABLE_ENV_VAR} to the BeRTA executable path."
    )


def validate_berta_executable(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(
            f"BeRTA executable not found: {path}. "
            f"Install BeRTA Renderer or set {BERTA_EXECUTABLE_ENV_VAR}."
        )
    if not path.is_file():
        raise FileNotFoundError(f"BeRTA executable path is not a file: {path}")


def _get_windows_creation_flags() -> int:
    """Return process creation flags used only on Windows.

    CREATE_NEW_CONSOLE makes BeRTA use its own console instead of sharing the
    Python tester console. On non-Windows platforms the flag must be zero.
    """
    if platform.system() != "Windows":
        return 0

    return subprocess.CREATE_NEW_CONSOLE


def launch_berta(settings_file: Path) -> LaunchResult:
    executable = get_default_berta_executable()
    validate_berta_executable(executable)

    if not settings_file.exists():
        raise FileNotFoundError(f"Settings file not found: {settings_file}")

    settings_file = settings_file.resolve()
    working_directory = executable.parent

    command = [str(executable), str(settings_file)]
    process = subprocess.Popen(
        command,
        cwd=str(working_directory),
        creationflags=_get_windows_creation_flags(),
    )

    return LaunchResult(
        executable=executable,
        working_directory=working_directory,
        settings_file=settings_file,
        process=process,
    )
