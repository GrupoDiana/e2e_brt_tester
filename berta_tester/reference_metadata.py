from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from berta_tester.paths import project_root
from berta_tester.test_definition import TestDefinition


@dataclass(frozen=True)
class ReferenceMetadataResult:
    """Result of resolving and reading a reference metadata YAML file."""

    path: Path | None
    exists: bool
    parsed: bool
    content: str
    message: str


def _resolve_project_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return project_root() / path


def _candidate_metadata_paths(test: TestDefinition) -> list[Path]:
    if test.reference_metadata_path:
        return [_resolve_project_path(test.reference_metadata_path)]

    if not test.reference_wav_path:
        return []

    reference_wav = _resolve_project_path(test.reference_wav_path)
    return [
        reference_wav.with_suffix(".yaml"),
        reference_wav.with_suffix(".yml"),
    ]


def resolve_reference_metadata_path(test: TestDefinition) -> Path | None:
    """Return the configured or inferred YAML metadata path for a test.

    If reference_metadata_path is explicitly configured, that path is returned
    even if the file does not exist. Otherwise, the function searches for a YAML
    or YML file next to the reference WAV using the same stem.
    """
    candidates = _candidate_metadata_paths(test)
    if not candidates:
        return None

    if test.reference_metadata_path:
        return candidates[0]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    # Return the preferred inferred path so the UI can explain what it expected.
    return candidates[0]


def read_reference_metadata(test: TestDefinition) -> ReferenceMetadataResult:
    """Read and format a YAML metadata file for display.

    The YAML structure is intentionally not validated against a fixed schema.
    Different reference files may document different models, resources or
    parameters. If parsing fails, the raw file is still returned so the user can
    inspect it from the tester UI.
    """
    path = resolve_reference_metadata_path(test)
    if path is None:
        return ReferenceMetadataResult(
            path=None,
            exists=False,
            parsed=False,
            content="",
            message="No reference metadata path is configured or inferable for this test.",
        )

    if not path.exists():
        return ReferenceMetadataResult(
            path=path,
            exists=False,
            parsed=False,
            content="",
            message=f"Reference metadata YAML file not found: {path}",
        )

    if not path.is_file():
        return ReferenceMetadataResult(
            path=path,
            exists=False,
            parsed=False,
            content="",
            message=f"Reference metadata path is not a file: {path}",
        )

    raw_text = path.read_text(encoding="utf-8")

    try:
        data: Any = yaml.safe_load(raw_text)
    except yaml.YAMLError as error:
        return ReferenceMetadataResult(
            path=path,
            exists=True,
            parsed=False,
            content=raw_text,
            message=f"Could not parse YAML. Showing raw file content. YAML error: {error}",
        )

    if data is None:
        formatted = "# Empty YAML file"
    else:
        formatted = yaml.safe_dump(
            data,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        ).rstrip()

    return ReferenceMetadataResult(
        path=path,
        exists=True,
        parsed=True,
        content=formatted,
        message="Reference metadata YAML loaded successfully.",
    )
