---
name: events-poster
description: Create ACC event announcement posts from Telegram conversations into repo-ready draft packages. Use when publishing an event/signup post for Across Cycling Club, including event frontmatter, body structure, asset classification, local preview generation, and review-before-publish workflow. Supports cover image, WeChat QR, and gallery assets under the ACC event asset rules.
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

## Operational rule

Preview first. Publish second.

Do not write final repo output until the Telegram review gate is explicitly approved.
