# Route Embed Rules

Use this reference when an event includes a route link.

## Preferred order

1. Komoot link
2. Strava route link
3. Strava activity link
4. GPX / static screenshot fallback

## Core rule

Prefer a native interactive route embed over a static route screenshot.

Ask for a Komoot or Strava link first.
Only fall back to a screenshot when there is no usable interactive route link.

## Resolver script

Use the bundled resolver instead of hand-building embed code:

```bash
python skills/events-poster/scripts/resolve_route_embed.py '<route-url>' --json
```

The resolver returns:
- provider
- route type
- canonical public link
- embed URL when the provider supports iframe embedding directly
- embed HTML snippet
- notes / caveats

## Provider rules

### Komoot

Supported inputs:
- `https://www.komoot.de/tour/<id>...`
- `https://www.komoot.com/tour/<id>...`
- `https://www.komoot.com/<locale>/invite-tour/<id>...`

Output pattern:
- canonical link → `https://www.komoot.com/tour/<id>[?share_token=...]`
- embed URL → `https://www.komoot.com/tour/<id>/embed?profile=1[&share_token=...]`
- preferred body section → `路线预览 / Route Preview / Routenvorschau`

Notes:
- keep the plain Komoot link in the event facts block
- if `share_token` is present, preserve it in canonical and embed URLs
- if `share_token` is missing, embed may still work for public tours, but treat that as less reliable

### Strava route

Supported input:
- `https://www.strava.com/routes/<id>`

Use the standard Strava embed placeholder + script returned by the resolver.

Notes:
- keep the plain Strava link in the facts block
- Strava route embed does not use the same iframe URL shape as Komoot in this workflow

### Strava activity

Supported input:
- `https://www.strava.com/activities/<id>`

Use only when the activity itself is the right thing to show.
For planned club events, a route link is usually better than an activity link.

## Body placement

When a route embed exists, place it after the structured event facts block.

Typical order:
1. opening narrative
2. event facts block
3. route embed section
4. logistics / return
5. join / participation

## Fallback rule

Use a static route image only when:
- there is no usable Komoot / Strava link
- embed generation fails
- page/script constraints make the interactive embed unusable
