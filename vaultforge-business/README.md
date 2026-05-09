# VaultForge Business

VaultForge Business is the client-facing generation lane for logos, icons, covers, brand marks, social tiles, and reusable business asset packs.

Business now targets the sibling shared generator at `..\vaultforge-engine` by default. This folder provides business wrappers, prompt banks, metadata, and output routing so client work does not mix with playground output.

Start with `NATH_START.md` when you want the shortest operator map for this
lane: read order, feature map, safe command examples, hard gates, and future
work.

`BUSINESS_CLIENT_READY_CRITERIA.md` defines the current paid-client readiness
target and separates safe packaging/intake work from pricing, licensing,
publication, live generation, and cross-lane approval gates.

`delivery-package-template\` is the reusable delivery skeleton for reviewed
client jobs. It includes export, preview, source, review, archive, and usage
note folders plus a client-facing README template.

`BUSINESS_SERVICE_CATALOG.md` documents the current preset, style, and mod
service menu from wrapper names and prompt-bank usage. It is an internal
operator catalog, not a price sheet or launch approval.

`BUSINESS_OUTPUT_REVIEW_CHECKLIST.md` defines how generated outputs move from
gallery/contact-sheet review into selected, rejected, archived, and packaged
client-ready files.

`BUSINESS_PAID_LAUNCH_DECISION_NOTE.md` is the Nath-facing decision surface for
pricing shape, service positioning, licensing wording, publication channel,
pilot/live generation scope, revision policy, and example/privacy choices. It
prepares the launch gate; it does not approve paid launch by itself.

## Prompt Bank Map

- Root `*-pack.txt` files are the current runnable text packs for `run-client-pack.ps1`.
- `my-prompts-bank\_template` holds markdown frontmatter templates.
- `my-prompts-bank\_intake\client-intake-template.md` is a non-runnable client
  brief template for turning service-style requests into later prompt notes.
- `my-prompts-bank\example-client` is the first runnable markdown prompt pack.
- `my-prompts-bank\vaultforge` is the starter VaultForge system-brand prompt pack.
- `my-prompts-bank\_archive\legacy-one-offs` keeps old manual scratch prompts.
- `my-prompts-bank\VaultForge Business Dashboard.md` is the starter Dataview dashboard for sorting prompt notes.
- `prompt template` is a legacy pointer to the archive, not an active workflow.

See `my-prompts-bank\README.md` before adding or reorganizing prompt-bank files.

## Quick Start

Dry-run a smoke test:

```bat
run_business_smoke.bat
```

Business `-DryRun` calls the shared engine in dry-run mode without writing
business metadata or generated workspace folders. Use `-WhatIf` to preview the
engine command without calling it, or add `-WriteMetadata` to `-DryRun` when you
intentionally want fixture files such as `prompt.txt`, `run.json`, and
`gallery-entry.json`.

Run one business prompt:

```bat
run_business.bat "Premium logo for Empower You Plan Management" "empower-you" "logo" "pack-01" "ndis,premium,local"
```

Run the starter pack:

```bat
run-client-pack.bat "Empower You Plan Management" "empower-you" "logo-pack-01" "round1" ".\logo-pack.txt"
```

Preview a pack without running commands or touching `logs\run-log.csv`:

```powershell
powershell -ExecutionPolicy Bypass -File .\run-client-pack.ps1 -InputValue "Empower You Plan Management" -Client "empower-you" -Project "logo-pack-01" -Tag "round1" -PromptFile ".\logo-pack.txt" -WhatIf
```

Add `-LogWhatIf` when you intentionally want preview rows appended to
`logs\run-log.csv`.

Build a generated-output review summary from existing `gallery-entry.json` files:

```bat
build-review-summary.bat -OutFile ".\generated\_review\business-summary.md"
```

The summary helper scans the existing business `generated` root, counts image
files beside each manifest, and writes a Markdown table for quick browsing.
It does not change generation commands or the business output folder shape.

Build contact sheets beside generated image runs:

```bat
build-contact-sheets.bat -GeneratedRoot ".\generated"
```

The contact-sheet helper scans `gallery-entry.json` files and writes
`contact-sheet.jpg` beside image variants for quicker visual review.

Build the HTML gallery:

```bat
build-gallery.bat -GeneratedRoot ".\generated"
```

The gallery is written to `generated\_gallery\index.html` and groups generated
runs into image-backed cards using contact sheets when available.

Prepare a reviewed client delivery package:

```text
delivery-package-template\
  CLIENT_README.md
  exports\
  previews\
  usage-notes\
  sources\
  review\
  archive\
