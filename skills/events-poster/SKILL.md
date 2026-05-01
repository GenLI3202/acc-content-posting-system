---
name: events-poster
description: Create ACC event announcement and signup posts from Telegram conversations into repo-ready draft packages. Use when publishing an Across Cycling Club event page such as an after-work ride, social ride, workshop, race, training-camp, club ride announcement, or signup post. Trigger on requests like “发活动帖”, “做报名帖”, “发布周六骑行活动”, “做 workshop event 页面”, or similar event-post intents. Handles event frontmatter, distance / official-ride metadata, body structure, asset classification, post-plan confirmation, local preview generation, and review-before-publish workflow. Supports cover image, WeChat QR, gallery assets, and event-related route/video links under the ACC event asset rules.
---

# Events Poster

## Core job

Create an `Event Post` draft package for ACC.

## Responsibilities

- collect event-specific required fields
- collect route-distance / official-ride metadata when relevant
- build a structured draft object
- classify and name event assets
- produce a local markdown draft and preview package
- wait for review approval before repo publish
- ask signup as a method question, not automatically as an external link question
- treat the human as an event manager / operator unless context clearly says otherwise
- stop immediately when a production-critical fact is unknown; ask instead of fabricating placeholders
- prefer Komoot / Strava route links for native embed over asking for static route screenshots
- ask whether the event is one-off or recurring when that affects placement or event semantics
- ask whether the event should appear in one section or multiple sections when site placement is relevant
- choose a simpler one-off draft shape by default; only use the richer recurring-official-ride shape when the event truly matches it

## Read before working

- `references/event-frontmatter-schema.md`
- `references/event-body-structure.md`
- `references/event-asset-rules.md`
- `references/event-preview-package-spec.md`
- `references/event-preview-rendering-strategy.md`
- `references/event-review-gate-spec.md`
- `references/event-publish-step-spec.md`
- `references/event-intake-question-flow.md`
- `references/event-draft-schema-example.md`
- `references/route-embed-rules.md`
- `references/events-operational-workflow.md`
- `references/router-to-events-handoff.md`
- `../../shared-references/posting-session-schema.md`
- `../../shared-references/asset-path-and-naming-rules.md`
- `../../shared-references/multilingual-output-rules.md`
- `../../shared-references/telegram-intake-conventions.md`

## Phase-1 scope

Phase 1 only covers `Event Post` publishing flow.

### Required outputs

- draft object / posting session state
- local markdown draft
- local preview package
- asset manifest

### Event asset classes

- `cover`
- `wechat-qr`
- `gallery/*`

## Read bundled templates

- `assets/templates/event-post-template.md`
- `assets/templates/event-gallery-section-template.md`

## Bundled helper script

- `scripts/resolve_route_embed.py` — normalize Komoot / Strava links into stable embed output

## User interaction protocol

Internally, follow the five-step event workflow strictly.

Do **not** expose the workflow structure to the user unless they explicitly ask for process details.

The user should experience the flow as smooth guided collaboration, not as a visible checklist.

### Required interaction rules

- start with the minimum useful next question or acknowledgement
- do not ask Step 2 questions before Step 1 is sufficiently complete
- do not move to Step 3 before Step 2 materials are sufficiently collected
- do not generate the full draft before Step 3 is explicitly confirmed
- do not publish before Step 5 approval

### User-facing style

- keep questions scoped to the current need
- prefer one compact Telegram-friendly message over a lecture
- do not repeat workflow context the user already has
- do not introduce yourself with long role descriptions unless asked
- do not announce internal rules like "5-step workflow" or "Step 1"
- when asked to publish an event, acknowledge briefly and move straight to the next needed question
- use plain user language such as `活动标题`, `封面图`, `报名方式`, `人数限制`, `活动说明`
- avoid engineering terms like `slug`, `frontmatter`, `repo`, `render`, `preview package` unless the collaborator explicitly wants technical detail
- progress updates must be extremely brief: only the caution / note and the next step
- if a key production input is unknown, stop and ask immediately
- when a route link is available, use `scripts/resolve_route_embed.py` instead of hand-building embed URLs or snippets
- if the operator requests multi-section display, preserve that intent explicitly instead of silently collapsing it to one section
- use `displaySections` as canonical ACC ClubHub output; keep `displaySection` only as legacy read-compatibility context
- do not add a `recurring` block just because an event belongs in `regular`; recurring means real auto-rolling behavior

### Signup / registration rule

Do not ask for a `registrationLink` by default.

Ask first for the **signup / join method** in plain language, for example:
- WeChat QR
- built-in site registration form
- email signup
- external registration page
- no registration needed

If the event is a ride / route-based activity, collect route distance explicitly.
Prefer `distanceKm` as the canonical event frontmatter field.
Treat `routeDistanceKm` only as legacy / compatibility context unless the ACC repo later redefines it.

If the event is an ACC official ride, treat distance as production-critical metadata rather than a nice-to-have detail.

Only ask for `registrationLink` if the human explicitly says the event should use an external signup page.

If the event uses a built-in site registration flow, collect only what is actually needed, such as:
- whether built-in registration should be used
- participant cap / max participants if relevant
- `registrationDeadline` if it should override the default
- `wechatQrCode` if the page should also direct people into a WeChat group
- `distanceKm` when the event is a ride / route-led event
- whether `ACCOfficialRide` should be true when the post is an official club ride

For signup-style event posts, do not forget to ask whether there is a participant limit.

### Transition rule

Only move to the next step after the current step has enough information to proceed.
If the current step is incomplete, continue collecting inside that step instead of jumping ahead.

## Operational rule

Preview first. Publish second.

Do not write final repo output until the Telegram review gate is explicitly approved.

## Repo boundary rule

Phase 1 is content-scoped. Allowed write surface only:
- `frontend/src/content/events/**`
- `frontend/public/images/events/**`

Do not modify other ACC ClubHub areas such as backend, infra, unrelated content collections, CI, or general repo config.

Immediately before final repo write / commit / push, sync the latest remote state and stop if there is a conflict, stale branch, dirty state, or unclear overwrite risk.

Before final repo write, run `scripts/validate_publish_scope.py` on the planned output paths. If it fails, stop and ask the human instead of writing anyway.
