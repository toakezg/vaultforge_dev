# Verification

This section now has a scaffolded Python package and prompt asset layout for the
VaultForge Code bridge.

## What exists

- Python package skeleton under `src/vf_code_bridge`
- prompt preset placeholders under `assets/prompts`
- run/report/event asset folders with `assets/runs/live` and
  `assets/runs/examples`
- smoke-safe local usage tracking runs
- env-backed config loading with validated overrides
- lightweight usage/event tests

## What does not exist yet

- prompt compilation flow
- project context collection
- OpenAI Responses API execution
- richer run manifests and append-only usage log files

## Suggested checks

From `vaultforge-coding\`:

```powershell
$env:PYTHONPATH = "src"
python -m vf_code_bridge --help
$env:VF_CODE_MODEL = "gpt-5.4-mini"
$env:VF_CODE_RUNS_DIR = "assets/runs/live"
python -m vf_code_bridge implement --task "Local tracking smoke test" --input-tokens 120 --output-tokens 30 --duration-ms 250 --json
Remove-Item Env:VF_CODE_MODEL
Remove-Item Env:VF_CODE_RUNS_DIR
python -m compileall src tests
python -m pytest
```

The CLI should write a run artifact, append lifecycle events, update
`assets/reports/usage_summary.json`, respect validated env overrides, compile
cleanly, and pass the local test suite once `pytest` is available in the active
environment.
