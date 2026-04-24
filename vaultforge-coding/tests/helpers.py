from __future__ import annotations

from pathlib import Path

RUNTIME_ROOT = Path(__file__).resolve().parent / "runtime"


def runtime_path(*parts: str) -> Path:
    return RUNTIME_ROOT.joinpath(*parts)


def clear_matching_files(directory: Path, *patterns: str) -> None:
    if not directory.exists():
        return
    for pattern in patterns:
        for path in directory.glob(pattern):
            if path.is_file():
                path.unlink()


def reset_bridge_root(name: str) -> Path:
    root = runtime_path(name)
    clear_matching_files(root / "assets" / "runs" / "live", "*.json")
    clear_matching_files(root / "assets" / "runs" / "examples", "*.json")
    clear_matching_files(root / "assets" / "reports", "*.json", "*.jsonl", "*.md")
    clear_matching_files(root / "assets" / "events", "*.json", "*.jsonl")
    return root
