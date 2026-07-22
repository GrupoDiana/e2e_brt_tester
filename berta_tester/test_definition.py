from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


class TestType(str, Enum):
    SMOKE = "smoke"
    PERCEPTUAL = "perceptual"
    ANALYTICAL = "analytical"


@dataclass(frozen=True)
class TestDefinition:
    """Declarative definition of an E2E BeRTA Renderer test."""

    id: str
    name: str
    description: str
    settings_file: str
    test_type: TestType = TestType.SMOKE
    source_id: str = "source1"
    movement_steps: int = 30
    movement_duration_seconds: float = 3.0
    generated_wav_path: str = "Results/analytical_ir/generated_ir.wav"
    reference_wav_path: str = "Referencefiles/analytical_ir_reference.wav"
    reference_metadata_path: str | None = None
    nrmse_margin_percent: float = 1.0
    osc_action_timeout_seconds: float = 30.0
    ir_duration_seconds: float = 2.0
    ir_period_samples: int = 0
    ir_delay_samples: int = 0
    ir_position: tuple[float, float, float] = (1.0, 0.0, 0.0)
    enable_complementary_diagnostics: bool = True
    detect_channel_swap: bool = True
    osc_sequence: Sequence[str] = field(default_factory=tuple)
    expected_results: Sequence[str] = field(default_factory=tuple)

    def menu_label(self) -> str:
        return f"[{self.id}] {self.name} ({self.test_type.value})"
