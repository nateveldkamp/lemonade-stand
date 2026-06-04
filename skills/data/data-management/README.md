---
kind: skill
slug: data.data-management
branch: data
name: Data management
tagline: Organizing data so it stays useful.
build_state: stub
tier_count: 5
tier_1_stand_stage: 1
prereqs:
  - foundations.spreadsheets
  - foundations.git
unlocks:
  - data.data-analysis
---

# Skill: Data management

*Organizing data so it stays useful.*

**Branch:** [Data](../). **Build state:** *stub.* **Tier-1 stand stage:** 1 — recurring weekend stand.

## What this Skill is

Data management is the discipline of *how* data is stored, named, organized, and shared — separately from what's *in* it. The same five numbers stored in a single well-named file in a known folder are useful for years. Scattered across a napkin photo, a Notes app entry, three emails, and a half-remembered conversation, they're useful for an afternoon.

This Skill is what determines whether the records you keep stay valuable as the business grows, or quietly rot into a mess no one wants to touch.

## Why this Skill

Most knowledge workers have never been taught data management explicitly. They picked up habits by osmosis from whatever team they joined, and those habits are usually bad — bespoke folder structures, ambiguous filenames, "where did we put the Q3 numbers" tribal knowledge.

The Skill becomes acute the moment a second person needs to find data without asking the first person. That moment lands at Stand stage 2 (family helps), which is why the **Excel-to-Git migration moment** ([narrative-arc.md Stage 2](../../../docs/narrative-arc.md)) anchors here. Data management Tier 2+ is where shared records stop being one person's spreadsheet.

## Tier map

| Tier | What you can do at this tier | Drill | Status |
|---|---|---|---|
| 1 | One source of truth. Take scattered scraps and consolidate them into a single well-named file in a sensible folder. | One source of truth | *not yet authored* |
| 2 | Establish a record-keeping convention that another person can follow. Naming, structure, where things live. | TBD | *not yet authored* |
| 3 | Move shared records out of a single-user spreadsheet into a versioned, shared format. The Excel-to-Git migration moment. | TBD | *not yet authored* |
| 4 | Schema design at small scale. What columns, what types, what gets indexed, what gets normalized. | TBD | *not yet authored* |
| 5 | Data governance at organizational scale. Catalogs, lineage, ownership, retention. | TBD | *not yet authored* |

## Cross-Skill connections

**Builds on:** [Spreadsheets](../../foundations/spreadsheets/), [Git](../../foundations/git/) (at Tier 3 — the Excel-to-Git migration moment).
**Unlocks:** [Data analysis](../data-analysis/) (analysis is much easier when the data is organized).

- **Data management Tier 1** is approachable with no prerequisites beyond knowing the audience already lives in spreadsheets and folders.
- **Data management Tier 3** is the **Out of the spreadsheet** milestone on the roadmap — the Excel-to-Git migration. Junctions hard with **Git** (Foundations) and motivates much of the **Systems** branch's later relevance.
- **Data management Tier 4+** junctions with **Databases** (also Data branch) — when a sensible schema is what's missing, databases become the answer.

## How Claude helps

Claude is very good at finding the structure hiding in unorganized data — given a folder of half-named files, it can propose a naming scheme, identify duplicates, flag ambiguity. The Tier 1 drill uses Claude as a reorganization collaborator: the learner explains what's in their scattered notes, Claude proposes a single consolidated structure, the learner picks the one that fits their habits.

The risk: Claude inventing structure that doesn't match how the learner actually thinks. Naming conventions need to feel native, or they don't stick.
