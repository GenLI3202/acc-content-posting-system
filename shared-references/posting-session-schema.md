# Posting Session Schema

Minimal cross-skill contract for a posting session / draft object.

## Purpose

Keep posting workflows stateful enough to avoid chaos, without building a heavyweight workflow engine.

## Minimal fields

```yaml
session_id: string
collection: events | routes | media | knowledge
post_type: string
source_language: zh | en | de
slug: string | null
status: intake | drafting | preview-ready | in-review | approved | published
fields: {}
assets: []
outputs: {}
```

## Notes

- this is a contract, not necessarily a separate service
- markdown is an output of the draft object, not the draft object itself
- review approval changes status but does not require a complex approval engine in v1
