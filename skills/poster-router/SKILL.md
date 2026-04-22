---
name: poster-router
description: Route ACC content posting requests from Telegram into the correct collection-specific posting skill. Use when a user wants to publish Across Cycling Club content but the target collection must be classified first, such as an event announcement, route page, recap/media post, or knowledge article. Trigger on requests like “发活动帖”, “做报名帖”, “发路线”, “做路书页面”, “整理活动回顾”, or “写训练/营养文章”. Perform thin intake, one-question clarification when necessary, and handoff only; do not own collection-specific schema filling, asset rules, or markdown generation.
---

# Poster Router

## Core job

Act as a thin intake and classification layer for ACC content posting requests.

## Do

- identify whether the request is for `events`, `routes`, `media`, or `knowledge`
- ask the minimum clarifying question when the target collection is ambiguous
- hand off to the correct specialized posting skill
- keep the interaction short and operational

## Do not do

- do not build full frontmatter
- do not write markdown drafts
- do not decide final asset paths
- do not act like a monolithic posting brain

## Classification guidance

- `events`: ride announcement, signup post, workshop announcement, event registration page
- `routes`: route page, roadbook, route guide, GPX/Komoot-based route content
- `media`: recap, post-event promo, gallery/story/video-driven post
- `knowledge`: training, nutrition, cycling knowledge, editorial education post

## Read shared contract

- `../../shared-references/router-handoff-contract.md`
- `references-routing-playbook.md`

## Output contract

After classification, explicitly state the chosen collection and continue via the corresponding posting skill using the minimal handoff contract.
