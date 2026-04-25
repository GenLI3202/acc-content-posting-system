# Router → Media Handoff

This file narrows the generic router handoff contract to the `media-poster` case.

## What `media-poster` expects from router

Minimum expected input:
- `collection = media`
- `post_type = media-post`
- a short user intent summary
- any already-mentioned links or media assets
- source language hint when available

## What `media-poster` does after handoff

Once handed off, `media-poster` owns:
- media-specific questioning
- source-shape classification
- editorial framing decisions
- missing field discovery
- media asset classification
- draft object creation/update
- preview package generation
- review loop handling until publish-ready

## What router should not pre-empt

Router should not try to decide:
- final media `type`
- final `featured` decision
- final cover choice
- final page framing
- final markdown structure

Those belong to `media-poster`.

## If ambiguity remains

If the request is clearly media-related but incomplete, router should still hand off rather than over-question.

Example:
- “帮我整理一下开春首骑的回顾”
- “把这个视频挂到 clubhub media”

Both are already enough to route into `media-poster`.
