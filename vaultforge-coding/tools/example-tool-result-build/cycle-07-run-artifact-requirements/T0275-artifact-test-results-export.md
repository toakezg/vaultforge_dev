# artifact-test-results-export

- id: T0275
- family: run-artifact
- operation: export
- priority: p1-high-use
- safety: preview-write
- generated_at: 2026-05-13T00:02:22.094959+00:00

## Purpose

create a structured artifact covering unit, integration, and targeted test result artifacts

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
- source: .obsidian\community-plugins.json
- source: tests\helpers.py
- source: tests\test_bridge.py
- source: tests\test_config.py
- source: tests\test_context_builder.py
- source: tests\test_event_writer.py
- source: tests\test_tool_runtime.py
- source: tests\test_usage_tracker.py
- source: tools\tool-runtime-build-status.md
- source: tools\example-tool-result-build\cost-route-cycle-3\dry-run-output.json
