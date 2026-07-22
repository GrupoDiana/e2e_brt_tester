from __future__ import annotations

from berta_tester.analytical_tests import run_analytical_impulse_response_test
from berta_tester.perceptual_tests import run_perceptual_localization_test
from berta_tester.test_definition import TestType
from berta_tester.test_runner import TestSession


def run_test_actions(session: TestSession, *, verbose: bool = True) -> None:
    """Dispatch executable actions for the selected test.

    The selected test is dispatched by TestType, not by its menu id, so tests can
    be reordered or new analytical tests can be added in test_registry.py without
    changing this dispatcher.
    """
    if session.test.test_type is TestType.PERCEPTUAL:
        # Perceptual tests do not have channel NRMSE values. They keep their
        # existing user-facing report in both verbose and compact menu actions.
        run_perceptual_localization_test(session)
        return

    if session.test.test_type is TestType.ANALYTICAL:
        run_analytical_impulse_response_test(session, verbose=verbose)
        return

    print()
    print(f"Test actions for '{session.test.name}' are not implemented yet.")
    print("BeRTA is still running and the OSC session remains open.")
    print()
