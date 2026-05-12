"""Fixed-contract local tool runtime for the VaultForge Code catalog."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Sequence

from .config import ConfigError, repository_root
from .file_ops import write_json

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
}
TEXT_SUFFIXES = {
    ".bat",
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsonl",
    ".md",
    ".ps1",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True, slots=True)
class ToolRecord:
    """One fixed tool definition loaded from the generated catalog index."""

    id: str
    tool: str
    category: str
    rel: str
    specialty: str
    domain: str
    purpose: str
    build: str
    operation: str
    priority_tag: str
    family: str
    implementation_shape: str
    safety_tags: tuple[str, ...]
    shared_handler_key: str

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "ToolRecord":
        """Create a tool record from a JSONL payload."""

        return cls(
            id=str(payload["id"]),
            tool=str(payload["tool"]),
            category=str(payload["category"]),
            rel=str(payload["rel"]),
            specialty=str(payload["specialty"]),
            domain=str(payload["domain"]),
            purpose=str(payload["purpose"]),
            build=str(payload["build"]),
            operation=str(payload.get("operation", "unknown")),
            priority_tag=str(payload.get("priority_tag", "")),
            family=str(payload.get("family", "")),
            implementation_shape=str(payload.get("implementation_shape", "")),
            safety_tags=tuple(str(tag) for tag in payload.get("safety_tags", ())),
            shared_handler_key=str(payload.get("shared_handler_key", "")),
        )


@dataclass(frozen=True, slots=True)
class ToolContract:
    """Generated compact contract for a fixed tool."""

    id: str
    tool: str
    contract: dict[str, Any]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> "ToolContract":
        """Create a contract from a JSONL payload."""

        return cls(
            id=str(payload["id"]),
            tool=str(payload["tool"]),
            contract=dict(payload["contract"]),
        )


class ToolRuntimeError(ValueError):
    """Raised when a tool call is invalid or blocked."""


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read a JSONL file into dictionaries."""

    if not path.exists():
        raise ConfigError(f"Required tool catalog file is missing: {path}")
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ConfigError(f"Invalid JSONL at {path}:{line_number}") from exc
    return rows


def load_tool_records(root: Path | None = None) -> dict[str, ToolRecord]:
    """Load tool records keyed by tool name."""

    workspace = (root or repository_root()).resolve()
    path = workspace / "tools" / "tool-list-index.jsonl"
    records = [ToolRecord.from_payload(payload) for payload in _read_jsonl(path)]
    return {record.tool: record for record in records}


def load_tool_contracts(root: Path | None = None) -> dict[str, ToolContract]:
    """Load compact contracts keyed by tool name."""

    workspace = (root or repository_root()).resolve()
    path = workspace / "tools" / "tool-list-contracts.jsonl"
    contracts = [ToolContract.from_payload(payload) for payload in _read_jsonl(path)]
    return {contract.tool: contract for contract in contracts}


def _under_root(path: Path, root: Path) -> bool:
    """Return whether path is inside root."""

    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _resolve_target(root: Path, target_root: str | None) -> Path:
    """Resolve and constrain a target root to the workspace."""

    if target_root:
        candidate = Path(target_root)
        if not candidate.is_absolute():
            candidate = root / candidate
    else:
        candidate = root
    resolved = candidate.resolve()
    if not _under_root(resolved, root):
        raise ToolRuntimeError(f"target_root is outside the workspace: {resolved}")
    if not resolved.exists():
        raise ToolRuntimeError(f"target_root does not exist: {resolved}")
    return resolved


def _safe_artifact_dir(root: Path, artifact_dir: str | None) -> Path:
    """Resolve and constrain an artifact directory."""

    base = root / "tools" / "example-tool-result-build"
    candidate = Path(artifact_dir) if artifact_dir else base
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve()
    allowed = (
        root / "tools" / "example-tool-result-build",
        root / "tools" / "artifacts",
        root / "assets" / "reports",
    )
    if not any(_under_root(resolved, parent.resolve()) for parent in allowed):
        raise ToolRuntimeError(
            "artifact_dir must be under tools/example-tool-result-build, "
            "tools/artifacts, or assets/reports"
        )
    return resolved


