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
displaySections:
  - upcoming
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

## Recurring event frontmatter

Use this when the event is a repeating weekly regular rather than a one-off occurrence.

```yaml
displaySections:
  - regular

recurring:
  frequency: weekly
  intervalWeeks: 1
  timezone: Europe/Berlin
  rolloverTime: "22:00"
  slugBase: afterwork-ride
  registrationDeadlineHoursBefore: 19.5
```

## Notes

- Prefer `cover`, not `coverImage`
- `status` should default to `draft` during preview stage
- Final publish can switch to `published` when approved
- `displaySections` is the canonical authoring field
- `displaySection` is legacy-compatibility input only; do not emit it in new event output unless a repo migration explicitly requires that fallback
- `displaySections` values:
  - `hero`
  - `upcoming`
  - `regular`
- `eventType` values:
  - `social-ride`
  - `training-camp`
  - `race`
  - `workshop`
- recurring fields currently supported in ACC ClubHub:
  - `frequency` → currently `weekly`
  - `intervalWeeks`
  - `timezone`
  - `rolloverTime`
  - `slugBase`
  - `registrationDeadlineHoursBefore`
  - optional `enabled` / `paused`

## Authoring rule

For one-off events:
- always emit `displaySections`
- omit `recurring` unless the operator explicitly wants recurring behavior

For recurring weekly regulars:
- ask whether the event should actually auto-roll, not just appear in the `regular` section
- if yes, emit both `displaySections` and `recurring`
- if no, treat it as a one-off event that merely appears in `regular`

## Repo output paths

For multilingual event output:
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`
