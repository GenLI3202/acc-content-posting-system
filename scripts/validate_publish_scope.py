#!/usr/bin/env python3
"""Validate that planned repo writes stay inside the ACC Phase-1 event content surface.

Usage:
  python scripts/validate_publish_scope.py \
    --repo-root /path/to/acc_clubhub \
    --policy specs/content-scope-policy.yaml \
    frontend/src/content/events/zh/foo.md \
    frontend/public/images/events/foo/cover.jpg

Exit codes:
  0 = all paths allowed for write
  1 = one or more paths violate scope or path safety
  2 = usage/config error
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import sys
from pathlib import Path
from typing import Dict, List


SECTIONS = {"write", "read", "forbid"}


def parse_policy(path: Path) -> Dict[str, List[str]]:
    if not path.exists():
        raise FileNotFoundError(f"policy file not found: {path}")

    data = {"write": [], "read": [], "forbid": []}
    current = None
    for raw_line in path.read_text().splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" ") and stripped.endswith(":"):
            key = stripped[:-1]
            current = key if key in SECTIONS else None
            continue
        if current and stripped.startswith("- "):
            data[current].append(stripped[2:].strip())
    if not data["write"]:
        raise ValueError(f"no write rules found in policy: {path}")
    return data


def normalize_rel_path(raw: str, repo_root: Path) -> str:
    candidate = Path(raw)
    if candidate.is_absolute():
        try:
            rel = candidate.resolve().relative_to(repo_root.resolve())
        except Exception as exc:
            raise ValueError(f"absolute path escapes repo root: {raw}") from exc
    else:
        rel = Path(os.path.normpath(raw))

    rel_str = rel.as_posix().lstrip("./")
    if rel_str in {"", "."}:
        raise ValueError(f"empty path is not writable: {raw}")
    if rel_str.startswith("../") or "/../" in f"/{rel_str}":
        raise ValueError(f"path traversal is not allowed: {raw}")
    return rel_str


def matches_any(path: str, patterns: List[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def validate_paths(paths: List[str], repo_root: Path, policy_path: Path) -> int:
    policy = parse_policy(policy_path)
    failures = []
    successes = []

    for raw in paths:
        try:
            rel = normalize_rel_path(raw, repo_root)
        except ValueError as exc:
            failures.append((raw, str(exc)))
            continue

        if matches_any(rel, policy["forbid"]):
            failures.append((rel, "matches forbidden scope"))
            continue
        if not matches_any(rel, policy["write"]):
            failures.append((rel, "outside allowed write scope"))
            continue
        successes.append(rel)

    if failures:
        print("PUBLISH_SCOPE_INVALID")
        for path, reason in failures:
            print(f"- {path}: {reason}")
        if successes:
            print("allowed_paths:")
            for path in successes:
                print(f"- {path}")
        return 1

    print("PUBLISH_SCOPE_OK")
    for path in successes:
        print(f"- {path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="planned repo write paths (relative to repo root or absolute inside repo root)")
    parser.add_argument("--repo-root", required=True, help="ACC ClubHub repo root")
    parser.add_argument("--policy", default="specs/content-scope-policy.yaml", help="scope policy yaml path")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).expanduser()
    policy_path = Path(args.policy).expanduser()
    if not policy_path.is_absolute():
        policy_path = Path.cwd() / policy_path

    try:
        return validate_paths(args.paths, repo_root=repo_root, policy_path=policy_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
