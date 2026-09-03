from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TestNameCode:
    code: str
    meaning: str


TEST_NAME_CODES: tuple[TestNameCode, ...] = (
    TestNameCode("P", "Impulse position"),
    TestNameCode("CARD", "Source position relative to the cardioid"),
    TestNameCode("INT", "Interpolation"),
    TestNameCode("ATT", "Distance attenuation"),
    TestNameCode("PD", "Propagation delay"),
    TestNameCode("O", "ISM order"),
    TestNameCode("AO", "Ambisonic order"),
    TestNameCode("D", "Distance parameter"),
    TestNameCode("SD", "Source distance"),
    TestNameCode("BS", "Buffer size"),
    TestNameCode("ABS", "Absorption coefficient"),
    TestNameCode("NF", "Near field"),
    TestNameCode("FI", "Fade In"),
    TestNameCode("FO", "Fade Out"),
    TestNameCode("SP", "Spatialization")
)


TARGET_CODE_NAMES: dict[str, tuple[str, ...]] = {
    "ListenerDirectHRTFConvolutionModel": ("P", "INT", "NF", "D", "BS"),
    "Directivity": ("CARD", "INT"),
    "FreeFieldEnvironmentModel": ("ATT", "PD", "SD", "BS"),
    "ISMEnvironmentModel": ("O", "D", "SD", "BS", "ABS"),
    "SDNEnvironmentModel": ("SD", "BS", "ABS"),
    "ListenerAmbisonicVirtualLoudspeakersModel": ("AO", "NF", "D", "BS"),
    "ListenerDirectBRIRConvolutionModel": ("SP", "INT", "FI", "FO")
}


TARGET_EXAMPLES: dict[str, str] = {
    "ListenerDirectHRTFConvolutionModel": (
        "DirectHRTF test [INT=ON NF=OFF D=1.2m BS=256]"
    ),
    "Directivity": "Directivity test [CARD=in INT=15]",
    "FreeFieldEnvironmentModel": "FreeField test [PD=ON SD=10m BS=512]",
    "ISMEnvironmentModel": "ISM test [O=5 D=20 SD=2.5m BS=2048 ABS=0.1]",
    "SDNEnvironmentModel": "SDN test [SD=2.5m BS=2048 ABS=0.1]",
    "ListenerAmbisonicVirtualLoudspeakersModel": (
        "AmbisonicVLS test [AO=3 NF=OFF D=10m BS=1024]"
    ),
    "ListenerDirectHRTFConvolutionModel": (
        "DirectBRIR test [SP=ON INT=ON FI=ON FO=ON]"
    )
}


COMMON_CODE_VALUES: tuple[tuple[str, str], ...] = (
    ("ON / OFF", "Enabled or disabled"),
    ("m", "Metres"),
    ("dB", "Decibels"),
)


def codes_for_target(target: str | None = None) -> tuple[TestNameCode, ...]:
    """Return all codes or only those used by one test target."""
    if target is None:
        return TEST_NAME_CODES

    selected = set(TARGET_CODE_NAMES.get(target, ()))
    return tuple(item for item in TEST_NAME_CODES if item.code in selected)
