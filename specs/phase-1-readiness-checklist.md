# Phase 1 Readiness Checklist

Project: `ACC Content Posting System`

Scope of this checklist:
- `poster-router`
- `events-poster`
- preview-before-publish loop
- Telegram-first review flow

---

## 1. Architecture and project governance

- [x] Project moved into `projects/acc-content-posting-system`
- [x] Independent project-level git history created
- [x] Public GitHub repository created
- [x] High-level system architecture documented
- [x] Layered architecture with preview-before-publish documented
- [x] Repository structure documented
- [x] Atomic local commits pushed to remote

## 2. Router layer

- [x] `poster-router` skill skeleton exists
- [x] Router intent classification documented
- [x] Minimal routing playbook documented
- [x] Router handoff contract documented
- [x] Event-specific router-to-events handoff documented
- [ ] Router message examples written out as executable prompt examples
- [ ] Router behavior tested against ambiguous real request examples

## 3. Events skill layer

- [x] `events-poster` skill skeleton exists
- [x] Event frontmatter schema documented
- [x] Event body structure documented
- [x] Event asset rules documented
- [x] Event intake question flow documented
- [x] Event operational workflow documented
- [x] Event preview package spec documented
- [x] Event review gate spec documented
- [x] Event preview rendering strategy documented
- [x] Event publish step spec documented
- [x] Event draft schema example documented
- [x] Event markdown templates added
- [ ] End-to-end event posting prompt examples added
- [ ] One realistic event case encoded as a complete worked example

## 4. Shared contracts

- [x] Posting session schema documented
- [x] Asset path and naming rules documented
- [x] Multilingual output rules documented
- [x] Telegram intake conventions documented
- [x] ACC repo governance summary documented
- [ ] Cross-reference consistency checked against latest ACC repo governance files

## 5. Preview-before-publish loop

- [x] Preview-first principle documented
- [x] Telegram as first review surface documented
- [x] Review gate defined before publish
- [x] Publish transition defined at spec level
- [ ] Concrete preview rendering mechanism selected for Phase 1
- [ ] Concrete preview artifact generation command/tool chosen
- [ ] Telegram delivery shape tested in a realistic loop

## 6. Publish path

- [x] Final event repo targets defined at spec level
- [x] Asset target paths defined at spec level
- [x] Publish preconditions documented
- [ ] Actual write strategy decided (`direct write` / `branch` / `PR`)
- [ ] Failure + retry behavior tested on a toy example

## 7. Multilingual strategy

- [x] Canonical draft object strategy documented
- [x] Three-language repo output strategy documented
- [ ] Decision made on Phase 1 generation mode:
      - source language only + placeholders
      - source language + machine-derived zh/en/de drafts
      - full three-language first draft
- [ ] One multilingual sample output reviewed for acceptability

## 8. What is ready now

The following are already solid enough at the design/spec level:
- overall system architecture
- Phase 1 system boundary
- router/event skill boundary
- EventDraft concept
- preview-before-publish principle
- Telegram review gate
- event schema/body/asset rules

## 9. What is not yet runnable

The project is **not yet runnable as a real posting agent** because these operational choices are still open:
- concrete preview rendering mechanism
- concrete publish write mechanism
- tested multilingual generation behavior
- worked examples for router and event flow

## 10. Minimum work needed before first trial run

These are the next minimum tasks before a real trial run is reasonable:

1. choose the Phase-1 preview rendering mechanism
2. choose the Phase-1 publish write mechanism
3. add one full realistic event worked example
4. add router ambiguity examples
5. run one dry-run simulation from Telegram request → preview package

## 11. Readiness verdict

Current state:

**Spec-ready, not yet trial-run ready.**

The architecture and Phase-1 workflow are sufficiently defined.
The next step is no longer more abstract design — it is selecting concrete execution mechanisms and building one worked dry run.
