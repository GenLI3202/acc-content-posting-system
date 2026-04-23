# Event Draft Schema Example

This file makes the generic posting-session contract concrete for the `events` collection.

## Purpose

Represent one event posting request as a structured draft object.

Markdown, preview images, and repo output are derived from this object.

## Example schema

```yaml
session_id: evt_2026_04_21_001
collection: events
post_type: event-post
source_channel: telegram
source_language: zh
slug: 2026-acc-season-opening
status: preview-ready

intent:
  summary: ACC season opening social ride announcement
  reviewer_surface: telegram-group

core_fields:
  title: ACC 2026 开春咖啡骑
  description: 新赛季第一骑，轻松节奏，骑完一起喝咖啡
  date: 2026-04-18 10:30
  location: 慕尼黑动物园 · Tierparkstraße 30, 81543 München
  eventType: social-ride
  displaySection: hero
  signup_mode: wechat-group

body_sections:
  opening_narrative: >-
    冬天终于要过去了……
  route_summary: >-
    41.6km，爬升 350m，咖啡骑节奏，无均速门槛。
  intensity_text: 无均速要求，沿途互相等候
  notes_text: 头盔必戴，公路车或砾石车，自备补给
  return_text: >-
    可选 S-Bahn 返回，或沿河道骑回市区。
  join_text: >-
    报名后请加入微信群获取最新通知。

links:
  route_link: https://www.komoot.com/...
  registration_link: null

route_embed:
  provider: komoot
  route_type: tour
  canonical_url: https://www.komoot.com/tour/2885696236?share_token=...
  embed_url: https://www.komoot.com/tour/2885696236/embed?profile=1&share_token=...
  embed_html: >-
    <iframe src="https://www.komoot.com/tour/2885696236/embed?profile=1&share_token=..."
    width="100%" height="700" frameborder="0" scrolling="no"></iframe>
  notes: []

assets:
  cover:
    source: telegram-upload
    planned_repo_path: frontend/public/images/events/2026-acc-season-opening/cover.jpg
    public_url: /images/events/2026-acc-season-opening/cover.jpg
    status: assigned
  wechat_qr:
    source: telegram-upload
    planned_repo_path: frontend/public/images/events/2026-acc-season-opening/wechat-qr.png
    public_url: /images/events/2026-acc-season-opening/wechat-qr.png
    status: assigned
  gallery:
    - source: telegram-upload
      planned_repo_path: frontend/public/images/events/2026-acc-season-opening/gallery/01-group-start.jpg
      public_url: /images/events/2026-acc-season-opening/gallery/01-group-start.jpg
      status: assigned
    - source: telegram-upload
      planned_repo_path: frontend/public/images/events/2026-acc-season-opening/gallery/02-cafe-stop.jpg
      public_url: /images/events/2026-acc-season-opening/gallery/02-cafe-stop.jpg
      status: assigned

review:
  preview_package_ready: true
  last_review_status: pending
  approval_signal: null

outputs:
  local_markdown_draft: /local/staging/events/2026-acc-season-opening.md
  local_preview_image: /local/staging/events/2026-acc-season-opening-preview.png
  repo_targets:
    - frontend/src/content/events/zh/2026-acc-season-opening.md
    - frontend/src/content/events/en/2026-acc-season-opening.md
    - frontend/src/content/events/de/2026-acc-season-opening.md
```

## Notes

- this object is intentionally richer than frontmatter
- review state belongs here
- asset manifest belongs here
- repo output targets belong here
- publish should consume this object, not reconstruct everything from chat history
