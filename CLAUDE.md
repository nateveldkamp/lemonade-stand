# Claude Code project notes — Lemonade Stand

This repo is an async training program for knowledge workers, not a product. The intended audience starts with zero tooling installed and ends by submitting a real PR to this repo.

## Read first

- `docs/teaching-philosophy.md` — pedagogical foundation; non-negotiable.
- `docs/vision.md` — why this repo exists.
- `docs/narrative-arc.md` — the lemonade-stand growth story. Skills anchor to stages here.
- `docs/skills.md` — the skill-tree framework: Branches, Skills, Tiers, Drills, slug convention, build states.
- `docs/roadmap.md` — canonical paired view of the prelude + full nine-branch tree. The progress board AND the build-state board.
- `docs/analogies.md` — canonical analogies (spreadsheets ↔ Git, etc.). Reach for these before inventing new ones.
- `docs/chat-vs-cowork-vs-code.md` — the three rooms, and the learner's deliberate path through them.
- `docs/plan.md` — architecture and build order. Some sections marked superseded after the shift to the skill tree.
- `docs/conventions.md` — formatting and structural rules. Follow these in every change.
- `docs/open-questions.md` — what we haven't decided yet. Check before assuming.
- `viz/` — the dynamic skill-tree visualization. Reads `viz/skills.json`, generated from YAML frontmatter on every Skill/branch README by `viz/build-skills-json.py`.

## Core principles

- **Skill tree, not linear chapters.** After the prelude, the curriculum is a multi-branch skill tree (see `docs/skills.md`). The learner picks where to go next; there is no required order. Every Skill plays the whole game inside itself — Tier 1 is t-ball for that Skill, complexity is added across tiers.
- **One continuous narrative.** The lemonade stand grows across stand stages (see `docs/narrative-arc.md`). Skills anchor to stages, not to fixed cycle numbers. Every Skill README and every drill opens with a story beat tied to the relevant stand stage.
- **Analogies first, definitions second.** Lead with what the audience already knows (spreadsheets, email, folders), bridge to the new concept, then name where the analogy breaks. See `docs/analogies.md`.
- **Full knowledge-work stack, not just AI.** AI fluency anchors the early cycles; business, planning, analytics, and automation are equally first-class as the arc progresses.
- **Deliver the course through the tools it teaches.** Claude is the primary interface. The learner starts in Cowork (prelude), graduates to Claude Code inside the Git Tier-1 drill at the **Move to the workshop** milestone, and stays in Code from there. See `docs/chat-vs-cowork-vs-code.md`.
- **The roadmap is the progress board AND the build-state board.** `docs/roadmap.md` shows every Skill in the tree with its current build state (*not started* / *stub* / *Tier N* / *complete*). `progress.py` will reprint it with each row's status filled in for the learner. New drills update the roadmap's build-state markers in the same PR.
- **Skill tree as dual channel.** The skill tree is *both* (a) the structured markdown the learner reads in Claude Code / Chat / GitHub and (b) a dynamic HTML map (`viz/`) with pan/zoom. Both channels read from the same source: YAML frontmatter on every Skill and branch README (schema in `docs/skills.md`). When a Skill is added, renamed, or restructured, the frontmatter is the single edit; `viz/build-skills-json.py` regenerates the JSON the visualization consumes. Interdependencies (prereqs/unlocks) are first-class — they show up in both channels.
- **Curate, don't recreate.** Link to canonical external docs (Anthropic, GitHub, etc.) instead of rewriting them. The repo's value is narrative and exercises, not reference material that will go stale.
- **Mac + Windows both first-class.** Every install step needs parallel instructions for both OSes.

## Conventions (highest-leverage reminders)

The canonical rules are in `docs/conventions.md`. Follow it. The reminders most likely to come up in AI-assisted edits:

- Markdown only. **No horizontal rules (`---`).** Use headings.
- **Lowercase kebab-case** for new filenames. Uppercase exceptions only: `README.md`, `CLAUDE.md`, `CONTRIBUTORS.md`, `LICENSE`, `CHANGELOG`.
- No screenshots unless explicitly requested.
- Default to no comments in code; let well-named identifiers speak.
- Don't add features, refactoring, or abstractions beyond what the task requires.

## Plans before code

The maintainer's standing rule: produce a detailed plan and get approval before writing implementation. This applies to learner-facing content too — propose cycle outlines before authoring them.

## Useful context

- The lemonade stand is currently a *motif and a story*, not a running simulation. The story (per `docs/narrative-arc.md`) is canonical and being filled in as cycles get built; the sim is not. Don't build sim mechanics until a teaching milestone needs them.
- The repo is meant to be zipped and distributed to learners with nothing installed. Anything Cycle 0 depends on must be runnable from a fresh machine with only a file explorer and a browser.
- `docs/` is for builders/collaborators (with `docs/roadmap.md` as the shared learner-facing exception). Learner-facing content lives in `skills/`. The prelude (`skills/prelude.welcome-to-the-stand/`) is built; six Skill stubs are built (Git, Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation); no drills are yet authored beyond the prelude. Every Skill and branch README carries YAML frontmatter (schema in `docs/skills.md`). Read the prelude and the existing Skill READMEs before authoring more — match their tone and structure.
- `viz/` is the dynamic skill-tree visualization. `viz/build-skills-json.py` walks `skills/`, parses frontmatter, and emits `viz/skills.json`. The HTML/JS layers are not yet built (Phase B onward). Regenerate `viz/skills.json` whenever Skill/branch frontmatter changes, and commit it in the same change.
- `game/` is a sibling artifact — a faithful Python recreation of the 1979 Apple II *Lemonade Stand*. It's the historical inspiration for the curriculum's lemonade-stand framing, not part of the curriculum itself. Don't wire it into Skills or drills; leave it alone unless a change is explicitly about the game.
- **Reference repo content, don't relay it.** Markdown renders natively in Claude Code, Chat, and Cowork. When the learner needs to read a pre-written file, point at the path and let the interface render it — don't reproduce the file verbatim in chat. Quoting a single relevant paragraph to answer a focused question is fine.
