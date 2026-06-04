# The skill tree

After the prelude (Cycle 0 — Welcome to the stand), the curriculum has no required order. The learner moves through a *skill tree* — a comprehensive map of competencies grouped by domain — picking what to develop next. This document is the framework: vocabulary, structure, slug convention, and build-state visibility.

## Vocabulary

- **The whole game** — running the lemonade-stand business. One continuous story; see [narrative-arc.md](narrative-arc.md).
- **Branch** — a domain of skill. Nine of them: Foundations, Data, Operations, Customer, Systems, Automation, Communication, People, Strategy.
- **Skill** — a named competency inside a branch (Git, Spreadsheets, Planning, ...). Each Skill has its own progression.
- **Tier** — vertical progression within a Skill. Tier 1 = basics; Tier 5 = mastery. Tier counts vary per Skill.
- **Drill** — a single unit of practice. Discrete, roughly 15–60 minutes. Each drill is anchored to a moment in the lemonade-stand story and earns progress in one or more Skills.
- **Practice (verb)** — what the learner does. *"You practice Git by completing its drills."*
- **Prelude** — the mandatory setup step. Sits outside the tree. Today this is *Welcome to the stand*.

## How the tree works

The tree allows progression along two axes at once:

- **Vertical (depth)** — completing higher tiers of a single Skill. *"I'm at Tier 3 of Spreadsheets."* Some tiers within a Skill build on lower tiers.
- **Horizontal (breadth)** — completing Tier 1 of multiple Skills. *"I've started Foundations across the board."* No prerequisites; learners can spread out across the foundational layer.

The tree is a graph, not a tower. Most cross-Skill prerequisites are *suggested*, not gating — the Skill README spells out what other Skills make a given tier easier.

A well-designed skill tree rewards both moves. Specialists go deep on one branch. Generalists go wide. The course design assumes most learners will mix.

## Branches

The tree has nine branches. Each branch's `README.md` lists its Skills and their current build state.

| Branch | What it covers | Tier-1 stand stage |
|---|---|---|
| [Foundations](../skills/foundations/) | The everyday tools a modern knowledge worker reaches for first. | 0–1 |
| [Data](../skills/data/) | Working with information — managing, analyzing, visualizing. | 1 |
| [Operations](../skills/operations/) | Running the stand day-to-day — planning, process, finance, decisions. | 1–2 |
| [Customer](../skills/customer/) | Finding and serving people who want lemonade. | 1–2 |
| [Systems](../skills/systems/) | Making and maintaining the software side. | 2–3 |
| [Automation](../skills/automation/) | Turning recurring work into systems that run themselves. The "factory not artifact" branch. | 1–3 |
| [Communication](../skills/communication/) | Telling the stand's story to people who matter. | 1–2 |
| [People](../skills/people/) | Working with everyone who helps run the stand. | 2 |
| [Strategy](../skills/strategy/) | Deciding where the stand goes next. | 4+ |

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

### Branch-only fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `skills` | list of slugs *or* inline objects | yes | The Skills this branch contains, in the order they should appear — including not-yet-started ones, so the viz can render placeholder nodes for the full planned tree. |

`skills:` entries take one of two forms:

- **Just a slug** (`- slug: foundations.git`) — used when the Skill has its own `README.md` with full frontmatter. The Skill README is authoritative.
- **An inline object** — used for not-started Skills that don't yet have a README. Provides enough metadata for the viz to render a placeholder node:
  ```yaml
  - slug: foundations.markdown-and-plain-text
    name: Markdown and plain text
    tagline: Plain text formats, modern document conventions.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 0
  ```

When a Skill graduates from not-started to stub, its inline object in the branch frontmatter shrinks back to just `- slug: ...`, and a real `README.md` with full frontmatter is added.

### Skill-only fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `branch` | branch slug | yes | The branch this Skill belongs to (`foundations`). |
| `tier_count` | integer | yes | Number of tiers in this Skill's tier map (usually 5). |
| `tier_1_stand_stage` | integer | yes | The narrative-arc stage (0–9) where this Skill's Tier 1 drill lands. See [narrative-arc.md](narrative-arc.md). |
| `prereqs` | list of Skill slugs | no (default `[]`) | Other Skills whose Tier 1 makes *this* Skill significantly easier. Skill-level granularity for now; finer (tier/drill-level) prereqs are tracked in prose for v1. |
| `unlocks` | list of Skill slugs | no (default `[]`) | Other Skills whose higher tiers depend on *this* Skill. The inverse direction of `prereqs`, surfaced so the viz can render edges from either end. |

### Example — a Skill README's frontmatter

```yaml
---
kind: skill
slug: foundations.git
branch: foundations
name: Git
tagline: Versioned text. Branching. Pull requests. The repo as a working artifact.
build_state: stub
tier_count: 5
tier_1_stand_stage: 0
prereqs: []
unlocks:
  - automation.spreadsheet-automation
  - systems.coding
---
```

### Example — a branch README's frontmatter

```yaml
---
kind: branch
slug: foundations
name: Foundations
tagline: The everyday tools a modern knowledge worker reaches for first.
build_state: stub
skills:
  - foundations.git
  - foundations.spreadsheets
---
```

### Why both `prereqs` and `unlocks`

Strictly, only one direction is needed — `unlocks` is just the reverse of `prereqs`. We declare both because:

1. The viz can render edges from either node's perspective without recomputing.
2. Authors think about it both ways: *what does my Skill build on?* and *what does my Skill enable?*
3. The generator script validates symmetry — if `A.prereqs` includes `B` but `B.unlocks` doesn't include `A`, that's a typo worth catching.

## How to add a new Skill or Drill

### Adding a new Skill

1. Pick the right branch. If the Skill doesn't fit any existing branch, propose a new branch in `docs/open-questions.md` first.
2. Create `skills/<branch>/<skill>/README.md` using the existing skill READMEs as templates. Start with the frontmatter block — copy the schema above.
3. Add the new Skill's slug to the branch `README.md`'s frontmatter `skills:` list, and to its Skills table.
4. Add `unlocks:` entries on any prereq Skills that should point at the new Skill (and the reverse `prereqs:` entry on this Skill). The generator script will warn if these don't match.
5. Update `docs/roadmap.md` to show the new Skill in the tree.
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
