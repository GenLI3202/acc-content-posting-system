# Multilingual Output Rules

## Recommended v1 strategy

Maintain one canonical draft object in a source language, then derive collection outputs for the required repo languages.

## Why

- reduces internal duplication
- keeps review focused on one canonical content object
- still supports ACC repo's multilingual file layout

## ACC event output example

- `frontend/src/content/events/zh/{slug}.md`
- `frontend/src/content/events/en/{slug}.md`
- `frontend/src/content/events/de/{slug}.md`

## Important distinction

Internal draft model:
- one canonical draft object

Repo output model:
- multiple language-specific markdown files
