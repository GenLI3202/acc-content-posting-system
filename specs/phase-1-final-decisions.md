# Phase 1 Final Decisions

Project: `ACC Content Posting System`

This file records the final Phase-1 decisions that close the current design round and define the first runnable loop boundary.

---

## 1. Scope boundary

Phase 1 only targets:
- `poster-router`
- `events-poster`

No other collection is part of the first runnable loop.

Priority order remains:
1. `events-poster`
2. `routes-poster`
3. `media-poster`
4. `knowledge-poster`

---

## 2. Review-before-publish principle

Phase 1 keeps the hard rule:

**Preview first. Publish second.**

The ACC repo is the publish target, not the first preview surface.
Telegram is the first review surface.

---

## 3. Preview rendering decision

### Default preview output
Use a **long screenshot preview** of the rendered markdown/page-like draft as the primary preview artifact.

### Required preview package components
A valid Phase-1 preview package should include:
1. long screenshot preview
2. draft markdown attachment
3. short summary text

### Optional fallback
A PDF preview may be added as a fallback when:
- the content is especially long
- long screenshot generation is unstable
- reviewers explicitly want a paginated reading form

### Preview hierarchy
Preferred order:
1. long screenshot preview
2. draft `.md`
3. PDF preview (optional fallback)

---

## 4. Publish write decision

After explicit Telegram approval, Phase 1 may write directly to the local ACC repo target paths.

This round does **not** require:
- automatic branch workflow
- automatic PR creation
- advanced GitHub choreography

Those can be added later.

### Publish target examples for events
- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`
- `frontend/public/images/events/{slug}/cover.jpg`
- `frontend/public/images/events/{slug}/wechat-qr.png`
- `frontend/public/images/events/{slug}/gallery/*`

---

## 5. First runnable loop definition

The first runnable loop should be:

1. Telegram user requests an event post
2. `poster-router` classifies as `events`
3. `events-poster` collects layered event information
4. `events-poster` constructs / updates EventDraft
5. `events-poster` normalizes assets
6. `events-poster` generates local markdown draft
7. `events-poster` generates long screenshot preview
8. preview package returns to Telegram for review
9. reviewer requests revision or approves
10. after approval, write final markdown + governed assets into ACC repo

---

## 6. Explicit non-goals for Phase 1

Do not block Phase 1 on:
- perfect ACC frontend-fidelity preview
- branch / PR automation
- multi-collection support
- complex permissions system
- heavy observability stack
- full workflow engine implementation

---

## 7. Decision status

These decisions are considered locked for the current design round unless a concrete implementation problem forces revision.
