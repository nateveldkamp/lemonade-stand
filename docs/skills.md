# The skill map

After the prelude (Welcome to the stand), the curriculum has no required order. The learner moves through a *skill map* — a comprehensive radial map of competencies — picking what to develop next. The map is a "Google Maps for skills": the lemonade stand at the center, skills placed outward by business complexity, connected by roads you navigate. This document is the framework: vocabulary, structure, slug convention, and build-state visibility.

## The three channels

The map deliberately keeps three different ideas on three separate channels, so none of them overloads the others:

- **Radius = business complexity.** Distance from the center is the *business scale* at which a skill first matters, on a Rule-of-3-and-10 log scale (≈1 → 3 → 10 → 30 → 100 → 300 people). Outward means a bigger, more complex business — *not* a harder skill. Captured per skill by `complexity_level`.
- **Roads = "builds on."** Directed prerequisite edges between skills (`prereqs`). These power navigation: pick a destination skill, and the map routes from where you are. Constrained by a **monotonicity rule** — a prerequisite never sits at a higher complexity level than the skill it unlocks, so roads flow inward → outward.
- **Tiers = skill mastery.** A skill's own depth (Tier 1 basics → Tier 5 mastery) is *vertical inside the node*, not a radial position.

## Vocabulary

- **The whole game** — running the lemonade-stand business. One continuous story; see [narrative-arc.md](narrative-arc.md).
- **Quadrant** — one of four families the wheel is divided into: **Craft** (how you work), **Build** (make things), **Run** (the business functions), **Lead** (scale & steer).
- **Slice** — a domain of skill, occupying an angular wedge inside a quadrant. Sixteen of them (see below). *(In the frontmatter and tooling these are still `kind: branch` for historical reasons.)*
- **Skill** — a named competency inside a slice (Writing, Spreadsheets, Bookkeeping, ...). Each Skill has its own tier progression.
- **Tier** — vertical progression within a Skill. Tier 1 = basics; Tier 5 = mastery. Tier counts vary per Skill.
- **Complexity level** — the radius ring a skill enters on (see [Complexity levels](#complexity-levels)).
- **Drill** — a single unit of practice. Discrete, roughly 15–60 minutes. Each drill is anchored to a moment in the lemonade-stand story and earns progress in one or more Skills.
- **Prelude** — the mandatory setup step. Sits at the center of the map. Today this is *Welcome to the stand*.

## The 16 slices

The wheel has four quadrants, each holding several slices. Each slice's `README.md` lists its Skills and their build state.

| Quadrant | Slices |
|---|---|
| **Craft** — how you work | [Communication](../skills/communication/), [Knowledge & context management](../skills/knowledge-management/), [Planning & execution](../skills/planning-execution/), [Decision-making & judgment](../skills/decision-judgment/) |
| **Build** — make things | [Data & analytics](../skills/data-analytics/), [Software & engineering](../skills/software-engineering/), [Automation & IT systems](../skills/automation-it/), [Product & design](../skills/product-design/) |
| **Run** — the business functions | [Finance & accounting](../skills/finance-accounting/), [Operations & supply chain](../skills/operations/), [Marketing](../skills/marketing/), [Sales & business development](../skills/sales/), [Customer success](../skills/customer-success/) |
| **Lead** — scale & steer | [People & leadership](../skills/people-hr/), [Strategy & corporate development](../skills/strategy/), [Legal, risk & governance](../skills/legal-risk/) |

## Complexity levels

The radius is a Rule-of-3-and-10 log scale (see [the Sequoia article](https://articles.sequoiacap.com/the-rule-of-3-and-10)): a business is forced to rethink how it operates at each ~3× step in scale. A skill's `complexity_level` is the ring where it first matters.

| Level | Rough scale | Lemonade stand |
|---|---|---|
| 0 | just you | card table |
| 1 | ~3 people | recurring weekend stand / family helps |
| 2 | ~10 / multiple locations | multiple locations |
| 3 | ~30 / first hires | wholesale, first hires, product lines |
| 4 | ~100 / regional | regional company |
| 5 | ~300 / manufacturing | manufacturing & supply chain |
| 6 | ~1,000 / national | national brand |
| 7 | global | global, public |

## How the map works

Progression happens along two axes at once:

- **Outward (breadth across complexity)** — taking on skills the business needs as it grows from a card table toward a company.
- **Vertical (depth)** — completing higher tiers of a single Skill. *"I'm at Tier 3 of Spreadsheets."*

The map is a graph, not a tower. Roads (`prereqs`) are *suggested* navigation, not hard gates — they tell you what makes a skill easier to reach, and let the map route you from where you are to where you want to go.

## Slug convention

Every drill has a stable slug used by `.progress/state.json`, the URL bar, and the roadmap. Format:

```
<branch>.<skill>.tier-N.<descriptive-name>
```

Examples:

- `foundations.git.tier-1.your-name-on-the-stand`
- `data.data-analysis.tier-1.what-did-we-learn-from-last-weekend`
- `automation.spreadsheet-automation.tier-3.first-report-generator`

Slugs are lowercase kebab-case. They appear as drill directory names: `skills/foundations/git/drills/tier-1.your-name-on-the-stand/`. They never change once authored — if a drill needs to be restructured, the old slug stays as a redirect rather than being deleted.

In conversation, the branch prefix can be dropped when unambiguous (`git.tier-1.your-name-on-the-stand`). The full form is canonical for state tracking.

## Build-state markers

The tree is visible from day one; most of it is empty. To make the "built vs. not built" line obvious, every Skill and Drill carries a build state.

| Marker | Meaning |
|---|---|
| **not started** | Nothing authored. No README, no drill content. The slot exists on the map. |
| **stub** | The Skill's `README.md` is authored (overview + tier map). No drills written yet. |
| **Tier 1** *(or Tier N)* | At least one drill at that tier has been authored. |
| **multi-tier** | Drills authored at two or more tiers. |
| **complete** | Every tier on the Skill's tier map has at least one authored drill. (Used sparingly.) |

These statuses appear in `docs/roadmap.md`, in each branch `README.md`, and at the top of each Skill `README.md`. When a state changes (e.g. a stub becomes Tier 1), it's updated in the same commit that lands the change — per the [index-files sweep rule](conventions.md).

## Frontmatter schema

Every `README.md` under `skills/` declares a YAML frontmatter block at the very top. The frontmatter is the *canonical structured form* of the tree — the human-readable prose below it is for learners; the frontmatter is for tooling. Both the markdown experience (roadmap, branch overviews, individual Skill pages) and the dynamic skill-tree visualization (`viz/`) read from the same frontmatter, so a single edit propagates everywhere.

The schema is intentionally small. It will grow as drills land and as the visualization gets richer; keep new fields optional so existing READMEs don't have to change every time the schema does.

### Common fields (all READMEs)

| Field | Type | Required | Meaning |
|---|---|---|---|
| `kind` | `branch` \| `skill` \| `prelude` | yes | Which kind of node this is. |
| `slug` | string | yes | Stable identifier. Branches use a single segment (`foundations`); Skills use `<branch>.<skill>` (`foundations.git`); the prelude uses `prelude.welcome-to-the-stand`. |
| `name` | string | yes | Human-readable display name (`Git`, `Foundations`, `Welcome to the stand`). |
| `tagline` | string | yes | The one-line italicized phrase under the H1. Used as the hover label in the viz. |
| `build_state` | `not-started` \| `stub` \| `tier-1` \| `tier-2` \| `tier-3` \| `tier-4` \| `tier-5` \| `multi-tier` \| `complete` | yes | Matches the markers in [Build-state markers](#build-state-markers) above. For branches, this is rolled up from the branch's Skills (use the *highest* state any Skill in the branch has reached). |

### Slice (branch) -only fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `quadrant` | `craft` \| `build` \| `run` \| `lead` | yes | Which quadrant of the wheel this slice sits in. Drives layout and color in the viz. |
| `skills` | list of slugs *or* inline objects | yes | The Skills this slice contains — including not-yet-started ones, so the viz can render placeholder nodes for the full planned map. |

`skills:` entries take one of two forms:

- **Just a slug** (`- slug: data-analytics.spreadsheets`) — used when the Skill has its own `README.md` with full frontmatter. The Skill README is authoritative.
- **An inline object** — used for not-started Skills that don't yet have a README. Provides enough metadata for the viz to render a node:
  ```yaml
  - slug: data-analytics.spreadsheets
    name: Spreadsheets
    tagline: Formulas, structure, totals.
    build_state: not-started
    tier_count: 5
    complexity_level: 1
    prereqs: [knowledge-management.files-and-folders]
  ```

When a Skill graduates from not-started to stub, its inline object shrinks back to just `- slug: ...`, and a real `README.md` with full frontmatter is added.

### Skill-only fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `branch` | slice slug | yes | The slice this Skill belongs to (`data-analytics`). |
| `tier_count` | integer | yes | Number of tiers in this Skill's tier map (usually 5). |
| `complexity_level` | integer (0–7) | yes | The radius ring — the business scale where this Skill first matters. See [Complexity levels](#complexity-levels). |
| `prereqs` | list of Skill slugs | no (default `[]`) | The Skills this one *builds on* — the directed "builds on" roads. Must obey the monotonicity rule: every prereq's `complexity_level` ≤ this Skill's. |

The inverse `unlocks` is **derived automatically** by the generator from everyone's `prereqs` — authors only ever write `prereqs`.

### Example — a Skill README's frontmatter

```yaml
---
kind: skill
slug: data-analytics.data-analysis
branch: data-analytics
name: Data analysis
tagline: Making sense of data — finding the signal.
build_state: stub
tier_count: 5
complexity_level: 1
prereqs: [data-analytics.spreadsheets, data-analytics.data-management]
---
```

### Example — a slice (branch) README's frontmatter

```yaml
---
kind: branch
slug: data-analytics
quadrant: build
name: Data & analytics
tagline: Turning what happened into something you can act on.
build_state: not-started
skills:
  - data-analytics.spreadsheets
  - data-analytics.data-management
---
```

### On `prereqs` and derived `unlocks`

Authors declare only `prereqs` (what a Skill builds on). The generator script:

1. Derives the reverse `unlocks` automatically, so the data stays symmetric without double-entry.
2. Emits an `edges` list (prereq → dependent) — the roads the viz draws and routes on.
3. Warns on any prereq that references an unknown Skill, or that violates **monotonicity** (sits at a higher complexity level than the Skill it unlocks).

## How to add a new Skill or Drill

### Adding a new Skill

1. Pick the right slice. If the Skill doesn't fit any existing slice, propose a new slice in `docs/open-questions.md` first.
2. Create `skills/<slice>/<skill>/README.md` using the existing skill READMEs as templates. Start with the frontmatter block — copy the schema above.
3. Add the new Skill's slug to the slice `README.md`'s frontmatter `skills:` list, and to its Skills table.
4. Set its `complexity_level` and `prereqs`. Keep prereqs monotonic (each at a complexity level ≤ this Skill's). The generator derives `unlocks` and the road edges automatically and warns on violations.
5. Update `docs/roadmap.md` to show the new Skill in the map.
6. Status starts at **stub**.
7. Regenerate `viz/skills.json` and commit it in the same change.

### Adding a new Drill

1. Pick the Skill and Tier the drill belongs to.
2. Create `skills/<branch>/<skill>/drills/tier-N.<descriptive-name>/` with at minimum a `README.md` (the drill itself), and `exercise.md` + `checkpoints.md` if the drill is long enough to need them.
3. Update the Skill's tier map in its `README.md`.
4. Bump the Skill's `build_state` in its frontmatter to the appropriate `tier-N` or `multi-tier`.
5. Update `docs/roadmap.md` build-state markers.
6. Slug never changes once committed.
7. Regenerate `viz/skills.json` and commit it in the same change.

## Why a tree, not a list

The original cycle map was linear: Cycle 0 → 1 → 2 → 3 → 4. Linear works when the path is forced. It fails when learners come from different backgrounds, want different outcomes, and need permission to skip what they already know.

A tree is what a modern, multi-discipline knowledge worker's development actually looks like: deep in some skills, foundational in others, junctioning at unexpected combinations. Treating the curriculum the same way models the work itself.

For the philosophical grounding (the "junior version" per Skill; "playing the whole game" at every tier), see [teaching-philosophy.md](teaching-philosophy.md).
