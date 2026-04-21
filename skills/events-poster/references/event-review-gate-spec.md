# Event Review Gate Spec

This spec defines the review boundary between local draft generation and repo publish.

## Principle

There must be a hard gate between:
- local preview output
- final repo publish

That gate is the human review step in Telegram.

## What is under review

The review object is not only the markdown text.

Review should cover the full draft package:
- frontmatter sanity
- body structure
- event facts
- cover / QR / gallery choices
- overall presentation quality in preview form

## Minimum approval checklist

A Phase-1 approval should confirm:
- the event type is correct
- title/date/location are correct
- signup/join information is correct
- the body does not contain obvious fabricated details
- cover choice is acceptable
- QR asset usage is correct if present
- draft is ready to become repo output

## Publish prohibition before approval

Do not write final repo output when:
- preview has not been shown
- reviewer asked for changes
- key fields are still placeholders
- asset assignment is still unresolved

## Approval signal

Phase 1 can accept a simple explicit textual approval in Telegram, for example:
- “OK 发布”
- “可以发”
- “approve”

Do not infer approval from silence.

## Revision loop

When review feedback arrives:
- update the existing posting session
- regenerate preview package if needed
- return to Telegram review

## Publish transition

Only after explicit approval:
- switch draft status to `approved` / `publish-ready`
- generate final repo write outputs
- proceed to publish flow
