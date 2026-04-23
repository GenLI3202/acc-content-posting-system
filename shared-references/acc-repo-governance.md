# ACC Repo Governance

This folder stores shared governance knowledge reused by multiple posting skills.

Primary upstream source of truth currently lives in the ACC repo:
- `MAINTENANCE.md`
- `docs/agent-posting-spec.md`

Use this file as the local summary index, not as an independent competing spec.

## Current key rules

- use collection-specific markdown paths under `frontend/src/content/...`
- use governed asset paths under `frontend/public/images/...`
- prefer `cover`, not `coverImage`
- do not publish before review approval
- treat Telegram review as the first review surface
- Phase 1 event posting write scope is limited to:
  - `frontend/src/content/events/**`
  - `frontend/public/images/events/**`
- do not modify backend, infra, GitHub workflow, or unrelated content collections
- immediately before final repo write / commit / push, sync remote latest state and stop on conflict or unclear overwrite risk
- use `scripts/validate_publish_scope.py` to enforce the allowed write surface before final repo write
