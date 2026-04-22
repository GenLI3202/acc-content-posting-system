---
name: events-poster
description: Create ACC event announcement and signup posts from Telegram conversations into repo-ready draft packages. Use when publishing an Across Cycling Club event page such as a social ride, workshop, race, training-camp, club ride announcement, or signup post. Trigger on requests like “发活动帖”, “做报名帖”, “发布周六骑行活动”, “做 workshop event 页面”, or similar event-post intents. Handles event frontmatter, body structure, asset classification, post-plan confirmation, local preview generation, and review-before-publish workflow. Supports cover image, WeChat QR, gallery assets, and event-related route/video links under the ACC event asset rules.
---

# Events Poster

## Core job

Create an `Event Post` draft package for ACC.

## Responsibilities

- collect event-specific required fields
- build a structured draft object
- classify and name event assets
- produce a local markdown draft and preview package
- wait for review approval before repo publish
- treat signup as a method question, not automatically as an external link question

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

### Conversation style rule

For user-facing conversation:
- keep the questioning scoped to the current need
- prefer short Telegram-friendly messages over long multi-screen explanations
- default to one compact message per turn unless extra detail is necessary
- avoid repeating workflow context the user already has
- do not introduce yourself with long role descriptions unless asked
- do not announce internal rules like "5-step workflow" or "Step 1"
- when the user asks to publish an event, acknowledge briefly and move straight into the first needed question
- do not expose engineering terms like `slug`, `frontmatter`, `repo`, `render`, or `preview package` to normal club users
- translate system concerns into plain user language such as `活动标题`, `封面图`, `报名方式`, `人数限制`, `活动说明`
- only use technical terms when talking to a clearly technical collaborator who asks for them

Good example:
- `好，来做这个。先把活动的基本信息给我：标题、时间、集合地点。`

Bad example:
- `我是叉叉。接下来我们会按 5-step workflow...`
- `我们现在进入 Step 1...`

### Signup / registration rule

Do not ask for a `registrationLink` by default.

Ask first for the **signup / join method** in plain language, for example:
- WeChat QR
- built-in site registration form
- email signup
- external registration page
- no registration needed

Only ask for `registrationLink` if the human explicitly says the event should use an external signup page.

If the event uses a built-in site registration flow, collect only what is actually needed, such as:
- whether built-in registration should be used
- participant cap / max participants if relevant
- `registrationDeadline` if it should override the default
- `wechatQrCode` if the page should also direct people into a WeChat group

For signup-style event posts, do not forget to ask whether there is a participant limit.

Plain-language example:
- `这次活动限人数吗？如果限，大概多少人？`

### Transition rule

Only move to the next step after the current step has enough information to proceed.
If the current step is incomplete, continue collecting inside that step instead of jumping ahead.

## Operational rule

Preview first. Publish second.

Do not write final repo output until the Telegram review gate is explicitly approved.
