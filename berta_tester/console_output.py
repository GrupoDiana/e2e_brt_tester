from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from berta_tester.console_style import bright_cyan


def print_section(title: str) -> None:
    """Print a visually distinct section heading."""
    normalized = title.upper()
    print()
    print(bright_cyan(normalized))
    print("-" * len(normalized))


def print_menu_title(title: str) -> None:
    """Print a menu heading using the shared navigation colour."""
    print(bright_cyan(title))
    print()


def print_key_values(rows: Iterable[tuple[str, Any]]) -> None:
    """Print aligned label/value rows, preserving multiline values."""
    prepared = [(str(label), str(value)) for label, value in rows]
    if not prepared:
        return

    label_width = max(len(label) for label, _ in prepared)
    continuation_indent = " " * (label_width + 3)

    for label, value in prepared:
        value_lines = value.splitlines() or [""]
        print(f"{label:<{label_width}} : {value_lines[0]}")
        for continuation in value_lines[1:]:
            print(f"{continuation_indent}{continuation}")


def print_indented_text(text: str, indent: int = 2) -> None:
    """Print multiline text with a stable indentation."""
    prefix = " " * indent
    for line in text.expandtabs(2).splitlines():
        print(f"{prefix}{line}")
