# vaultforge-art v01

`vaultforge-art_v00.md` captured the starting point and the requirements for promotion.

`v01` is the first usable art-lane pass.

## Current State

- The lane is now documented as an active art section.
- The lane has a thin wrapper over the shared engine.
- Direct prompt runs are lane-owned and save into `output\`.
- Batch prompt runs are lane-owned through `inbox\`.
- `ART_KEY` is the lane-owned API key entry point.

## v01 Requirements Met

- Engine hook through the shared `vaultforge-engine`
- Direct user input through the command line
- Inbox-based batch input through `inbox\`
- Local output routing through `output\`
- Dry-run support for safe prompt validation

## What Still Belongs in Later Passes

- Art-specific preset expansion
- Style libraries and prompt packs
- Output curation workflows
- Gallery or review surfaces for selected results
- Deeper testing once the lane starts producing real images regularly

## Exit Criteria

`vaultforge-art` can be treated as Active when the following stay easy to repeat:

- `.\run_art.bat --dry-run "prompt"` works
- `.\run_art.bat "prompt"` routes to the shared engine
- `.\run_art.bat --batch inbox` processes lane-owned prompt files
- generated images land in `output\`
