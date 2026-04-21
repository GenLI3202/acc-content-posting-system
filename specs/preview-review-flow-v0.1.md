# Preview / Review Flow v0.1

## Event posting flow

1. `poster-router` classifies the request as `events`
2. `events-poster` collects required event information and assets
3. `events-poster` builds / updates the posting session draft object
4. `events-poster` produces:
   - local markdown draft
   - preview image
   - asset summary
5. preview package is returned to Telegram
6. reviewer either:
   - requests revision
   - approves publish
7. only after approval does the system prepare repo-write output
8. publish step writes markdown + governed assets into ACC repo

## Non-goal

This spec does not yet define branch / PR / direct-commit behavior. It only defines the review gate before publish.
