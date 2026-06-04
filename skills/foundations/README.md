---
kind: branch
slug: foundations
name: Foundations
tagline: The everyday tools a modern knowledge worker reaches for first.
build_state: stub
skills:
  - slug: foundations.git
  - slug: foundations.spreadsheets
  - slug: foundations.markdown-and-plain-text
    name: Markdown and plain text
    tagline: Plain text formats, modern document conventions.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 0
  - slug: foundations.command-line
    name: Command line
    tagline: Basic terminal use.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 1
  - slug: foundations.ai-fluency
    name: AI fluency
    tagline: Talking to Claude effectively.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 0
---

# Branch: Foundations

*The everyday tools a modern knowledge worker reaches for first.*

This is where most learners will spend their earliest tiers. Most of the audience already half-has these — they live in spreadsheets, they know what a folder is, they've heard of Git. Foundations is about closing the gap from *familiar* to *fluent* so the rest of the tree has somewhere to stand.

These five Skills are the bedrock that everything else builds on. None of them require the others as prerequisites; a learner can start any one of them after the prelude.

## Skills in this branch

| Skill | Status | Tier-1 stand stage | What it covers |
|---|---|---|---|
| [Git](git/) | **stub** | 0 — card table | Versioned text. Commits, branches, PRs. The repo as a working artifact. |
| [Spreadsheets](spreadsheets/) | **stub** | 1 — recurring weekend stand | Formulas, structure, totals. The tool the audience already half-knows, taken to fluent. |
| Markdown and plain text | not started | 0–1 | Plain text formats, modern document conventions. |
| Command line | not started | 1–2 | Basic terminal use. *(Becomes relevant when Claude Code arrives mid-Cycle-1.)* |
| AI fluency | not started | 0 | Talking to Claude effectively. Prompting, file references, the rhythm of working with a collaborator. |

## How this branch relates to the others

Foundations is the *substrate*. Almost every Skill in every other branch becomes easier once Foundations are in place — Git enables versioning everywhere, Spreadsheets enable everything in the Data branch, AI fluency makes the Automation branch tractable.

That doesn't make Foundations *required* before other branches. A learner can start a Tier-1 drill in Operations or Data without finishing Foundations first. But anything beyond Tier 1 tends to depend on at least one Foundations Skill.

See the [skill tree framework](../../docs/skills.md) for how horizontal and vertical progression work, and the [roadmap](../../docs/roadmap.md) for the live status of every Skill in the tree.
