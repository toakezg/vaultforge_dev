"""Filesystem helpers for the VaultForge Code bridge."""

from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from .config import default_paths
from .models import BridgePaths


def ensure_directories(paths: Iterable[Path]) -> tuple[Path, ...]:
    """Create each directory if it does not already exist."""

    created = []
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return tuple(created)


def ensure_bridge_layout(
    root: Path | None = None,
    *,
    paths: BridgePaths | None = None,
) -> BridgePaths:
    """Create the expected asset folders and return the resolved path set."""

    resolved_paths = paths or default_paths(root)
    ensure_directories(
        (
            resolved_paths.assets_dir,
            resolved_paths.prompts_dir,
            resolved_paths.runs_root_dir,
            resolved_paths.runs_dir,
            resolved_paths.runs_examples_dir,
            resolved_paths.reports_dir,
            resolved_paths.events_dir,
        )
    )
    return resolved_paths


def _json_ready(value: Any) -> Any:
    """Convert values into JSON-serializable primitives."""

    if is_dataclass(value):
        return _json_ready(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_ready(item) for item in value]
    return value


def write_json(path: Path, payload: Any) -> Path:
    """Write one JSON document with stable formatting."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_json_ready(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def append_jsonl(path: Path, payload: Any) -> Path:
    """Append one JSONL line using UTF-8 encoding."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(_json_ready(payload), sort_keys=True))
        handle.write("\n")
    return path
