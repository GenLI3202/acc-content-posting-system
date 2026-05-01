# Event Intake Question Flow

This file defines the Phase-1 questioning strategy for `events-poster`.

## Goal

Collect enough information to produce a real ACC event preview package without over-interrogating the human.

## Questioning principle

Ask in layers, not as a giant form dump.

User input beats artificial completeness.

If a production-critical fact is unknown or ambiguous, stop and ask immediately.
Do not invent placeholder facts just to make the draft look complete.
An explicit unknown is better than a polished fake.

### Layer 1 · Establish the event core
These are the first things to secure:
- title / what is this ride or event called
- date and start time
- meeting point / location
- what kind of event it is
- whether this is a signup/announcement post
- whether this is a one-off dated event or a recurring series

If these are still unclear, do not jump into asset details yet.

### Layer 2 · Secure the publishable minimum
Ask for the minimum set needed to create a credible event draft:
- short description / what this event is about
- route or plan summary
- route distance if this is a ride / route-led event
- intensity / who it is for
- whether this is a one-off event or a recurring / regular event
- signup method or join method
- whether there is a participant limit
- important notes / equipment / prerequisites
- whether this should be marked `ACCOfficialRide` when official-club ride semantics matter

Important:
- do not ask for a registration link by default
- first ask how people join or register
- only ask for an external link if the human says signup should happen on an external page
- built-in site registration form is a valid default path and does not require a registration link
- when aligning to the current ACC working event-file pattern, built-in registration may still serialize as `registrationLink: ''` in frontmatter
- for signup-style events, participant cap should be asked early, not forgotten until the very end
- do not treat `regular` display and `recurring` behavior as the same thing; confirm both when needed

### Layer 3 · Collect assets and supporting materials
Once the event core is clear, ask for:
- cover image candidates
- WeChat QR image if relevant
- gallery photos if they should appear in preview
- route links (prefer Komoot / Strava; GPX if no interactive route page exists)
- any other media that should be reflected in the draft

Route rule:
- prefer asking for a Komoot or Strava link before asking for a route screenshot/image
- when a usable Komoot or Strava route link exists, prefer native route embed in the event page
- use route screenshots only as fallback when no interactive route link is available
- normalize route links through `scripts/resolve_route_embed.py` instead of hand-building embed URLs
- for new ACC event output, write route distance into `distanceKm`, not `routeDistanceKm`
- if the event is an official club ride, do not leave route distance unspecified

### Layer 4 · Fill enhancement fields
Only after the above:
- exact max participants number if not already confirmed
- registration deadline
- external registration link if needed
- route distance if it is still missing on a ride / route-led event
- display emphasis / placement target
  - ask whether the event should appear in `hero`, `upcoming`, `regular`, or multiple sections if the target site supports multi-placement
  - if the human wants multiple placements, capture the full intent instead of silently collapsing it to one value
- recurring details if relevant
  - whether the event should auto-roll as a recurring series, or just be a one-off event in the `regular` section
  - for current ACC ClubHub behavior, recurring support should be framed around weekly cadence first
  - if recurring is desired, confirm the practical fields that affect behavior:
    - `intervalWeeks`
    - `timezone` (default can be Europe/Berlin unless told otherwise)
    - `rolloverTime`
    - `slugBase` when relevant
    - relative registration deadline rule if it should move with each occurrence
- multilingual nuance if needed

## Profile choice rule

Before drafting the full body, decide which profile fits better:

### one-off-baseline
Use by default for:
- weekend rides
- single-date workshops
- special one-off events

Use `2026-acc-season-opening` as a practical structure reference for this baseline profile.

### recurring-official-ride
Use only when the event genuinely behaves like a recurring official club ride.

The current `afterwork-ride-munchen-nord` file is a good reference for this richer profile.
It must not silently become the default body shape for all events.

## Preferred compact questions

When section placement matters, prefer a compact operator-friendly question such as:

- `这个活动要显示在哪些位置？hero / upcoming / regular，可以多选。`

When recurrence matters, prefer a compact question such as:

- `这是一次性的，还是要做成每周自动滚动的 regular 活动？`

When recurring details are still missing, ask only the next missing behavior-critical item, not the full config dump.

## Hard-required fields for Phase 1 draft generation

At minimum, secure:
- title
- date/time
- location
- short description
- event intent / signup context

If one of these is missing, keep collecting before generating a meaningful draft.

## Can be deferred to revision round
These can be placeholders in an early preview if necessary:
- final cover choice
- final gallery set
- exact return logistics
- final participant cap
- final registration deadline

## When to stop asking and generate preview
Generate the first preview when:
- the event core is stable
- the publishable minimum is available
- enough asset info exists to form a reasonable draft package

Do not wait for perfection if the draft can already be reviewed meaningfully.

## Anti-patterns

Do not:
- dump 15 questions at once
- ask collection-irrelevant questions
- pretend missing facts exist
- silently reduce a multi-section display request to a single section without telling the human
- block preview just because enhancement fields are missing
