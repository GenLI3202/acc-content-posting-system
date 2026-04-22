# Content Scope Restriction

Project: `ACC Content Posting System`

This spec defines the path-level scope restriction strategy for the poster agent in Phase 1.

## Goal

Apply **least privilege** without prematurely splitting the ACC repository into multiple repos.

Phase 1 uses **path sandboxing** rather than repository splitting.

---

## Decision

For Phase 1, the poster agent should **not** receive unrestricted working access to the full `acc_clubhub` repository.

Instead, it should operate as a **content-scoped agent** with:
- explicit write-allowed paths
- explicit read-only support paths
- explicit forbidden paths

---

## Why this approach

### Why not full repo access
Because the poster agent should not be able to:
- touch backend code
- alter unrelated infra/config
- modify general repo internals outside the content publishing surface

### Why not split repos yet
Because splitting into content sub-repos with sync-back into the main repo is possible, but would introduce unnecessary complexity too early:
- sync direction questions
- source-of-truth ambiguity
- subtree/submodule workflow overhead
- conflict resolution burden

Phase 1 should validate the content-posting workflow before repo topology is redesigned.

---

## Phase 1 path model

### Write-allowed scope
For Phase 1, writable scope should be limited to the **event posting surface** only.

### Read-only support scope
The agent may read selected schema/template/governance files needed to build compliant outputs.

### Forbidden scope
Everything unrelated to event content publication should be forbidden by default.

---

## Implementation guidance

Use a dual-layer restriction model:

### Layer 1 · Human/agent-readable
Document the scope in Markdown so the skill and humans understand the boundary.

### Layer 2 · Machine-readable
Represent the same scope in YAML so future validation steps or tooling can enforce it more reliably.

Markdown is good for explanation.
YAML is better for machine-consumable restriction.

---

## Phase 1 principle

The poster agent should behave as if it is working inside a content-only workspace, even though the underlying ACC project remains a single repository.

---

## Future option

After Phase 1 and Phase 2 prove stable, reevaluate whether ACC content should move to a dedicated content repository.

That question is explicitly deferred.
