# cliwrap-dry-run-modes-export

- id: T1510
- family: cli-wrapper
- operation: export
- priority: p3-later
- safety: preview-write
- generated_at: 2026-05-13T00:12:25.264469+00:00

## Purpose

create a structured artifact covering preview or dry-run behavior that proves no writes happened

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
- source: tests\test_context_builder.py
- source: tests\test_tool_runtime.py
- source: tools\tool-list-builder-workflow.md
- source: tools\tool-runtime-build-status.md
- source: tools\example-tool-result-build\coverage-cycle-15-output.json
- source: tools\example-tool-result-build\cycle-05-14-summary.json
- source: tools\example-tool-result-build\catalog-list-cycle-4\list-output.json
- source: tools\example-tool-result-build\cost-route-cycle-3\batch-summary.json
- source: tools\example-tool-result-build\cost-route-cycle-3\dry-run-output.json
- source: tools\example-tool-result-build\cost-route-cycle-3\live-run-output.json
