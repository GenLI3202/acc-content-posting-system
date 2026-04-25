---
name: routes-poster
description: Create ACC route posts and roadbook-style route pages from conversational input into repo-ready draft packages. Use when publishing route collection content such as ride routes, route guides, route pages, GPX/Komoot-based route posts, and roadbook-style route descriptions. Trigger on requests like “发路线”, “做路书页面”, “整理 Komoot 路线”, or similar route-post intents. Handles route-specific schema, body structure, and route asset rules.
---

# Routes Poster

## Status

Planned as Priority 2 after `events-poster`.

## Intended job

Create structured ACC route draft packages aligned with the `routes` collection.

## Expected responsibilities

- collect route-specific fields
- build route draft objects
- map route outputs into ACC route markdown structure
- support preview-before-publish workflow
- explicitly remind the user not to resend the same route map / screenshot / image content multiple times as if it were a new asset

## Read before working

- `../../shared-references/source-material-intake-hygiene.md`
- `../../shared-references/publish-success-and-frontmatter-safety.md`

## Not implemented yet

This skill is currently a placeholder skeleton. Fill collection-specific references before active use.
