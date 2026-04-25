# Media Publish Step Spec

This file defines the publish transition after Telegram review approval for `media-poster`.

## Principle

Publish is downstream of approval.

The publish step consumes the approved MediaDraft and its asset manifest.
It should not reconstruct content from raw chat history.

## Preconditions for publish

Before publish, all of the following should be true:
- draft status is `approved` or `publish-ready`
- markdown draft exists
- planned asset names and paths are stable
- required media fields are no longer unresolved placeholders
- preview has already been reviewed in Telegram
- remote repo state has been refreshed immediately before final repo write
- target output paths are confirmed to be inside the allowed media-content surface only
- the final frontmatter mapping is confirmed against current ACC ClubHub media schema before final write

## Publish outputs

A Phase-1 media publish should prepare and write:

### Markdown targets
- `frontend/src/content/media/zh/{slug}.md`
- `frontend/src/content/media/en/{slug}.md`
- `frontend/src/content/media/de/{slug}.md`

### Asset targets
- `frontend/public/images/media/{type}/{slug}/cover.jpg`
- `frontend/public/images/media/{type}/{slug}/gallery/*` (if present)

## Frontmatter mapping rules

- emit fields that match the real current ACC ClubHub media schema
- prefer `cover`, not `coverImage`, in new output
- emit `videoUrl` only when it is genuinely part of the page contract
- emit `xiaohongshuUrl` as an external/source link, not as a substitute for body content
- emit `featured` only from an approved editorial decision, not by guesswork
- do not silently output stale legacy media type values when canonical current values are available

## Publish transition sequence

### Step 1 · freeze approved draft
Mark the draft as approved and stop changing structural decisions unless a new revision is requested.

### Step 2 · sync and verify remote repo state
Immediately before final repo write:
- fetch / pull the latest remote default branch state
- verify the local target branch is not stale
- verify target paths do not conflict with newly-arrived remote changes
- stop and ask for human intervention if there is a conflict, dirty state, or unclear overwrite risk

### Step 3 · resolve final output paths
Ensure all markdown and asset target paths are final.

Read `media-asset-path-rules.md` and verify the planned outputs follow it exactly.
In particular:
- markdown must land under `frontend/src/content/media/**`
- assets must land under `frontend/public/images/media/**`
- `src/content/media/**` without the `frontend/` prefix is a blocking path error

If a publish-scope guard exists for media paths, run it before any final write.
If the guard returns non-zero, do not write.

### Step 4 · materialize final publish set
Prepare the publish set from the approved draft object:
- multilingual markdown outputs
- asset files
- asset references inside markdown
- canonical frontmatter fields that match current ACC ClubHub authoring expectations

### Step 5 · write to repo target
Write the final output set into the ACC repo target paths.

Write is limited to the Phase-1 media content surface only:
- `frontend/src/content/media/**`
- `frontend/public/images/media/**`

Do not write outside that surface.

### Step 6 · mark published state
Update draft/session state to reflect that repo publish has occurred.

## Failure handling guidance

If publish fails after approval:
- keep the approved draft object
- do not discard asset manifest
- allow a safe retry from publish-ready state

If the failure comes from sync conflict, schema mismatch, or path-scope violation:
- do not force write
- report the blocking note briefly
- ask for the next human decision
