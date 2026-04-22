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

When the request is clearly an `Event Post`, first tell the user the full five-step workflow before collecting detailed information.

Use this structure in plain language:

1. `Intake & Intent Capture`
2. `Asset & Source Material Collection`
3. `Post Plan / Outline Confirmation`
4. `Full Draft + Preview Package`
5. `Review / Revise / Publish`

Then work strictly step by step.

### Required interaction rules

- first give the user the five-step overview
- then start Step 1 only
- do not ask Step 2 questions before Step 1 is sufficiently complete
- do not move to Step 3 before Step 2 materials are sufficiently collected
- do not generate the full draft before Step 3 is explicitly confirmed
- do not publish before Step 5 approval

### Conversation style rule

At the start of each step:
- state which step the user is in
- state what information is being collected in this step
- keep the questioning scoped to the current step

### Transition rule

Only move to the next step after the current step has enough information to proceed.
If the current step is incomplete, continue collecting inside that step instead of jumping ahead.

## Operational rule

Preview first. Publish second.

Do not write final repo output until the Telegram review gate is explicitly approved.
