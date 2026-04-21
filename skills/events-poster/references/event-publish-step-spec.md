# Event Publish Step Spec

This file defines the publish transition after Telegram review approval.

## Principle

Publish is downstream of approval.

The publish step consumes the approved EventDraft and its asset manifest.
It should not reconstruct content from raw chat history.

## Preconditions for publish

Before publish, all of the following should be true:
- draft status is `approved` or `publish-ready`
- markdown draft exists
- planned asset names and paths are stable
- required event fields are no longer unresolved placeholders
- preview has already been reviewed in Telegram

## Publish outputs

A Phase-1 event publish should prepare and write:

### Markdown targets
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`

### Asset targets
- `frontend/public/images/events/{slug}/cover.jpg`
- `frontend/public/images/events/{slug}/wechat-qr.png` (if present)
- `frontend/public/images/events/{slug}/gallery/*` (if present)

## Publish transition sequence

### Step 1 · freeze approved draft
Mark the draft as approved and stop changing structural decisions unless a new revision is requested.

### Step 2 · resolve final output paths
Ensure all markdown and asset target paths are final.

### Step 3 · materialize final publish set
Prepare the publish set from the approved draft object:
- multilingual markdown outputs
- asset files
- asset references inside markdown

### Step 4 · write to repo target
Write the final output set into the ACC repo target paths.

### Step 5 · mark published state
Update draft/session state to reflect that repo publish has occurred.

## Important boundary

This spec defines **what** should be written and **when** writing is allowed.

It does not yet lock the transport mechanism:
- direct local repo write
- branch write
- PR creation

That can be defined later without changing the review-before-publish contract.

## Failure handling guidance

If publish fails after approval:
- keep the approved draft object
- do not discard asset manifest
- allow a safe retry from publish-ready state

Do not force the user to rebuild the draft from scratch.
