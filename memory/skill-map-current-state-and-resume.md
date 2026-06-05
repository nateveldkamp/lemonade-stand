---
name: skill-map-current-state-and-resume
description: Where the skill-map redesign stands and how to resume — currently rebuilding skills level by level (L0 first); slices emptied.
metadata:
  type: project
---

**Last worked: 2026-06-04.** Read this first when resuming the skill-map / curriculum work.

## The model we landed on (settled)

The curriculum is a radial **skill map** — "Google Maps for skills." Three things kept on **three separate channels** so none overloads the others:

- **Radius = business complexity** (Rule of 3 and 10: ~1 → 3 → 10 → 30 → 100 → 300 people). Field: `complexity_level` (0–7). Outward = bigger/more complex business, NOT a harder skill. Ring labels in the viz show the people-scale.
- **Roads = "builds on"** = authored `prereqs` (directed). Powers routing: mark skills you have ("you are here"), pick a destination, the map charts the path. **Monotonicity rule:** a prereq's `complexity_level` must be ≤ the skill's (roads flow inward→outward). `build-skills-json.py` enforces it and auto-derives `unlocks`.
- **Tiers = skill mastery** (Tier 1→5), vertical *inside* a node, not a radial position. Not yet rendered.

Structure (settled): **16 slices in 4 quadrants** — Craft (how you work), Build (make things), Run (business functions), Lead (scale & steer). Quadrants/slices live in `docs/skills.md`. The stand is the center hub; AI fluency is NOT a slice or hub — it's an emergent capability that composes from other slices (could later be drawn as a highlighted *path* across the map).

## CURRENT STATE — mid-rebuild

We **deleted all ~70 seed skills** and are **rebuilding them level by level** (start at L0, work outward). The 16 slice READMEs currently have `skills: []` (empty) — slice scaffolding/taglines/quadrants are kept. `viz/skills.json` is regenerated to 0 skills / 0 edges. The old per-skill content is recoverable via git history if needed.

**Why level-by-level:** defining skills by asking "what does the business newly need to *do* at this scale?" (per complexity level) produces a more coherent set than defining each slice in isolation. Earlier slice-first authoring produced bad stage values (e.g. logistics typed as 7).

## RESUME HERE: the L0 proposal awaiting Nate's answer

Proposed **Level 0 — "just you" (card table)**: 5 skills, almost all Craft + the one irreducible business act (a sale):

| Slice | Skill | Rationale |
|---|---|---|
| communication | Writing | clear expression; also the basis of good prompting |
| knowledge-management | Organizing your work (files/folders/plain text) | findable digital workspace from day one |
| planning-execution | Personal planning | decide before you act, even solo |
| decision-judgment | Critical thinking | basic reasoning; good vs plausible |
| sales | Selling basics | asking someone to buy — the one act a card table can't skip |

Deferred to L1+: bookkeeping/money, pricing, customer understanding (recurring-stand skills); all Build and Lead skills.

**Two open questions Nate hasn't answered yet:**
1. Is a 5-skill L0 right, too sparse, or too rich? (e.g., does a bare "money basics" belong at L0 or is it L1?)
2. Any L0 skill missing — something a solo person needs before any scale?

Next: get his answers, write L0 skills into the relevant slice READMEs (inline entries with `complexity_level: 0`, no prereqs since L0 = roots), regenerate, then proceed to L1, L2, …

## How a skill is recorded (schema)

Inline entry under a slice README's `skills:` list (see `docs/skills.md` for full schema):
```yaml
  - slug: communication.writing
    name: Writing
    tagline: ...
    build_state: not-started
    tier_count: 5
    complexity_level: 0
    prereqs: [<slug>, ...]   # omit at L0 (roots); must be monotonic (level <= this)
```
Authors write only `prereqs`; the generator derives `unlocks` + the `edges` list.

## Build pipeline & gotchas

- `viz/build-skills-json.py` walks `skills/**/README.md` frontmatter → `viz/skills.json`.
- `viz/build-viz.py` reads `skills.json` → self-contained `viz/index.html` (opens via file://, D3 from CDN).
- Run BOTH after any frontmatter change, commit results together.
- **Python on this Windows machine:** `python`/`python3` are NOT on PATH (Store stubs). Use `& "C:\Users\natev\.local\bin\python3.14.exe" viz/build-skills-json.py` (PowerShell). The console is cp1252 — avoid non-ASCII in `print()`.

## Complexity-level reference (radius rings)

0 just you (card table) · 1 ~3 people (weekend stand/family) · 2 ~10/multiple locations · 3 ~30/first hires · 4 ~100/regional · 5 ~300/manufacturing · 6 ~1,000/national · 7 global. Maps onto `docs/narrative-arc.md` stages.

## Still-stale docs (cleanup backlog)

`docs/narrative-arc.md`, `docs/analogies.md`, `docs/plan.md`, and the prelude README still reference the OLD 9-branch / Git-Spreadsheets-Foundations framing. Not yet swept. `docs/skills.md`, `docs/roadmap.md`, `CLAUDE.md` ARE updated to the new model.

## Related memory
- `skill-graph-computation-rule-of-3-and-10.md` — the radius math + reconciliation decision (separate channels), now implemented.
