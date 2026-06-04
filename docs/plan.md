# Plan

This is the working architectural plan for the repo. The canonical paired view of the curriculum — the artifact a learner sees as their journey — lives in [roadmap.md](roadmap.md). The vocabulary and structure of the skill tree (what we used to call "cycles") live in [skills.md](skills.md). Open questions live in [open-questions.md](open-questions.md).

> **Note (superseded sections below):** the original "Cycle 1 detailed design" and the linear Cycle 1–4 cycle map were written before the curriculum shifted to a multi-Skill tree. Those sections are kept below as historical reference and as the source material for what eventually became *Foundations / Git / Tier 1 — Your name on the stand*. The current curriculum design lives in the skill tree (`docs/skills.md`, `docs/roadmap.md`, and the `skills/` directory). When the two diverge, the skill tree wins.

## Guiding principles

Every later decision must check back against these.

1. **Whole game from minute one.** Cycle 1 ends with the learner's first PR on this repo, in a single sitting. No "you'll get to play once you finish the prerequisites."
2. **Cycles, not chapters.** The curriculum is recursive. Cycle 1 is t-ball; each later cycle replays the entire loop (plan → use Claude Code → commit → push → PR → review) with more complexity dialed in.
3. **Add complexity only when a teaching milestone motivates it.** No tool, concept, or feature appears in the repo unless a cycle specifically needs it.
4. **Curate, don't recreate.** External docs are linked, not rewritten. The repo's unique value is *narrative*, *exercises*, and *the lemonade-stand frame*.
5. **Zero assumed tooling.** START_HERE works with nothing but a file explorer and a browser. Everything else is installed inside the experience.
6. **One continuous narrative.** The lemonade stand grows from a card table to a global public company across the cycles. Each cycle is a stage in that one story. New skills land on top of business complexity the learner has just earned. See [narrative-arc.md](narrative-arc.md).
7. **Analogies first, definitions second.** Lead with what the audience already knows — spreadsheets, email, shared folders — bridge to the new concept, then name where the analogy breaks. See [analogies.md](analogies.md).
8. **Full knowledge-work stack, not just AI.** AI fluency anchors the early cycles because it is the current acute need, but the broader subject is business, planning, analytics, automation, and AI/systems together. Later cycles use AI tooling to teach the rest of the stack.
9. **Deliver the course through the tools it teaches.** Claude is the primary interface. The learner starts in Cowork (the easiest on-ramp — no install), graduates to Claude Code mid-Cycle 1, and stays in Code from then on. The chat-vs-cowork-vs-code distinction is *experienced*, not just explained. See [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md).
10. **Mac + Windows both first-class.** Every install step has parallel instructions and screenshots.

## The cycle architecture

The repo is organized around progressive cycles. Each cycle has the same five-phase shape:

| Phase | What the learner does | Skills exercised |
|---|---|---|
| **Hook** | Reads a short "why this matters" framing, scaled down to a lemonade-stand example. | Motivation, context. |
| **Setup** | Installs only the tool(s) this cycle requires. | Environment, package managers. |
| **Play** | Uses the tool against a lemonade-stand exercise. | The actual skill being taught. |
| **Ship** | Commits, pushes, opens a PR back to this repo. | Git/GitHub fluency. |
| **Reflect** | Updates a personal progress file; optionally writes a one-line learning to `CONTRIBUTORS.md`. | Metacognition, the "factory" mindset. |

The five phases repeat in every cycle. That repetition *is* the teaching device — the loop becomes muscle memory.

### Cycle map (initial sketch)

Each cycle pairs a stage of the lemonade-stand business (from [narrative-arc.md](narrative-arc.md)) with the skills needed to handle that stage. Cycle names lead with the story; the technique focus is the subtitle. The canonical paired view a learner sees is [roadmap.md](roadmap.md); the map below is the builder/architecture view.

| # | Cycle name (story) | Technique focus | Stand stage | Interface | Time |
|---|---|---|---|---|---|
| **0** | Welcome to the stand | Setup, orientation | 0 — card table | Cowork | ~15–30 min |
| **1** | Your name on the stand | First PR (Claude Code, Git, GitHub, VS Code, Python minimal) | 0 — card table | **Cowork → Code** (graduation milestone mid-cycle) | ~1–2 hr |
| **2** | Your first season | Editing with intent (planning mode, slash commands, branching) | 1 — recurring weekend stand | Code | ~2–3 hr |
| **3** | Bringing in help | The factory mindset (subagents, evals, simple MCP) — includes the **Excel-to-Git migration moment** | 2 — family helps out | Code | ~half day |
| **4** | Going multi-stand | Agents at work (agentic workflows, scheduled/recurring tasks) | 3 — multiple locations | Code | ~full day |
| **5+** | *Future stages — TBD* | Contribute substantively — propose a cycle for an emerging stage | 4+ (wholesale, hires, product lines, regional, manufacturing, national, global) | Code | open-ended |

