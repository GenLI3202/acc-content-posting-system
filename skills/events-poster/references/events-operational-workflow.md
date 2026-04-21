# Events Operational Workflow

This file defines the practical working sequence for `events-poster` in Phase 1.

## Goal

Turn an event-related Telegram request into a reviewed event draft package that is ready for repo publish after approval.

## Workflow

### Step 1 · Accept handoff
Receive the event handoff from `poster-router`.

Expected minimum:
- event-related intent
- source language hint if available
- any already-mentioned links/assets

### Step 2 · Initialize or update EventDraft
Create a new EventDraft when this is a new posting task.

If this is clearly a revision to an existing in-progress draft:
- update the same EventDraft
- do not fork a second draft unless explicitly requested

### Step 3 · Fill missing event core
Secure the event core first:
- title
- date/time
- location
- event type / intent
- announcement/signup context

### Step 4 · Fill publishable minimum
Collect enough information for a credible first preview:
- short description
- route/plan summary
- intensity
- notes
- join/signup information

### Step 5 · Process assets
Collect and assign assets:
- cover
- WeChat QR
- gallery
- route links or related supporting links

Normalize naming and planned paths before finalizing markdown references.

### Step 6 · Generate local draft outputs
Produce:
- local markdown draft
- asset manifest
- local preview image or equivalent render-like preview
- Telegram summary text

### Step 7 · Enter review
Return the preview package to Telegram.

Status should move into review-oriented state, for example:
- `preview-ready`
- `in-review`

### Step 8 · Handle review loop
If reviewer asks for changes:
- update the same EventDraft
- regenerate affected outputs
- return an updated preview package

### Step 9 · Prepare publish-ready output
Only after explicit approval:
- mark draft approved
- switch status to publish-ready
- prepare final repo-write targets

### Step 10 · Publish
Publish step is downstream from approval.

It should consume the reviewed draft object instead of rebuilding the content from raw chat history.

## Phase-1 guardrails

- preview before publish
- do not fabricate missing facts
- do not over-question when a meaningful preview can already be produced
- do not treat repo write as draft preview
