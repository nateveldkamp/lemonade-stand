---
name: skill-graph-computation-rule-of-3-and-10
description: Revisit computing node placement on the skill map; use the Rule of 3 and 10 (log complexity scale) as the radius axis.
metadata:
  type: project
---

**Status:** IMPLEMENTED 2026-06-04 (first pass). `complexity_level` (0–7) is now the radius field on every skill; viz rings are labeled with the 3-and-10 scale; roads = authored `prereqs` with monotonicity enforced by `build-skills-json.py`. Remaining refinements below are future polish, not blockers.

## Revisit: make node placement mathematical, not hand-typed

We currently hand-assign `tier_1_stand_stage` per skill, which produced obvious errors (e.g., logistics typed as stage 7). The agreed direction is to **compute** a skill's radius (and ideally its relationships) from a model instead of typing it. An earlier proposal: radius from a "builds on" prerequisite graph via `level(i) = max(stageFloor(i), 1 + max(level(p) for p in prereqs(i)))`. That's still on the table, but Nate has a stronger idea for the radius axis itself (below).

## The Rule of 3 and 10 as the radius axis

Reference: https://articles.sequoiacap.com/the-rule-of-3-and-10 — a company has to fundamentally rethink how it operates at each ~3x and 10x increase in scale (≈1, 3, 10, 30, 100, 300, 1000 … employees/customers/etc.).

Idea: make the map's **radius a log scale with gridlines at multiples of 3 and 10** (roughly even log spacing, factor ≈ 3.16 per ring). Each ring = an order of business complexity. A skill is placed on the ring corresponding to the complexity level at which the business *first needs it*.

The power of it: many measurable quantities grow together along this same scale, so the rings can be defined by real numbers rather than vibes — e.g.:
- number of employees (1 → 3 → 10 → 30 → 100 …)
- steps in a process
- number of files / documents / records
- SKUs / product lines
- locations
- customers, revenue

Plotting a few of these along the 3-and-10 scale and relating them back to a simple business (the lemonade stand) ties the narrative arc, the radius, and "complexity added as the business grows" into one quantitative spine. The existing narrative stages (card table → weekend stand → family helps → multiple locations → first hire → … → global) should map onto these 3/10 thresholds.

## Reconciliation decision: business-complexity vs. skill-advancement (separate channels)

Radius was being asked to encode two different ontologies — a *company* property (scale/maturity) and a *skill* property (advancement/prereq-depth). Decision (2026-06-04): keep them on **separate channels**, not one combined radius:

- **Radius = business complexity** (the 3-and-10 axis). The map's geography: what scale of business first needs this capability. Outward = bigger business, NOT harder skill.
- **Builds-on = roads/edges.** "What you learn before what" lives in the road network (the Google Maps model), independent of radius.
- **Skill mastery = tiers inside a node.** A skill's own depth is vertical *within* the node, not a radial position.
- **Monotonicity constraint that links them:** a skill's prerequisites must sit on a ring no further out than the skill itself (prereqs at complexity ≤ ring). This makes the road network flow inward→outward naturally, preserving "builds outward as the business grows" while radius stays honestly = business complexity.

## To work through when we revisit
- Pick the canonical quantity (or composite) that defines the rings; map the narrative stages onto 1/3/10/30/100… thresholds.
- Decide how a skill's entry ring is determined (which complexity threshold first demands it).
- Reconcile with the "builds on" graph: radius from complexity scale, edges/relationships still needed for routing (the Google Maps model).
- Update `tier_1_stand_stage` (or replace it with a complexity-level field) and the viz ring labels accordingly.
