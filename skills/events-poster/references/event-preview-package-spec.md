# Event Preview Package Spec

This spec defines what `events-poster` must produce before any repo publish is allowed.

## Core rule

Preview is the first formal output.

Repo write is not allowed until the preview package has been reviewed and explicitly approved.

## Preview package contents

A valid Phase-1 event preview package should contain:

### 1. Preview image
A rendered or render-like visual preview that helps humans review quickly in Telegram.

Preferred forms:
- page-like screenshot
- markdown-render screenshot
- structured visual summary if full render is not yet available

### 2. Markdown draft attachment
A draft `.md` file representing the current event content.

This gives reviewers something concrete to inspect beyond the image preview.

### 3. Summary text in Telegram
A short message that explains:
- collection: `events`
- slug
- title
- event date
- current draft status
- what changed if this is a revision

### 4. Asset summary
A compact summary of assets included in this draft:
- chosen cover image
- whether WeChat QR is present
- gallery count
- final planned file names if already decided

## Recommended Telegram preview shape

A preview response should ideally look like:

1. short summary text
2. preview image attachment
3. markdown draft attachment
4. optional asset thumbnails / asset summary text

## Draft status progression

Suggested status values during Phase 1:

- `drafting`
- `preview-ready`
- `in-review`
- `approved`
- `publish-ready`
- `published`

## Review outcomes

### Outcome A: needs revision
If the reviewer asks for changes:
- keep status in `in-review` or move back to `drafting`
- revise the same posting session
- do not create a new independent event unless the user explicitly restarts

### Outcome B: approved
If the reviewer approves:
- mark the draft as `approved`
- prepare repo-write output
- only then move to publish flow

## Phase-1 simplification

Phase 1 does not require a complex approval engine.

A clear explicit approval signal in Telegram is enough, as long as the draft object / session status is updated accordingly.
