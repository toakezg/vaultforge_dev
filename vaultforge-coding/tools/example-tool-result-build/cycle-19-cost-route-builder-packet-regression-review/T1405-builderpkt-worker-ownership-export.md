# builderpkt-worker-ownership-export

- id: T1405
- family: builder-packet
- operation: export
- priority: p1-high-use
- safety: preview-write
- generated_at: 2026-05-13T00:11:47.419456+00:00

## Purpose

create a structured artifact covering file write ownership and conflict boundaries

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
- source: tools\tool-list-builder-workflow.md
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0035-registry-output-specs-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0040-registry-risk-labels-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0045-registry-owner-notes-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0050-registry-version-markers-export.md
