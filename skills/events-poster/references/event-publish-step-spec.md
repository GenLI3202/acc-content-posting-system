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
- remote repo state has been refreshed immediately before final repo write
- target output paths are confirmed to be inside the allowed event-content surface only

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

### Step 2 · sync and verify remote repo state
Immediately before final repo write:
- fetch / pull the latest remote default branch state
- verify the local target branch is not stale
- verify target paths do not conflict with newly-arrived remote changes
- stop and ask for human intervention if there is a conflict, dirty state, or unclear overwrite risk

Do not skip this sync check just because the draft was prepared locally earlier.

### Step 3 · resolve final output paths
Ensure all markdown and asset target paths are final.

Before any final write, run the publish-scope guard against the planned output paths:

```bash
python scripts/validate_publish_scope.py \
  --repo-root /path/to/acc_clubhub \
  --policy specs/content-scope-policy.yaml \
  <planned-path-1> <planned-path-2> ...
```

If the guard returns non-zero, do not write.

### Step 4 · materialize final publish set
Prepare the publish set from the approved draft object:
- multilingual markdown outputs
- asset files
- asset references inside markdown

### Step 5 · write to repo target
Write the final output set into the ACC repo target paths.

Write is limited to the Phase-1 event content surface only:
- `frontend/src/content/events/**`
- `frontend/public/images/events/**`

Do not write outside that surface.

### Step 6 · mark published state
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

If the failure comes from sync conflict or path-scope violation:
- do not force write
- report the blocking note briefly
- ask for the next human decision
