---
kind: skill
slug: data.data-analysis
branch: data
name: Data analysis
tagline: Making sense of data.
build_state: stub
tier_count: 5
tier_1_stand_stage: 1
prereqs:
  - foundations.spreadsheets
  - data.data-management
unlocks: []
---

# Skill: Data analysis

*Making sense of data.*

**Branch:** [Data](../). **Build state:** *stub.* **Tier-1 stand stage:** 1 — recurring weekend stand.

## What this Skill is

Data analysis is the discipline of turning a set of numbers into *a thing somebody can do something with*. Summarize. Compare. Find the pattern. State what you learned in a sentence a non-analyst can act on.

The audience often confuses data analysis with the *tools* of analysis (pivot tables, BI platforms, ML models). The Skill is the underlying habit: pose a question, find the evidence, draw a conclusion, communicate it. The tool is incidental.

## Why this Skill

Most data work that gets done in organizations is *describing* data rather than *analyzing* it. A weekly report that shows last week's numbers is description. A weekly report that explains *what changed and why* is analysis. The two look almost identical from the outside and produce wildly different decisions.

This Skill is the bridge from "we have data" to "the data informed something." Without it, the Data branch's other Skills are infrastructure with no payoff.

## Tier map

| Tier | What you can do at this tier | Drill | Status |
|---|---|---|---|
| 1 | Look at one weekend of sales data. Write a three-sentence observation: what sold best, what total revenue was, what (if anything) the weather did to either. | What did we learn from last weekend? | *not yet authored* |
| 2 | Compare two periods. Find the meaningful differences. Distinguish *signal* from *noise*. | TBD | *not yet authored* |
| 3 | Forecast. Use historical data to predict next period. Articulate the assumptions, not just the number. | TBD | *not yet authored* |
| 4 | Segment. Break a population into meaningful sub-groups. Multi-dimensional analysis. | TBD | *not yet authored* |
| 5 | Drive a real decision with analysis. Frame the question so the data can answer it. Defend the conclusion when challenged. | TBD | *not yet authored* |

## Cross-Skill connections

**Builds on:** [Spreadsheets](../../foundations/spreadsheets/), [Data management](../data-management/) (at Tier 2+).
**Unlocks:** Higher tiers junction with **Planning**, **Communication**, and **Strategy** — analysis only pays off when it changes a decision.

- **Data analysis Tier 1** needs only **Spreadsheets Tier 1** as a working prerequisite — you need to be able to read the sheet.
- **Data analysis Tier 2+** benefits significantly from **Data management Tier 2+** — analysis is much easier when the data is organized.
- **Data analysis Tier 3+** (forecasting) junctions with **Planning Tier 3** (planning with evidence) — the analyst and the planner are the same person, doing the same work.
- **Data analysis Tier 5** junctions with **Communication** (writing, presentation) — analysis that doesn't change behavior was insufficient.

## How Claude helps

Claude can do the *grunt work* of analysis very quickly — summarize a sheet, propose pivots, run comparisons, sketch charts — leaving the learner to focus on the *question* and the *interpretation*. The Tier 1 drill leans into this: paste the spreadsheet into Cowork, ask Claude for the basic summary, then have the learner write the three-sentence observation themselves.

The risk: outsourcing the interpretation. The Skill levels up by the learner doing the meaning-making, not by Claude generating impressive-sounding conclusions.
