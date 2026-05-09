Recorded the cycle as blocked rather than inventing results.

I added a run-packet handoff at [cycle-1-root-recorder-handoff.md](F:/vaultforge/runs/workflow-b/20260509T201250-run-approved-section-local-build-slices/cycle-1-root-recorder-handoff.md) and added a root coordination note in [CHANGELOG.md](F:/vaultforge/CHANGELOG.md).

Verification was blocked: every shell command failed before PowerShell started with `windows sandbox: CryptUnprotectData failed: 2148073483`. Because I could not inspect the run packet or current worktree, I did not update affected section handoffs or claim any builder/reviewer results.