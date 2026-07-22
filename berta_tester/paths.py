from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def settingsfiles_dir() -> Path:
    return project_root() / "Settingsfiles"


def logs_dir() -> Path:
    return project_root() / "Logs"


def results_dir() -> Path:
    return project_root() / "Results"


def resolve_settings_file(filename: str) -> Path:
    path = settingsfiles_dir() / filename
    if not path.exists():
        raise FileNotFoundError(
            f"Settings file not found: {path}. "
            "Create it inside the Settingsfiles folder or update the test definition."
        )
    if not path.is_file():
        raise FileNotFoundError(f"Settings path is not a file: {path}")
    return path
