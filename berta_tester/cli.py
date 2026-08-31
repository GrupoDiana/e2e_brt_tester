from __future__ import annotations

from pathlib import Path

from berta_tester.app_config import APP_TITLE
from berta_tester.batch_runner import print_analytical_batch_summary, run_analytical_tests
from berta_tester.console_output import print_indented_text, print_key_values, print_section
from berta_tester.console_style import bright_green, cyan, format_outcome, red
from berta_tester.paths import project_root
from berta_tester.reference_metadata import read_reference_metadata, resolve_reference_metadata_path
from berta_tester.test_actions import run_test_actions
from berta_tester.test_definition import TestDefinition, TestType
from berta_tester.test_registry import get_tests, group_tests_by_target
from berta_tester.test_runner import TestSession, start_test_session


MAIN_MENU_PATH = "Main Menu"
ANALYTICAL_MENU_LABEL = "Analytical tests"
PERCEPTUAL_MENU_LABEL = "Perceptual tests"


def print_header() -> None:
    print(APP_TITLE)
    print()


def print_breadcrumb(path: str) -> None:
    """Print the current navigation path as a clearly separated block."""
    text = f" Path: {path} "
    separator = "-" * max(40, len(text))
    print(separator)
    print(text)
    print(separator)
    print()


def print_main_menu() -> None:
    print_breadcrumb(MAIN_MENU_PATH)
    print("[1] Analytical tests")
    print("[2] Perceptual tests")
    print("[0] Exit")
    print()


def tests_by_type(test_type: TestType) -> tuple[TestDefinition, ...]:
    return tuple(test for test in get_tests() if test.test_type is test_type)


def get_test_by_id_from_tests(
    test_id: str,
    tests: tuple[TestDefinition, ...],
) -> TestDefinition | None:
    normalized = test_id.strip()
    for test in tests:
        if test.id == normalized:
            return test
    return None


def print_test_type_menu(
    path: str,
    tests: tuple[TestDefinition, ...],
) -> None:
    print_breadcrumb(path)
    print("Available tests:")
    print()

    if not tests:
        print("No tests are currently defined in this category.")
        print()
    else:
        for test in tests:
            print(test.menu_label())
            print(f"    {test.description}")
            print(f"    Settings file: Settingsfiles/{test.settings_file}")
            print()

    print("[9] Back to main menu")
    print("[0] Exit")
    print()


def print_analytical_target_menu(
    path: str,
    groups: tuple[tuple[str, tuple[TestDefinition, ...]], ...],
) -> None:
    print_breadcrumb(path)
    print("Analytical test targets:")
    print()

    for index, (target, tests) in enumerate(groups, start=1):
        print(f"[{index}] {target} ({len(tests)} tests)")

    print()
    print("[A] Run all analytical tests")
    print("[9] Back to main menu")
    print("[0] Exit")
    print()


def print_target_tests_menu(
    path: str,
    target: str,
    tests: tuple[TestDefinition, ...],
) -> None:
    print_breadcrumb(path)
    print(f"Available tests for {target}:")
    print()

    for test in tests:
        print(f"[{test.id}] {test.name}")

    print()
    print(f"[A] Run all tests for {target}")
    print("[9] Back to analytical test targets")
    print("[0] Exit")
    print()


def ask_for_option(prompt: str = "Select option: ") -> str:
    return input(prompt).strip()


def _project_path(path_text: str) -> Path:
    path = Path(path_text)
    return path if path.is_absolute() else project_root() / path


def _enabled(value: bool) -> str:
    return "enabled" if value else "disabled"


