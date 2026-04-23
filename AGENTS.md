# AGENTS.md

Project-level working rules for the ACC Content Posting System.

## Core discipline

- Keep the system collection-specific: router decides destination, collection posters own collection logic.
- Prefer preview-first, publish-second workflows.
- Do not silently weaken repo-safety or publish-approval constraints.
- Align specs to the **real current ACC ClubHub schema/runtime**, not stale templates or assumptions.

## Commit-and-check-progress rule

Whenever you make a meaningful project commit:

1. Open `PROGRESS.md`
2. Check which checklist items changed status because of the work
3. Update the relevant checkboxes and immediate next focus if needed
4. Then commit the code/spec changes together with the progress update when practical

Do not let `PROGRESS.md` drift far behind the real project state.

## Architecture docs rule

When architecture direction changes materially:

- update the relevant file under `specs/architecture/`
- update `PROGRESS.md` in the same work cycle
- keep diagrams and prose aligned

## Collection expansion rule

Before adding a new collection poster:

- inspect the real ACC ClubHub schema and runtime behavior first
- define boundaries against existing posters first
- define intake, draft, preview, and publish flow before implementation details
