# Router Handoff Contract

This file defines the minimum contract between `poster-router` and any specialized posting skill.

## Goal

Keep router thin while ensuring the specialized skill receives enough context to start effectively.

## Router responsibilities before handoff

Router should only do three things:
1. classify the target collection
2. resolve obvious ambiguity with the minimum clarifying question
3. hand off with a minimal structured context package

## Minimal handoff package

```yaml
collection: events | routes | media | knowledge
post_type: string
user_intent_summary: string
known_inputs:
  text_summary: string
  mentioned_assets: []
  mentioned_links: []
source_channel: telegram
source_language: zh | en | de | unknown
session_hint: optional string
```

## Rules

- Router does not need to collect full frontmatter
- Router should not try to solve collection-specific asset questions
- Router should not guess detailed schema fields when information is missing
- Router should preserve ambiguity notes for the specialized skill

## Event-specific handoff example

```yaml
collection: events
post_type: event-post
user_intent_summary: User wants to publish a new ACC ride announcement post
known_inputs:
  text_summary: Saturday social ride announcement with route, meetup point, and coffee stop
  mentioned_assets:
    - 1 cover candidate image
    - 1 WeChat QR image
    - 3 ride photos
  mentioned_links:
    - Komoot route link
source_channel: telegram
source_language: zh
session_hint: new draft
```
