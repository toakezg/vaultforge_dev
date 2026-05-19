# schema-json-files-export

- id: T0655
- family: schema-data
- operation: export
- priority: p1-high-use
- safety: preview-write
- generated_at: 2026-05-13T00:04:49.831924+00:00

## Purpose

create a structured artifact covering JSON files and JSONL records

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
- source: .obsidian\app.json
- source: .obsidian\appearance.json
- source: .obsidian\community-plugins.json
- source: .obsidian\core-plugins.json
- source: .obsidian\types.json
- source: .obsidian\workspace.json
- source: tools\tool-list-contracts.jsonl
- source: tools\tool-list-index.jsonl
- source: tools\Unknown.json
- source: tools\example-tool-result-build\catalog-list-cycle-4\list-output.json
