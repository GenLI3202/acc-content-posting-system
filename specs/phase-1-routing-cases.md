# Phase 1 Routing Cases

Project: `ACC Content Posting System`

Purpose:
Validate whether `poster-router` can reliably distinguish `events` requests from nearby but different intents.

---

## Expected router behavior

Router should:
- classify obvious requests directly
- ask at most one clarifying question if the target collection is ambiguous
- hand off early once classification is stable

---

## Event-positive cases

### E1
**User says:**
> 我想发一个周三 afterwork ride 的活动帖

**Expected classification:** `events`
**Expected post_type:** `event-post`
**Expected router behavior:** direct handoff, no extra clarification needed

### E2
**User says:**
> 帮我做一个报名帖，这周六俱乐部 social ride 要发出来

**Expected classification:** `events`
**Expected post_type:** `event-post`
**Expected router behavior:** direct handoff

### E3
**User says:**
> 我们要发布一个 workshop event 页面

**Expected classification:** `events`
**Expected post_type:** `event-post`
**Expected router behavior:** direct handoff

### E4
**User says:**
> 需要发一个 race 活动通知和报名信息

**Expected classification:** `events`
**Expected post_type:** `event-post`
**Expected router behavior:** direct handoff

---

## Route-positive cases

### R1
**User says:**
> 把这条 Komoot 路线发到网站上，做成一个路书页面

**Expected classification:** `routes`
**Expected router behavior:** direct handoff to `routes-poster`

### R2
**User says:**
> 我想整理一条 Munich south gravel route

**Expected classification:** `routes`

---

## Media-positive cases

### M1
**User says:**
> 把上周末骑行做成一个回顾帖

**Expected classification:** `media`

### M2
**User says:**
> 这些活动照片帮我做个 recap post

**Expected classification:** `media`

---

## Knowledge-positive cases

### K1
**User says:**
> 写一篇营养补给的科普帖

**Expected classification:** `knowledge`

### K2
**User says:**
> 做一个训练知识文章，讲 FTP interval

**Expected classification:** `knowledge`

---

## Ambiguous cases requiring one clarification

### A1
**User says:**
> 我想发一个 afterwork ride 的 post

**Ambiguity:** could be event announcement or recap

**Expected router question:**
> 这是要发活动报名帖，还是活动结束后的回顾帖？

### A2
**User says:**
> 这条路线和周三活动都想发

**Ambiguity:** route page vs event post

**Expected router behavior:** ask which content should be created first, then hand off one collection at a time

---

## Anti-patterns to watch for

Router should fail this test if it:
- asks for full metadata before classification
- asks multiple chained clarification questions
- starts drafting content itself
- delays handoff after classification is already obvious
