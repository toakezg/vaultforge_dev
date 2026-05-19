# codexrun-run-closeout-export

- id: T1130
- family: codex-run
- operation: export
- priority: p0-foundation
- safety: preview-write
- generated_at: 2026-05-13T00:10:00.198370+00:00

## Purpose

create a structured artifact covering final response facts, verification status, and changed-file list

## Contract

- inputs: target_root, scope, artifact_id, format
- outputs: artifact_path, artifact_id, summary
- reads: allowlisted repo roots
- writes: tools/artifacts, assets/reports
- blocked: arbitrary shell, arbitrary paths, secret printing, destructive writes
- proof: parse fixture, bad-input test, blocked-path test, artifact-exists check

## Evidence

- matched_items: 20
- catalog_tools: 1825
- catalog_missing_ids: 0
- source: CODEX_START.md
- source: vaultforge_code_codex_api_bridge_spec_v_2.md
- source: tests\test_tool_runtime.py
- source: tools\tool-runtime-build-status.md
- source: tools\example-tool-result-build\cost-route-cycle-3\dry-run-output.json
- source: tools\example-tool-result-build\cost-route-cycle-3\live-run-output.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
