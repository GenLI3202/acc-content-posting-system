# Media Draft Schema Example

This file makes the generic posting-session contract concrete for the `media` collection.

## Purpose

Represent one media posting request as a structured draft object.

Markdown, preview images, and repo output are derived from this object.

## Example schema

```yaml
session_id: med_2026_04_25_001
collection: media
post_type: media-post
source_channel: telegram
source_language: zh
slug: 2026-season-opening-recap
status: preview-ready

intent:
  summary: ACC 2026 season opening recap post
  reviewer_surface: telegram

core_fields:
  title: 影像回顾：2026 ACC 开春首骑
  description: 开春第一骑圆满收官，春日阳光、分组骑行与轻松社交的一次完整回顾。
  type: group-ride
  date: 2026-04-20
  author: ACC Club
  featured: true
  status: draft
  tags:
    - social-ride
    - munich-south
    - season-opening

source_bundle:
  source_shape: mixed-brief
  inputs:
    - telegram-text
    - telegram-images
    - event-page-link

primary_asset:
  kind: recap-story
  role: story-anchor
  notes: 活动回顾是主轴，图片和 event link 作为支撑

links:
  videoUrl: null
  xiaohongshuUrl: null
  related_event_url: /zh/events/2026-acc-season-opening

assets:
  cover:
    source: telegram-upload
    planned_repo_path: frontend/public/images/media/group-ride/2026-season-opening-recap/cover.jpg
    public_url: /images/media/group-ride/2026-season-opening-recap/cover.jpg
    status: assigned
  gallery:
    - source: telegram-upload
      planned_repo_path: frontend/public/images/media/group-ride/2026-season-opening-recap/gallery/01-group-start.jpg
      public_url: /images/media/group-ride/2026-season-opening-recap/gallery/01-group-start.jpg
      status: assigned

body_plan:
  framing: recap-led
  sections:
    - opening-summary
    - ride-story
    - highlights
    - related-links

review:
  preview_package_ready: true
  last_review_status: pending
  approval_signal: null

outputs:
  local_markdown_draft: /local/staging/media/2026-season-opening-recap.md
  local_preview_image: /local/staging/media/2026-season-opening-recap-preview.png
  repo_targets:
    - frontend/src/content/media/zh/2026-season-opening-recap.md
    - frontend/src/content/media/en/2026-season-opening-recap.md
    - frontend/src/content/media/de/2026-season-opening-recap.md
```

## Notes

- this object is intentionally richer than frontmatter
- review state belongs here
- asset manifest belongs here
- repo output targets belong here
- publish should consume this object, not reconstruct everything from chat history
- `source_shape` and `framing` should both be recorded; they are not interchangeable
- the draft should preserve the editorial role of each link/asset, not just the raw URLs
