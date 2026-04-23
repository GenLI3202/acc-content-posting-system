#!/usr/bin/env python3
"""Resolve route links into stable embed metadata for ACC event posts.

Supports:
- Komoot tours / invite-tour links
- Strava routes / activities links

Examples:
  python skills/events-poster/scripts/resolve_route_embed.py \
    'https://www.komoot.de/tour/2902292294?share_token=abc'

  python skills/events-poster/scripts/resolve_route_embed.py \
    'https://www.strava.com/routes/3155579856449932622' --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from html import escape
from typing import Optional
from urllib.parse import parse_qs, urlparse


@dataclass
class RouteEmbed:
    provider: str
    route_type: str
    source_url: str
    canonical_url: str
    embed_url: Optional[str]
    embed_html: str
    notes: list[str]


def _clean_url(url: str) -> str:
    url = url.strip()
    if not url:
        raise ValueError("empty route url")
    if not re.match(r"^https?://", url, re.I):
        url = "https://" + url
    return url


def resolve_komoot(url: str) -> RouteEmbed:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    m = re.search(r"/(?:[a-z]{2}(?:-[a-z]{2})?/)?(?:invite-)?tour/(\d+)", parsed.path, re.I)
    if not m:
        raise ValueError("unsupported Komoot url; expected /tour/<id> or /invite-tour/<id>")
    tour_id = m.group(1)
    share_token = qs.get("share_token", [None])[0]
    canonical_url = f"https://www.komoot.com/tour/{tour_id}"
    embed_url = f"https://www.komoot.com/tour/{tour_id}/embed?profile=1"
    notes: list[str] = []
    if share_token:
        canonical_url = f"{canonical_url}?share_token={share_token}"
        embed_url = f"{embed_url}&share_token={share_token}"
    else:
        notes.append("Komoot share_token missing; embed may depend on public visibility of the tour.")
    embed_html = (
        f'<iframe src="{escape(embed_url, quote=True)}" width="100%" height="700" '
        'frameborder="0" scrolling="no"></iframe>'
    )
    return RouteEmbed(
        provider="komoot",
        route_type="tour",
        source_url=url,
        canonical_url=canonical_url,
        embed_url=embed_url,
        embed_html=embed_html,
        notes=notes,
    )


def resolve_strava(url: str) -> RouteEmbed:
    parsed = urlparse(url)
    route_match = re.search(r"/routes/(\d+)", parsed.path, re.I)
    activity_match = re.search(r"/activities/(\d+)", parsed.path, re.I)
    notes: list[str] = []

    if route_match:
        embed_id = route_match.group(1)
        canonical_url = f"https://www.strava.com/routes/{embed_id}"
        embed_html = (
            f'<div class="strava-embed-placeholder" data-embed-type="route" '
            f'data-embed-id="{escape(embed_id, quote=True)}" data-style="standard" '
            'data-slippy="true"></div>\n'
            '<script src="https://strava-embeds.com/embed.js"></script>'
        )
        return RouteEmbed(
            provider="strava",
            route_type="route",
            source_url=url,
            canonical_url=canonical_url,
            embed_url=None,
            embed_html=embed_html,
            notes=notes,
        )

    if activity_match:
        embed_id = activity_match.group(1)
        canonical_url = f"https://www.strava.com/activities/{embed_id}"
        embed_html = (
            f'<div class="strava-embed-placeholder" data-embed-type="activity" '
            f'data-embed-id="{escape(embed_id, quote=True)}" data-style="standard" '
            'data-from-embed="false"></div>\n'
            '<script src="https://strava-embeds.com/embed.js"></script>'
        )
        notes.append("Strava activity embed depends on the activity being public and script execution being allowed on the page.")
        return RouteEmbed(
            provider="strava",
            route_type="activity",
            source_url=url,
            canonical_url=canonical_url,
            embed_url=None,
            embed_html=embed_html,
            notes=notes,
        )

    raise ValueError("unsupported Strava url; expected /routes/<id> or /activities/<id>")


def resolve_route_embed(url: str) -> RouteEmbed:
    url = _clean_url(url)
    host = urlparse(url).netloc.lower()
    if "komoot" in host:
        return resolve_komoot(url)
    if "strava" in host:
        return resolve_strava(url)
    raise ValueError("unsupported provider; expected Komoot or Strava url")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Komoot or Strava route/activity link")
    parser.add_argument("--json", action="store_true", help="print JSON result")
    args = parser.parse_args()

    try:
        result = resolve_route_embed(args.url)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return 0

    print(f"provider: {result.provider}")
    print(f"route_type: {result.route_type}")
    print(f"canonical_url: {result.canonical_url}")
    if result.embed_url:
        print(f"embed_url: {result.embed_url}")
    print("embed_html:")
    print(result.embed_html)
    if result.notes:
        print("notes:")
        for note in result.notes:
            print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
