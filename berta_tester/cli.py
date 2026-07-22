from __future__ import annotations

from berta_tester.app_config import APP_TITLE
from berta_tester.batch_runner import print_analytical_batch_summary, run_all_analytical_tests
from berta_tester.reference_metadata import read_reference_metadata
from berta_tester.test_actions import run_test_actions
from berta_tester.test_definition import TestDefinition, TestType
from berta_tester.test_registry import get_tests
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

    if any(test.test_type is TestType.ANALYTICAL for test in tests):
        print("[A] Run all analytical tests")
    print("[9] Back to main menu")
    print("[0] Exit")
    print()


def ask_for_option(prompt: str = "Select option: ") -> str:
    return input(prompt).strip()


def print_session_ready(session: TestSession, path: str) -> None:
    print_breadcrumb(path)
    print("BeRTA Renderer launched successfully.")
    print(f"Executable: {session.launch_result.executable}")
    print(f"Working directory: {session.launch_result.working_directory}")
    print(f"Settings file: {session.launch_result.settings_file}")
    print(f"Process PID: {session.launch_result.process.pid}")
    print()
    print("OSC verification succeeded.")
    print(
        "BeRTA OSC endpoint: "
        f"{session.osc_verification.berta_endpoint.ip}:"
        f"{session.osc_verification.berta_endpoint.port}"
    )
    print(
        "Tester OSC endpoint: "
        f"{session.osc_verification.tester_endpoint.ip}:"
        f"{session.osc_verification.tester_endpoint.port}"
    )
    print(f"Version: {session.osc_verification.version}")
    print()


def print_test_actions_menu(path: str) -> None:
    print_breadcrumb(path)
    print("Test session actions:")
    print("[1] Show session status")
    print("[2] Send /control/ping")
    print("[3] Request /control/version")
    print("[4] Run test actions verbose")
    print("[5] Run test actions")
    print("[6] Show reference metadata")
    print("[9] Disconnect and return to test menu")
    print("[0] Disconnect and exit")
    print()




def print_reference_metadata(session: TestSession, path: str) -> None:
    """Show the YAML metadata associated with the selected test reference file."""
    print()
    print_breadcrumb(path)
    print("Reference metadata")
    print("------------------")

    result = read_reference_metadata(session.test)
    if result.path is not None:
        print(f"File: {result.path}")
    print(result.message)

    if result.content:
        print()
        print(result.content)

    print()

def run_session_menu(session: TestSession, path: str) -> str:
    """Run the menu for a verified BeRTA session.

    Returns:
        "menu" to go back to the current test category menu.
        "exit" to terminate the tester application.
    """
    while True:
        print_test_actions_menu(path)
        choice = ask_for_option("Select action: ")

        if choice == "1":
            print()
            print_breadcrumb(path)
            print(f"Selected test: {session.test.name}")
            print(f"BeRTA process running: {session.is_berta_process_running()}")
            print(f"PID: {session.launch_result.process.pid}")
            print(f"Version: {session.osc_verification.version}")
            print()
            continue

        if choice == "2":
            try:
                session.ping()
                print()
                print_breadcrumb(path)
                print("/control/ping reply received.")
                print()
            except Exception as error:
                print()
                print_breadcrumb(path)
                print(f"ERROR sending /control/ping: {error}")
                print()
            continue

        if choice == "3":
            try:
                version = session.get_version()
                print()
                print_breadcrumb(path)
                print(f"Version: {version}")
                print()
            except Exception as error:
                print()
                print_breadcrumb(path)
                print(f"ERROR requesting /control/version: {error}")
                print()
            continue

        if choice == "4":
            try:
                print()
                print_breadcrumb(path)
                run_test_actions(session, verbose=True)
            except Exception as error:
                print()
                print_breadcrumb(path)
                print(f"ERROR running test actions: {error}")
                print()
            continue


        if choice == "5":
            try:
                print()
                print_breadcrumb(path)
                run_test_actions(session, verbose=False)
            except Exception as error:
                print()
                print_breadcrumb(path)
                print(f"ERROR running test actions: {error}")
                print()
            continue

        if choice == "6":
            try:
                print_reference_metadata(session, path)
            except Exception as error:
                print()
                print_breadcrumb(path)
                print(f"ERROR showing reference metadata: {error}")
                print()
            continue

        if choice == "9":
            print()
            print_breadcrumb(path)
            print("Disconnecting OSC session, closing BeRTA Renderer, and returning to test menu.")
            session.close()
            print()
            return "menu"

        if choice == "0":
            print()
            print_breadcrumb(path)
            print("Disconnecting OSC session, closing BeRTA Renderer, and exiting.")
            session.close()
            print()
            return "exit"

        print("Invalid option. Please try again.")
        print()


def run_test_type_menu(test_type: TestType, menu_label: str) -> str:
    """Show tests for one category and run selected sessions.

    Returns:
        "menu" to go back to the main menu.
        "exit" to terminate the tester application.
    """
    path = f"{MAIN_MENU_PATH} / {menu_label}"

    while True:
        tests = tests_by_type(test_type)
        print_test_type_menu(path, tests)
        choice = ask_for_option("Select test: ")

        if choice == "9":
            return "menu"

        if choice == "0":
            return "exit"

        if choice.lower() == "a" and test_type is TestType.ANALYTICAL:
            batch_path = f"{path} / Run all analytical tests"
            print()
            print_breadcrumb(batch_path)
            batch_result = run_all_analytical_tests(tests, show_progress=True)
            print_analytical_batch_summary(batch_result)
            continue

        test = get_test_by_id_from_tests(choice, tests)
        if test is None:
            print("Invalid option. Please try again.")
            print()
            continue

        session: TestSession | None = None
        session_path = f"{path} / Test {test.id}"
        try:
            print()
            print_breadcrumb(session_path)
            print(f"Selected test: {test.name}")
            session = start_test_session(test)
            print_session_ready(session, session_path)
            next_action = run_session_menu(session, session_path)
            if next_action == "exit":
                return "exit"
        except Exception as error:
            if session is not None:
                session.close()
            print()
            print_breadcrumb(session_path)
            print(f"ERROR: {error}")
            print()
            return "menu"


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
