# Curated resources

The reading list. Every entry should answer three questions: **what it is**, **why we link it (instead of writing our own)**, and **when in the curriculum a learner should reach for it**.

This is a living document. Add entries as the curriculum grows. Remove entries that go stale.

## Format

Each entry uses this template:

```
### <Resource title>
**Link:** <URL>
**What it is:** <one-line description>
**Why we link this:** <why this beats writing our own version>
**Read this when:** <which cycle / which moment in the curriculum>
```

Keep entries short. The point is curation, not summary.

## Claude Code and the Anthropic platform

### Anthropic developer docs (root)
**Link:** https://docs.claude.com
**What it is:** Anthropic's official documentation hub for Claude, the API, the SDK, and Claude Code.
**Why we link this:** maintained by Anthropic, always current; rewriting it ourselves would guarantee staleness.
**Read this when:** any time the learner wants the authoritative reference rather than our narrative.

### Anthropic public skills repository
**Link:** *to confirm — github.com/anthropics/skills (verify before linking publicly)*
**What it is:** an open-source collection of skills (reusable structured prompts/workflows) published by Anthropic, including the vertical-product examples referenced in `docs/vision.md`.
**Why we link this:** real-world artifact of "knowledge work as code." Studying it is itself a teaching moment.
**Read this when:** Cycle 3 (the factory mindset) or later, once the learner has the vocabulary to read a skill.

## Git and GitHub

### Git (official site)
**Link:** https://git-scm.com
**What it is:** download + reference docs for Git.
**Why we link this:** authoritative source for install and the full reference.
**Read this when:** Cycle 1, install step.

### GitHub
**Link:** https://github.com
**What it is:** the GitHub platform itself; sign up here.
**Read this when:** Cycle 1, the "get access" step.

### GitHub Docs
**Link:** https://docs.github.com
**What it is:** GitHub's full documentation — accounts, repos, PRs, Actions.
**Why we link this:** authoritative; our PR instructions will reference specific pages here rather than reproducing them.
**Read this when:** Cycle 1 (basic PR flow) and Cycle 2+ (branching, review).

### GitHub CLI
**Link:** https://cli.github.com
**What it is:** the `gh` command-line tool — opens PRs, manages issues, authenticates against GitHub.
**Why we link this:** the install + auth flow lives upstream and changes occasionally; we link rather than mirror.
**Read this when:** Cycle 1, opening the first PR.

## Tooling (editor, runtimes)

### Visual Studio Code
**Link:** https://code.visualstudio.com
**What it is:** the editor we standardize on.
**Read this when:** Cycle 1, first install step.

### Python (official)
**Link:** https://www.python.org
**What it is:** official Python downloads.
**Read this when:** Cycle 1, install Python step.

### Markdown Guide
**Link:** https://www.markdownguide.org
**What it is:** plain-English reference for markdown syntax.
**Why we link this:** learners will be writing markdown from Cycle 1 onward; this is the gentlest reference available.
**Read this when:** any time the learner needs a syntax refresher.

## Pedagogy and motivation

These are deeper references for understanding *why* the curriculum is designed the way it is. Optional reading for learners; recommended for contributors.

### Making Learning Whole — David Perkins
**What it is:** the book that frames "playing the whole game" and names the failure modes (elementitis, abouttitis).
**Why we link this:** the foundational source for `docs/teaching-philosophy.md`. Worth reading in full if you'll be authoring cycles.
**Read this when:** before contributing a new cycle.

### The Art of Learning — Josh Waitzkin
**What it is:** Waitzkin's account of how he learns, including the king-and-pawn endgame example referenced in `docs/teaching-philosophy.md`.
**Why we link this:** the second pillar of the philosophy. Short, readable.
**Read this when:** before contributing a new cycle.

### Naval Ravikant on the SWE shift (podcast)
**Link:** *to be added — maintainer to drop the exact episode link*
**What it is:** the source of the "build the factory, not the artifact" framing used in `docs/vision.md`.
**Why we link this:** captures the strategic argument better than any paraphrase.
**Read this when:** before Cycle 3, the "factory mindset" cycle.

## How to add to this list

Open a PR. The bar for inclusion is high: a new entry should pass the "would I genuinely recommend this to a colleague at this point in the curriculum?" test. If it wouldn't, leave it out — the curation discipline is itself part of what we're teaching.
