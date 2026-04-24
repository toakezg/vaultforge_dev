"""Prompt preset discovery for the VaultForge Code scaffold."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from .config import default_paths
from .models import BridgePaths, PromptTemplate

PRESET_MODES = ("review", "implement", "tighten", "audit", "scaffold")


def list_prompt_templates(
    root: Path | None = None,
    *,
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
    paths: BridgePaths | None = None,
) -> tuple[PromptTemplate, ...]:
    """Return the expected prompt template files for every preset mode."""

    resolved_paths = paths or default_paths(root, env=env, overrides=overrides)
    return tuple(
        PromptTemplate(mode=mode, path=resolved_paths.prompts_dir / f"{mode}.md")
        for mode in PRESET_MODES
    )


def prompt_path_for_mode(
    mode: str,
    root: Path | None = None,
    *,
    env: Mapping[str, str] | None = None,
    overrides: Mapping[str, object] | None = None,
    paths: BridgePaths | None = None,
) -> Path:
    """Resolve a preset mode to its prompt path."""

    if mode not in PRESET_MODES:
        valid = ", ".join(PRESET_MODES)
        raise ValueError(f"Unknown mode '{mode}'. Expected one of: {valid}")
    resolved_paths = paths or default_paths(root, env=env, overrides=overrides)
    return resolved_paths.prompts_dir / f"{mode}.md"
