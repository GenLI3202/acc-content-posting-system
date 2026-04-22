# First Runnable Implementation Plan v0.1

Project: `ACC Content Posting System`

Scope of this plan:
- `poster-router`
- `events-poster`

Goal:
Build the **first runnable loop** for event posting:

`Telegram request -> router classification -> event intake -> asset collection -> post plan confirmation -> full draft -> long screenshot preview -> Telegram review -> approval -> ACC repo write`

---

## Success definition

The first runnable loop is successful when the system can:

1. recognize an event-post request from Telegram
2. guide the user through the fixed 5-step event workflow
3. build a structured `EventDraft`
4. produce a local markdown draft
5. produce a long screenshot preview
6. return the preview package to Telegram
7. accept approval or revision feedback
8. on approval, write markdown + governed assets into the ACC repo target paths

---

## Task sequence overview

### Track A — `poster-router`
1. implement minimal route classification behavior
2. implement one-question ambiguity handling
3. implement minimal handoff package generation
4. validate with example prompts

### Track B — `events-poster`
1. implement EventDraft initialization/update
2. implement 5-step interaction protocol
3. implement event-specific field collection logic
4. implement asset classification and naming plan
5. implement post plan generation + confirmation gate
6. implement markdown draft generation
7. implement long screenshot preview generation
8. implement Telegram preview package response
9. implement review loop state transitions
10. implement publish step into ACC repo targets

### Track C — integration dry run
1. run one realistic end-to-end event case
2. inspect output quality
3. patch rough edges

---

# Detailed minimal task sequence

## Phase 1A — Router runnable core

### R1. Define event trigger examples
Create a small set of realistic event-like user requests.

Examples:
- 我想发一个周六骑行活动帖
- 帮我发 ACC 的开春骑报名帖
- 发布一个 workshop event

### R2. Define non-event contrast examples
Create a small set of route/media/knowledge examples so router can be sanity-checked.

### R3. Implement router decision rule
Router should:
- classify obvious event requests directly
- ask one clarifying question if ambiguous
- stop analyzing once classification is stable

### R4. Emit minimal handoff package
Router output should produce the minimal structured context needed by `events-poster`:
- collection
- post_type
- user_intent_summary
- known_inputs
- source_channel
- source_language
- session hint if applicable

### R5. Dry-check router behavior
Run prompt-only dry checks against the example set.

**Exit criterion:** Router can reliably hand event requests to `events-poster` without over-questioning.

---

## Phase 1B — EventDraft runnable core

### E1. Implement EventDraft file format
Choose a lightweight persisted representation for EventDraft.

Recommended Phase-1 choice:
- local YAML or JSON file in a staging area

Required fields:
- session_id
- collection
- post_type
- source_language
- slug
- status
- core_fields
- body_sections
- links
- assets
- review
- outputs

### E2. Create local staging layout
Define a predictable local staging area for Phase 1.

Recommended structure:
```text
.local-staging/
  event-sessions/
  drafts/
  previews/
  assets/
```

### E3. Initialize EventDraft on first handoff
When router hands off a new event task:
- create a new draft file
- assign a session id
- persist the initial known inputs

### E4. Update EventDraft on revision
When the same conversation continues:
- update the existing EventDraft
- do not fork a new draft unless explicitly requested

**Exit criterion:** EventDraft lifecycle exists and is stably persisted locally.

---

## Phase 1C — 5-step user interaction loop

### E5. Implement workflow announcement message
When `events-poster` starts, it must first say the 5-step workflow:
1. Intake & Intent Capture
2. Asset & Source Material Collection
3. Post Plan / Outline Confirmation
4. Full Draft + Preview Package
5. Review / Revise / Publish

### E6. Implement Step 1 collection
Collect only event-core inputs:
- title
- date/time
- location
- event intent
- announcement/signup context

### E7. Implement Step 2 collection
Collect only source materials and asset-role clarifications:
- cover candidates
- QR image
- gallery
- route links
- video links
- signup links

### E8. Implement Step 3 post plan generation
Generate a compact post plan:
- working title
- one-line summary
- key frontmatter plan
- planned sections
- planned asset usage

### E9. Implement Step 3 confirmation gate
Do not move to Step 4 until the post plan is explicitly confirmed.

**Exit criterion:** The agent can lead a user through Steps 1–3 without skipping ahead.

---

## Phase 1D — Draft generation and preview

### E10. Implement markdown draft generator
Generate the event markdown draft from EventDraft using the event template.

### E11. Implement asset naming plan
For event assets, generate final planned names such as:
- `cover.jpg`
- `wechat-qr.png`
- `gallery/01-group-start.jpg`

### E12. Implement long screenshot preview generation
Preferred Phase-1 behavior:
- render markdown/page-like output locally
- generate a long screenshot image

Fallback allowed:
- structured preview image
- optional PDF export

### E13. Implement preview package assembly
Return to Telegram:
- long screenshot preview
- draft `.md`
- short summary text
- asset summary

**Exit criterion:** A reviewer can meaningfully review the event post in Telegram.

---

## Phase 1E — Review and publish

### E14. Implement review state transitions
At minimum support:
- drafting
- preview-ready
- in-review
- approved
- publish-ready
- published

### E15. Implement revision loop
If user requests changes:
- update EventDraft
- regenerate preview package
- remain inside same posting session

### E16. Implement approval recognition
Accept explicit approval only.
Do not infer approval from silence.

### E17. Implement publish output materialization
On approval, prepare final outputs:
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`
- event assets under `frontend/public/images/events/{slug}/...`

### E18. Implement local repo write
Write the approved markdown and assets into the ACC repo target paths.

### E19. Mark published state
Update the EventDraft status accordingly.

**Exit criterion:** Approved draft can be written into ACC repo target paths without reconstructing from raw chat history.

---

## Phase 1F — End-to-end dry run

### I1. Prepare one realistic sample event
Use a realistic event case including:
- basic text info
- one route link
- one cover image
- one QR image
- two gallery images

### I2. Simulate full Telegram flow
Run through:
- request
- routing
- intake
- asset collection
- post plan
- confirmation
- draft
- preview
- review
- publish

### I3. Inspect outputs
Check:
- markdown quality
- preview usefulness
- asset naming correctness
- repo target correctness
- multilingual output acceptability

### I4. Patch critical issues
Fix only the blockers to first usability.
Do not expand scope.

---

## Recommended implementation order

### Order 1 — foundations
- R1–R5
- E1–E4

### Order 2 — conversation loop
- E5–E9

### Order 3 — output generation
- E10–E13

### Order 4 — review/publish
- E14–E19

### Order 5 — dry run
- I1–I4

---

## Explicit non-goals for first runnable implementation

Do not block on:
- routes/media/knowledge support
- PR automation
- perfect frontend-faithful preview
- complex permission model
- multi-user concurrency resolution
- full observability stack

---

## Recommended checkpoint strategy

After each implementation block, stop and check:
- does this reduce uncertainty?
- does this move the runnable loop forward?
- is this a direct dependency for the next block?

If not, defer it.

---

## Final note

This plan is intentionally biased toward the smallest credible runnable loop, not the most elegant final architecture.