def print_test_definition(test: TestDefinition) -> None:
    """Print the selected test as structured, type-specific sections."""
    print_section("Test definition")
    print_key_values(
        (
            ("ID", test.id),
            ("Name", test.name),
            ("Target", test.test_target),
            ("Type", test.test_type.value),
        )
    )
    print()
    print("Description:")
    print_indented_text(test.description.rstrip())

    if test.test_type is TestType.ANALYTICAL:
        print_section("Analytical configuration")
        print_key_values(
            (
                ("IR position", test.ir_position),
                ("IR duration", f"{test.ir_duration_seconds:g} s"),
                ("IR period", f"{test.ir_period_samples} samples"),
                ("IR delay", f"{test.ir_delay_samples} samples"),
                ("NRMSE margin", f"{test.nrmse_margin_percent:g} %"),
                ("OSC action timeout", f"{test.osc_action_timeout_seconds:g} s"),
                ("Diagnostics", _enabled(test.enable_complementary_diagnostics)),
                ("Channel swap check", _enabled(test.detect_channel_swap)),
            )
        )
    elif test.test_type is TestType.PERCEPTUAL:
        print_section("Perceptual configuration")
        print_key_values(
            (
                ("Source ID", test.source_id),
                ("Movement steps", test.movement_steps),
                ("Movement duration", f"{test.movement_duration_seconds:g} s"),
                ("OSC sequence", ", ".join(test.osc_sequence) or "not configured"),
                ("Expected results", ", ".join(test.expected_results) or "not configured"),
            )
        )

    metadata_path = resolve_reference_metadata_path(test)
    print_section("Files")
    file_rows: list[tuple[str, object]] = [
        ("Settings file", project_root() / "Settingsfiles" / test.settings_file),
    ]
    if test.test_type is TestType.ANALYTICAL:
        file_rows.extend(
            (
                ("Generated WAV", _project_path(test.generated_wav_path)),
                ("Reference WAV", _project_path(test.reference_wav_path)),
                ("Reference metadata", metadata_path or "not configured"),
            )
        )
    print_key_values(file_rows)


def print_session_ready(session: TestSession) -> None:
    print_key_values(
        (
            ("Status", format_outcome(True)),
            ("Version", session.osc_verification.version),
            ("Executable", session.launch_result.executable),
            ("Working directory", session.launch_result.working_directory),
            ("Settings file", session.launch_result.settings_file),
            ("Process PID", session.launch_result.process.pid),
            ("OSC verification", format_outcome(session.osc_verification.connected)),
        )
    )


def print_test_actions_menu() -> None:
    print_section("Test session actions")
    print("[1] Show session status")
    print("[2] Send /control/ping")
    print("[3] Request /control/version")
    print(cyan("[4] Run test actions verbose"))
    print(bright_green("[5] Run test actions"))
    print("[6] Show reference metadata")
    print("[9] Disconnect and return to test menu")
    print("[0] Disconnect and exit")
    print()




def print_reference_metadata(session: TestSession) -> None:
    """Show the YAML metadata associated with the selected test reference file."""
    print_section("Reference metadata")
    result = read_reference_metadata(session.test)
    print_key_values(
        (
            ("Status", format_outcome(result.exists)),
            ("File", result.path or "not configured"),
            ("Message", result.message),
        )
    )

    if result.content:
        print()
        print(result.content)

    print()

def run_session_menu(session: TestSession) -> str:
    """Run the menu for a verified BeRTA session.

    Returns:
        "menu" to go back to the current test category menu.
        "exit" to terminate the tester application.
    """
    while True:
        print_test_actions_menu()
        choice = ask_for_option("Select action: ")

        if choice == "1":
            running = session.is_berta_process_running()
            print_section("Session status")
            print_key_values(
                (
                    ("Selected test", session.test.name),
                    ("BeRTA process", format_outcome(running)),
                    ("Process PID", session.launch_result.process.pid),
                    ("Version", session.osc_verification.version),
                )
            )
            continue

        if choice == "2":
            print_section("OSC ping")
            try:
                session.ping()
                print_key_values((("Status", format_outcome(True)),))
            except Exception as error:
                print_key_values(
                    (("Status", format_outcome(False)), ("Reason", red(str(error))))
                )
            continue

        if choice == "3":
            print_section("BeRTA version")
            try:
                version = session.get_version()
                print_key_values(
                    (("Status", format_outcome(True)), ("Version", version))
                )
            except Exception as error:
                print_key_values(
                    (("Status", format_outcome(False)), ("Reason", red(str(error))))
                )
            continue

        if choice == "4":
            print_section("Verbose test execution")
            try:
                run_test_actions(session, verbose=True)
            except Exception as error:
                print_key_values(
                    (("Status", format_outcome(False)), ("Reason", red(str(error))))
                )
            continue

        if choice == "5":
            print_section("Test execution")
            try:
                run_test_actions(session, verbose=False)
            except Exception as error:
                print_key_values(
                    (("Status", format_outcome(False)), ("Reason", red(str(error))))
                )
            continue

        if choice == "6":
            try:
                print_reference_metadata(session)
            except Exception as error:
                print_section("Reference metadata")
                print_key_values(
                    (("Status", format_outcome(False)), ("Reason", red(str(error))))
                )
            continue

        if choice == "9":
            print_section("Closing session")
            print("Disconnecting OSC session, closing BeRTA Renderer, and returning to test menu.")
            session.close()
            return "menu"

        if choice == "0":
            print_section("Closing session")
            print("Disconnecting OSC session, closing BeRTA Renderer, and exiting.")
            session.close()
            return "exit"

        print(red("Invalid option. Please try again."))
        print()


