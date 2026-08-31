from __future__ import annotations

from berta_tester import console_output


def test_print_section_uses_a_matching_separator(capsys, monkeypatch) -> None:
    monkeypatch.setattr(console_output, "bright_cyan", lambda text: text)

    console_output.print_section("Test definition")

    assert capsys.readouterr().out == (
        "\nTEST DEFINITION\n---------------\n"
    )


def test_print_key_values_aligns_labels_and_multiline_values(capsys) -> None:
    console_output.print_key_values(
        (("ID", "7"), ("Description", "first line\nsecond line"))
    )

    assert capsys.readouterr().out == (
        "ID          : 7\n"
        "Description : first line\n"
        "              second line\n"
    )


def test_print_indented_text_expands_tabs(capsys) -> None:
    console_output.print_indented_text("summary\n\t- parameter")

    assert capsys.readouterr().out == "  summary\n    - parameter\n"
