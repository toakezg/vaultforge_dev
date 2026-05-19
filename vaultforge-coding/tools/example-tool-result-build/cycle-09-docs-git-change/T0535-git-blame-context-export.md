# git-blame-context-export

- id: T0535
- family: git-change
- operation: export
- priority: p1-high-use
- safety: preview-write
- generated_at: 2026-05-13T00:03:44.525162+00:00

## Purpose

create a structured artifact covering recent authorship around risky lines

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
- source: Changelog-Auto.md
- source: CHANGELOG.md
- source: tests\test_context_builder.py
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\batch-summary.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\batch-summary.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\dry-run-output.json
