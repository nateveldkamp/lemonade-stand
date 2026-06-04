---
kind: skill
slug: foundations.spreadsheets
branch: foundations
name: Spreadsheets
tagline: The tool the audience already half-knows. Taken to fluent.
build_state: stub
tier_count: 5
tier_1_stand_stage: 1
prereqs: []
unlocks:
  - data.data-analysis
  - data.data-management
  - automation.spreadsheet-automation
---

# Skill: Spreadsheets

*The tool the audience already half-knows. Taken to fluent.*

**Branch:** [Foundations](../). **Build state:** *stub.* **Tier-1 stand stage:** 1 — recurring weekend stand.

## What this Skill is

A spreadsheet is a grid of cells. Each cell holds a value or a formula. Formulas reference other cells. The whole thing recalculates when anything changes. Almost every knowledge worker uses spreadsheets — Excel, Google Sheets, Numbers — and almost every knowledge worker uses them at maybe 20% of their capability.

This Skill is about closing that gap. The same audience that hand-tallies a totals row by typing each number into a calculator can use `SUMIF` and `VLOOKUP` (or `XLOOKUP`) once shown — and once they do, the time it takes to do their job changes by an order of magnitude. The Tier 1 drill is the most concrete possible version of this.

## Why this Skill

Spreadsheets are the *first competent tool* the curriculum can rely on. They're already installed. The audience is already not afraid of them. They support real analysis, real planning, real record-keeping at the scale most knowledge workers actually operate at.

Spreadsheets are also the *bridge* to harder concepts later in the tree. A formula is a function. A sheet is a file. A workbook is a project. The spreadsheet-to-Git analogy ([analogies.md](../../../docs/analogies.md)) is the single highest-leverage teaching device in the curriculum, and it depends on the learner being genuinely fluent in spreadsheets first.

## Tier map

| Tier | What you can do at this tier | Drill | Status |
|---|---|---|---|
| 1 | Open a sheet, log data, add a totals row, format it readably. The mechanical basics, fluently. | Your first sales record | *not yet authored* |
| 2 | Use formulas (`SUMIF`, `VLOOKUP` / `XLOOKUP`, basic conditional logic) to compute things the sheet should compute for you. | TBD | *not yet authored* |
| 3 | Build a small model — multiple sheets that reference each other. Forecasts, scenarios. | TBD | *not yet authored* |
| 4 | Pivot tables. Real summarization. Multi-dimensional comparison. | TBD | *not yet authored* |
| 5 | Robust models with input separation, scenario analysis, sensitivity. The fluent spreadsheet practitioner. | TBD | *not yet authored* |

## Cross-Skill connections

**Builds on:** — (Spreadsheets is foundational; no prerequisites).
**Unlocks:** [Data analysis](../../data/data-analysis/), [Data management](../../data/data-management/), [Spreadsheet automation](../../automation/spreadsheet-automation/).

- **Spreadsheets Tier 1–2** is the prerequisite for **Data analysis Tier 1** and **Data management Tier 1** — most learners will be doing both inside a spreadsheet at first.
- **Spreadsheets Tier 2** + **AI fluency Tier 1** unlocks **Spreadsheet automation Tier 1** — the moment when "the spreadsheet does work for you" becomes "Claude does work *on* the spreadsheet *for* you."
- **Spreadsheets Tier 4+** starts to overlap with **Coding** (Systems branch). When the spreadsheet model gets complex enough, code becomes the better tool. Recognizing that moment is itself a Tier-5 capability.

## How Claude helps

Spreadsheets are also a place where Claude is genuinely good. Claude can read a sheet, suggest formulas, explain what a complicated formula does, propose simplifications, and (with Code) actually edit the file. The Tier 1 drill leans on Claude for the easy parts (suggesting the totals formula) while leaving the manual entry to the learner — to ground the experience in real data.

The risk: Claude doing the *thinking*. The Skill levels up by getting the learner to internalize *what* the formulas express, not just paste in suggestions.
