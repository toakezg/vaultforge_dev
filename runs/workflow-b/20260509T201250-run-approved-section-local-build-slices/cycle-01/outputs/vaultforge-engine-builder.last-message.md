Completed a narrow engine-local Workflow B slice.

Changed:
- [TASKS.md](F:/vaultforge/vaultforge-engine/TASKS.md): marked `engine-conf-dry-run-variants` and `engine-manifest-contract-review` complete, added follow-up tasks for dry-run smoke config and run-manifest field list, kept gallery hooks blocked behind the manifest field list.
- [PLAN.md](F:/vaultforge/vaultforge-engine/PLAN.md): recorded the two build-slice decisions.
- [CHANGELOG.md](F:/vaultforge/vaultforge-engine/CHANGELOG.md): added the 2026-05-09 engine-local slice note.
- [SIGN_UP.md](F:/vaultforge/vaultforge-engine/SIGN_UP.md): added the Workflow B builder/recorder handoff and next prompt.

Verification is blocked: every shell command failed before PowerShell started with `CryptUnprotectData failed: 2148073483`, including packet listing, `git status`, and a minimal PowerShell version check. I kept the change docs/task-only because I could not safely inspect or test code in this turn.