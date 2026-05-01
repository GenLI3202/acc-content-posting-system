# Event Body Structure

Phase-1 event posts should not be just frontmatter. They should generate a readable ACC event page draft.

## Recommended body structure

## Profile distinction

Do not treat one successful recurring event file as the mandatory body shape for every event.

Use two mental profiles:

### Profile A · one-off event baseline
Typical for:
- weekend rides
- one-time workshops
- special one-date events
- race / camp / gathering announcements

Reference example:
- `2026-acc-season-opening`

Baseline shape can be:
1. opening narrative
2. facts block
3. optional route preview
4. logistics
5. join section

Only add extra sections when the event actually needs them.

This one-off baseline does **not** need to inherit every rich section from recurring after-work rides.
For example, bike-type row, participant-limit row, insurance / fee section, or long activity-explanation prose should stay optional.

### Profile B · recurring official ride reference
Typical for:
- recurring after-work rides
- regular official club rides

Reference example:
- `afterwork-ride-munchen-nord`

This profile may legitimately include richer sections such as:
- route preview
- activity explanation
- insurance / fee section
- QR section

The current `afterwork-ride-munchen-nord` file should be treated as this profile, not as the universal default.

### 1. Opening narrative
A short inviting paragraph or two explaining:
- what the event is
- who it is for
- the vibe / expectation

### 2. Structured event facts block
Capture the practical event facts in a compact block or table.
The currently well-performing ACC event example supports a richer facts block such as:
- time
- meeting point
- route
- intensity
- suitable bike type
- notes
- participant limit

### 2.5 Route embed section
When a usable Komoot or Strava link exists, prefer an interactive route embed section after the facts block.

- prefer native Komoot / Strava embed over uploading a static route screenshot
- keep the plain route link in the facts block
- use a screenshot only when interactive embed is unavailable

### 3. Activity explanation section
After route preview, allow a short prose section that explains:
- the spirit of the activity
- whether it is social / training / relaxed / beginner-friendly
- any expectation-setting that should not be buried inside the facts table

This pattern exists in the working `afterwork-ride-munchen-nord` event and should be treated as a strong `recurring official ride` reference shape, not an accidental one-off.

### 4. Logistics / return section
Optional but useful when relevant:
- return options
- train/S-Bahn options
- parking or meetup notes

### 5. Join / participation section
Explain:
- how to sign up
- where to join the Telegram / WeChat group
- any registration deadline or participant limit

When built-in site registration is used, the body may still explicitly explain that QR/group join does not equal successful registration.

### 6. Insurance / fee section
When the event is an official ACC ride, allow a dedicated section for:
- insurance eligibility
- member / non-member pricing
- student discount rule
- on-site payment note

Do not emit this section by default for unrelated one-off events.

### 7. Gallery / media preview section
When gallery images exist, allow a simple image section or placeholders for preview.

## Phase-1 generation rule

If not all details are available, generate a draft with clear placeholders rather than pretending facts exist.

## Tone

- operational but inviting
- club-native, not corporate
- specific, not generic
- do not over-polish into empty marketing copy

## Separator preference

The current working ACC event example uses `***` between major sections.
Treat that as a preferred event-post body separator style when generating new drafts, unless the repo later standardizes on a different separator.
