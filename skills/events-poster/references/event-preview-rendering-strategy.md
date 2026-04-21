# Event Preview Rendering Strategy

This file defines the practical preview rendering strategy for `events-poster` in Phase 1.

## Goal

Return a human-reviewable visual preview to Telegram before any repo publish occurs.

## Principle

The preview image does not need to be a perfect final-site rendering on day one.

It only needs to be good enough for humans to assess:
- structure
- obvious factual issues
- cover choice
- overall presentation quality

## Recommended fallback ladder

### Level 1 · Structured preview image
If a true page render is not yet available, generate a structured visual preview that includes:
- title
- date/time
- location
- short description
- body section summary
- chosen cover image
- asset summary

This is the minimum acceptable Phase-1 fallback.

### Level 2 · Markdown-render preview
If local markdown-to-HTML rendering is available, generate a markdown-render screenshot.

This is better because reviewers can see:
- hierarchy
- spacing
- readability
- image placement

### Level 3 · Frontend-like preview
If the system can reuse the ACC frontend rendering pipeline or a close approximation, produce a page-like screenshot.

This is the ideal target, but not required for the first usable iteration.

## Phase-1 recommendation

Start with a practical strategy:
- prefer a markdown-render preview if it is easy to generate
- otherwise use a structured preview image
- do not block the whole system on perfect site-faithful rendering

## Preview package minimum

The preview rendering strategy must support a Telegram preview package containing:
- one visual preview image
- one markdown draft attachment
- short summary text

## What the preview must make visible

A valid preview image should expose enough information for fast review of:
- title
- date/time
- location
- event identity and tone
- major body sections
- chosen cover presence
- obvious missing or placeholder sections

## Non-goal in Phase 1

Do not build a full dedicated preview webapp just to support review.

Prefer lightweight rendering that can evolve later.
