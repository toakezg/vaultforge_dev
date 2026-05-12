# How To Use

1. Start the local app with `.\run-interface.bat` or `npm.cmd start`.
2. Let the intro screen clear, or press `Enter`.
3. Use quick access on the left to jump between Workshop, Lanes, Tools,
   Templates, and Preview.
4. Choose one or more lanes in the lane panel. Use `All lanes` when you want
   the command draft to include every current VaultForge lane.
5. Pick Natural or Technical mode from the top bar.
6. Use template buttons to assemble a prompt, or type directly in the input.
7. Set the local run plan: cycle count, timebox, hard-gate mode, and commit
   mode.
8. Fill the evidence fields for files touched, verification, blocker or
   decision, and next action when preparing a handoff.
9. Review the generated run draft, command draft, evidence handoff, and preview
   gallery.
10. Check the local execution gate. It is visible but disabled during this
    Workflow B run.
11. Press `Queue draft` or `Ctrl+Enter` to add a local draft entry.
12. Read the Operator terminal for draft activity. It shows what the interface
    staged or copied, but it does not mean a VaultForge process started.
13. Open Settings to change theme, density, and keybinds.

Default keybinds:

```text
Ctrl+Enter  Queue draft
Ctrl+K      Focus prompt input
Ctrl+,      Open settings
Ctrl+1      Workshop
Ctrl+2      Lanes
Ctrl+3      Tools
Ctrl+4      Templates
Ctrl+5      Preview
```

This interface does not execute VaultForge lane commands. The command surface is
a draft-only planning aid, uses Workflow B lane ids, and intentionally omits
`--execute`. Real command execution needs a separate local approval before the
disabled gate can change. The token ticker is an approximate draft-size counter
for the visible prompt, command, and handoff text.

Small mod and plugin-style additions are documented in `EXTENDING.md`.
