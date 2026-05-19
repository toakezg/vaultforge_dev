# VaultForge Art

`vaultforge-art` is the active art lane for VaultForge.

It stays intentionally small:

- direct prompt generation for art-focused work
- inbox-based batch runs for repeatable prompts
- a thin wrapper over the shared `vaultforge-engine`
- local output routing in `output\`

## Quick Start

Set `ART_KEY` in `.env`, then use the wrapper:

```powershell
.\run_art.bat "a ceremonial brass compass floating above a midnight archive"
```

To run prompt files from the lane inbox:

```powershell
.\run_art.bat --batch inbox
```

Dry-runs are supported and should be the first check for new prompts:

```powershell
.\run_art.bat --dry-run "a minimal moonlit relic icon"
```

## Lane Files

- `CODEX_START.md` - entry order for Codex threads
- `SYSTEM.md` - lane rules and boundaries
- `PLAN.md` - current direction and watchpoints
- `TASKS.md` - active art work
- `CHANGELOG.md` - lane history
- `SIGN_UP.md` - thread handoff log
- `vaultforge-art_v00.md` - current baseline and v01 requirements
- `vaultforge-art_v01.md` - the promoted lane target state
