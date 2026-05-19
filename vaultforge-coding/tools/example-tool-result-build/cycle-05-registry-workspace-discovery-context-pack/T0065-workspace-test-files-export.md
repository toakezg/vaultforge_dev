# workspace-test-files-export

- id: T0065
- family: workspace-discovery
- operation: export
- priority: p0-foundation
- safety: preview-write
- generated_at: 2026-05-13T00:01:13.395531+00:00

## Purpose

create a structured artifact covering test suites, fixtures, snapshots, and runtime test folders

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
- source: .obsidian\workspace.json
- source: tests\helpers.py
- source: tests\test_bridge.py
- source: tests\test_config.py
- source: tests\test_context_builder.py
- source: tests\test_event_writer.py
- source: tests\test_tool_runtime.py
- source: tests\test_usage_tracker.py
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
