# First Dry-Run Script v0.1

Project: `ACC Content Posting System`

Purpose:
Run the first realistic dry-run against the `poster-router + events-poster` Phase-1 loop.

---

## Dry-run target

Use the canonical event case:
- `afterwork-ride-canonical`

---

## Preconditions

Before dry-run:
- Telegram bot can receive text and image inputs
- Telegram bot can return text and file/image attachments
- `poster-router` and `events-poster` descriptions are trigger-hardened
- Event specs and templates are present
- content scope restriction policy exists

---

## Dry-run sequence

### Step 0 · Setup
Prepare:
- one Telegram test group
- one human operator
- one event request
- one cover image
- one QR image
- one route link
- optional extra gallery images

### Step 1 · Send initial request
Human sends:
> 我们 ACC 马上要发布 Afterwork ride 了，帮我做一个 event post。

### Step 2 · Observe routing
Check whether the system:
- classifies the request as `events`
- starts with the 5-step workflow announcement
- enters Step 1 rather than jumping ahead

### Step 3 · Complete Step 1
Provide the event core answers.

### Step 4 · Complete Step 2
Provide cover / QR / route link / gallery inputs.

### Step 5 · Evaluate Step 3
Check whether the system presents a clear post plan for confirmation.

### Step 6 · Approve plan
Confirm the post plan and allow full draft generation.

### Step 7 · Evaluate Step 4 outputs
Check whether the system returns:
- markdown draft
- long screenshot preview
- summary text
- asset summary

### Step 8 · Request one revision
Intentionally change one thing, such as:
- cover choice
- wording of route section
- shorter notes section

### Step 9 · Approve draft
After the revision loop, provide explicit approval.

### Step 10 · Evaluate publish readiness
Check whether the system now has enough information to:
- resolve repo targets
- resolve governed asset paths
- move into publish-ready state

---

## Evaluation checklist

### Router quality
- Did it classify correctly?
- Did it avoid over-questioning?
- Did it hand off early enough?

### Workflow discipline
- Did it explicitly announce the 5-step process?
- Did it stay within the current step?
- Did it avoid skipping from Step 1 to Step 4?

### Asset handling
- Did it distinguish cover vs QR vs gallery?
- Did it ask clarifying usage questions when needed?
- Did planned names/paths look sane?

### Draft quality
- Did the markdown structure look like a real ACC event page?
- Was the post plan reflected in the final draft?
- Did the preview support meaningful review?

### Review gate quality
- Did the system revise the same draft instead of forking a new one?
- Did it wait for explicit approval before moving forward?

---

## Dry-run verdict categories

### PASS
The loop is coherent and can proceed to implementation hardening.

### PASS WITH FIXES
The loop works, but one or two issues should be corrected before broader testing.

### FAIL
The loop breaks at routing, step discipline, preview generation, or review gating.

---

## Immediate next action after dry-run

If the result is `PASS` or `PASS WITH FIXES`, create a short issue list and move to implementation hardening instead of re-opening the architecture discussion.
