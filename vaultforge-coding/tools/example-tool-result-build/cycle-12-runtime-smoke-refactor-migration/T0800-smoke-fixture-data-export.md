# smoke-fixture-data-export

- id: T0800
- family: runtime-smoke
- operation: export
- priority: p3-later
- safety: external-gated, preview-write
- generated_at: 2026-05-13T00:05:33.522049+00:00

## Purpose

create a structured artifact covering seed data needed for repeatable smoke tests

## Contract

- inputs: target_root, scope, artifact_id, format
- outputs: artifact_path, artifact_id, summary
- reads: allowlisted repo roots
- writes: tools/artifacts, assets/reports
- blocked: arbitrary shell, arbitrary paths, secret printing, destructive writes, ungated external calls
- proof: parse fixture, bad-input test, blocked-path test, artifact-exists check

## Evidence

- matched_items: 20
- catalog_tools: 1825
- catalog_missing_ids: 0
- source: vaultforge_code_codex_api_bridge_spec_v_2.md
- source: tests\test_tool_runtime.py
- source: tools\tool-runtime-build-status.md
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0035-registry-output-specs-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0040-registry-risk-labels-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0045-registry-owner-notes-export.md