def _keywords(record: ToolRecord) -> tuple[str, ...]:
    """Derive simple search terms from one tool record."""

    text = " ".join(
        (
            record.tool,
            record.category,
            record.domain,
            record.purpose,
            record.family,
        )
    ).lower()
    raw = re.findall(r"[a-z0-9]{3,}", text)
    blocked = {"tool", "tools", "and", "for", "the", "with", "into", "from"}
    ordered = []
    for item in raw:
        if item in blocked or item in ordered:
            continue
        ordered.append(item)
    return tuple(ordered[:12])


def _iter_candidate_files(target: Path, *, max_files: int) -> list[Path]:
    """Collect candidate text files under a target root."""

    files: list[Path] = []
    for path in target.rglob("*"):
        if len(files) >= max_files:
            break
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def _path_matches(path: Path, keywords: Sequence[str]) -> bool:
    """Check whether a path matches any keyword."""

    lowered = str(path).lower()
    return any(keyword in lowered for keyword in keywords)


def _scan(record: ToolRecord, target: Path, *, max_items: int) -> dict[str, Any]:
    """Run a bounded read-only path scan."""

    keywords = _keywords(record)
    candidates = _iter_candidate_files(target, max_files=max(max_items * 10, max_items))
    matches = [path for path in candidates if _path_matches(path, keywords)]
    if record.family == "registry":
        registry_paths = [
            target / "tools" / "tool-list.md",
            target / "tools" / "tool-list-index.jsonl",
            target / "tools" / "tool-list-contracts.jsonl",
            target / "tools" / "tool-list-builder-workflow.md",
        ]
        matches = [path for path in registry_paths if path.exists()] + matches
    if not matches:
        matches = candidates[:max_items]
    unique_matches = []
    seen = set()
    for path in matches:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_matches.append(path)
        if len(unique_matches) >= max_items:
            break
    return {
        "keywords": keywords,
        "items": [str(path.relative_to(target)) for path in unique_matches],
        "counts": {
            "candidate_files": len(candidates),
            "matched_items": len(unique_matches),
        },
        "source_root": str(target),
    }


def _catalog_stats(root: Path) -> dict[str, Any]:
    """Return basic catalog statistics."""

    records = load_tool_records(root)
    ids = sorted(int(record.id[1:]) for record in records.values())
    names = [record.tool for record in records.values()]
    name_counts = Counter(names)
    family_counts = Counter(record.family for record in records.values())
    return {
        "tool_count": len(records),
        "min_id": min(ids) if ids else 0,
        "max_id": max(ids) if ids else 0,
        "missing_ids": [
            f"T{num:04d}" for num in range(min(ids), max(ids) + 1) if num not in ids
        ]
        if ids
        else [],
        "duplicate_names": sorted(name for name, count in name_counts.items() if count > 1),
        "top_families": family_counts.most_common(10),
    }


