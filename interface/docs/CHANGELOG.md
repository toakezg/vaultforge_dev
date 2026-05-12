# Interface Changelog

## 2026-05-13

- Reviewed the cycle 1 builder result, fixed the browser smoke harness to serve
  the static app over ephemeral localhost instead of `file://`, and reverified
  the interface contract, Edge smoke flow, and interface diff hygiene.
- Strengthened the preview surface with draft-only Workflow B run planning
  controls, a copyable command draft that intentionally omits `--execute`, and
  dynamic gallery cards for run plan, prompt, command, and evidence review.
- Added the first static VaultForge operator interface with intro loading
  screen, quick access navigation, lane and multilane selection, workshop run
  dock, prompt builder, quick prompting templates, preview and gallery
  placeholders, natural and technical modes, settings, theme controls,
  tooltips, and customizable keybinds.
- Added interface-local setup and usage docs.
- Added a dependency-free Node contract test for the interface files.
- Added Workflow B handoff evidence and headless Edge render artifacts for
  desktop, mobile, and intro screen checks.
- Added a local intro image asset and keyboard `Enter` support for clearing the
  load screen.
- Added a real browser smoke test for local Edge that clicks and verifies the
  main operator interactions, persistence, and mobile overflow.
- Added extension notes for safe template, keybind, theme, and lane additions.
