# Router → Events Handoff

This file narrows the generic router handoff contract to the `events-poster` case.

## What `events-poster` expects from router

Minimum expected input:
- `collection = events`
- `post_type = event-post`
- a short user intent summary
- any already-mentioned assets or route links
- source language hint when available

## What `events-poster` does after handoff

Once handed off, `events-poster` owns:
- event-specific questioning
- missing field discovery
- event asset classification
- draft object creation/update
- preview package generation
- review loop handling until publish-ready

## What router should not pre-empt

Router should not try to decide:
- final `displaySections`
- final recurring vs one-off behavior
- final `eventType`
- final cover choice
- final gallery file names
- final markdown structure

Those belong to `events-poster`.

## If ambiguity remains

If the request is clearly event-related but incomplete, router should still hand off rather than over-question.

Example:
- “帮我发周六骑行活动”

This is already enough to route into `events-poster`.
