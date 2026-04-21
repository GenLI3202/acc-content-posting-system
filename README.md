# ACC Content Posting System

A Telegram-driven, repo-native content posting system for Across Cycling Club.

## Purpose

This project defines and implements a content posting workflow that:
- receives posting requests from Telegram
- routes them into collection-specific posting skills
- generates local draft previews before publish
- gates publish through human review
- writes approved outputs into the ACC website repo

## Current scope

Priority order:
1. `events-poster`
2. `routes-poster`
3. `media-poster`
4. `knowledge-poster`

## Structure

- `skills/` — posting skills and router
- `shared-references/` — cross-skill governance and contracts
- `diagrams/` — architecture diagrams
- `specs/` — working specs and phase plans
- `renders/` — rendered architecture images
