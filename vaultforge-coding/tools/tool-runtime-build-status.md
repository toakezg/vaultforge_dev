# Tool Runtime Build Status

Status: fixed-contract runtime landed and local example proof now covers all
1,825 catalog tool records.

## Runtime Surface

- CLI entry point: `vaultforge-tool`
- Source module: `src/vf_code_bridge/tool_runtime.py`
- Test module: `tests/test_tool_runtime.py`
- Catalog source: `tools/tool-list-index.jsonl`
- Contract source: `tools/tool-list-contracts.jsonl`

The runtime resolves a known tool name from the generated catalog before it runs.
It does not expose arbitrary shell, arbitrary path access, secret printing,
destructive writes, or live external calls.

## Supported Operations

- `scan`: bounded read-only path scan.
- `validate`: catalog continuity, duplicate-name validation, and family context
  for `.4` queue tools.
- `summarize`: compact tool handoff summary.
- `diff`: low-risk catalog consistency diff.
- `route`: family/lane routing suggestion.
- `export`: preview-write/live local artifact export under allowed folders.
- `coverage`: read-only/live-local report of catalog IDs with stored example
  proof.

Gated safety tags are surfaced in result metadata. External calls, paid API use,
destructive writes, and ungated live writes remain blocked in local proof mode.

## Selector Mode

Tools can be selected by explicit name or by catalog filters. The same filter
surface can also list matching catalog rows without running tools:

```powershell
vaultforge-tool registry-tool-manifests-scan --target-root . --json
vaultforge-tool --family dot4-queue --operation validate --limit 3 --target-root . --json
vaultforge-tool --list --family registry --limit 5 --json
vaultforge-tool --coverage --artifact-dir tools/example-tool-result-build/coverage-cycle-24 --live --json
vaultforge-tool registry-input-specs-export --artifact-dir tools/example-tool-result-build/manual --format markdown --live --json
vaultforge-tool --family registry --limit 30 --target-root . --artifact-dir tools/example-tool-result-build/registry-cycle-1 --live --json
```

## Live Example Batches

Stored under `tools/example-tool-result-build`:

- `registry-cycle-1`: 30 registry tools live-tested.
- `dot4-cycle-2`: 20 `.4` queue tools live-tested.
- `cost-route-cycle-3`: 20 cost-route tools live-tested.
- `tool-builder-cycle-3`: 20 tool-builder tools live-tested.
- `catalog-list-cycle-4`: read-only catalog listing example.
- `cycle-05-registry-workspace-discovery-context-pack`: 100 tools live-tested.
- `cycle-06-context-pack-prompt-handoff-cost-route`: 100 tools live-tested.
- `cycle-07-run-artifact-requirements`: 100 tools live-tested.
- `cycle-08-verification-review`: 100 tools live-tested.
- `cycle-09-docs-git-change`: 100 tools live-tested.
- `cycle-10-environment-security-privacy`: 100 tools live-tested.
- `cycle-11-schema-data-multi-agent`: 100 tools live-tested.
- `cycle-12-runtime-smoke-refactor-migration`: 100 tools live-tested.
- `cycle-13-quality-release-vaultforge-notes`: 100 tools live-tested.
- `cycle-14-tool-builder-vaultforge-section-codex-run`: 100 tools live-tested.
- `cycle-05-14-summary.json`: compact index of the 10-cycle expansion.
- `cycle-16-codex-run-mcp-proof`: 100 tools live-tested.
- `cycle-17-mcp-proof-obsidian-plugin-prompt-bank`: 100 tools live-tested.
- `cycle-18-prompt-bank-windows-local-cost-route`: 100 tools live-tested.
- `cycle-19-cost-route-builder-packet-regression-review`: 100 tools live-tested.
- `cycle-20-regression-review-cli-wrapper-document-source`: 100 tools live-tested.
- `cycle-21-prototype-archive-data-xp4l-event`: 100 tools live-tested.
- `cycle-22-xp4l-event-handoff-design-visual`: 100 tools live-tested.
- `cycle-23-dot4-queue`: 35 tools live-tested.
- `cycle-16-23-summary.json`: compact index of the final expansion cycles.
- `coverage-cycle-15`: checkpoint JSON and Markdown coverage report.
- `coverage-cycle-24`: final JSON and Markdown coverage report.
- `tools/review-refine/tool-proof-review-cycle-1.*`: first review/refine audit.
- `tools/review-refine/tool-proof-review-cycle-2.*`: clean second review/refine
  audit after summary range metadata refinement.

Current totals under `tools/example-tool-result-build`:

- live per-tool result files: 1,825
- JSON export payload files: 18
- Markdown export payload files: 347
- dry-run output files: 22
- live-run output files: 22
- JSON batch summaries: 22
- Markdown batch summaries: 18
- catalog list examples: 1
- coverage report artifacts: 4
- review/refine report artifacts: 4

Latest coverage report:

- catalog tools: 1,825
- live-tested tools: 1,825
- untested tools: 0
- coverage: 100.0%
- tested ranges: T0001-T1825
- untested ranges: none

Latest review/refine result:

- missing result IDs: 0
- duplicate result IDs: 0
- non-completed result statuses: 0
- contract/index mismatches: 0
- generated summary range issues: 0 after adding explicit `id_ranges`

## Verification

Commands run:

```powershell
python -m compileall src tests
python -m pytest
vaultforge-tool registry-tool-manifests-scan registry-tool-manifests-validate --target-root . --json
vaultforge-tool --family dot4-queue --operation validate --limit 3 --target-root . --json
vaultforge-tool --list --family registry --limit 5 --json
vaultforge-tool registry-input-specs-export --artifact-dir tools/example-tool-result-build/manual-md-smoke --format markdown --json
vaultforge-tool --coverage --json
```

Latest result:

- compile: passed
- pytest: 23 passed
- dry registry CLI smoke: passed
- dry selector CLI smoke: passed
- read-only catalog list CLI smoke: passed
- dry Markdown export preview smoke: passed
- coverage CLI smoke: passed
- live local example batches: passed

## Next Build Slice

Recommended next cycle:

- add CLI-level negative tests for bad artifact format and gated external tags;
- add richer family-specific validation where generic local proof is too thin;
- decide whether example artifacts should remain committed or be archived before
  heavier external/live-gated integrations.
