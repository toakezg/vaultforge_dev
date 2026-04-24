"""Context builder placeholder for the VaultForge Code bridge."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ContextBuildResult:
    """Summary of a future context collection pass."""

    project_root: Path
    files_used: tuple[str, ...] = ()
    max_files: int | None = None
    include: tuple[str, ...] = ()
    exclude: tuple[str, ...] = ()
    skipped_reason: str = "Context loading is not implemented yet."


def build_context_manifest(
    project_root: Path,
    include: Iterable[str] = (),
    exclude: Iterable[str] = (),
    max_files: int | None = None,
) -> ContextBuildResult:
    """Return a neutral placeholder manifest until the real collector exists."""

    return ContextBuildResult(
        project_root=project_root.resolve(),
        max_files=max_files,
        include=tuple(include),
        exclude=tuple(exclude),
    )