```

Copy this skeleton for a real package only after outputs are selected from the
gallery or contact sheets. Keep `exports\final` for approved client files and
keep prompts/manifests under `sources` for reproducibility.

Review generated outputs before packaging:

```text
BUSINESS_OUTPUT_REVIEW_CHECKLIST.md
```

Use the checklist with `gallery-entry.json`, `run.json`, contact sheets, the
HTML gallery, and delivery-package folders so final exports stay separated from
raw generations and rejected alternates.

Update a markdown prompt note after review:

```bat
update-prompt-note.bat -PromptPath ".\my-prompts-bank\example-client\logo-01.md" -Status review -Rating 8 -Notes "strong option"
```

Or update from a run folder that has `run.json` with `source_prompt_file`:

```bat
update-prompt-note.bat -RunDir ".\generated\client\asset\preset\style\date\job-name" -Status generated
```

Preview markdown prompt-bank execution without generating anything:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -IncludeTemplates -WhatIf -Limit 1
```

Run draft markdown notes through the business wrapper in dry-run mode:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun
```

To keep dry-run metadata fixtures from a markdown-bank run:

```bat
run_business_md_bank.bat -Path ".\my-prompts-bank" -DryRun -WriteMetadata
```

The markdown runner skips `_template` by default, ignores non-prompt notes such
as READMEs and dashboards, reads frontmatter, removes the opening H1 from the
prompt body, passes business fields into `run_business.ps1`, and saves the
source note beside the run as `prompt.source.md`.

## Output Shape

Business output is routed to:

```text
generated\{client_slug}\{asset_slug}\{business_preset_slug}\{primary_style_slug}\{date}\job-{job_slug}\
```

Each run writes:

- `prompt.txt`
- `run.json`
- `gallery-entry.json`
- generated image files
- engine image sidecar `.json` files when the shared engine writes per-image metadata

## Metadata Contract

`run.json` is the detailed run manifest. It keeps raw operator-facing fields
such as `client`, `asset_type`, `job`, `tag`, `business_preset`,
`business_styles`, and `business_mods`, then records matching `*_slug` fields
for downstream sorting and review.

`gallery-entry.json` is the lightweight browse/index manifest. It repeats the
same raw naming fields plus the slug fields needed to reconstruct folder and
filename-safe grouping without parsing the path.

Raw fields preserve what the operator typed. Slug fields are lower-case,
folder-safe values made from letters, numbers, and hyphens. Prefer kebab-case
for `client`, `asset_type`, and `job` inputs. Use `tag` as a short
comma-separated context string, for example `local,premium` or `round1`; the
wrapper stores raw `tag` and normalized `tag_slug`.

The pack runner's `Project` value maps to the business wrapper's `job` field.
Prompt-bank markdown uses `tags` as a YAML list; the markdown runner flattens
that list into the wrapper's singular `-Tag` string.

Business keeps `run.json` and `gallery-entry.json` as the authoritative
client/job/gallery manifests. Engine image sidecars are per-image technical
provenance: model, composed engine prompt, output path, variant index, native
engine preset/style, and image-reference hashes when present. Do not replace
the business manifests with sidecars yet. Review tools should read the business
manifests first and optionally attach sidecar details per generated image.

## Current Bridge Behavior

The shared generator supports the original VaultForge presets and styles only. The business wrapper accepts business-friendly fields, injects them into the prompt, maps to the closest supported generator preset/style, passes native engine `--client`, `--job`, `--tag`, and `--variants` fields through, and keeps the original business fields in business metadata.

`-InputImage` and `-ReferenceImage` now pass through to the shared engine when
supplied. Relative paths are resolved from the business wrapper before the
engine is called, and both raw and resolved paths are recorded in business
metadata. `-Tweak` stays business-owned prompt context until a shared tweak/edit
contract exists.
