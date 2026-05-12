import json
from pathlib import Path

import pytest

from vf_code_bridge.tool_runtime import (
    ToolRuntimeError,
    list_tools,
    load_tool_records,
    run_tool,
    run_tool_batch,
    select_tool_names,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row) + "\n" for row in rows),
        encoding="utf-8",
    )


def _seed_catalog(root: Path) -> None:
    rows = [
        {
            "id": "T0001",
            "num": 1,
            "tool": "registry-tool-manifests-scan",
            "category": "Core Registry & Contracts",
            "rel": "foundation",
            "specialty": "read-only inventory",
            "domain": "tool governance",
            "purpose": "find and list tool manifest files and declared tool metadata",
            "build": "read-only; use allowlisted roots",
            "operation": "scan",
            "subject_key": "registry-tool-manifests",
            "line": 1,
            "priority_tag": "p0-foundation",
            "family": "registry",
            "implementation_shape": "path-list",
            "safety_tags": ["read-only"],
            "shared_handler_key": "registry::scan::path-list",
            "status": "candidate",
        },
        {
            "id": "T0002",
            "num": 2,
            "tool": "registry-tool-manifests-validate",
            "category": "Core Registry & Contracts",
            "rel": "foundation",
            "specialty": "rule check",
            "domain": "tool governance",
            "purpose": "validate tool manifest files and declared tool metadata",
            "build": "read-only; return pass/fail",
            "operation": "validate",
            "subject_key": "registry-tool-manifests",
            "line": 2,
            "priority_tag": "p0-foundation",
            "family": "registry",
            "implementation_shape": "status-summary",
            "safety_tags": ["read-only"],
            "shared_handler_key": "registry::validate::status-summary",
            "status": "candidate",
        },
        {
            "id": "T0003",
            "num": 3,
            "tool": "registry-tool-manifests-export",
            "category": "Core Registry & Contracts",
            "rel": "foundation",
            "specialty": "preview artifact",
            "domain": "tool governance",
            "purpose": "create a structured artifact covering tool manifest files",
            "build": "preview-write by default",
            "operation": "export",
            "subject_key": "registry-tool-manifests",
            "line": 3,
            "priority_tag": "p0-foundation",
            "family": "registry",
            "implementation_shape": "markdown-report",
            "safety_tags": ["preview-write"],
            "shared_handler_key": "registry::export::markdown-report",
            "status": "candidate",
        },
    ]
    contracts = [
        {
            "id": row["id"],
            "tool": row["tool"],
            "family": row["family"],
            "operation": row["operation"],
            "priority_tag": row["priority_tag"],
            "safety_tags": row["safety_tags"],
            "implementation_shape": row["implementation_shape"],
            "shared_handler_key": row["shared_handler_key"],
            "contract": {
                "inputs": ["target_root"],
                "outputs": ["result"],
                "reads": ["allowlisted repo roots"],
                "writes": ["none"],
                "blocked": ["arbitrary paths"],
                "proof": ["fixture run"],
            },
        }
        for row in rows
    ]
    _write_jsonl(root / "tools" / "tool-list-index.jsonl", rows)
    _write_jsonl(root / "tools" / "tool-list-contracts.jsonl", contracts)
    (root / "tools" / "tool-list.md").write_text("# tools\n", encoding="utf-8")


def test_load_tool_records_reads_fixed_catalog(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    records = load_tool_records(tmp_path)

    assert "registry-tool-manifests-scan" in records
    assert records["registry-tool-manifests-scan"].family == "registry"


def test_run_tool_scan_and_validate_catalog(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    scan = run_tool("registry-tool-manifests-scan", root=tmp_path)
    validation = run_tool("registry-tool-manifests-validate", root=tmp_path)

    assert scan["status"] == "completed"
    assert scan["scan"]["counts"]["matched_items"] >= 1
    assert validation["validation"]["pass"] is True


def test_export_tool_dry_run_and_live_write(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    dry = run_tool("registry-tool-manifests-export", root=tmp_path)
    live = run_tool(
        "registry-tool-manifests-export",
        root=tmp_path,
        artifact_dir="tools/example-tool-result-build",
        dry_run=False,
    )

    assert "artifact_preview" in dry
    artifact_path = Path(live["artifact_path"])
    assert artifact_path.exists()
    assert json.loads(artifact_path.read_text(encoding="utf-8"))["record"]["id"] == "T0003"


def test_run_tool_blocks_outside_target_root(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    with pytest.raises(ToolRuntimeError, match="outside the workspace"):
        run_tool(
            "registry-tool-manifests-scan",
            root=tmp_path,
            target_root=str(tmp_path.parent),
        )


def test_live_batch_stores_each_tool_result(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    payload = run_tool_batch(
        [
            "registry-tool-manifests-scan",
            "registry-tool-manifests-validate",
        ],
        root=tmp_path,
        artifact_dir="tools/example-tool-result-build",
        dry_run=False,
    )

    result_dir = tmp_path / "tools" / "example-tool-result-build" / "tool-results"
    summary_path = tmp_path / "tools" / "example-tool-result-build" / "batch-summary.json"

    assert payload["tool_count"] == 2
    assert summary_path.exists()
    assert (result_dir / "T0001-registry-tool-manifests-scan.json").exists()
    assert (result_dir / "T0002-registry-tool-manifests-validate.json").exists()


def test_select_tool_names_filters_catalog(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    selected = select_tool_names(
        root=tmp_path,
        family="registry",
        operation="validate",
        limit=1,
    )

    assert selected == ("registry-tool-manifests-validate",)


def test_list_tools_returns_catalog_rows(tmp_path: Path) -> None:
    _seed_catalog(tmp_path)

    rows = list_tools(root=tmp_path, family="registry", limit=2)

    assert [row["id"] for row in rows] == ["T0001", "T0002"]
    assert rows[0]["operation"] == "scan"