def run_tool(
    tool_name: str,
    *,
    root: Path | None = None,
    target_root: str | None = None,
    artifact_dir: str | None = None,
    max_items: int = 20,
    dry_run: bool = True,
) -> dict[str, Any]:
    """Run one fixed catalog tool by name."""

    workspace = (root or repository_root()).resolve()
    records = load_tool_records(workspace)
    contracts = load_tool_contracts(workspace)
    if tool_name not in records:
        raise ToolRuntimeError(f"Unknown tool: {tool_name}")
    record = records[tool_name]
    contract = contracts.get(tool_name)
    target = _resolve_target(workspace, target_root)
    timestamp = datetime.now(UTC).isoformat()
    operation = record.operation
    scan_result = _scan(record, target, max_items=max_items)
    stats = _catalog_stats(workspace)
    result: dict[str, Any] = {
        "tool": record.tool,
        "id": record.id,
        "status": "completed",
        "dry_run": dry_run,
        "timestamp": timestamp,
        "category": record.category,
        "family": record.family,
        "operation": operation,
        "safety_tags": record.safety_tags,
        "implementation_shape": record.implementation_shape,
        "shared_handler_key": record.shared_handler_key,
        "contract": contract.contract if contract else None,
    }

    if operation == "scan":
        result["scan"] = scan_result
    elif operation == "validate":
        issues = []
        if stats["missing_ids"]:
            issues.append({"code": "missing_ids", "items": stats["missing_ids"][:10]})
        if stats["duplicate_names"]:
            issues.append({"code": "duplicate_names", "items": stats["duplicate_names"][:10]})
        result["validation"] = {
            "pass": not issues,
            "issues": issues,
            "next_tool": "",
            "catalog": stats,
        }
    elif operation == "summarize":
        result["summary"] = {
            "brief": (
                f"{record.tool} is a {record.specialty} tool in {record.category}; "
                f"it uses {record.implementation_shape} and belongs to {record.family}."
            ),
            "matched_items": scan_result["items"][:5],
            "blockers": [],
        }
    elif operation == "diff":
        result["diff"] = {
            "baseline": "generated contract catalog",
            "added": [],
            "changed": [],
            "missing": stats["missing_ids"],
            "risk_level": "low" if not stats["missing_ids"] else "medium",
        }
    elif operation == "route":
        result["route"] = {
            "target_lane": record.family,
            "confidence": "medium",
            "blockers": [],
            "required_proof": ["fixture run", "blocked-path negative test"],
        }
    elif operation == "export":
        artifact_root = _safe_artifact_dir(workspace, artifact_dir)
        artifact_path = artifact_root / f"{record.id}-{record.tool}.json"
        artifact_payload = {
            "record": asdict(record),
            "scan": scan_result,
            "catalog": stats,
            "contract": contract.contract if contract else None,
            "generated_at": timestamp,
        }
        if dry_run:
            result["artifact_preview"] = str(artifact_path)
        else:
            write_json(artifact_path, artifact_payload)
            result["artifact_path"] = str(artifact_path)
    else:
        result["status"] = "unsupported"
        result["error"] = f"Unsupported operation: {operation}"
    return result


def run_tool_batch(
    tool_names: Sequence[str],
    *,
    root: Path | None = None,
    target_root: str | None = None,
    artifact_dir: str | None = None,
    max_items: int = 20,
    dry_run: bool = True,
) -> dict[str, Any]:
    """Run a deterministic batch of fixed tools."""

    workspace = (root or repository_root()).resolve()
    results = []
    for tool_name in tool_names:
        results.append(
            run_tool(
                tool_name,
                root=workspace,
                target_root=target_root,
                artifact_dir=artifact_dir,
                max_items=max_items,
                dry_run=dry_run,
            )
        )
    payload = {
        "status": "completed",
        "dry_run": dry_run,
        "tool_count": len(results),
        "results": results,
    }
    if not dry_run:
        artifact_root = _safe_artifact_dir(workspace, artifact_dir)
        result_dir = artifact_root / "tool-results"
        for result in results:
            write_json(result_dir / f"{result['id']}-{result['tool']}.json", result)
        write_json(
            artifact_root / "batch-summary.json",
            {
                "status": payload["status"],
                "dry_run": payload["dry_run"],
                "tool_count": payload["tool_count"],
                "tools": [
                    {
                        "id": result["id"],
                        "tool": result["tool"],
                        "status": result["status"],
                        "operation": result["operation"],
                    }
                    for result in results
                ],
            },
        )
    return payload


