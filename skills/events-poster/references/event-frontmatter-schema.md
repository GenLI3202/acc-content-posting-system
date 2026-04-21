# Event Frontmatter Schema

This file defines the practical Phase-1 event frontmatter contract for ACC event posts.

## Source of truth

Cross-check against the live ACC repo:
- `frontend/src/content.config.ts`
- `docs/content-templates/events.md`
- `docs/agent-posting-spec.md`
- `MAINTENANCE.md`

## Phase-1 required fields

```yaml
slug: my-event-slug
title: Event Title
location: Meeting point / venue
date: 2026-06-01
displaySection: upcoming
eventType: social-ride
cover: /images/events/my-event-slug/cover.jpg
status: draft
```

## Strongly recommended fields

```yaml
description: Short one-line summary shown in cards and meta surfaces
author: ACC Club
wechatQrCode: /images/events/my-event-slug/wechat-qr.png
maxParticipants: 30
registrationDeadline: 2026-05-25
```

## Notes

- Prefer `cover`, not `coverImage`
- `status` should default to `draft` during preview stage
- Final publish can switch to `published` when approved
- `displaySection` values:
  - `hero`
  - `upcoming`
  - `regular`
- `eventType` values:
  - `social-ride`
  - `training-camp`
  - `race`
  - `workshop`

## Repo output paths

For multilingual event output:
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`
