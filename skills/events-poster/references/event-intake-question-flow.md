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

If these are still unclear, do not jump into asset details yet.

### Layer 2 · Secure the publishable minimum
Ask for the minimum set needed to create a credible event draft:
- short description / what this event is about
- route or plan summary
- intensity / who it is for
- signup method or join method
- whether there is a participant limit
- important notes / equipment / prerequisites

Important:
- do not ask for a registration link by default
- first ask how people join or register
- only ask for an external link if the human says signup should happen on an external page
- built-in site registration form is a valid default path and does not require a registration link
- for signup-style events, participant cap should be asked early, not forgotten until the very end

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

### Layer 4 · Fill enhancement fields
Only after the above:
- exact max participants number if not already confirmed
- registration deadline
- external registration link if needed
- display emphasis (`hero` / `upcoming` / `regular`)
- multilingual nuance if needed

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
- block preview just because enhancement fields are missing
