# Lemonade Stand

An async, hands-on training repo for upskilling knowledge workers on the full modern skill stack — **business fundamentals, planning, analytics, automation, and AI/system-design** — taught through one continuous story of a lemonade stand that grows from a card table to a global public company. AI fluency (Claude Code, Git, GitHub, agentic workflows) anchors the early cycles because it is the current acute need, not because it is the whole subject.

The course is delivered through Claude itself: learners start in **Cowork** (the easiest on-ramp — no install) and graduate to **Claude Code** when their first Skill drill calls for it. The chat-vs-cowork-vs-code distinction is experienced, not just explained.

After the one mandatory prelude (*Welcome to the stand*), the curriculum is a **skill tree** — nine branches (Foundations, Data, Operations, Customer, Systems, Automation, Communication, People, Strategy), each containing several Skills with their own tiered drills. There is no required order. The learner picks where to go next.

**Status:** early build phase. The prelude is authored; the skill-tree framework, the roadmap, and six Skills (Git, Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation) have stub overviews. No drills authored beyond the prelude. The skill tree is now structured: every Skill and branch README carries YAML frontmatter, and a dynamic visualization lives in [viz/](viz/) (Phase A landed; the interactive HTML is next). The repo is not ready for learner use yet — see [docs/roadmap.md](docs/roadmap.md) for the live build state of every Skill.

## If you just landed here, read in this order

1. **[docs/teaching-philosophy.md](docs/teaching-philosophy.md)** — the pedagogical foundation. Everything else flows from here.
2. **[docs/vision.md](docs/vision.md)** — why this repo exists and the problem it solves.
3. **[docs/narrative-arc.md](docs/narrative-arc.md)** — the lemonade stand's growth story, from card table to global company. The story bible Skills reference.
4. **[docs/skills.md](docs/skills.md)** — the skill-tree framework: Branches, Skills, Tiers, Drills, slugs, build states.
5. **[docs/roadmap.md](docs/roadmap.md)** — the paired view: the prelude + the full nine-branch tree with current build state of every Skill. The progress board.
6. **[docs/analogies.md](docs/analogies.md)** — canonical analogies (spreadsheets ↔ Git, etc.) the curriculum leans on.
7. **[docs/chat-vs-cowork-vs-code.md](docs/chat-vs-cowork-vs-code.md)** — the three rooms, and the learner's deliberate Cowork → Code path through them.
8. **[docs/plan.md](docs/plan.md)** — the architecture and build order. Some sections are marked superseded after the shift to the skill tree.
9. **[viz/](viz/)** — the dynamic skill-tree visualization. Same source data as the markdown (YAML frontmatter on every Skill and branch README), rendered as a pan/zoom map. Build phases tracked in [docs/open-questions.md #16](docs/open-questions.md).

## Then, as you contribute

- **[docs/conventions.md](docs/conventions.md)** — formatting and structural rules. Follow these in every change.
- **[docs/open-questions.md](docs/open-questions.md)** — decisions still to be made. React in PRs.
- **[resources/curated-links.md](resources/curated-links.md)** — external resources we recommend, with curation rationale.

## For learners (when it's ready)

When the first Tier-1 drills are authored and `START_HERE.pdf` is rendered, learners will receive this repo as a zipped folder and open the PDF at the root. The prelude source is already in place (`skills/prelude.welcome-to-the-stand/`); drill content and the PDF render are next. Until then, the repo is for builders only — see [docs/plan.md](docs/plan.md) for the build order.

## For contributors

This repo is built to be collaborated on. The fastest way to engage: react to [docs/open-questions.md](docs/open-questions.md) or open a PR against any doc in `docs/`. PRs are the unit of progress here — see [docs/chat-vs-cowork-vs-code.md](docs/chat-vs-cowork-vs-code.md) for why.

## The 1979 game

[game/](game/) holds a faithful Python recreation of the 1979 Apple II classic *Lemonade Stand* (original by Bob Jamison / Charlie Kellner, MECC). It's a sibling artifact — not part of the curriculum — kept here as the historical inspiration for the lemonade-stand framing the training program uses. See [game/README.md](game/README.md) to play it.

## Conventions

See [docs/conventions.md](docs/conventions.md) for the canonical formatting and structural rules — filenames, markdown, cycle layout, contribution flow, enforcement. If you're using Claude Code on this repo, [CLAUDE.md](CLAUDE.md) is loaded automatically and points to the same place.
