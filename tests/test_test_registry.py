from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from berta_tester.test_definition import TestType as DefinitionTestType
from berta_tester.test_registry import get_tests, group_tests_by_target


EXPECTED_ANALYTICAL_TARGET_COUNTS = {
    "ListenerDirectHRTFConvolutionModel": 39,
    "Directivity": 3,
    "FreeFieldEnvironmentModel": 10,
    "ISMEnvironmentModel": 40,
    "SDNEnvironmentModel": 8,
    "ListenerAmbisonicVirtualLoudspeakersModel": 36,
}
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def analytical_tests():
    return tuple(
        test
        for test in get_tests()
        if test.test_type is DefinitionTestType.ANALYTICAL
    )


def test_every_test_has_a_target() -> None:
    assert all(test.test_target.strip() for test in get_tests())


def test_analytical_tests_are_grouped_by_expected_target() -> None:
    groups = group_tests_by_target(analytical_tests())

    assert {target: len(tests) for target, tests in groups} == (
        EXPECTED_ANALYTICAL_TARGET_COUNTS
    )


def test_compact_analytical_names_are_unique() -> None:
    names = [test.name for test in analytical_tests()]

    assert len(names) == 136
    assert len(set(names)) == len(names)


def test_test_target_is_not_duplicated_in_descriptions() -> None:
    assert all(
        "Model to be tested:" not in test.description
        for test in analytical_tests()
    )


def test_authoritative_positions_are_reflected_in_corrected_descriptions() -> None:
    tests_by_id = {test.id: test for test in analytical_tests()}

    assert "Impulse position: (-0.1,0,0)" in tests_by_id["6"].description
    for test_id in (
        "48.2",
        "49.2",
        "50.2",
        "51.2",
        "52.2",
        "53.2",
        "54.2",
        "55.2",
        "56.2",
        "57.2",
        "58.2",
        "59.2",
    ):
        assert "Distance parameter: 10m" in tests_by_id[test_id].description


def test_targets_match_their_settings_architecture() -> None:
    for test in analytical_tests():
        settings_path = PROJECT_ROOT / "Settingsfiles" / test.settings_file
        settings = json.loads(settings_path.read_text(encoding="utf-8-sig"))
        architecture = settings["ModelsArchitecture"]

        if test.test_target == "Directivity":
            commands = {
                item["command"]
                for item in settings.get("SceneConfiguration", [])
                if "command" in item
            }
            assert "/source/enableDirectivity" in commands
            continue

        models = (
            architecture.get("EnvironmentModels")
            or architecture.get("ListenerModels")
        )
        assert models[0]["Model"] == test.test_target


def test_described_positions_match_ir_position() -> None:
    for test in analytical_tests():
        match = re.search(r"Impulse position:\s*(\([^\n]+\))", test.description)
        assert match is not None
        described_position = tuple(
            float(value) for value in ast.literal_eval(match.group(1))
        )
        assert described_position == test.ir_position