def run_selected_test(test: TestDefinition, parent_path: str) -> str:
    """Launch one test and return to the menu that selected it."""
    session_path = f"{parent_path} / Test {test.id}"
    print()
    print_breadcrumb(session_path)
    print_test_definition(test)
    print_section("BeRTA startup")
    print("Opening BeRTA Renderer and verifying the connection...")

    try:
        session = start_test_session(test)
    except Exception as error:
        print_key_values(
            (("Status", format_outcome(False)), ("Reason", red(str(error))))
        )
        return "menu"

    print_session_ready(session)
    try:
        return run_session_menu(session)
    except Exception as error:
        session.close()
        print_section("Session error")
        print_key_values(
            (("Status", format_outcome(False)), ("Reason", red(str(error))))
        )
        return "menu"


def run_analytical_target_menu(menu_label: str) -> str:
    """Navigate analytical tests by target and allow target-level batches."""
    path = f"{MAIN_MENU_PATH} / {menu_label}"

    while True:
        tests = tests_by_type(TestType.ANALYTICAL)
        groups = group_tests_by_target(tests)
        print_analytical_target_menu(path, groups)
        choice = ask_for_option("Select test target: ")

        if choice == "9":
            return "menu"
        if choice == "0":
            return "exit"
        if choice.lower() == "a":
            batch_path = f"{path} / Run all analytical tests"
            print()
            print_breadcrumb(batch_path)
            result = run_analytical_tests(tests, show_progress=True)
            print_analytical_batch_summary(result)
            continue

        try:
            selected_index = int(choice) - 1
            target, target_tests = groups[selected_index]
            if selected_index < 0:
                raise IndexError
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            print()
            continue

        next_action = run_analytical_family_menu(path, target, target_tests)
        if next_action == "exit":
            return "exit"


def run_analytical_family_menu(
    parent_path: str,
    target: str,
    tests: tuple[TestDefinition, ...],
) -> str:
    """Select or batch-run tests belonging to one analytical target."""
    path = f"{parent_path} / {target}"

    while True:
        print_target_tests_menu(path, target, tests)
        choice = ask_for_option("Select test: ")

        if choice == "9":
            return "menu"
        if choice == "0":
            return "exit"
        if choice.lower() == "a":
            batch_path = f"{path} / Run all tests"
            print()
            print_breadcrumb(batch_path)
            result = run_analytical_tests(tests, show_progress=True)
            print_analytical_batch_summary(result)
            continue

        test = get_test_by_id_from_tests(choice, tests)
        if test is None:
            print("Invalid option. Please try again.")
            print()
            continue

        if run_selected_test(test, path) == "exit":
            return "exit"


def run_test_type_menu(test_type: TestType, menu_label: str) -> str:
    """Show tests for one category and run selected sessions."""
    if test_type is TestType.ANALYTICAL:
        return run_analytical_target_menu(menu_label)

    path = f"{MAIN_MENU_PATH} / {menu_label}"
    while True:
        tests = tests_by_type(test_type)
        print_test_type_menu(path, tests)
        choice = ask_for_option("Select test: ")

        if choice == "9":
            return "menu"
        if choice == "0":
            return "exit"

        test = get_test_by_id_from_tests(choice, tests)
        if test is None:
            print("Invalid option. Please try again.")
            print()
            continue

        if run_selected_test(test, path) == "exit":
            return "exit"


def run_cli() -> int:
    print_header()

    while True:
        print_main_menu()
        choice = ask_for_option()

        if choice == "0":
            print("Exiting.")
            return 0

        if choice == "1":
            next_action = run_test_type_menu(TestType.ANALYTICAL, ANALYTICAL_MENU_LABEL)
            if next_action == "exit":
                print("Exiting.")
                return 0
            continue

        if choice == "2":
            next_action = run_test_type_menu(TestType.PERCEPTUAL, PERCEPTUAL_MENU_LABEL)
            if next_action == "exit":
                print("Exiting.")
                return 0
            continue

        print("Invalid option. Please try again.")
        print()
