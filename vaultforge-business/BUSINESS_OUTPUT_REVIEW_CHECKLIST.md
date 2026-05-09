# Business Output Review Checklist

Date: 2026-05-09

## Purpose

This checklist defines the business-local review pass between generated output
and a client-ready delivery package.

Use it after a run has `gallery-entry.json`, `run.json`, image files, and
preferably a contact sheet or gallery card. It does not approve live
generation, pricing, licensing, public publication, or commercial rights
language. Those remain Nath-facing gates.

## Review Inputs

Start with these artifacts when they exist:

- `generated\_review\business-summary.md` from `build-review-summary.bat`
- `generated\_gallery\index.html` from `build-gallery.bat`
- `contact-sheet.jpg` beside each generated run from `build-contact-sheets.bat`
- each run's `gallery-entry.json`
- each run's `run.json`
- engine sidecar JSON files for optional technical provenance
- copied `prompt.source.md` or the original prompt-bank note
- approved input or reference images used for the job

## Selection Pass

For each run, mark the outcome before anything enters a delivery package:

- `select`: strong enough for client review or final packaging
- `revise`: promising but needs another prompt, reference, crop, or export pass
- `reject`: not client-ready and should not be shown outside internal review
- `hold`: ambiguous, needs Nath or client direction before choosing

Prefer a small selected set over a large mixed folder. The delivery package
should show curation, not every usable-looking generation.

## Quality Checks

Select only outputs that pass the relevant checks:

- The silhouette reads clearly at small size.
- The image matches the client, asset type, preset, style, mod, and tag intent.
- The output does not rely on unreadable text, broken letters, or fake marks
  that look like promised typography.
- The composition is not visibly cropped wrong for the requested use.
- The main subject is coherent, not duplicated, melted, or artifact-heavy.
- Colors feel intentional and do not fight the brief or service catalog lane.
- The result can plausibly work in the target context, such as icon, logo,
  cover, social tile, brand board, badge, or starter pack.
- Transparent-background or print-safe claims are only made after the actual
  export file is checked.
- Reference-image use is traceable in the source materials when references were
  part of the request.
- The selected file has enough source metadata to reproduce or explain the run.

## Reject Immediately

Reject or quarantine outputs with:

- broken, misleading, or pseudo-readable client text
- obvious visual glitches, duplicated subjects, or malformed symbols
- marks that could be confused with existing brands or trademarks
- unsafe, private, or unapproved reference material
- output that contradicts the intake note or client usage context
- missing `run.json` or `gallery-entry.json` when reproducibility matters
- files generated from an unapproved live run

## Review Notes

Record short review notes near the package or source run. Keep them practical:

```text
Run:
Decision: select | revise | reject | hold
Best files:
Reason:
Issues:
Next action:
Source prompt:
Manifest:
Reference files:
```

For prompt-bank notes, use `update-prompt-note.bat` to set `status`, `rating`,
`image`, and `notes` when the source prompt is known. Keep manual notes in the
delivery package `review\` folder when the review spans several runs.

## Package Mapping

When a file is selected, copy or export it into the delivery skeleton with this
shape:

- reviewed contact sheets to `review\contact-sheets\`
- selected internal candidates to `review\selected\`
- client preview images to `previews\`
- approved final files to `exports\final\`
- transparent variants to `exports\transparent\`
- social crops or tiles to `exports\social\`
- print-minded exports to `exports\print\` only after review approval
- source prompts to `sources\prompts\`
- `run.json`, `gallery-entry.json`, and sidecars to `sources\manifests\`
- approved input/reference images to `sources\references\`
- client-facing usage notes to `usage-notes\`
- superseded alternates to `archive\`

Do not put raw, unreviewed generations straight into `exports\final\`.

## Client-Ready Exit Criteria

A package is ready for client review only when:

- selected files are separated from rejected or uncertain alternates
- every delivered file has a clear intended use
- the package README has client, job, version, asset summary, and review status
- source prompts and manifests are archived for reproducibility
- usage notes avoid pricing, licensing, publication, trademark, or commercial
  rights wording unless Nath has approved that language
- live generation, if used, was explicitly approved and recorded

## Next Safe Step

After this checklist lands, the remaining business-local planning item is the
Nath-facing paid launch decision note. That note should prepare options for
pricing, licensing, publication, and service positioning without presenting
those decisions as already approved.
