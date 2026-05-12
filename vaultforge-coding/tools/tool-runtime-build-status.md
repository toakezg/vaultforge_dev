# Tool Runtime Build Status

Status: first local fixed-contract runtime landed.

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
- `validate`: catalog continuity and duplicate-name validation.
- `summarize`: compact tool handoff summary.
- `diff`: low-risk catalog consistency diff.
- `route`: family/lane routing suggestion.
- `export`: preview-write/live local artifact export under allowed folders.

## Selector Mode

Tools can be selected by explicit name or by catalog filters. The same filter
surface can also list matching catalog rows without running tools:

```powershell
vaultforge-tool registry-tool-manifests-scan --target-root . --json
vaultforge-tool --family dot4-queue --operation validate --limit 3 --target-root . --json
vaultforge-tool --list --family registry --limit 5 --json
vaultforge-tool --family registry --limit 30 --target-root . --artifact-dir tools/example-tool-result-build/registry-cycle-1 --live --json
```

## Live Example Batches

Stored under `tools/example-tool-result-build`:

- `registry-cycle-1`: 30 registry tools live-tested.
- `dot4-cycle-2`: 20 `.4` queue tools live-tested.
- `cost-route-cycle-3`: 20 cost-route tools live-tested.
- `tool-builder-cycle-3`: 20 tool-builder tools live-tested.
- `catalog-list-cycle-4`: read-only catalog listing example.

Totals from this build pass:

- live per-tool result files: 90
- export payload files: 18
- dry-run output files: 4
- live-run output files: 4
- batch summaries: 4
- catalog list examples: 1

## Verification

Commands run:

```powershell
python -m compileall src tests
python -m pytest
vaultforge-tool registry-tool-manifests-scan registry-tool-manifests-validate --target-root . --json
vaultforge-tool --family dot4-queue --operation validate --limit 3 --target-root . --json
vaultforge-tool --list --family registry --limit 5 --json
```

Latest result:

- compile: passed
- pytest: 20 passed
- dry registry CLI smoke: passed
- dry selector CLI smoke: passed
- read-only catalog list CLI smoke: passed
- live local example batches: passed

## Next Build Slice

Recommended next cycle:

- add richer family-specific validation for `dot4-queue`;
- add markdown summary export alongside JSON examples;
- add blocked external/live-call negative tests for gated families.
