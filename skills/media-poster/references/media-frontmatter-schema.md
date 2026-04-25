# Media Frontmatter Schema

This file defines the practical Phase-1 media frontmatter contract for ACC media posts.

## Source of truth

Cross-check against the live ACC repo:
- `frontend/src/content.config.ts`
- `docs/content-templates/media.md`
- `docs/core/content_governance_guide.md`
- existing entries under `frontend/src/content/media/**`

## Phase-1 required fields

```yaml
slug: my-media-post
title: Post Title
date: 2026-06-01
type: group-ride
cover: /images/media/group-ride/my-media-post/cover.jpg
status: draft
```

## Strongly recommended fields

```yaml
description: Short one-line summary shown in cards and meta surfaces
author: ACC Club
tags: [season-opening, munich-south]
featured: false
videoUrl: https://...
xiaohongshuUrl: https://www.xiaohongshu.com/...
```

## Notes

- Prefer `cover`, not `coverImage`, in new output
- `status` should default to `draft` during preview stage
- Final publish can switch to `published` when approved
- Current schema supports these canonical media type values:
  - `video`
  - `interview`
  - `adventure`
  - `group-ride`
- legacy values still exist for compatibility in the repo schema:
  - `影像`
  - `访谈`
  - `翻山越岭`
- some docs still mention `gallery`, but the currently inspected runtime/schema path is safer with `video | interview | adventure | group-ride`
- treat `gallery` as a schema-drift warning, not as a default fresh output choice

## Authoring rule

For new `media-poster` output:
- prefer current canonical runtime-supported type values
- do not emit legacy localized type values unless a repo migration explicitly requires that fallback
- do not emit `gallery` as a fresh default without confirming current runtime support in the target repo state
- if the operator wants a gallery-like piece but runtime support is unclear, keep the framing gallery-like in the body plan but confirm the final frontmatter `type` before publish

## Field intent reminders

- `featured` controls whether the media entry appears in the featured shelf on the media index page
- `videoUrl` enables embedded video rendering on the detail page when supported
- `xiaohongshuUrl` is an external source/distribution link, not a substitute for body content
- `tags` should support search/filter usefulness, not become a noisy keyword dump

## Repo output paths

For multilingual media output:
- `frontend/src/content/media/zh/{slug}.md`
- `frontend/src/content/media/en/{slug}.md`
- `frontend/src/content/media/de/{slug}.md`
