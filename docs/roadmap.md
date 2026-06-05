# Roadmap

The single view of the curriculum: the prelude at the center, then the 16 slices of the skill map arranged in four quadrants. This file is the *progress board* — `progress.py` will reprint it with each learner's completed drills marked in (when that CLI lands).

It is also the **build-state board**. Every slice and skill shows its current state — what's been authored, what's still a slot on the map. Contributors land changes by moving a skill from one state to another.

## Build-state legend

| Marker | Meaning |
|---|---|
| **not started** | Slot exists on the map; nothing authored beyond a seed entry (name, tagline, complexity level, prereqs). No drills. |
| **stub** | The skill's own `README.md` is authored (overview + tier map). No drills yet. |
| **Tier N** | At least one drill at Tier N has been authored. |
| **multi-tier** | Drills authored at two or more tiers. |
| **complete** | All tiers on the skill's map have at least one authored drill. (Used sparingly.) |

For the framework these markers fit into — quadrants, slices, skills, tiers, complexity levels, the three channels (radius / roads / tiers) — see [skills.md](skills.md).

## The prelude

One mandatory step before the map opens up. Sits at the center.

| Step | Story beat | What you ship | Interface | Build state |
|---|---|---|---|---|
| **Welcome to the stand** | You've inherited a tiny lemonade stand. Today you get oriented. | Nothing — orientation. | Cowork | **authored** ([source](../skills/prelude.welcome-to-the-stand/)) |

After the prelude, the learner picks any skill to start. There is no required order; the map routes them from what they have to what they want.

## The map

Four quadrants, 16 slices. The skill set is **being rebuilt level by level** (L0 outward) — see the resume note in `memory/skill-map-current-state-and-resume.md`. The 16 slice READMEs are currently **empty of skills** (`skills: []`); their scaffolding (quadrant, tagline) is in place.

The slices, by quadrant:

- **Craft — how you work:** [Communication](../skills/communication/) · [Knowledge & context management](../skills/knowledge-management/) · [Planning & execution](../skills/planning-execution/) · [Decision-making & judgment](../skills/decision-judgment/)
- **Build — make things:** [Data & analytics](../skills/data-analytics/) · [Software & engineering](../skills/software-engineering/) · [Automation & IT systems](../skills/automation-it/) · [Product & design](../skills/product-design/)
- **Run — the business functions:** [Finance & accounting](../skills/finance-accounting/) · [Operations & supply chain](../skills/operations/) · [Marketing](../skills/marketing/) · [Sales & business development](../skills/sales/) · [Customer success](../skills/customer-success/)
- **Lead — scale & steer:** [People & leadership](../skills/people-hr/) · [Strategy & corporate development](../skills/strategy/) · [Legal, risk & governance](../skills/legal-risk/)

### Level-by-level build — in progress

We add skills one **complexity level** at a time, asking "what does the business newly need to *do* at this scale?" A skill's `complexity_level` is the radius ring it enters on.

| Level | Scale | Status |
|---|---|---|
| L0 | just you (card table) | **proposing** — 5 candidate skills (Writing, Organizing your work, Personal planning, Critical thinking, Selling basics); awaiting sign-off |
| L1 | ~3 people (weekend stand) | not started |
| L2 | ~10 / multiple locations | not started |
| L3 | ~30 / first hires | not started |
| L4+ | ~100 → global | not started |

## Build state at a glance

As of this commit:

- **1 prelude authored.**
- **16 slices roughed in** (READMEs with frontmatter, quadrant); **0 skills** currently defined (mid level-by-level rebuild).
- **0 drills authored** beyond the prelude.

Once the skill set is rebuilt level by level, authoring proceeds drill-by-drill: each new drill moves a skill from *not started* → *stub* → *Tier N*. Contributors update the skill's `README.md` tier map *and* this roadmap in the same commit (the [index-files sweep rule](conventions.md)).

## Milestones inside drills

Some named moments are big enough to track even though they sit *inside* a drill.

- **🛠 Move to the workshop** — inside Knowledge & context management → Version control (Tier 1), the moment Claude Code is installed and the learner switches from Cowork to Code. See [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md).

More named milestones land here as the drills that contain them get authored.

## How progress is tracked

A learner's progress lives in `.progress/state.json` (gitignored — local only). Each completed drill is keyed by its [slug](skills.md) (e.g. `knowledge-management.version-control.tier-1.your-name-on-the-stand`). Slugs never change once committed.

Running `python3 progress.py` (when it lands) reads `.progress/state.json` and reprints this roadmap with each row's status annotated for the learner — and, on the map, marks the skills they already have so routing can chart from "you are here."

## How this doc relates to the others

- [skills.md](skills.md) is the **framework** — vocabulary, the three channels, complexity levels, slug rules, schema.
- [narrative-arc.md](narrative-arc.md) is the **story bible** — the stand stages the complexity levels map onto.
- [plan.md](plan.md) is the **architectural plan** — repo structure, build order.
- This file (`roadmap.md`) is the **map view + progress + build-state board**.
