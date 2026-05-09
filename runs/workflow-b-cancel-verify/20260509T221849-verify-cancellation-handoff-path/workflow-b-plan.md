# Workflow B Plan

- Run id: `20260509T221849-verify-cancellation-handoff-path`
- Created: `2026-05-09T22:18:49+10:00`
- Root: `F:\vaultforge`
- Cycles: `1`
- Execute: `True`
- Parallel: `False`
- Commit mode: `review`
- Workflow review every: `2`
- Watch workflows: `True`
- Timebox minutes: `0.0`
- Usage budget USD: `0.0`
- Estimated agent USD: `0.0`
- Hard gate mode: `switch-safe`
- Task: Verify cancellation handoff path

## Agents

- root-coordinator: coordinator, lane `root`, workdir `F:\vaultforge`
- root-recorder: recorder, lane `root`, workdir `F:\vaultforge`

## Resume

```bat
run_workflow_b.bat --cycles 1 --lane root --task "Verify cancellation handoff path"
```
