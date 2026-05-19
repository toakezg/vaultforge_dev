# obsidian-community-plugins-export

- id: T1210
- family: obsidian-plugin
- operation: export
- priority: p1-high-use
- safety: preview-write
- generated_at: 2026-05-13T00:10:33.597365+00:00

## Purpose

create a structured artifact covering community-plugins.json and enabled plugin ID alignment

## Contract

- inputs: target_root, scope, artifact_id, format
- outputs: artifact_path, artifact_id, summary
- reads: allowlisted repo roots, configured vault roots
- writes: tools/artifacts, assets/reports
- blocked: arbitrary shell, arbitrary paths, secret printing, destructive writes
- proof: parse fixture, bad-input test, blocked-path test, artifact-exists check

## Evidence

- matched_items: 20
- catalog_tools: 1825
- catalog_missing_ids: 0
- source: Changelog-Auto.md
- source: CHANGELOG.md
- source: CODEX_START.md
- source: PLAN.md
- source: pyproject.toml
- source: README.md
- source: requirements.txt
- source: setup_venv.bat
- source: SIGN_UP.md
- source: SYSTEM.md
