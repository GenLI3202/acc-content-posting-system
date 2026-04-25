# PROGRESS.md

This file tracks the design and implementation progress of the **ACC Content Posting System**.

Rule: whenever a meaningful project change is committed, review this file and update the relevant checklist items in the same working cycle.

---

## 1. System foundation

- [x] Define project purpose: Telegram-driven, repo-native content posting workflow
- [x] Establish `poster-router` as the common routing entrypoint
- [x] Define preview-first, publish-second review contract
- [x] Require explicit approval before publish
- [x] Define collection-specific poster direction instead of one monolithic poster
- [ ] Finalize stable cross-collection draft object conventions
- [ ] Finalize stable router → collection handoff contract for all supported collections

## 2. Phase-1 repo safety and publish governance

- [x] Restrict Phase-1 repo write surface for ACC ClubHub event publishing
- [x] Add publish-scope validation guard script
- [x] Define sync-remote-before-final-publish rule
- [x] Stop publish on dirty state / stale branch / conflict risk
- [x] Compact and clean event publishing guidance without removing safeguards
- [ ] Automatically wire publish guard invocation into final publish execution path
- [ ] Consider stronger sandboxing beyond current scope guard if later needed

## 3. Telegram / runtime behavior

- [x] Switch tester access model from pairing to Telegram DM allowlist
- [x] Keep group behavior in mention-gated open mode for testing
- [x] Confirm DM session isolation behavior
- [x] Confirm skill/prompt updates do not require gateway restart to affect new sessions
- [ ] Continue real Telegram testing in new sessions when major workflow changes land

## 4. Events-poster architecture and workflow

- [x] Define events-poster Phase-1 workflow
- [x] Define event draft schema example
- [x] Define event preview package contract
- [x] Define event publish step spec
- [x] Add route-link-first strategy for Komoot / Strava
- [x] Add route embed resolver script
- [x] Add route embed rules reference
- [x] Update event templates to support route embed section
- [x] Align events-poster with ACC ClubHub `displaySections` canonical output
- [x] Distinguish `regular` placement from true `recurring` behavior
- [x] Update event intake flow for one-off vs recurring and multi-section placement
- [x] Update event publish mapping to current ACC ClubHub frontmatter expectations
- [ ] Add explicit recurring event output examples beyond current schema sample
- [ ] Define final implementation path for automated publish execution from approved EventDraft

## 5. ACC ClubHub alignment work

- [x] Normalize Komoot-backed event pages to embed mode
- [x] Pull latest `acc_clubhub` master before aligning new event/media behavior
- [x] Review current event frontmatter reality (`displaySections`, `recurring`)
- [x] Raise issue for inconsistent `displaySection` vs `displaySections`
- [x] Unify canonical `displaySections` authoring in ACC ClubHub
- [x] Update docs/templates/CMS config to prefer `displaySections`
- [x] Keep legacy read compatibility for singular `displaySection`
- [x] Verify ACC ClubHub tests/build after the displaySections fix

## 6. Routes-poster design

- [ ] Decide whether `routes-poster` remains a standalone poster or is partially absorbed into broader knowledge workflows
- [ ] Review real ACC ClubHub routes schema and runtime behavior
- [ ] Draft routes-poster top-level architecture
- [ ] Define route intake workflow
- [ ] Define route frontmatter schema reference
- [ ] Define route draft schema example
- [ ] Define route body structure patterns
- [ ] Define route publish step spec
- [ ] Define router-to-routes handoff reference
- [ ] Define route asset/link handling rules (Komoot / Strava / GPX / cover / gallery)

## 7. Media-poster design

- [x] Decide to build `media-poster` as a dedicated collection-specific poster
- [x] Draft initial media-poster architecture diagram
- [x] Review real ACC ClubHub media schema and runtime behavior
- [x] Refine media-poster architecture around real media schema
- [x] Add GitHub-renderable media architecture markdown with Mermaid
- [x] Define `media-poster` SKILL.md
- [x] Define media intake question flow
- [x] Define media frontmatter schema reference
- [x] Define media draft schema example
- [x] Define media body structure families
- [x] Define media publish step spec
- [x] Define router-to-media handoff reference
- [x] Define media asset naming/path rules if current shared rules are insufficient

## 8. Knowledge-poster design

- [ ] Decide final split strategy for gear / training / routes / broader knowledge
- [ ] Draft knowledge-poster top-level architecture
- [ ] Review real ACC ClubHub knowledge schema and runtime behavior
- [ ] Define knowledge intake workflow
- [ ] Define knowledge frontmatter schema reference
- [ ] Define knowledge draft schema example
- [ ] Define knowledge body structure patterns
- [ ] Define knowledge publish step spec
- [ ] Define router-to-knowledge handoff reference

## 9. Documentation and maintenance discipline

- [x] Add project-level progress tracker (`PROGRESS.md`)
- [x] Add project rule to check and update progress after meaningful commits
- [ ] Review `PROGRESS.md` whenever a new collection skill is added or architecture direction changes
- [ ] Keep architecture docs in `specs/architecture/` aligned with latest decisions

---

## Immediate next focus

1. Finish the remaining `media-poster` gaps:
   - decide whether a media markdown template should be added now or after first real usage
   - run the first real end-to-end media drafting trial
2. After media stabilizes, design `knowledge-poster` with the same discipline.
