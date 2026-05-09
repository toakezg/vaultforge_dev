# VaultForge Engine

VaultForge Engine is the planned shared generation core for VaultForge lanes.

This folder now contains the first copy-based engine prototype. The source generator was copied from:

```text
E:\tools\image_generation\vaultforge-art
```

That sibling project is dirty, so this prototype was copied without modifying the sibling worktree.

## Purpose

`vaultforge-engine` should eventually own reusable generation behavior:

- CLI parsing
- config and `@file.conf` argument support
- prompt loading
- markdown/frontmatter prompt cleanup
- batch mode
- preset/style/mod plumbing
- output path helpers
- metadata writing
- API request building
- native client/job/tag context metadata and variant loops
- native image input/reference plumbing for local files and Markdown embeds

## Consumers

Expected consumers:

- `vaultforge-art` for art experiments and playground output
- `vaultforge-business` for client logos, icons, covers, brand boards, and galleries
- future lanes such as icons, social, print, or project-specific packs

## Current Status

The first prototype preserves the current shared CLI behavior under:

```text
src\generate.py
```

It also includes copied/adapted tests and a simple Windows launcher:

```text
tests\test_generate.py
run_engine.bat
```

See `VERIFICATION.md` for the first dry-run and unit-test notes.

Business now targets the shared engine directly through `run_business.ps1`.

The engine now accepts native low-risk business handoff flags:

```text
--client
--job
--tag
--variants
--input-image
--reference-image
```

The context and variant fields affect output naming, variant count, dry-run
previews, and optional sidecar run metadata. They do not inject lane context
into prompt text; business and art wrappers still own their lane-specific prompt
composition.

`--input-image` and `--reference-image` attach local `.png`, `.jpg`, `.jpeg`,
`.webp`, `.gif`, `.svg`, or `.ico` files to the Responses API request as image
inputs. Markdown batch prompt notes can also embed images with standard
`![alt](path.png)`, Obsidian wiki embeds like `![[path.png]]`, or simple
`<img src="path.png">` tags; the engine removes the embed syntax from the text
prompt and sends the image file beside the composed prompt. Relative Markdown
image paths resolve from the prompt note's folder first.

## Execution For Now

Keep engine execution launcher-based or direct-script based for now:

```text
py .\src\generate.py ...
.\run_engine.bat ...
```

This keeps the current business and art wrappers aligned with the verified
prototype and avoids making a dedicated editable install in `.venv` part of the
shared engine contract before the package shape settles.

`run_engine.bat` will use `.venv\Scripts\python.exe` if that local environment
already exists, but the engine does not require an editable install yet.
