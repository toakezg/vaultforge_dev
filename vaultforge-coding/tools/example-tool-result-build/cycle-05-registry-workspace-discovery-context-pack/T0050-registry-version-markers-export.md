# registry-version-markers-export

- id: T0050
- family: registry
- operation: export
- priority: p0-foundation
- safety: preview-write
- generated_at: 2026-05-13T00:01:10.698878+00:00

## Purpose

create a structured artifact covering version numbers, migration notes, and deprecation state

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
- source: tools\tool-list.md
- source: tools\tool-list-index.jsonl
- source: tools\tool-list-contracts.jsonl
- source: tools\tool-list-builder-workflow.md
- source: .obsidian\core-plugins.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0035-registry-output-specs-export.md
