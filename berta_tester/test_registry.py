from __future__ import annotations

from typing import Iterable

from berta_tester.test_definition import TestDefinition, TestType


TESTS: tuple[TestDefinition, ...] = (
    TestDefinition(
        id="1",
        name='DirectHRTF test [P=(1,0,0)]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1,0,0)\n"
            "\t-Record duration: 1 second\n"
        ),
        settings_file="analytical_test_1.json",
        test_target='ListenerDirectHRTFConvolutionModel',
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
        name='DirectHRTF test [P=(0,1,0)]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0,1,0)\n"
            "\t-Record duration: 1 second\n"
        ),
        settings_file="analytical_test_1.json",
        test_target='ListenerDirectHRTFConvolutionModel',
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
        name='DirectHRTF test [NF=ON P=(-0.1,-0.1,0)]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (-0.1,-0.1,0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Near field: ON\n"
        ),
        settings_file="analytical_test_3.json",
        test_target='ListenerDirectHRTFConvolutionModel',
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
        id="4",
        name='Directivity test [CARD=in]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (-1,0,0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Source directivity: in cardioid\n"
        ),
        settings_file="analytical_test_4.json",
        test_target='Directivity',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_4.wav",
        reference_wav_path="Referencefiles/analytical_test_6_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(-1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="5",
        name='Directivity test [CARD=out]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (-0.9,0.41,0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Source directivity: out of cardioid\n"
        ),
        settings_file="analytical_test_5.json",
        test_target='Directivity',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_5.wav",
        reference_wav_path="Referencefiles/analytical_test_6_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(-0.9, 0.41, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="6",
        name='Directivity test [CARD=in INT=15]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (-0.1,0,0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Source directivity: in cardioid\n"
            "\t-Interpolation: 15\n"
        ),
        settings_file="analytical_test_6.json",
        test_target='Directivity',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_6.wav",
        reference_wav_path="Referencefiles/analytical_test_6_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(-0.1, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="7",
        name='FreeField test [ATT=6dB SD=1m]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.71,0.71,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Distance attenuation: 6db\n"
            "\t-Source distance: 1m\n"
        ),
        settings_file="analytical_test_7.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_7.wav",
        reference_wav_path="Referencefiles/analytical_test_7_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.71, 0.71, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="7.1",
        name='FreeField test [ATT=6dB SD=10m]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.17,7.17,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Distance attenuation: 6db\n"
            "\t-Source distance: 10m\n"
        ),
        settings_file="analytical_test_7.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_7.1.wav",
        reference_wav_path="Referencefiles/analytical_test_7.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.17, 7.17, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="8",
        name='FreeField test [ATT=7dB SD=1m]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.71,0.71,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Distance attenuation: 7db\n"
            "\t-Source distance: 1m\n"
        ),
        settings_file="analytical_test_8.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_8.wav",
        reference_wav_path="Referencefiles/analytical_test_8_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.71, 0.71, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="8.1",
        name='FreeField test [ATT=7dB SD=10m]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.17,7.17,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Distance attenuation: 7db\n"
            "\t-Source distance: 10m\n"
        ),
        settings_file="analytical_test_8.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_8.1.wav",
        reference_wav_path="Referencefiles/analytical_test_8.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.17, 7.17, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="10",
        name='FreeField test [PD=ON SD=1m BS=512]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.71,0.71,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 1m\n"
            "\t-Buffer size: 512\n"
        ),
        settings_file="analytical_test_10.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_10.wav",
        reference_wav_path="Referencefiles/analytical_test_10_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.71, 0.71, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="10.1",
        name='FreeField test [PD=ON SD=10m BS=512]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.17,7.17,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 10m\n"
            "\t-Buffer size: 512\n"
        ),
        settings_file="analytical_test_10.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_10.1.wav",
        reference_wav_path="Referencefiles/analytical_test_10.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.17, 7.17, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="10.2",
        name='FreeField test [PD=ON SD=100m BS=512]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (71.7,71.7,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 100m\n"
            "\t-Buffer size: 512\n"
        ),
        settings_file="analytical_test_10.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_10.2.wav",
        reference_wav_path="Referencefiles/analytical_test_10.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(71.7, 71.7, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="11",
        name='FreeField test [PD=ON SD=1m BS=2048]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.71,0.71,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 1m\n"
            "\t-Buffer size: 2048\n"
        ),
        settings_file="analytical_test_11.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_11.wav",
        reference_wav_path="Referencefiles/analytical_test_11_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.71, 0.71, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="11.1",
        name='FreeField test [PD=ON SD=10m BS=2048]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.17,7.17,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 10m\n"
            "\t-Buffer size: 2048\n"
        ),
        settings_file="analytical_test_11.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_11.1.wav",
        reference_wav_path="Referencefiles/analytical_test_11.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.17, 7.17, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="11.2",
        name='FreeField test [PD=ON SD=100m BS=2048]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (71.7,71.7,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Propagation delay: enabled\n"
            "\t-Source distance: 100m\n"
            "\t-Buffer size: 2048\n"
        ),
        settings_file="analytical_test_11.json",
        test_target='FreeFieldEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_11.2.wav",
        reference_wav_path="Referencefiles/analytical_test_11.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(71.7, 71.7, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="12",
        name='ISM test [O=1 SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_12.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_12.wav",
        reference_wav_path="Referencefiles/analytical_test_12_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="12.1",
        name='ISM test [O=1 SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_12.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_12.1.wav",
        reference_wav_path="Referencefiles/analytical_test_12.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="13",
        name='ISM test [O=1 SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_13.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_13.wav",
        reference_wav_path="Referencefiles/analytical_test_13_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="13.1",
        name='ISM test [O=1 SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_13.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_13.1.wav",
        reference_wav_path="Referencefiles/analytical_test_13.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="14",
        name='ISM test [O=1 SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_14.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_14.wav",
        reference_wav_path="Referencefiles/analytical_test_14_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="14.1",
        name='ISM test [O=1 SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_14.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_14.1.wav",
        reference_wav_path="Referencefiles/analytical_test_14.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="15",
        name='ISM test [O=1 SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_15.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_15.wav",
        reference_wav_path="Referencefiles/analytical_test_15_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="15.1",
        name='ISM test [O=1 SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 1\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_15.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_15.1.wav",
        reference_wav_path="Referencefiles/analytical_test_15.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="16",
        name='ISM test [O=3 SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_16.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_16.wav",
        reference_wav_path="Referencefiles/analytical_test_16_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="16.1",
        name='ISM test [O=3 SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_16.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_16.1.wav",
        reference_wav_path="Referencefiles/analytical_test_16.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="17",
        name='ISM test [O=3 SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_17.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_17.wav",
        reference_wav_path="Referencefiles/analytical_test_17_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="17.1",
        name='ISM test [O=3 SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_17.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_17.1.wav",
        reference_wav_path="Referencefiles/analytical_test_17.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="18",
        name='ISM test [O=3 SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_18.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_18.wav",
        reference_wav_path="Referencefiles/analytical_test_18_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="18.1",
        name='ISM test [O=3 SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_18.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_18.1.wav",
        reference_wav_path="Referencefiles/analytical_test_18.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="19",
        name='ISM test [O=3 SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_19.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_19.wav",
        reference_wav_path="Referencefiles/analytical_test_19_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="19.1",
        name='ISM test [O=3 SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 3\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_19.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_19.1.wav",
        reference_wav_path="Referencefiles/analytical_test_19.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="20",
        name='ISM test [O=5 D=5 SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_20.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_20.wav",
        reference_wav_path="Referencefiles/analytical_test_20_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="20.1",
        name='ISM test [O=5 D=5 SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_20.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_20.1.wav",
        reference_wav_path="Referencefiles/analytical_test_20.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="21",
        name='ISM test [O=5 D=5 SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_21.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_21.wav",
        reference_wav_path="Referencefiles/analytical_test_21_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="21.1",
        name='ISM test [O=5 D=5 SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_21.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_21.1.wav",
        reference_wav_path="Referencefiles/analytical_test_21.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="22",
        name='ISM test [O=5 D=5 SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_22.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_22.wav",
        reference_wav_path="Referencefiles/analytical_test_22_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="22.1",
        name='ISM test [O=5 D=5 SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_22.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_22.1.wav",
        reference_wav_path="Referencefiles/analytical_test_22.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="23",
        name='ISM test [O=5 D=5 SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_23.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_23.wav",
        reference_wav_path="Referencefiles/analytical_test_23_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="23.1",
        name='ISM test [O=5 D=5 SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 5\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_23.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_23.1.wav",
        reference_wav_path="Referencefiles/analytical_test_23.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="24",
        name='ISM test [O=5 D=10 SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_24.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_24.wav",
        reference_wav_path="Referencefiles/analytical_test_24_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="24.1",
        name='ISM test [O=5 D=10 SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_24.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_24.1.wav",
        reference_wav_path="Referencefiles/analytical_test_24.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="25",
        name='ISM test [O=5 D=10 SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_25.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_25.wav",
        reference_wav_path="Referencefiles/analytical_test_25_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="25.1",
        name='ISM test [O=5 D=10 SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_25.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_25.1.wav",
        reference_wav_path="Referencefiles/analytical_test_25.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="26",
        name='ISM test [O=5 D=10 SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_26.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_26.wav",
        reference_wav_path="Referencefiles/analytical_test_26_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="26.1",
        name='ISM test [O=5 D=10 SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_26.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_26.1.wav",
        reference_wav_path="Referencefiles/analytical_test_26.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="27",
        name='ISM test [O=5 D=10 SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_27.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_27.wav",
        reference_wav_path="Referencefiles/analytical_test_27_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="27.1",
        name='ISM test [O=5 D=10 SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 10\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_27.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_27.1.wav",
        reference_wav_path="Referencefiles/analytical_test_27.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="28",
        name='ISM test [O=5 D=20 SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_28.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_28.wav",
        reference_wav_path="Referencefiles/analytical_test_28_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="28.1",
        name='ISM test [O=5 D=20 SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_28.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_28.1.wav",
        reference_wav_path="Referencefiles/analytical_test_28.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="29",
        name='ISM test [O=5 D=20 SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_29.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_29.wav",
        reference_wav_path="Referencefiles/analytical_test_29_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="29.1",
        name='ISM test [O=5 D=20 SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_29.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_29.1.wav",
        reference_wav_path="Referencefiles/analytical_test_29.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="30",
        name='ISM test [O=5 D=20 SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_30.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_30.wav",
        reference_wav_path="Referencefiles/analytical_test_30_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="30.1",
        name='ISM test [O=5 D=20 SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_30.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_30.1.wav",
        reference_wav_path="Referencefiles/analytical_test_30.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="31",
        name='ISM test [O=5 D=20 SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_31.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_31.wav",
        reference_wav_path="Referencefiles/analytical_test_31_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="31.1",
        name='ISM test [O=5 D=20 SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-ISM order: 5\n"
            "\t-Distance parameter: 20\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_31.json",
        test_target='ISMEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_31.1.wav",
        reference_wav_path="Referencefiles/analytical_test_31.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=10.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="32",
        name='SDN test [SD=0.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_32.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_32.wav",
        reference_wav_path="Referencefiles/analytical_test_32_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="32.1",
        name='SDN test [SD=2.5m BS=512 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_32.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_32.1.wav",
        reference_wav_path="Referencefiles/analytical_test_32.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="33",
        name='SDN test [SD=0.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_33.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_33.wav",
        reference_wav_path="Referencefiles/analytical_test_33_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="33.1",
        name='SDN test [SD=2.5m BS=512 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 512\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_33.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_33.1.wav",
        reference_wav_path="Referencefiles/analytical_test_33.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="34",
        name='SDN test [SD=0.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_34.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_34.wav",
        reference_wav_path="Referencefiles/analytical_test_34_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="34.1",
        name='SDN test [SD=2.5m BS=2048 ABS=0.5]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.5\n"
        ),
        settings_file="analytical_test_34.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_34.1.wav",
        reference_wav_path="Referencefiles/analytical_test_34.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
        TestDefinition(
        id="35",
        name='SDN test [SD=0.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.35,0.35,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 0.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_35.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_35.wav",
        reference_wav_path="Referencefiles/analytical_test_35_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.35, 0.35, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="35.1",
        name='SDN test [SD=2.5m BS=2048 ABS=0.1]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,2.25,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Source distance: 2.5m\n"
            "\t-Buffer size: 2048\n"
            "\t-Absorption coefficient: 0.1\n"
        ),
        settings_file="analytical_test_35.json",
        test_target='SDNEnvironmentModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_35.1.wav",
        reference_wav_path="Referencefiles/analytical_test_35.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 2.25, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="36",
        name='DirectHRTF test [INT=ON NF=ON D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_36.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_36.wav",
        reference_wav_path="Referencefiles/analytical_test_36_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="36.1",
        name='DirectHRTF test [INT=ON NF=ON D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_36.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_36.1.wav",
        reference_wav_path="Referencefiles/analytical_test_36.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="36.2",
        name='DirectHRTF test [INT=ON NF=ON D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_36.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_36.2.wav",
        reference_wav_path="Referencefiles/analytical_test_36.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="37",
        name='DirectHRTF test [INT=ON NF=OFF D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_37.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_37.wav",
        reference_wav_path="Referencefiles/analytical_test_37_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="37.1",
        name='DirectHRTF test [INT=ON NF=OFF D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_37.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_37.1.wav",
        reference_wav_path="Referencefiles/analytical_test_37.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="37.2",
        name='DirectHRTF test [INT=ON NF=OFF D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_37.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_37.2.wav",
        reference_wav_path="Referencefiles/analytical_test_37.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="38",
        name='DirectHRTF test [INT=OFF NF=ON D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_38.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_38.wav",
        reference_wav_path="Referencefiles/analytical_test_38_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="38.1",
        name='DirectHRTF test [INT=OFF NF=ON D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_38.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_38.1.wav",
        reference_wav_path="Referencefiles/analytical_test_38.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="38.2",
        name='DirectHRTF test [INT=OFF NF=ON D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_38.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_38.2.wav",
        reference_wav_path="Referencefiles/analytical_test_38.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="39",
        name='DirectHRTF test [INT=OFF NF=OFF D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_39.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_39.wav",
        reference_wav_path="Referencefiles/analytical_test_39_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="39.1",
        name='DirectHRTF test [INT=OFF NF=OFF D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_39.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_39.1.wav",
        reference_wav_path="Referencefiles/analytical_test_39.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="39.2",
        name='DirectHRTF test [INT=OFF NF=OFF D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_39.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_39.2.wav",
        reference_wav_path="Referencefiles/analytical_test_39.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="40",
        name='DirectHRTF test [INT=ON NF=ON D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_40.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_40.wav",
        reference_wav_path="Referencefiles/analytical_test_40_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="40.1",
        name='DirectHRTF test [INT=ON NF=ON D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_40.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_40.1.wav",
        reference_wav_path="Referencefiles/analytical_test_40.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="40.2",
        name='DirectHRTF test [INT=ON NF=ON D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_40.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_40.2.wav",
        reference_wav_path="Referencefiles/analytical_test_40.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="41",
        name='DirectHRTF test [INT=ON NF=OFF D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_41.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_41.wav",
        reference_wav_path="Referencefiles/analytical_test_41_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="41.1",
        name='DirectHRTF test [INT=ON NF=OFF D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_41.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_41.1.wav",
        reference_wav_path="Referencefiles/analytical_test_41.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="41.2",
        name='DirectHRTF test [INT=ON NF=OFF D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_41.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_41.2.wav",
        reference_wav_path="Referencefiles/analytical_test_41.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="42",
        name='DirectHRTF test [INT=OFF NF=ON D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_42.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_42.wav",
        reference_wav_path="Referencefiles/analytical_test_42_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="42.1",
        name='DirectHRTF test [INT=OFF NF=ON D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_42.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_42.1.wav",
        reference_wav_path="Referencefiles/analytical_test_42.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="42.2",
        name='DirectHRTF test [INT=OFF NF=ON D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_42.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_42.2.wav",
        reference_wav_path="Referencefiles/analytical_test_42.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="43",
        name='DirectHRTF test [INT=OFF NF=OFF D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_43.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_43.wav",
        reference_wav_path="Referencefiles/analytical_test_43_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="43.1",
        name='DirectHRTF test [INT=OFF NF=OFF D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_43.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_43.1.wav",
        reference_wav_path="Referencefiles/analytical_test_43.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="43.2",
        name='DirectHRTF test [INT=OFF NF=OFF D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_43.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_43.2.wav",
        reference_wav_path="Referencefiles/analytical_test_43.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="44",
        name='DirectHRTF test [INT=ON NF=ON D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_44.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_44.wav",
        reference_wav_path="Referencefiles/analytical_test_44_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="44.1",
        name='DirectHRTF test [INT=ON NF=ON D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_44.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_44.1.wav",
        reference_wav_path="Referencefiles/analytical_test_44.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="44.2",
        name='DirectHRTF test [INT=ON NF=ON D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_44.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_44.2.wav",
        reference_wav_path="Referencefiles/analytical_test_44.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="45",
        name='DirectHRTF test [INT=ON NF=OFF D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_45.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_45.wav",
        reference_wav_path="Referencefiles/analytical_test_45_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="45.1",
        name='DirectHRTF test [INT=ON NF=OFF D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_45.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_45.1.wav",
        reference_wav_path="Referencefiles/analytical_test_45.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="45.2",
        name='DirectHRTF test [INT=ON NF=OFF D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: ON\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_45.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_45.2.wav",
        reference_wav_path="Referencefiles/analytical_test_45.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="46",
        name='DirectHRTF test [INT=OFF NF=ON D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_46.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_46.wav",
        reference_wav_path="Referencefiles/analytical_test_46_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="46.1",
        name='DirectHRTF test [INT=OFF NF=ON D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_46.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_46.1.wav",
        reference_wav_path="Referencefiles/analytical_test_46.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="46.2",
        name='DirectHRTF test [INT=OFF NF=ON D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_46.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_46.2.wav",
        reference_wav_path="Referencefiles/analytical_test_46.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="47",
        name='DirectHRTF test [INT=OFF NF=OFF D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_47.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_47.wav",
        reference_wav_path="Referencefiles/analytical_test_47_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="47.1",
        name='DirectHRTF test [INT=OFF NF=OFF D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_47.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_47.1.wav",
        reference_wav_path="Referencefiles/analytical_test_47.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="47.2",
        name='DirectHRTF test [INT=OFF NF=OFF D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Interpolation: OFF\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_47.json",
        test_target='ListenerDirectHRTFConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_47.2.wav",
        reference_wav_path="Referencefiles/analytical_test_47.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="48",
        name='AmbisonicVLS test [AO=1 NF=ON D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_48.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_48.wav",
        reference_wav_path="Referencefiles/analytical_test_48_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="48.1",
        name='AmbisonicVLS test [AO=1 NF=ON D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_48.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_48.1.wav",
        reference_wav_path="Referencefiles/analytical_test_48.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="48.2",
        name='AmbisonicVLS test [AO=1 NF=ON D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_48.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_48.2.wav",
        reference_wav_path="Referencefiles/analytical_test_48.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="49",
        name='AmbisonicVLS test [AO=1 NF=OFF D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_49.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_49.wav",
        reference_wav_path="Referencefiles/analytical_test_49_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="49.1",
        name='AmbisonicVLS test [AO=1 NF=OFF D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_49.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_49.1.wav",
        reference_wav_path="Referencefiles/analytical_test_49.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="49.2",
        name='AmbisonicVLS test [AO=1 NF=OFF D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_49.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_49.2.wav",
        reference_wav_path="Referencefiles/analytical_test_49.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="50",
        name='AmbisonicVLS test [AO=3 NF=ON D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_50.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_50.wav",
        reference_wav_path="Referencefiles/analytical_test_50_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="50.1",
        name='AmbisonicVLS test [AO=3 NF=ON D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_50.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_50.1.wav",
        reference_wav_path="Referencefiles/analytical_test_50.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="50.2",
        name='AmbisonicVLS test [AO=3 NF=ON D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_50.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_50.2.wav",
        reference_wav_path="Referencefiles/analytical_test_50.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="51",
        name='AmbisonicVLS test [AO=3 NF=OFF D=0.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_51.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_51.wav",
        reference_wav_path="Referencefiles/analytical_test_51_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="51.1",
        name='AmbisonicVLS test [AO=3 NF=OFF D=1.2m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_51.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_51.1.wav",
        reference_wav_path="Referencefiles/analytical_test_51.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="51.2",
        name='AmbisonicVLS test [AO=3 NF=OFF D=10m BS=128]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 128\n"
        ),
        settings_file="analytical_test_51.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_51.2.wav",
        reference_wav_path="Referencefiles/analytical_test_51.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="52",
        name='AmbisonicVLS test [AO=1 NF=ON D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_52.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_52.wav",
        reference_wav_path="Referencefiles/analytical_test_52_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="52.1",
        name='AmbisonicVLS test [AO=1 NF=ON D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_52.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_52.1.wav",
        reference_wav_path="Referencefiles/analytical_test_52.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="52.2",
        name='AmbisonicVLS test [AO=1 NF=ON D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_52.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_52.2.wav",
        reference_wav_path="Referencefiles/analytical_test_52.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="53",
        name='AmbisonicVLS test [AO=1 NF=OFF D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_53.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_53.wav",
        reference_wav_path="Referencefiles/analytical_test_53_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="53.1",
        name='AmbisonicVLS test [AO=1 NF=OFF D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_53.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_53.1.wav",
        reference_wav_path="Referencefiles/analytical_test_53.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="53.2",
        name='AmbisonicVLS test [AO=1 NF=OFF D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_53.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_53.2.wav",
        reference_wav_path="Referencefiles/analytical_test_53.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="54",
        name='AmbisonicVLS test [AO=3 NF=ON D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_54.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_54.wav",
        reference_wav_path="Referencefiles/analytical_test_54_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="54.1",
        name='AmbisonicVLS test [AO=3 NF=ON D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_54.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_54.1.wav",
        reference_wav_path="Referencefiles/analytical_test_54.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="54.2",
        name='AmbisonicVLS test [AO=3 NF=ON D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_54.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_54.2.wav",
        reference_wav_path="Referencefiles/analytical_test_54.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="55",
        name='AmbisonicVLS test [AO=3 NF=OFF D=0.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_55.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_55.wav",
        reference_wav_path="Referencefiles/analytical_test_55_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="55.1",
        name='AmbisonicVLS test [AO=3 NF=OFF D=1.2m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_55.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_55.1.wav",
        reference_wav_path="Referencefiles/analytical_test_55.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="55.2",
        name='AmbisonicVLS test [AO=3 NF=OFF D=10m BS=256]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 256\n"
        ),
        settings_file="analytical_test_55.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_55.2.wav",
        reference_wav_path="Referencefiles/analytical_test_55.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="56",
        name='AmbisonicVLS test [AO=1 NF=ON D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_56.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_56.wav",
        reference_wav_path="Referencefiles/analytical_test_56_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="56.1",
        name='AmbisonicVLS test [AO=1 NF=ON D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_56.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_56.1.wav",
        reference_wav_path="Referencefiles/analytical_test_56.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="56.2",
        name='AmbisonicVLS test [AO=1 NF=ON D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_56.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_56.2.wav",
        reference_wav_path="Referencefiles/analytical_test_56.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="57",
        name='AmbisonicVLS test [AO=1 NF=OFF D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_57.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_57.wav",
        reference_wav_path="Referencefiles/analytical_test_57_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="57.1",
        name='AmbisonicVLS test [AO=1 NF=OFF D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_57.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_57.1.wav",
        reference_wav_path="Referencefiles/analytical_test_57.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="57.2",
        name='AmbisonicVLS test [AO=1 NF=OFF D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 1\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_57.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_57.2.wav",
        reference_wav_path="Referencefiles/analytical_test_57.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="58",
        name='AmbisonicVLS test [AO=3 NF=ON D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_58.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_58.wav",
        reference_wav_path="Referencefiles/analytical_test_58_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="58.1",
        name='AmbisonicVLS test [AO=3 NF=ON D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_58.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_58.1.wav",
        reference_wav_path="Referencefiles/analytical_test_58.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="58.2",
        name='AmbisonicVLS test [AO=3 NF=ON D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: ON\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_58.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_58.2.wav",
        reference_wav_path="Referencefiles/analytical_test_58.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="59",
        name='AmbisonicVLS test [AO=3 NF=OFF D=0.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.14,0.14,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 0.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_59.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_59.wav",
        reference_wav_path="Referencefiles/analytical_test_59_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.14, 0.14, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="59.1",
        name='AmbisonicVLS test [AO=3 NF=OFF D=1.2m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.85,0.85,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 1.2m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_59.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_59.1.wav",
        reference_wav_path="Referencefiles/analytical_test_59.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.85, 0.85, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="59.2",
        name='AmbisonicVLS test [AO=3 NF=OFF D=10m BS=1024]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (7.1,7.1,0.0)\n"
            "\t-Record duration: 1 second\n"
            "\t-Ambisonic order: 3\n"
            "\t-Near field: OFF\n"
            "\t-Distance parameter: 10m\n"
            "\t-Buffer size: 1024\n"
        ),
        settings_file="analytical_test_59.json",
        test_target='ListenerAmbisonicVirtualLoudspeakersModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_59.2.wav",
        reference_wav_path="Referencefiles/analytical_test_59.2_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=1.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(7.1, 7.1, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    
    
    
    
    
    
    
    
    
    
    
    
    
    TestDefinition(
        id="60",
        name='DirectBRIR test [SP=ON INT=ON FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_60.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_60.wav",
        reference_wav_path="Referencefiles/analytical_test_60_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="60.1",
        name='DirectBRIR test [SP=ON INT=ON FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_60.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_60.1.wav",
        reference_wav_path="Referencefiles/analytical_test_60.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="61",
        name='DirectBRIR test [SP=ON INT=ON FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_61.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_61.wav",
        reference_wav_path="Referencefiles/analytical_test_61_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="61.1",
        name='DirectBRIR test [SP=ON INT=ON FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_61.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_61.1.wav",
        reference_wav_path="Referencefiles/analytical_test_61.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="62",
        name='DirectBRIR test [SP=ON INT=ON FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON(F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_62.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_62.wav",
        reference_wav_path="Referencefiles/analytical_test_62_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="62.1",
        name='DirectBRIR test [SP=ON INT=ON FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_62.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_62.1.wav",
        reference_wav_path="Referencefiles/analytical_test_62.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="63",
        name='DirectBRIR test [SP=ON INT=ON FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_63.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_63.wav",
        reference_wav_path="Referencefiles/analytical_test_63_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="63.1",
        name='DirectBRIR test [SP=ON INT=ON FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: ON\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_63.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_63.1.wav",
        reference_wav_path="Referencefiles/analytical_test_63.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="64",
        name='DirectBRIR test [SP=ON INT=OFF FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: OFF\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_64.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_64.wav",
        reference_wav_path="Referencefiles/analytical_test_64_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="65",
        name='DirectBRIR test [SP=ON INT=OFF FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: OFF\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_65.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_65.wav",
        reference_wav_path="Referencefiles/analytical_test_65_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="66",
        name='DirectBRIR test [SP=ON INT=OFF FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: OFF\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_66.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_66.wav",
        reference_wav_path="Referencefiles/analytical_test_66_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="67",
        name='DirectBRIR test [SP=ON INT=OFF FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Spatialization: ON\n"
            "\t-Interpolation: OFF\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_67.json",
        test_target='ListenerDirectBRIRConvolutionModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_67.wav",
        reference_wav_path="Referencefiles/analytical_test_67_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    
    TestDefinition(
        id="68",
        name='RVL test [AO=1 FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_68.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_68.wav",
        reference_wav_path="Referencefiles/analytical_test_68_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="68.1",
        name='RVL test [AO=1 FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_68.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_68.1.wav",
        reference_wav_path="Referencefiles/analytical_test_68.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="69",
        name='RVL test [AO=1 FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_69.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_69.wav",
        reference_wav_path="Referencefiles/analytical_test_69_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="69.1",
        name='RVL test [AO=1 FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_69.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_69.1.wav",
        reference_wav_path="Referencefiles/analytical_test_69.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="70",
        name='RVL test [AO=1 FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_70.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_70.wav",
        reference_wav_path="Referencefiles/analytical_test_70_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="70.1",
        name='RVL test [AO=1 FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_70.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_70.1.wav",
        reference_wav_path="Referencefiles/analytical_test_70.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="71",
        name='RVL test [AO=1 FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_71.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_71.wav",
        reference_wav_path="Referencefiles/analytical_test_71_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="71.1",
        name='RVL test [AO=1 FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_71.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_71.1.wav",
        reference_wav_path="Referencefiles/analytical_test_71.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="72",
        name='RVL test [AO=3 FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_72.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_72.wav",
        reference_wav_path="Referencefiles/analytical_test_72_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="72.1",
        name='RVL test [AO=1 FI=ON FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_72.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_72.1.wav",
        reference_wav_path="Referencefiles/analytical_test_72.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="73",
        name='RVL test [AO=3 FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_73.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_73.wav",
        reference_wav_path="Referencefiles/analytical_test_73_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="73.1",
        name='RVL test [AO=1 FI=ON FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: ON (FI: 50 ms ,Rise: 10 ms)\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_73.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_73.1.wav",
        reference_wav_path="Referencefiles/analytical_test_73.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="74",
        name='RVL test [AO=3 FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_74.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_74.wav",
        reference_wav_path="Referencefiles/analytical_test_74_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
     TestDefinition(
        id="74.1",
        name='RVL test [AO=1 FI=OFF FO=ON]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: ON (F0: 1 second ,Rise: 100 ms)\n"
        ),
        settings_file="analytical_test_74.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_74.1.wav",
        reference_wav_path="Referencefiles/analytical_test_74.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="75",
        name='RVL test [AO=3 FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (1.0,0.0,0.0)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_75.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_75.wav",
        reference_wav_path="Referencefiles/analytical_test_75_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(1.0, 0.0, 0.0),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    TestDefinition(
        id="75.1",
        name='RVL test [AO=1 FI=OFF FO=OFF]',
        description=(
            "A stereo impulse response will be generated using BeRTA and compared with a reference file, using a strict NRMSE per channel.\n"
            "\t-Impulse position: (0.75,0.43,0.5)\n"
            "\t-Record duration: 2 second\n"
            "\t-Ambisonic Order: 1\n"
            "\t-Fade In: OFF\n"
            "\t-Fade Out: OFF\n"
        ),
        settings_file="analytical_test_75.json",
        test_target='ListenerAmbisonicReverberantVirtualLoudspeakerModel',
        test_type=TestType.ANALYTICAL,
        generated_wav_path="Results/analytical_ir/generated_test_75.1.wav",
        reference_wav_path="Referencefiles/analytical_test_75.1_reference.wav",
        nrmse_margin_percent=1.0,
        osc_action_timeout_seconds=5.0,
        ir_duration_seconds=2.0,
        ir_period_samples=0,
        ir_delay_samples=0,
        ir_position=(0.75, 0.43, 0.5),
        enable_complementary_diagnostics=True,
        detect_channel_swap=True,
    ),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    TestDefinition(
        id="339",
        name='Perceptual localization test',
        description=(
            "You will hear the source in front of you and it will move toward one ear."
        ),
        settings_file="test1.json",
        test_target='Perceptual localization',
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


def group_tests_by_target(
    tests: Iterable[TestDefinition],
) -> tuple[tuple[str, tuple[TestDefinition, ...]], ...]:
    """Group tests by target while preserving their registry order."""
    groups: dict[str, list[TestDefinition]] = {}
    for test in tests:
        groups.setdefault(test.test_target, []).append(test)
    return tuple((target, tuple(items)) for target, items in groups.items())
