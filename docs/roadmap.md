# Roadmap

The single paired view of the curriculum. The prelude at the top; nine branches of the skill tree below. This file is the *progress board* — `progress.py` will reprint it with each learner's completed drills marked in (when that CLI lands).

This file is also the **build-state board**. Every Skill and every tier shows its current state — what's been authored, what's still a slot on the map. The repo's contributors land changes by moving a Skill or tier from one state to another.

## Build-state legend

| Marker | Meaning |
|---|---|
| **not started** | Slot exists on the map; nothing authored. No README, no drill content. |
| **stub** | The Skill's `README.md` is authored (overview + tier map). No drills written yet. |
| **Tier N** | At least one drill at Tier N has been authored. |
| **multi-tier** | Drills authored at two or more tiers. |
| **complete** | All tiers on the Skill's map have at least one authored drill. (Used sparingly.) |

For the framework these markers fit into — Skills, Tiers, Drills, Branches — see [skills.md](skills.md).

## The prelude

One mandatory step before the tree opens up. Sits outside the branches.

| Step | Stand stage | Story beat | What you ship | Interface | Time | Build state |
|---|---|---|---|---|---|---|
| **Welcome to the stand** | 0 — card table | You've inherited a tiny lemonade stand. Today you get oriented. | Nothing — Cycle 0 is orientation. | Cowork | ~15–30 min | **authored** ([source](../skills/prelude.welcome-to-the-stand/)) |

After the prelude, the learner picks a Skill to start from the tree below. There is no required next step.

## The skill tree

Nine branches; ~40 Skills. Most cells are empty on day one — the structure is the artifact. Authoring happens deliberately, one drill at a time, with the build state above being the source of truth.

### Branch 1 — Foundations

The everyday tools a modern knowledge worker reaches for first.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| [Git](../skills/foundations/git/) | **stub** | 0 — card table |
| [Spreadsheets](../skills/foundations/spreadsheets/) | **stub** | 1 — recurring weekend stand |
| Markdown and plain text | not started | 0–1 |
| Command line | not started | 1–2 |
| AI fluency | not started | 0 |

### Branch 2 — Data

Working with information.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| [Data management](../skills/data/data-management/) | **stub** | 1 |
| [Data analysis](../skills/data/data-analysis/) | **stub** | 1 |
| Data visualization | not started | 1–2 |
| Databases | not started | 2–3 |
| Data engineering | not started | 4+ |

### Branch 3 — Operations

Running the stand day-to-day.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| [Planning](../skills/operations/planning/) | **stub** | 1 |
| Process design | not started | 2 |
| Finance and accounting | not started | 1–2 |
| Decision making | not started | 1+ |
| Risk and compliance | not started | 4+ |

### Branch 4 — Customer

Finding and serving people who want lemonade.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| Customer understanding | not started | 1 |
| Pricing | not started | 1–2 |
| Marketing | not started | 1–2 |
| Sales | not started | 4 |
| Customer success | not started | 5+ |

### Branch 5 — Systems

Making and maintaining the software side.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| Coding | not started | 2 |
| APIs and integrations | not started | 3 |
| System design | not started | 3–4 |
| Testing and quality | not started | 3+ |
| Observability | not started | 4+ |

### Branch 6 — Automation

Turning recurring work into systems that run themselves.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| [Spreadsheet automation](../skills/automation/spreadsheet-automation/) | **stub** | 1 |
| Document automation | not started | 2 |
| Workflow automation | not started | 3 |
| Agentic workflows | not started | 3–4 |
| Skill engineering | not started | 4+ |
| Eval design | not started | 4+ |

### Branch 7 — Communication

Telling the stand's story to people who matter.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| Writing | not started | 1 |
| Storytelling | not started | 2 |
| Presentation | not started | 2–3 |
| Stakeholder updates | not started | 3 |
| Documentation | not started | 2+ |

### Branch 8 — People

Working with everyone who helps run the stand.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| Collaboration | not started | 2 |
| Feedback | not started | 2 |
| Coaching and management | not started | 4 |
| Hiring | not started | 4 |
| Org design | not started | 6+ |

### Branch 9 — Strategy

Deciding where the stand goes next.

| Skill | Build state | Tier-1 stand stage |
|---|---|---|
| Strategy | not started | 4 |
| Vision | not started | 5+ |
| Competitive analysis | not started | 5+ |
| Capital allocation | not started | 6+ |
| Board and governance | not started | 7+ |

## Build state at a glance

As of this commit:

- **1 prelude authored.**
- **6 Skill stubs authored** (Git, Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation).
- **~34 Skills still at "not started."**
- **0 drills authored** beyond the prelude.

The next phase of authoring is drill-by-drill. Each new drill moves one Skill from *stub* to *Tier N*; each new tier moves it forward through the build states. Contributors land changes by updating both the Skill's own `README.md` tier map *and* this roadmap in the same commit (the [index-files sweep rule](conventions.md)).

## Milestones inside drills

Some named moments are big enough to track even though they sit *inside* a drill rather than being their own.

- **🛠 Move to the workshop** — inside Git Tier 1, the moment Claude Code is installed and the learner switches from Cowork to Code. The Cowork → Code graduation. See [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md).
- **📒 Out of the spreadsheet** — Data management Tier 3, the moment shared records migrate from `.xlsx` files into the repo as `.csv`. The Excel-to-Git migration moment.

More named milestones land here as the drills that contain them get authored.

## How progress is tracked

A learner's progress lives in `.progress/state.json` (gitignored — local only). Each completed drill is keyed by its [slug](skills.md) (e.g. `foundations.git.tier-1.your-name-on-the-stand`). Slugs never change once committed; if a drill is restructured, the old slug stays as a redirect. This is how local progress survives course updates.

Running `python3 progress.py` (when it lands) reads `.progress/state.json` and reprints this roadmap with each row's status annotated for the learner — *built* vs. *not started* from the contributor's view becomes *done* vs. *not yet attempted* from the learner's. Two views of the same artifact.

## How this doc relates to the others

- [skills.md](skills.md) is the **framework** — vocabulary, slug rules, how the tree works.
- [narrative-arc.md](narrative-arc.md) is the **story bible** — what each stand stage is and what complexity it introduces. Skills' Tier-1 entries above point to stand stages defined there.
- [plan.md](plan.md) is the **architectural plan** — repo structure, build order, broader design decisions.
- This file (`roadmap.md`) is the **paired view + progress + build-state board**.
