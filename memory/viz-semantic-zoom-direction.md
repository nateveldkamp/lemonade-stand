---
name: viz-semantic-zoom-direction
description: The skill-tree viz should use semantic zoom (level-of-detail), not just geometric zoom — branches→skills→tiers→drills.
metadata:
  type: project
---

The `viz/` skill-tree visualization should evolve from single-level geometric zoom (scaling pixels) to **semantic zoom / level-of-detail**, where the zoom level changes *what* is shown and re-lays-out at each level. Nate's framing (2026-06-04): a blend of Borderlands 2 legibility (collapsed) and Path of Exile comprehensiveness (expanded) — the same artifact at different resolution.

The collapse/expand levels map onto existing vocabulary (see `docs/skills.md`):
- Level 0 (most collapsed): the stand / 9 branches as big nodes — "here's the whole business"
- Level 1: branches expand into ~46 Skills
- Level 2: Skills expand into Tiers (~5 each)
- Level 3 (most expanded): Tiers expand into Drills — the full PoE-scale web

**Why:** Consistent with the curriculum's "play the whole game" principle — abstract complexity away to start, add it as you progress.

**How to apply:** Keep two axes straight — zoom = *breadth/resolution* (how much of the map is drawn); tier progression = *depth* (difficulty inside one node). They meet at Level 2, where Tiers (depth) become visible as you zoom in. Current `viz/build-viz.py` is single-level and will need re-architecting (nested, zoom-driven layout) to support this. Decide level transitions (click-to-expand vs. zoom-threshold auto-expand) and layout strategy (pre-baked vs. live simulation) before coding.
