# Poster Router Minimal Routing Playbook

This file defines the minimal practical routing behavior for `poster-router`.

## Goal

Route quickly and accurately without turning the router into a giant all-knowing agent.

## General rule

Prefer early handoff over over-analysis.

If a request is clearly collection-shaped, route it.
Only ask a clarifying question when the target collection is genuinely ambiguous.

## Routing cues

### Route to `events-poster`
Typical user intent examples:
- 我想发一个活动帖
- 帮我发周六骑行活动
- 做个报名帖
- 发布 workshop / social ride / race announcement

### Route to `routes-poster`
Typical user intent examples:
- 把这条路线发到网站上
- 做个路书页面
- 发布一个 route page
- 这是 Komoot/GPX 路线，帮我整理

### Route to `media-poster`
Typical user intent examples:
- 把这次活动整理成回顾帖
- 发一篇宣传 recap
- 做一个 gallery / interview / story 类型 post

### Route to `knowledge-poster`
Typical user intent examples:
- 写一篇营养补给文章
- 发一个训练科普
- 做个骑行知识帖

## When to ask one clarifying question

Ask one short question if the request could reasonably map to more than one collection.

Example:
- “这是要发活动报名帖，还是活动结束后的回顾帖？”

Do not chain many clarifying questions inside router.

## Handoff rule

Once classification is stable:
- state the chosen collection internally
- construct the minimal handoff package
- transfer control to the specialized posting skill

## Anti-patterns

Do not:
- ask for full metadata in router
- ask for final cover selection in router
- build markdown in router
- hold the conversation too long before handoff
