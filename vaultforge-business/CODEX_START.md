# Codex Start

Read these first:

1. `..\CODEX_START.md`
2. `..\SYSTEM.md`
3. `..\THREAD_MAP.md`
4. `NATH_START.md`
5. `README.md`
6. `SYSTEM.md`
7. `PLAN.md`
8. `TASKS.md`
9. `CHANGELOG.md`
10. `SIGN_UP.md`
11. see *update* below 

The current high-value slice is to keep improving the business lane while keeping the shared engine and wrappers aligned.
*update:  putting in place a vaultforge-business  orientatied mechanics to fuurther serperate from the shared vaultforge-art section  of vaultforge tto successfuuly and cleanly stop any bleed/noise/interaction/influence from vualtforge-art. bTo also better make clear and sort what preset belongs with -business  what with -art and what is shared and build hard into the engine -- determine  by a solid evaluation  of the current archecture  if which tasks can be implemented now safetly  and orderly  to achieve this goal - if the evalution proves to result in a confident answer to which tasks are to be done, prioritize, and then in a clean systematiic order proceed with tasks. if NO solid rfinding as to which tasks or no confident direction do not prroceed with these tasks and ree-evaluate next best tasks suited for current state - in all cases provide a detailed summary of analyis and ur ffindingss and and any changes  in repsonse and also in required documentation - proceed with my confidence in you evauluations and determinnism when facing next steps and tasks and proceeding to tackle them without any further permission unless required, desired, oor  each route  retuns nul implmentations  should be proceeded with in this run*

Important engine fact:

`..\vaultforge-engine\src\generate.py --help` currently shows the shared engine CLI. Business presets and styles are bridged in `run_business.ps1`; native engine metadata fields are passed through where the engine supports them.

- At the end of a business run, update `CHANGELOG.md`. If the change affects root coordination or engine contracts, also update the root handoff/changelog docs.
