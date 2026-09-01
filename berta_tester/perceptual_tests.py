from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass
from enum import Enum

from berta_tester.console_output import print_key_values, print_menu_title, print_section
from berta_tester.console_style import format_status, red
from berta_tester.test_runner import TestSession


class EarDirection(str, Enum):
    LEFT = "left"
    RIGHT = "right"

    @property
    def endpoint(self) -> tuple[float, float, float]:
        if self is EarDirection.LEFT:
            return (0.0, 1.0, 0.0)
        return (0.0, -1.0, 0.0)

    @property
    def label(self) -> str:
        if self is EarDirection.LEFT:
            return "left ear (0, 1)"
        return "right ear (0, -1)"


@dataclass(frozen=True)
class PerceptualTestResult:
    passed: bool
    expected_direction: EarDirection
    user_direction: EarDirection


def _send_source_location(
    session: TestSession,
    x: float,
    y: float,
    z: float = 0.0,
) -> None:
    session.osc_client.send(
        "/source/location",
        session.test.source_id,
        float(x),
        float(y),
        float(z),
    )


def _run_circular_source_movement(
    session: TestSession,
    target_direction: EarDirection,
) -> None:
    steps = max(2, session.test.movement_steps)
    duration_seconds = max(0.0, session.test.movement_duration_seconds)
    sleep_between_steps = duration_seconds / (steps - 1) if steps > 1 else 0.0
    y_sign = 1.0 if target_direction is EarDirection.LEFT else -1.0

    for index in range(steps):
        theta = (math.pi / 2.0) * (index / (steps - 1))
        x = math.cos(theta)
        y = y_sign * math.sin(theta)
        _send_source_location(session, x=x, y=y, z=0.0)

        if index < steps - 1 and sleep_between_steps > 0:
            time.sleep(sleep_between_steps)


def _ask_user_direction() -> EarDirection:
    while True:
        print()
        print_menu_title("What movement did you hear?")
        print("[1] From the center/front to the LEFT ear (0, 1)")
        print("[2] From the center/front to the RIGHT ear (0, -1)")
        answer = input("Select answer: ").strip().lower()

        if answer in {"1", "left", "l", "izquierda"}:
            return EarDirection.LEFT
        if answer in {"2", "right", "r", "derecha"}:
            return EarDirection.RIGHT

        print(red("Invalid answer. Please try again."))


def run_perceptual_localization_test(session: TestSession) -> PerceptualTestResult:
    """Run Test 1: source movement from front to a random ear."""
    target_direction = random.choice((EarDirection.LEFT, EarDirection.RIGHT))

    print()
    print(f"Running: {session.test.name}")
    print(session.test.description)
    print(f"Source ID: {session.test.source_id}")
    print(
        "Movement: circular trajectory from front (1, 0) "
        "to one randomly selected ear."
    )
    print()
    input("Press Enter to start the movement...")

    _send_source_location(session, x=1.0, y=0.0, z=0.0)
    time.sleep(0.25)
    _run_circular_source_movement(session, target_direction)

    user_direction = _ask_user_direction()
    passed = user_direction is target_direction

    print_section("Test result")
    if passed:
        print_key_values(
            (
                ("Status", format_status("PASS")),
                ("Reason", "The perceived movement matches the generated trajectory."),
            )
        )
    else:
        print_key_values(
            (
                ("Status", format_status("FAIL")),
                ("Reason", "The perceived movement does not match the generated trajectory."),
                ("Expected movement", f"center/front to the {target_direction.label}"),
                ("User answer", f"center/front to the {user_direction.label}"),
            )
        )

    return PerceptualTestResult(
        passed=passed,
        expected_direction=target_direction,
        user_direction=user_direction,
    )
