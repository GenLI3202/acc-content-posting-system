# Events Operational Workflow

This file defines the practical working sequence for `events-poster` in Phase 1.

## Goal

Turn an event-related Telegram request into a reviewed event draft package that is ready for repo publish after approval.

## The five-step workflow

When interacting with the user, first present this workflow clearly:

1. Intake & Intent Capture
2. Asset & Source Material Collection
3. Post Plan / Outline Confirmation
4. Full Draft + Preview Package
5. Review / Revise / Publish

Then execute it step by step.

---

## Step 1 · Intake & Intent Capture

### Purpose
Confirm that this is an event-post request and secure the event core.

### Collect
- title or working title
- date and start time
- location / meeting point
- event intent
- whether this is an announcement / signup-style post
- whether it is one-off or recurring
- intended display placement (`hero`, `upcoming`, `regular`, or multi-section)

### EventDraft action
- create a new EventDraft if this is a new task
- update the same EventDraft if this is an in-progress revision

### Rule
Do not ask asset-heavy questions yet unless they are unavoidable.

---

## Step 2 · Asset & Source Material Collection

### Purpose
Collect the media and supporting materials that shape the final post.

### Collect
- cover candidates
- WeChat QR image
- gallery images
- route links
- video links
- signup links
- supporting notes and source materials

### Clarify usage
For each important asset or link, clarify how it should be used:
- cover or not
- QR or not
- gallery or reference only
- embed in post or keep as background source

### Rule
Do not move to outline confirmation before the core source materials are sufficiently collected.

---

## Step 3 · Post Plan / Outline Confirmation

### Purpose
Show the user the planned event post structure before writing the full draft.

### Present
A compact post plan should include:
- working title
- one-line summary
- key frontmatter plan
- section placement plan
- one-off vs recurring plan
- planned sections
- planned use of cover / QR / gallery / route links / video links

### User decision
The user should confirm one of:
- OK, continue
- revise the plan first

### Rule
Do not generate the full draft until the outline / post plan is explicitly confirmed.

---

## Step 4 · Full Draft + Preview Package

### Purpose
Expand the confirmed plan into a real draft and package it for review.

### Produce
- local markdown draft
- asset manifest
- preview image (prefer long screenshot)
- Telegram summary text
- optional PDF fallback when needed

### Status
At this point the draft can move into states such as:
- `preview-ready`
- `in-review`

---

## Step 5 · Review / Revise / Publish

### Purpose
Use Telegram as the first formal review surface.

### If reviewer requests changes
- update the same EventDraft
- regenerate the affected draft outputs
- return an updated preview package

### If reviewer approves
- mark draft as approved / publish-ready
- prepare final repo-write targets
- publish downstream into the ACC repo

### Rule
Publish is downstream of approval.
Do not rebuild from raw chat history; publish from the approved EventDraft.

---

## Phase-1 guardrails

- preview before publish
- do not fabricate missing facts
- do not over-question when a meaningful preview can already be produced
- do not treat repo write as draft preview
- do not skip from early intake directly to full draft generation
