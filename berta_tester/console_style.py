from __future__ import annotations

from typing import Any

try:
    from colorama import Fore, Style, just_fix_windows_console
except ImportError:  # pragma: no cover - fallback if dependency is missing
    Fore = None
    Style = None

    def just_fix_windows_console() -> None:
        return None


_CONSOLE_INITIALIZED = False


def init_console_style() -> None:
    """Enable ANSI colour support where needed.

    On recent Windows terminals this fixes ANSI handling when necessary.
    On macOS and Linux it is effectively harmless.
    """
    global _CONSOLE_INITIALIZED
    if _CONSOLE_INITIALIZED:
        return

    just_fix_windows_console()
    _CONSOLE_INITIALIZED = True


def _colour(text: str, colour_code: str) -> str:
    init_console_style()

    if Fore is None or Style is None:
        return text

    return f"{colour_code}{text}{Style.RESET_ALL}"


def green(text: str) -> str:
    return _colour(text, Fore.GREEN if Fore is not None else "")


def red(text: str) -> str:
    return _colour(text, Fore.RED if Fore is not None else "")


def yellow(text: str) -> str:
    return _colour(text, Fore.YELLOW if Fore is not None else "")


def cyan(text: str) -> str:
    return _colour(text, Fore.CYAN if Fore is not None else "")


def format_status(status: Any) -> str:
    """Return a coloured PASS/FAIL/ERROR status.

    Accepts either a ComparisonStatus enum value or a plain string.
    """
    value = getattr(status, "value", str(status))
    normalized = value.upper()

    if normalized == "PASS":
        return green(value)

    if normalized == "FAIL":
        return red(value)

    if normalized == "ERROR":
        return yellow(value)

    return yellow(value)


def format_status_count(label: str, count: int) -> str:
    """Colour summary labels consistently."""
    normalized = label.upper()

    if normalized == "PASS":
        return f"{green(label)}: {count}"

    if normalized == "FAIL":
        return f"{red(label)}: {count}"

    if normalized == "ERROR":
        return f"{yellow(label)}: {count}"

    return f"{label}: {count}"