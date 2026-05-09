# Workflow B Plan

- Run id: `20260509T212911-verify-business-if-done-prompt-inclusion`
- Created: `2026-05-09T21:29:11+10:00`
- Root: `F:\vaultforge`
- Cycles: `1`
- Execute: `False`
- Parallel: `False`
- Commit mode: `review`
- Workflow review every: `2`
- Watch workflows: `True`
- Task: Verify business-if-done prompt inclusion

## Agents

- root-coordinator: coordinator, lane `root`, workdir `F:\vaultforge`
- vaultforge-business-builder: builder, lane `vaultforge-business`, workdir `F:\vaultforge\vaultforge-business`
- vaultforge-business-reviewer: reviewer, lane `vaultforge-business`, workdir `F:\vaultforge\vaultforge-business`
- root-recorder: recorder, lane `root`, workdir `F:\vaultforge`

## Resume

```bat
run_workflow_b.bat --cycles 1 --lane vaultforge-business --task "Verify business-if-done prompt inclusion"
```