def select_tool_names(
    *,
    root: Path | None = None,
    family: str | None = None,
    priority: str | None = None,
    operation: str | None = None,
    limit: int | None = None,
) -> tuple[str, ...]:
    """Select fixed tool names from catalog filters."""

    workspace = (root or repository_root()).resolve()
    records = load_tool_records(workspace)
    selected = []
    for record in sorted(records.values(), key=lambda item: int(item.id[1:])):
        if family and record.family != family:
            continue
        if priority and record.priority_tag != priority:
            continue
        if operation and record.operation != operation:
            continue
        selected.append(record.tool)
        if limit is not None and len(selected) >= limit:
            break
    return tuple(selected)


def list_tools(
    *,
    root: Path | None = None,
    family: str | None = None,
    priority: str | None = None,
    operation: str | None = None,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    """List fixed catalog tools matching optional filters."""

    workspace = (root or repository_root()).resolve()
    records = load_tool_records(workspace)
    names = select_tool_names(
        root=workspace,
        family=family,
        priority=priority,
        operation=operation,
        limit=limit,
    )
    return [
        {
            "id": records[name].id,
            "tool": records[name].tool,
            "family": records[name].family,
            "operation": records[name].operation,
            "priority_tag": records[name].priority_tag,
            "safety_tags": records[name].safety_tags,
            "implementation_shape": records[name].implementation_shape,
        }
        for name in names
    ]


def build_parser() -> argparse.ArgumentParser:
    """Build the local tool runtime parser."""

    parser = argparse.ArgumentParser(
        prog="vaultforge-tool",
        description="Run fixed local tools from tools/tool-list-index.jsonl.",
    )
    parser.add_argument("tools", nargs="*", help="Fixed tool names to run.")
    parser.add_argument("--family", help="Select tools by family when names are omitted.")
    parser.add_argument("--priority", help="Select tools by priority tag when names are omitted.")
    parser.add_argument("--operation", help="Select tools by operation when names are omitted.")
    parser.add_argument("--limit", type=int, help="Cap selected tools.")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List selected tools without running them.",
    )
    parser.add_argument("--target-root", help="Workspace-relative target root.")
    parser.add_argument(
        "--artifact-dir",
        help="Workspace-relative artifact directory for export/live examples.",
    )
    parser.add_argument("--max-items", type=int, default=20)
    parser.add_argument("--live", action="store_true", help="Write approved preview artifacts.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point for fixed local tool calls."""

    parser = build_parser()
    namespace = parser.parse_args(argv)
    tool_names = tuple(namespace.tools)
    if namespace.list:
        payload = {
            "status": "completed",
            "dry_run": True,
            "tools": list_tools(
                family=namespace.family,
                priority=namespace.priority,
                operation=namespace.operation,
                limit=namespace.limit,
            ),
        }
        if namespace.json:
            print(json.dumps(payload, indent=2, default=str))
        else:
            print(f"VaultForge catalog tools: {len(payload['tools'])}")
            for item in payload["tools"]:
                print(f"- {item['id']} {item['tool']} [{item['family']}/{item['operation']}]")
        return 0
    if not tool_names:
        tool_names = select_tool_names(
            family=namespace.family,
            priority=namespace.priority,
            operation=namespace.operation,
            limit=namespace.limit,
        )
    if not tool_names:
        print("Tool runtime error: no tools selected")
        return 2
    try:
        payload = run_tool_batch(
            tool_names,
            target_root=namespace.target_root,
            artifact_dir=namespace.artifact_dir,
            max_items=namespace.max_items,
            dry_run=not namespace.live,
        )
    except (ConfigError, ToolRuntimeError) as exc:
        print(f"Tool runtime error: {exc}")
        return 2
    if namespace.json:
        print(json.dumps(payload, indent=2, default=str))
    else:
        print(
            f"VaultForge tool batch: {payload['tool_count']} tools, "
            f"dry_run={payload['dry_run']}"
        )
        for result in payload["results"]:
            print(f"- {result['id']} {result['tool']}: {result['status']}")
    return 0
