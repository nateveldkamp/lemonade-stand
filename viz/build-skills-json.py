#!/usr/bin/env python3
"""Build viz/skills.json from frontmatter on every skills/**/README.md.

The skill-tree visualization (viz/index.html) reads skills.json.
This script is the bridge from the markdown source-of-truth to that JSON.
Run after any change to a branch or Skill README's frontmatter.

Usage:
    python3 viz/build-skills-json.py

Exit codes:
    0 — success, skills.json written
    1 — validation error (missing referenced Skill, asymmetric edges, etc.)

The YAML parser here is deliberately minimal — it handles only the subset
of YAML used by our frontmatter schema (see docs/skills.md). It does not
require pyyaml, so the repo stays self-contained.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
OUTPUT_PATH = REPO_ROOT / "viz" / "skills.json"
SCHEMA_VERSION = 1


def main() -> int:
    branch_docs: list[dict] = []
    skill_docs: list[dict] = []
    prelude_doc: dict | None = None

    for readme_path in sorted(SKILLS_DIR.rglob("README.md")):
        fm = parse_frontmatter(readme_path.read_text(encoding="utf-8"))
        if fm is None:
            warn(f"no frontmatter: {readme_path.relative_to(REPO_ROOT)}")
            continue
        kind = fm.get("kind")
        if kind == "branch":
            branch_docs.append(fm)
        elif kind == "skill":
            skill_docs.append(fm)
        elif kind == "prelude":
            prelude_doc = fm
        else:
            warn(f"unknown kind={kind!r} in {readme_path.relative_to(REPO_ROOT)}")

    # Build the unified Skill list. Skills with their own README are
    # authoritative; not-started Skills are picked up from the inline
    # entries in their branch's `skills:` list.
    skills_by_slug: dict[str, dict] = {}
    for s in skill_docs:
        slug = s["slug"]
        if slug in skills_by_slug:
            error(f"duplicate Skill slug: {slug}")
            return 1
        skills_by_slug[slug] = {
            "slug": slug,
            "branch": s["branch"],
            "name": s["name"],
            "tagline": s["tagline"],
            "build_state": s["build_state"],
            "tier_count": s.get("tier_count", 5),
            "complexity_level": s.get("complexity_level"),
            "has_readme": True,
            "prereqs": s.get("prereqs") or [],
            "unlocks": [],
        }

    # Walk each branch's `skills:` list. For entries that are just slugs,
    # they must already be in skills_by_slug. For entries with inline data
    # (not-started Skills), build a placeholder Skill.
    branches_out: list[dict] = []
    for b in branch_docs:
        branch_slug = b["slug"]
        skill_slugs_in_order: list[str] = []
        for entry in b.get("skills") or []:
            entry_slug = entry["slug"]
            skill_slugs_in_order.append(entry_slug)
            if entry_slug in skills_by_slug:
                # README is authoritative; nothing to do here.
                continue
            # Inline declaration. Build a placeholder Skill node.
            skills_by_slug[entry_slug] = {
                "slug": entry_slug,
                "branch": branch_slug,
                "name": entry.get("name", entry_slug.split(".", 1)[-1]),
                "tagline": entry.get("tagline", ""),
                "build_state": entry.get("build_state", "not-started"),
                "tier_count": entry.get("tier_count", 5),
                "complexity_level": entry.get("complexity_level"),
                "has_readme": False,
                "prereqs": entry.get("prereqs") or [],
                "unlocks": [],
            }
        branches_out.append(
            {
                "slug": branch_slug,
                "name": b["name"],
                "tagline": b["tagline"],
                "quadrant": b.get("quadrant"),
                "build_state": b["build_state"],
                "skill_slugs": skill_slugs_in_order,
            }
        )

    # Validate prereq references, derive the inverse `unlocks`, and check the
    # monotonicity rule: a prerequisite must sit at a complexity level no
    # higher than the skill it unlocks (roads flow inward -> outward).
    errors: list[str] = []
    warnings: list[str] = []
    for skill in skills_by_slug.values():
        for target in skill["prereqs"]:
            if target not in skills_by_slug:
                warnings.append(
                    f"{skill['slug']}.prereqs references unknown Skill {target!r}"
                )
                continue
            # Derive the reverse edge so authors only write `prereqs`.
            skills_by_slug[target]["unlocks"].append(skill["slug"])
            lvl = skill.get("complexity_level")
            plvl = skills_by_slug[target].get("complexity_level")
            if lvl is not None and plvl is not None and plvl > lvl:
                warnings.append(
                    f"monotonicity: {skill['slug']} (L{lvl}) lists prereq "
                    f"{target} (L{plvl}) which sits further out"
                )

    for skill in skills_by_slug.values():
        skill["unlocks"] = sorted(set(skill["unlocks"]))

    for w in warnings:
        warn(w)
    for e in errors:
        error(e)
    if errors:
        return 1

    # Emit a flat edges list. Use prereq direction as canonical
    # (from prereq -> to dependent).
    edges: list[dict] = []
    seen_edges: set[tuple[str, str]] = set()
    for skill in skills_by_slug.values():
        for prereq_slug in skill["prereqs"]:
            pair = (prereq_slug, skill["slug"])
            if pair in seen_edges:
                continue
            seen_edges.add(pair)
            edges.append({"from": prereq_slug, "to": skill["slug"]})

    output = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "prelude": (
            {
                "slug": prelude_doc["slug"],
                "name": prelude_doc["name"],
                "tagline": prelude_doc["tagline"],
                "build_state": prelude_doc.get("build_state", "complete"),
            }
            if prelude_doc
            else None
        ),
        "branches": branches_out,
        "skills": [skills_by_slug[s] for s in sorted(skills_by_slug)],
        "edges": edges,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}: "
        f"{len(branches_out)} branches, {len(skills_by_slug)} Skills, "
        f"{len(edges)} edges"
    )
    if warnings:
        print(f"  ({len(warnings)} warnings — see above)")
    return 0


# ----- frontmatter / YAML-subset parser ----------------------------------


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return parse_yaml(text[4:end])


def parse_yaml(text: str) -> dict:
    """Parse the small YAML subset our frontmatter uses.

    Supports:
      - top-level scalar keys (string, int, bool, null)
      - inline lists on one line ([a, b, c])
      - multi-line list-of-scalars under a key
      - multi-line list-of-objects under a key, where each object's keys
        live at the indent past the leading '- '
    Does NOT support: nested dicts under top-level keys (other than the
    list-of-objects pattern), multi-line strings, anchors/aliases, flow maps.
    """
    result: dict = {}
    lines = [line.rstrip() for line in text.splitlines()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith((" ", "\t")):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest:
            result[key] = _scalar(rest)
            i += 1
            continue
        # Multi-line block.
        block_lines = []
        j = i + 1
        while j < len(lines):
            if not lines[j].strip():
                j += 1
                continue
            if lines[j].startswith((" ", "\t")):
                block_lines.append(lines[j])
                j += 1
            else:
                break
        result[key] = _parse_list_block(block_lines)
        i = j
    return result


def _scalar(value: str):
    if not value:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_scalar(p.strip()) for p in _split_top_level_commas(inner)]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in ("null", "~"):
        return None
    try:
        return int(value)
    except ValueError:
        pass
    return value


def _split_top_level_commas(s: str) -> list[str]:
    parts = []
    depth = 0
    current = []
    for ch in s:
        if ch in "[{":
            depth += 1
            current.append(ch)
        elif ch in "]}":
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def _parse_list_block(lines: list[str]) -> list:
    items: list = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if not stripped.startswith("- "):
            i += 1
            continue
        content = stripped[2:]
        if ":" in content:
            obj: dict = {}
            k, _, v = content.partition(":")
            obj[k.strip()] = _scalar(v.strip())
            obj_key_indent = indent + 2
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nxt_stripped = nxt.lstrip()
                if not nxt_stripped:
                    i += 1
                    continue
                nxt_indent = len(nxt) - len(nxt_stripped)
                if nxt_stripped.startswith("- "):
                    break
                if nxt_indent == obj_key_indent and ":" in nxt_stripped:
                    k, _, v = nxt_stripped.partition(":")
                    obj[k.strip()] = _scalar(v.strip())
                    i += 1
                else:
                    break
            items.append(obj)
        else:
            items.append(_scalar(content))
            i += 1
    return items


# ----- logging -----------------------------------------------------------


def warn(msg: str) -> None:
    print(f"warn: {msg}", file=sys.stderr)


def error(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
