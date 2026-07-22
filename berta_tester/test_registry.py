from __future__ import annotations

from berta_tester.test_definition import TestDefinition, TestType


TESTS: tuple[TestDefinition, ...] = (
    TestDefinition(
        id="1",
        name="IR test of Listener_Direct_HRTF_Convolution Model",
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Model to be tested: Listener_Direct_HRTF_ConvolutionModel\n"
            "\t-Impulse position: (1,0,0)\n"
            "\t-Record duration: 1 second\n"
        ),
        settings_file="analytical_test_1.json",
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_1_ir.wav",
        reference_wav_path="Referencefiles/analytical_test_1_ir_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="2",
        name="IR test of Listener_Direct_HRTF_Convolution Model",
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Model to be tested: Listener_Direct_HRTF_ConvolutionModel\n"
            "\t-Impulse position: (0,1,0)\n"
            "\t-Record duration: 1 second\n"
        ),
        settings_file="analytical_test_1.json",
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_2_ir.wav",
        reference_wav_path="Referencefiles/analytical_test_2_ir_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.0, 1.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="3",
        name="IR test of Nearfield of Listener_Direct_HRTF_Convolution Model",
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Model to be tested: Nearfield of Listener_Direct_HRTF_ConvolutionModel\n"
            "\t-Impulse position: (-0.1,-0.1,0)\n"
            "\t-Record duration: 1 second\n"
        ),
        settings_file="analytical_test_3.json",
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_3_ir.wav",
        reference_wav_path="Referencefiles/analytical_test_3_ir_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(-0.1, -0.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="39",
        name="Perceptual localization test",
        description=(
            "You will hear the source in front of you and it will move toward one ear."
        ),
        settings_file="test1.json",
        test_type=TestType.PERCEPTUAL,
        source_id="source1",
        movement_steps=30,
        movement_duration_seconds=3.0,
    ),
)


def get_tests() -> tuple[TestDefinition, ...]:
    return TESTS


def get_test_by_id(test_id: str) -> TestDefinition | None:
    for test in TESTS:
        if test.id == test_id:
            return test
    return None
