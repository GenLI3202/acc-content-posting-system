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
date: 2026-06-01 18:30
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
registrationDeadline: 2026-05-31T22:00:00
registrationLink: ''
distanceKm: 48.5
ACCOfficialRide: true
```

## Distance field rule

For new event output, prefer:

```yaml
distanceKm: 48.5
```

Do not emit `routeDistanceKm` as the default authoring field for new event posts.
Treat `routeDistanceKm` as legacy / compatibility context only.

If the event is a ride, route-led event, or other distance-based activity, collect distance explicitly.
If the event is an `ACCOfficialRide`, treat distance as effectively required metadata.

## Reference-profile rule

The live `afterwork-ride-munchen-nord` file is a strong reference for:
- real field names
- a valid recurring event shape
- a valid official-ride shape
- a valid built-in registration pattern

But it is **not** the universal template for all events.

Treat it as a `recurring official ride` reference profile, not a generic one-off event reference.

For one-off baseline structure, prefer to cross-check against:
- `2026-acc-season-opening`

For one-off events such as weekend rides, workshops, or single-date special events:
- do not emit `recurring` by default
- do not default `ACCOfficialRide` to true
- do not force `regular` placement just because a recurring reference file uses it
- do not force insurance / fee copy unless the event actually needs it
- do not force rich recurring-ride body sections unless the event actually needs them

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
- `date` should normally include time, not just a bare date
- `registrationDeadline` should use a full timestamp string when manually overridden
- built-in registration flows may still preserve `registrationLink: ''` as an explicit empty string when following the established working event-file pattern
- `displaySections` is the canonical authoring field
- `displaySection` is legacy-compatibility input only; do not emit it in new event output unless a repo migration explicitly requires that fallback
- `displaySections` values:
  - `hero`
  - `upcoming`
  - `regular`
- `eventType` values:
  - `after-work`
  - `social-ride`
  - `training-ride`
  - `training-camp`
  - `race`
  - `workshop`
  - `special`
  - `gathering`
  - `multi-day`
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
- emit `distanceKm` whenever the activity has a meaningful route distance
- default to a simpler event shape than recurring after-work reference files

For recurring weekly regulars:
- ask whether the event should actually auto-roll, not just appear in the `regular` section
- if yes, emit both `displaySections` and `recurring`
- if no, treat it as a one-off event that merely appears in `regular`

For official club rides:
- set `ACCOfficialRide: true` when the ride should follow official-ride semantics
- do not leave distance unspecified

For recurring official rides:
- `afterwork-ride-munchen-nord` is a valid shape reference
- richer metadata such as QR, insurance notes, and recurring settings may be appropriate
- do not silently copy that richer shape into unrelated one-off events

## Repo output paths

For multilingual event output:
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`
