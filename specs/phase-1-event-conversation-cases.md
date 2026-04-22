# Phase 1 Event Conversation Cases

Project: `ACC Content Posting System`

Purpose:
Define realistic event-post dry-run conversations for `events-poster`.

---

## Canonical test case

### Case name
`afterwork-ride-canonical`

### User intent
Publish an ACC afterwork ride event announcement post.

### Initial request
> 我们 ACC 马上要发布 Afterwork ride 了，帮我做一个 event post。

### Expected behavior
The agent should:
1. recognize this as `events`
2. announce the 5-step workflow
3. start with Step 1 only
4. avoid asking Step 2 questions too early

---

## Step 1 expected conversation shape

### Agent should say something like
> 好的。接下来我们需要完成 5 步：
> 1. Intake & Intent Capture
> 2. Asset & Source Material Collection
> 3. Post Plan / Outline Confirmation
> 4. Full Draft + Preview Package
> 5. Review / Revise / Publish
>
> 我们先完成第 1 步。

### Agent should collect
- working title
- date/time
- location
- event intent
- whether this is an announcement/signup post

### Example user answers
- title: ACC Afterwork Ride
- date/time: Wednesday 18:30
- location: Friedensengel
- intent: social afterwork ride announcement
- post type: signup/announcement

---

## Step 2 expected conversation shape

### Agent should now collect
- cover candidate image
- WeChat QR if available
- gallery images if intended
- route link
- video links if any
- signup/join method
- supporting notes

### Example user answers
- cover: one sunset ride photo
- QR: one WeChat group QR image
- route: Komoot link
- gallery: two additional ride photos
- video: none
- join method: scan QR and join WeChat group

### Important behavior
The agent should ask asset-role questions such as:
- 哪张作为封面？
- 这张是不是微信群二维码？
- 这两张是正文配图，还是只是参考？

---

## Step 3 expected conversation shape

### Agent should present a compact post plan
It should include:
- title
- one-line summary
- frontmatter direction
- planned sections
- planned use of cover / QR / route link / gallery

### Example plan summary
- opening intro paragraph
- event facts table
- short route/intensity section
- join via QR section
- optional gallery section

### Required user decision
The user must explicitly confirm or revise the plan before draft generation.

---

## Step 4 expected conversation shape

### Agent should produce
- markdown draft
- long screenshot preview
- summary text
- asset summary
- optional PDF only if needed

### Review expectation
The preview should already look coherent enough for a teammate to assess.

---

## Step 5 expected conversation shape

### Revision path
If the user says something like:
> 封面换第二张，路线说明再短一点

The agent should:
- revise the same draft
- regenerate preview package
- stay in review loop

### Approval path
If the user says something like:
> OK，发布

The system may proceed to publish-ready state and prepare repo write.

---

## Pass criteria

This case passes if the agent:
- follows the 5-step order
- does not skip directly to full draft
- classifies assets correctly enough for a coherent preview
- produces a usable event preview package
- respects review-before-publish
