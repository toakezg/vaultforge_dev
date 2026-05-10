# Run Manifest Field List

Date: 2026-05-09

This is the first shared field list for engine-written sidecar JSON files.
Gallery and contact-sheet tooling can depend on these fields before richer
metadata contracts exist.

The engine still writes one JSON sidecar beside each generated image when
metadata is enabled. This note describes the stable minimum fields consumers
should read, not every additive field the engine may include.

## Stable Fields

| Field | Type | Meaning |
|---|---|---|
| `version` | number | Sidecar schema version. Current value is `1`. |
| `created_at` | string | Local ISO timestamp for the generation run. |
| `output_path` | string | Full path to the generated image this sidecar describes. |
| `prompt` | string | Prompt text before preset/style/mod fragments are appended. |
| `composed_prompt` | string | Full prompt sent to the image request. |
| `model` | string or null | Model that produced the image. Dry-run previews can show metadata paths but do not write sidecars. |
| `models_to_try` | array of strings | Ordered model fallback list for the run. |
| `preset` | string or null | Shared engine preset name, if supplied. |
| `style` | array of strings | Shared engine style names or accepted aliases, in CLI order. |
| `mod` | array of strings | Shared engine modifier names, in CLI order. |
| `constraint` | array of strings | Shared engine production constraint names, in CLI order. |
| `size` | string | Requested image size. |
| `quality` | string | Requested image quality. |
| `format` | string | Requested output format. |
| `background` | string | Requested background handling. |
| `client` | string | Raw client metadata from `--client`, or empty string. |
| `client_slug` | string | Filename-safe client slug, or empty string. |
| `job` | string | Raw job metadata from `--job`, or empty string. |
| `job_slug` | string | Filename-safe job slug, or empty string. |
| `tag` | string | Raw tag metadata from `--tag`, or empty string. |
| `tag_slug` | string | Filename-safe tag slug, or empty string. |
| `variant` | number | One-based variant number for this output. |
| `variants` | number | Total variants requested for this prompt. |

## Conditional Fields

| Field | Type | Meaning |
|---|---|---|
| `prompt_file` | string | Batch prompt file path when the output came from batch mode. |
| `image_references` | array of objects | Input/reference images used by the run. Each item includes `path`, `source`, and `sha256`. |

## Consumer Rules

- Treat unknown fields as additive and safe to ignore.
- Use `version` before assuming field semantics.
- Prefer `output_path`, `prompt_file`, and `created_at` for gallery indexing.
- Prefer `client_slug`, `job_slug`, `tag_slug`, `variant`, and `variants` for grouping.
- Use `image_references[].sha256` to detect changed local reference assets.
- Do not require sidecars for dry-run previews; dry-runs print the intended metadata path but do not write JSON.
- Keep lane-owned gallery files separate from engine sidecars unless a later root-approved contract says otherwise.

## Gallery Index Hook

The engine can now build an index over existing sidecars with:

```powershell
py .\src\generate.py --gallery-index --gallery-source assets\generated --gallery-output assets\gallery-index.json
```

The index is intentionally small and mechanical:

| Field | Type | Meaning |
|---|---|---|
| `version` | number | Gallery index schema version. Current value is `1`. |
| `created_at` | string | Local ISO timestamp for the index build. |
| `source_dir` | string | Folder scanned for sidecar JSON. |
| `entry_count` | number | Number of valid sidecars included. |
| `ignored_count` | number | JSON files skipped because they were invalid or not run sidecars. |
| `entries` | array of objects | Gallery-ready sidecar entries, sorted by `created_at`, `output_path`, and `sidecar_path`. |

Each entry copies the stable sidecar fields needed for grouping and review, plus
`sidecar_path`. Contact-sheet renderers can consume this index later without
depending on incidental sidecar fields.

`--gallery-index` rejects `--dry-run` so the dry-run contract stays no-write.
Run the normal gallery-index command only when the JSON index write is intended.
