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
- shared gallery index generation from engine sidecar metadata

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
--api-key
--api-key-env
--gallery-index
--gallery-source
--gallery-output
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

By default, direct engine runs look for an OpenAI key in
`vaultforge-engine\.env`:

```text
VAULTFORGE_ENGINE_OPENAI_API_KEY=sk-your-key
```

Lane wrappers can override that per run with `--api-key`, or by passing one or
more lane-owned environment variable names with `--api-key-env`, for example
`--api-key-env VAULTFORGE_ICON_OPENAI_API_KEY`. For backward compatibility, the
engine also still accepts `IMAGE_GENERATION_KEY_B_OPENAI_API_KEY` and
`OPENAI_API_KEY` if they are already present.

The default generation model is pinned to `gpt-image-2-2026-04-21`. That is the
snapshot for GPT Image 2, the current state-of-the-art image generation model in
the OpenAI docs. Fallbacks are `gpt-image-2`, `gpt-5.5`, and `gpt-5.2`.

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

## Smoke Config

The committed smoke config is:

```text
assets\batch-input-smoke\smoke.conf
```

Run it from the engine folder with:

```powershell
py .\src\generate.py '@assets\batch-input-smoke\smoke.conf'
```

It includes `--dry-run`, batch prompt loading, explicit output routing, native
client/job/tag metadata, two variants, and a local `--reference-image`. It is
safe to run without an API key and should not write generated images or sidecar
JSON.

The first shared sidecar field list for future gallery/contact-sheet consumers
lives in `RUN_MANIFEST.md`.

## Gallery Index

The engine can build a small gallery index from existing sidecar JSON without
calling the image API:

```powershell
py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output assets\gallery-index.json
```

This reads engine-written sidecars, skips unrelated JSON, and writes a compact
index with one entry per valid sidecar. It is a shared hook for later gallery or
contact-sheet tooling; lane-specific gallery pages, review surfaces, and
delivery folders still belong to their lanes.

`--gallery-index` cannot be combined with `--dry-run` because building the index
is itself a write operation. Use the normal gallery-index command only when that
JSON output is intended.
