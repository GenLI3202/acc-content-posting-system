# Media Asset and Path Rules

This file defines the practical path rules for `media-poster` outputs.

## Core rule

Media markdown files must be written under the ACC ClubHub frontend content tree, not a repo-root shortcut.

Correct markdown target shape:
- `frontend/src/content/media/{lang}/{slug}.md`

Wrong shape:
- `src/content/media/{lang}/{slug}.md`

If the markdown lands in the wrong root, the site will not read it even if the file content itself looks correct.

## Canonical markdown targets

For multilingual output:
- `frontend/src/content/media/zh/{slug}.md`
- `frontend/src/content/media/en/{slug}.md`
- `frontend/src/content/media/de/{slug}.md`

## Canonical asset targets

Cover image:
- `frontend/public/images/media/{type}/{slug}/cover.jpg`

Gallery images:
- `frontend/public/images/media/{type}/{slug}/gallery/{nn}-{descriptor}.jpg`

## Type-aware path rule

The `{type}` folder should match the approved media type used in frontmatter, for example:
- `group-ride`
- `video`
- `interview`
- `adventure`

Do not invent a path type folder that disagrees with the final frontmatter `type`.

## Pre-write checklist

Before final write, verify all of the following:
- markdown targets start with `frontend/src/content/media/`
- asset targets start with `frontend/public/images/media/`
- the `{type}` path segment matches the final approved media type
- multilingual targets share the same slug
- no repo-root `src/content/media/...` path remains in the planned output set

## Failure rule

If planned output paths include `src/content/media/...` without the `frontend/` prefix:
- stop
- treat it as a blocking path error
- fix the target paths before commit / push

Do not rely on later review to catch this.
