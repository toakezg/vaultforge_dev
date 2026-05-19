# prompt-live-pass-prompts-export

- id: T0200
- family: prompt-handoff
- operation: export
- priority: p0-foundation
- safety: live-write-gated, preview-write
- generated_at: 2026-05-13T00:01:55.036506+00:00

## Purpose

create a structured artifact covering GPT app or external live verification prompts

## Contract

- inputs: target_root, scope, artifact_id, format
- outputs: artifact_path, artifact_id, summary
- reads: allowlisted repo roots
- writes: tools/artifacts, assets/reports
- blocked: arbitrary shell, arbitrary paths, secret printing, destructive writes, ungated live writes
- proof: parse fixture, bad-input test, blocked-path test, artifact-exists check

## Evidence

- matched_items: 20
- catalog_tools: 1825
- catalog_missing_ids: 0
- source: tools\example-tool-result-build\cost-route-cycle-3\live-run-output.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0205-cost-usage-ledgers-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0210-cost-token-estimates-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0215-cost-model-choices-export.json
- source: tools\example-tool-result-build\cost-route-cycle-3\T0220-cost-budget-caps-export.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\live-run-output.json
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0035-registry-output-specs-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0040-registry-risk-labels-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0045-registry-owner-notes-export.md
- source: tools\example-tool-result-build\cycle-05-registry-workspace-discovery-context-pack\T0050-registry-version-markers-export.md
