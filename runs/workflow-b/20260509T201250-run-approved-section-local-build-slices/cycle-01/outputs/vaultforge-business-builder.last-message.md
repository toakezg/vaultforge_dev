Blocked before implementation.

Every shell command failed with:

```text
windows sandbox: CryptUnprotectData failed: 2148073483
```

So I did not inspect or modify `run_business.ps1` blindly. I recorded the hard gate in [SIGN_UP.md](F:/vaultforge/vaultforge-business/SIGN_UP.md) under `2026-05-09 - workflow-b builder hard gate`.

Files touched:
- `SIGN_UP.md` only

Verification:
- `apply_patch` succeeded for the handoff note.
- `git status --short` and all shell reads failed with the sandbox error above.

Resume point:
```text
Continue Workflow B cycle 1 for vaultforge-business. Read SIGN_UP.md latest entry, then implement business-engine-native-metadata-adoption if git status and wrapper/engine reads are available.
```