The transition from Cycle 3 to Cycle 4 is where the Naval "build the factory, not the artifact" quote lands hardest — the moment the learner *experiences* the shift. It is also the first cycle where the lemonade stand has grown past what one person can run by hand, which is what makes "the factory" feel necessary rather than abstract.

## Cycle 1 detailed design

This is the most important cycle to nail. Everything downstream is a variation on this template.

### Narrative arc

> "You just inherited a tiny lemonade stand. Today, you'll make one improvement to how it's run — and you'll do it the way modern knowledge work gets done: using AI as a collaborator, tracked in a repo, reviewed by your peers."

### Step-by-step (what Cycle 1 literally walks through)

Cycle 0 has already happened in Cowork (folder unzipped, project created in Cowork, narrative-arc and roadmap read with Claude's help). Cycle 1 opens in Cowork too, and the **Move to the workshop** milestone — installing Claude Code and switching over — sits in the middle of the cycle as the climactic graduation. First PR happens in Code.

**Phase: Hook (in Cowork)**

1. Open the Cycle 1 README in Cowork. Read the narrative beat: *"You've just inherited a tiny lemonade stand. Today, you'll make one real improvement — and you'll do it the way modern knowledge work gets done."*
2. **A quick aside on rooms.** Pointer to [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md). "You're in Cowork right now. By the end of today, you'll have moved to Code. Here's why."

**Phase: Setup (in Cowork → still browser-only, no terminal yet)**

3. **Install VS Code.** Mac + Windows side-by-side with screenshots. Gives a real editor.
4. **Open this folder in VS Code.** One-click.
5. **Install Git.** Verify with `git --version` in the integrated terminal.
6. **Install Python.** Minimum viable — enough to run a script later. Verify with `python3 --version`.
7. **Install Claude Code.** `npm i -g @anthropic-ai/claude-code` (so Node also gets installed), authenticate.

**🛠 Milestone — Move to the workshop (Cowork → Code graduation)**

8. **Open this folder in Claude Code.** First terminal interaction. Side-by-side screenshot: same files, same `CLAUDE.md`, same `docs/`, now operated on by Claude with versioning underneath. The learner *feels* the difference between Cowork and Code in the same task on the same files.

**Phase: Play (in Code)**

9. **Get GitHub access.** Sign up at github.com (or use an existing account). Authenticate `gh` CLI.
10. **First Claude Code task.** Scripted, low-risk prompt: *"Add my name and a one-line note about my role to `CONTRIBUTORS.md`."* The learner sees Claude Code propose and apply an edit for the first time — the same kind of edit they just made in Cowork, but now it's a real change to a tracked file.

**Phase: Ship (in Code)**

11. **Commit.** Use Claude Code to write the commit message. Reinforces "use the tool" over "learn the tool."
12. **Branch + push.** Claude-Code-assisted `git checkout -b cycle-1/<name>` and `git push`.
13. **Open the PR.** `gh pr create` walkthrough. Title + body templates provided.

**Phase: Reflect (in Code)**

14. **Update progress.** Run `python3 progress.py`; see the roadmap reprint with Cycle 1 marked done and the workshop graduation milestone ticked. Optionally write a one-sentence "what surprised me" in the PR description.

### Deliverable for the learner

A real PR with their name on it. The dopamine hit and the proof point.

### Success criteria for us (the builders)

- A complete novice on a fresh Mac or fresh Windows machine finishes Cycle 1 unaided in under 2 hours.
- Every step has both Mac and Windows instructions, or is OS-agnostic with a clear note.
- No step requires reading external documentation unless we explicitly chose to outsource it via curation.
- The learner's last interaction is celebratory, not "now go read these docs."

## Delivery interface

Claude is the primary interface to the curriculum. The learner moves through three rooms in a deliberate order — and the move itself is part of the lesson.

| Phase | Interface | Why this interface |
|---|---|---|
| Pre-Cycle 0 | None — file explorer + browser only | Hard constraint: a fresh machine with no installs must be able to start. |
| Cycle 0 — Welcome to the stand | **Cowork** | Lowest-friction "Claude is now in the room" experience. No CLI, no install. Markdown renders natively, so the learner reads cycle content with Claude already alongside them. |
| Cycle 1 — Your name on the stand | **Cowork → Code** | Setup steps happen in Cowork. The **Move to the workshop** milestone — installing Claude Code and re-opening the folder there — is the deliberate graduation moment. First PR happens in Code. |
| Cycle 2 onward | **Code** | Steady state. Code is the workshop the rest of the curriculum lives in. |

See [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md) for the full argument. The point is that the learner *experiences* moving up the stack instead of being told about it.

### What `START_HERE.pdf` becomes

Previously imagined as the entire Cycle 0 in one PDF. With Cowork as the foyer, the PDF shrinks dramatically:

- A short "how to open this folder in Cowork" walkthrough — Mac + Windows side-by-side, ~2 pages.
- A pointer to the rest of Cycle 0, which lives in markdown in `cycles/cycle-00-welcome-to-the-stand/` and renders inside Cowork natively.

The "zero assumed tooling" constraint is preserved: the PDF + file explorer + browser are still enough to start.

## Repo structure (target)

What the learner sees when they unzip the folder:

```
lemonade-stand/
├── START_HERE.pdf                          # the only thing they're told to open first
├── README.md                               # front door; mirrors the prelude framing
├── CLAUDE.md                               # for any Claude Code session opened here
├── CONTRIBUTORS.md                         # where the Git Tier-1 drill adds the learner's name
├── progress.py                             # local CLI; reads .progress/state.json, prints roadmap.md with status
├── docs/                                   # planning + collaboration context
│   ├── teaching-philosophy.md
│   ├── vision.md
│   ├── plan.md                             # (this file)
│   ├── skills.md                           # skill-tree framework (vocab, slugs, tiers)
│   ├── roadmap.md                          # the paired view + build-state board (learner-facing)
│   ├── conventions.md
│   ├── narrative-arc.md
│   ├── analogies.md
│   ├── chat-vs-cowork-vs-code.md
│   └── open-questions.md
├── skills/                                 # all learner-facing content
│   ├── prelude.welcome-to-the-stand/       # mandatory; outside the tree
│   │   ├── README.md
│   │   └── open-in-cowork.md               # Mac+Windows walkthrough; also the START_HERE.pdf source
│   ├── foundations/
│   │   ├── README.md                       # branch overview + Skills list
│   │   ├── git/
│   │   │   ├── README.md                   # Skill overview + tier map
│   │   │   └── drills/
│   │   │       └── tier-1.your-name-on-the-stand/     # (not yet authored)
│   │   ├── spreadsheets/
│   │   │   ├── README.md
│   │   │   └── drills/
│   │   ├── markdown-and-plain-text/        # not started
│   │   ├── command-line/                   # not started
│   │   └── ai-fluency/                     # not started
│   ├── data/
│   │   ├── README.md
│   │   ├── data-management/
│   │   ├── data-analysis/
│   │   ├── data-visualization/             # not started
│   │   ├── databases/                      # not started
│   │   └── data-engineering/               # not started
│   ├── operations/
│   │   ├── README.md
│   │   ├── planning/
│   │   ├── process-design/                 # not started
│   │   ├── finance-and-accounting/         # not started
│   │   ├── decision-making/                # not started
│   │   └── risk-and-compliance/            # not started
│   ├── customer/                           # all Skills not started
│   ├── systems/                            # all Skills not started
│   ├── automation/
│   │   ├── README.md
│   │   ├── spreadsheet-automation/
│   │   ├── document-automation/            # not started
│   │   ├── workflow-automation/            # not started
│   │   ├── agentic-workflows/              # not started
│   │   ├── skill-engineering/              # not started
│   │   └── eval-design/                    # not started
│   ├── communication/                      # all Skills not started
│   ├── people/                             # all Skills not started
│   └── strategy/                           # all Skills not started
├── lemonade-stand/                         # the motif — shared playground content
│   ├── README.md
│   ├── data/                               # .xlsx files first; .csv migration is the Data-management Tier-3 moment
│   ├── scenarios/
│   └── exercises/
├── resources/
│   ├── curated-links.md
│   └── glossary.md
├── viz/                                    # dynamic skill-tree visualization
│   ├── build-skills-json.py                # parses frontmatter; emits skills.json
│   ├── skills.json                         # generated, committed
│   ├── index.html                          # (Phase B onward — not yet built)
│   └── vendor/                             # D3.js, marked.js — vendored, no CDN
└── .progress/
    └── README.md                           # local-only progress tracking (gitignored)
```

Notes on the structure:

- `lemonade-stand/` is the *motif and the story*, not a running sim. Tiny `.xlsx` files and scenario docs are enough at first; the directory is a placeholder for an eventual generator.
- `.progress/` is git-ignored. The learner's local state never gets committed; keeps PRs clean.
- `docs/` is mostly for builders/collaborators. The exception is `roadmap.md`, which is shared — `progress.py` reprints it for the learner.

## START_HERE delivery

Hard constraint: must be readable with **only** a file explorer + double-click + browser.

- **PDF is the foyer key, not the foyer itself.** Cycle 0 lives in Cowork; the PDF is a thin ~2-page "how to open this folder in Cowork" walkthrough — Mac + Windows side-by-side. Once the learner is in Cowork, the rest of Cycle 0 renders from markdown in `cycles/cycle-00-welcome-to-the-stand/`.
- **Single PDF, not a wiki.** A learner with no editor opens one file.
- **Front page is a literal map**: "By the end of today, your name will be on this repo. Here's how." Sets up the full-circle moment.
- **All screenshots dual (Mac + Windows)** with clearly labeled tabs/columns.

PDF build pipeline (Pandoc vs Python-only) is an open question — see [open-questions.md](open-questions.md). With the PDF now ~2 pages instead of a whole cycle, the pipeline choice matters less.

## The full-circle PR moment

PR scope ladders up across cycles:

- **Cycle 1 — Your name on the stand:** add yourself to `CONTRIBUTORS.md`. Smallest possible meaningful change. Cannot fail. Also the cycle where the learner experiences the **Cowork → Code graduation**.
- **Cycle 2 — Your first season:** add a new lemonade-stand exercise or pricing scenario using a provided template. First time the learner contributes *curriculum*, not just consumes it.
- **Cycle 3+ — Bringing in help and beyond:** progressively more ambitious — a new scenario, a new dataset, a new sub-cycle outline.

Each PR uses a different template (under `.github/PULL_REQUEST_TEMPLATE/`); the cycle's instructions point to the right one.

## Gamification / progress tracking

Constraints: no backend, no accounts, no web service. Must work offline after unzip. The roadmap *is* the progress board.

- **[roadmap.md](roadmap.md) is the source of truth.** Every cycle and every named milestone (e.g. *Move to the workshop*, *Out of the spreadsheet*) appears there.
- **`.progress/state.json`** — gitignored, written by the learner (via a tiny CLI we ship). Tracks which cycles and milestones are complete.
- **`python3 progress.py`** — runs locally, reads `.progress/state.json`, and *reprints `roadmap.md`* with each row annotated (`✓ done`, `• in progress`, ` locked`). One artifact, two views: empty grid for new learners, filling grid for active ones. No infrastructure.
- **Public-but-optional badges:** opening a PR for each cycle leaves a permanent visible record on GitHub. That's the social gamification layer without us building infrastructure.
- **Streaks deliberately omitted.** Streak mechanics conflict with async-and-at-scale delivery and create anxiety. Cycle completion is the unit, not daily activity.

## Curation strategy ("don't recreate" doctrine)

`resources/curated-links.md` is the spine. Each entry uses the format:

> **Claude Code basics** — official Anthropic docs, ~10 min read.
> *Why we link this:* current, maintained, better than anything we could write that would go stale in 3 months.
> *Read this when:* you finished Cycle 1 and want to go deeper before Cycle 2.

This both honors the rule and *models* the meta-evaluative thinking we want learners to develop.

## First build phase

Updated to reflect the skill-tree architecture. Build in this order:

1. **Prelude content** — `skills/prelude.welcome-to-the-stand/`. The Cowork-foyer content. ✅ landed.
2. **Skill-tree framework and roadmap** — `docs/skills.md`, `docs/roadmap.md`, the nine branch READMEs, and stubs for the first six Skills (Git, Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation). ✅ landed.
3. **Skill-tree visualization, Phase A — structured data.** YAML frontmatter on every Skill, branch, and prelude README; `viz/build-skills-json.py` generator; committed `viz/skills.json`. ✅ landed.
4. **Skill-tree visualization, Phase B+ — interactive HTML.** `viz/index.html` + D3-based map; pan/zoom with semantic level-of-detail; click-to-read content pane. Tracked in [open-questions.md #16](open-questions.md).
5. **First drill: Git Tier 1 — Your name on the stand.** Authored as `skills/foundations/git/drills/tier-1.your-name-on-the-stand/`. Install guides for VS Code, Git, Python, Claude Code, the **Move to the workshop** milestone, and the first-PR walkthrough. This is what was previously planned as "Cycle 1."
6. **Tier-1 drills for the other five stubbed Skills** — Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation. Each gives the learner a real first drill in that Skill so the choose-your-own-adventure model has actual destinations.
7. **`lemonade-stand/` motif scaffolding** — a placeholder `.xlsx` dataset and the first scenario (your stand, your first weekend).
8. **`progress.py`** tiny CLI + `.progress/` layout. The CLI reads state (keyed by slug) and reprints `docs/roadmap.md` with each row annotated.
9. **PR templates** under `.github/PULL_REQUEST_TEMPLATE/` and a starter `CONTRIBUTORS.md`.
10. **PDF build pipeline** and the first rendered `START_HERE.pdf`.
11. **Drill-by-drill expansion** — each subsequent drill is its own deliberate build, anchored to a Skill, Tier, and stand stage.

The most important shift from the previous plan: there's no longer a *required linear order* after the prelude. The course is a tree from step 3 onward, and the learner can pick any of the authored Tier-1 drills as their first non-mandatory step.
