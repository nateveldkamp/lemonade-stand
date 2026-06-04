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
  - data.data-management
---

# Skill: Git

*Versioned text. Branching. Pull requests. The repo as a working artifact.*

**Branch:** [Foundations](../). **Build state:** *stub.* **Tier-1 stand stage:** 0 — card table.

## What this Skill is

Git is the discipline of treating any artifact — a document, a spreadsheet, a script, a curriculum — as something with *history*. Every change is tracked. Every change has an author, a timestamp, and a reason. Every change is reversible. Every change is reviewable.

If you've ever saved a file as `report_v2_FINAL_final.xlsx` and then `report_v2_FINAL_USE_THIS_ONE.xlsx`, you've been doing a primitive version of Git by hand. The Git Skill is about replacing that habit with something that actually scales. (For the full mapping of spreadsheet conventions to Git operations, see [analogies.md](../../../docs/analogies.md).)

## Why this Skill

Without Git, knowledge work that crosses more than one person collapses into version chaos. With Git, an arbitrary number of people can work on the same artifact, see each other's changes, propose edits without committing them, review each other's work, and roll back when something breaks.

Git is also the *substrate for the Automation branch.* Any automation you build that's worth keeping ends up in a repo. Skipping this Skill blocks every higher tier of Spreadsheet automation, Workflow automation, and Skill engineering.

## Tier map

| Tier | What you can do at this tier | Drill | Status |
|---|---|---|---|
| 1 | Make your first commit. Open your first PR. Understand commits, branches, and PRs as concepts. | Your name on the stand | *not yet authored* |
| 2 | Branch for a change. Push the branch. Open a PR with a useful description. Merge it. | TBD | *not yet authored* |
| 3 | Review someone else's PR. Leave a useful comment. Understand the *reviewer's* job, not just the author's. | TBD | *not yet authored* |
| 4 | Resolve a merge conflict. Understand what a merge actually does. | TBD | *not yet authored* |
| 5 | Multi-author workflows. Rebase vs. merge. Cherry-pick. The advanced moves. | TBD | *not yet authored* |

## Cross-Skill connections

**Builds on:** — (Git is foundational; no prerequisites).
**Unlocks:** [Spreadsheet automation](../../automation/spreadsheet-automation/), [Data management](../../data/data-management/), and most non-trivial work in the Systems branch.

- **Git Tier 1** is implicitly required by anything that ships a PR. Most other Skills' higher tiers assume Git Tier 1 is done.
- **Git Tier 2** (branching) is the prerequisite for **Spreadsheet automation Tier 3+** (so the generated artifacts can be committed) and for any meaningful collaboration with another person.
- **Git Tier 3** (reviewing) pairs with **Feedback** (People branch) — code review is one of the highest-quality feedback channels most knowledge workers have.

## How Claude helps

Git is one of the places Claude shows up most usefully. Claude Code in particular runs Git commands for you, writes commit messages from your changes, and walks you through resolving conflicts. The Tier-1 drill is designed so the learner uses Claude Code to do their first commit — *use the tool* before learning the underlying commands.

The risk: Claude doing too much. The Skill levels up by understanding what's happening, not by getting commits done. The drills are written to make the learner pause and look.
