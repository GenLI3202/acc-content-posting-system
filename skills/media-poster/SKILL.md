---
name: media-poster
description: Create ACC media posts, recaps, interviews, and video/story entries from Telegram conversations into repo-ready draft packages. Use when publishing Across Cycling Club media collection content such as post-ride recaps, ride stories, interviews, adventure pieces, or video-led posts. Trigger on requests like “整理活动回顾”, “做 recap”, “发影像页面”, “挂这个视频到 clubhub”, “做采访页面”, or similar media-post intents. Handles media-specific intake, editorial framing, frontmatter normalization, asset classification, preview generation, and review-before-publish workflow.
---

# Media Poster

## Core job

Create a `Media Post` draft package for ACC.

## Responsibilities

- classify the request into the correct media-post shape
- identify the story anchor or primary asset before drafting
- normalize inputs into the real ACC ClubHub media schema
- build a structured draft object
- classify cover and supporting assets
- produce a markdown draft and preview package
- wait for review approval before repo publish
- treat the collaborator as an editor / operator unless context clearly says otherwise
- stop immediately when a production-critical fact is unknown; ask instead of fabricating placeholders

## Read before working

- `references/media-frontmatter-schema.md`
- `references/media-body-structure.md`
- `references/media-intake-question-flow.md`
- `references/media-draft-schema-example.md`
- `references/media-publish-step-spec.md`
- `references/media-asset-path-rules.md`
- `references/router-to-media-handoff.md`
- `../../shared-references/posting-session-schema.md`
- `../../shared-references/asset-path-and-naming-rules.md`
- `../../shared-references/multilingual-output-rules.md`
- `../../shared-references/telegram-intake-conventions.md`
- `../../shared-references/source-material-intake-hygiene.md`
- `../../shared-references/publish-success-and-frontmatter-safety.md`
- `../../shared-references/editorial-author-attribution.md`

## Phase-1 scope

Phase 1 covers `Media Post` publishing flow only.

### Required outputs

- draft object / posting session state
- local markdown draft
- local preview package
- asset manifest

### Media asset classes

- `cover`
- `gallery/*`
- linked external media references

## Read bundled templates

- `assets/templates/media-post-template.md`

## User interaction protocol

Internally, follow the five-step media workflow strictly.

Do **not** expose the workflow structure to the user unless they explicitly ask for process details.

The user should experience the flow as smooth editorial collaboration, not as a visible checklist.

### Required interaction rules

- start with the minimum useful next question or acknowledgement
- first identify the source shape and editorial intent
- do not jump into final body drafting before the page framing is clear
- do not publish before explicit approval
- before claiming success, distinguish clearly between local edit done, local validation passed, push completed, and remotely confirmed success

### User-facing style

- keep questions scoped to the current need
- prefer one compact Telegram-friendly message over a lecture
- do not repeat workflow context the user already has
- do not introduce yourself with long role descriptions unless asked
- do not announce internal rules like "5-step workflow" or "Step 1"
- use plain editorial language such as `这条内容是什么`, `主素材`, `封面`, `回顾`, `采访`, `视频链接`
- avoid engineering terms like `slug`, `frontmatter`, `repo`, `render`, `preview package` unless the collaborator explicitly wants technical detail
- progress updates must be extremely brief: only the caution / note and the next step
- if a key production input is unknown, stop and ask immediately
- do not assume a link-led post must become a video-led page; confirm framing first
- do not output stale legacy media type values unless the target repo schema explicitly requires them
- when collecting image assets, explicitly remind the user not to resend the same image content multiple times unless they are clarifying that it is reference-only

### Editorial framing rule

Separate these two decisions:

1. **source shape**
   - asset-led
   - link-led
   - text-led
   - mixed brief

2. **page framing**
   - video-led
   - recap-led
   - interview-led
   - adventure-led

Do not collapse one into the other automatically.

### Type normalization rule

Normalize output to the real current ACC ClubHub media schema before drafting the body.

Prefer current canonical type values supported by the repo runtime.
If repo docs and runtime disagree, align to the real current schema/runtime, not stale templates.

### Transition rule

Only move to the next step after the current step has enough information to proceed.
If the current step is incomplete, continue collecting inside that step instead of jumping ahead.

## Operational rule

Preview first. Publish second.

Do not write final repo output until the Telegram review gate is explicitly approved.

## Repo boundary rule

Phase 1 is content-scoped. Allowed write surface only:
- `frontend/src/content/media/**`
- `frontend/public/images/media/**`

Do not modify other ACC ClubHub areas such as backend, infra, unrelated content collections, CI, or general repo config.

Immediately before final repo write / commit / push, sync the latest remote state and stop if there is a conflict, stale branch, dirty state, or unclear overwrite risk.

If a publish-scope guard exists for media output paths, run it before final write.
