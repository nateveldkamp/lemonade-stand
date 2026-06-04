---
kind: skill
slug: automation.spreadsheet-automation
branch: automation
name: Spreadsheet automation
tagline: Using AI to take a recurring spreadsheet task and make it run itself.
build_state: stub
tier_count: 5
tier_1_stand_stage: 1
prereqs:
  - foundations.spreadsheets
  - foundations.git
unlocks: []
---

# Skill: Spreadsheet automation

*Using AI to take a recurring spreadsheet task and make it run itself.*

**Branch:** [Automation](../). **Build state:** *stub.* **Tier-1 stand stage:** 1 — recurring weekend stand.

## What this Skill is

This is the Skill where the **factory not artifact** idea ([vision.md](../../../docs/vision.md)) first lands in a form spreadsheet-fluent learners can immediately use. The audience already has spreadsheets they update every week — sales summaries, expense trackers, weekly status sheets, monthly P&L roll-ups. Each one is a recurring task. Each one is a candidate to be automated.

This Skill starts at the most immediate version: paste a spreadsheet into Cowork, ask Claude to do the summary you normally do by hand, get back the summary. The learner *experiences* the factory moment within ten minutes of the Tier 1 drill — *Claude just did the thing I do every Monday.*

From there, the Skill scales. Tier 2 is asking Claude to *replicate* a process you describe. Tier 3 is committing a script that runs the process the same way every time without Claude in the loop. Tier 4+ is full agentic workflows where Claude pulls the inputs, runs the analysis, and posts the output to the right place on a schedule.

## Why this Skill

For most of the audience, this is the single Skill with the highest immediate ROI in their actual job. Spreadsheet processes consume disproportionate amounts of knowledge-worker time. Automating even one of them frees real hours every week.

It's also the *gateway* Skill into the Automation branch. Once a learner has automated one spreadsheet, they recognize the pattern everywhere — every recurring task they do becomes a candidate. The mindset shift is what carries them into higher tiers.

## Tier map

| Tier | What you can do at this tier | Drill | Status |
|---|---|---|---|
| 1 | Paste a spreadsheet into Cowork. Ask Claude to summarize and chart it. Notice the human work just got smaller. | Ask Claude about your sales | *not yet authored* |
| 2 | Describe a process to Claude in prose. Have Claude execute it on the spreadsheet. Compare to what you'd do by hand. | TBD | *not yet authored* |
| 3 | Move the process out of one-off chat. Use Claude Code to write a script that runs the same way every time. Commit it. The first **report generator**. | TBD | *not yet authored* |
| 4 | Schedule it. Make the script run on a recurring trigger without you in the loop. Real automation. | TBD | *not yet authored* |
| 5 | Multi-step agentic workflow: Claude pulls inputs, runs analysis, drafts the report, posts it where it belongs, with eval gates so you can trust the output. | TBD | *not yet authored* |

## Cross-Skill connections

**Builds on:** [Spreadsheets](../../foundations/spreadsheets/) (you have to have a sheet to automate), [Git](../../foundations/git/) (from Tier 3 onward, to commit the script).
**Unlocks:** Once authored, Document and Workflow automation Skills extend the same pattern to non-spreadsheet artifacts.

- **Spreadsheet automation Tier 1** requires only **Spreadsheets Tier 1** (you have to have a sheet to automate) and **AI fluency Tier 1** (Cycle 0 setup).
- **Tier 2** benefits from **Data analysis Tier 1** — you need to know what *good* output looks like before you can recognize when Claude is producing it.
- **Tier 3** requires **Git Tier 1+** (committing the script) and **Coding Tier 1+** (Systems branch — reading what Claude wrote).
- **Tier 4–5** requires real chunks of the **Systems** branch (Coding, APIs, Observability) and **Eval design** (also Automation branch).

This Skill is the cleanest example of how the tree's *junctions* work. The lower tiers are standalone; the higher tiers are where breadth across the tree pays off.

## How Claude helps

This Skill is *literally about* using Claude. Every tier has Claude in the loop in some form. The Skill grows by changing *how* Claude is used: from chat-flavored back-and-forth at Tier 1, to commit-and-run scripts at Tier 3, to scheduled agentic workflows at Tier 5.

The risk: stopping at Tier 1. Tier 1 feels magical and many learners stop there. The drills at higher tiers exist to push past the magic into the discipline.
