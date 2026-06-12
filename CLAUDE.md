# Claude Code project notes — Lemonade Stand

This repo is an async training program for knowledge workers, not a product. The intended audience starts with zero tooling installed and ends by submitting a real PR to this repo.

## Read first

- `docs/teaching-philosophy.md` — pedagogical foundation; non-negotiable.
- `docs/vision.md` — why this repo exists.
- `docs/narrative-arc.md` — the lemonade-stand growth story. Skills anchor to stages here.
- `docs/skills.md` — the skill-map framework: quadrants, slices, skills, tiers, complexity levels, the three channels (radius / roads / tiers), slug convention, build states.
- `docs/roadmap.md` — canonical view of the prelude + the 16-slice map in 4 quadrants. The progress board AND the build-state board.
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
- **Onboarding front door (redesigned 2026-06-12, pushed to `main`).** Learners no longer get a zip + PDF. The course now opens on a **GitHub Pages site**: `index.html` is a single interactive page that carries the cold open, day-1 game, the reveal, and the skill map directly as readable content, with short self-contained "copy this to your AI" prompts interwoven at the moments AI conversation helps (playing day 1, placing yourself on the skill map). `about.html` is the "why" page (David Perkins / business+AI-together); `llms.txt` and `.nojekyll` round out the entry artifacts; `game/play-by-chat.md` (Python-free game rules) is the canonical reference the day-1 prompt is distilled from. The root `README.md` points learners to the page and carries a short fallback note for AI assistants with repo access. Browser/mobile-first; learners graduate to working out of a cloned repo (Claude Code / Codex / Cursor — their choice) much later. **Before touching onboarding, read `memory/onboarding-front-door.md`.** Do NOT steer learners to a specific AI provider; steer toward graduating to a repo so they stop copy-pasting.
- `docs/` is for builders/collaborators (with `docs/roadmap.md` as the shared learner-facing exception). Learner-facing content lives in `skills/`. The prelude (`skills/prelude.welcome-to-the-stand/`) is built. The curriculum is organized as a radial **skill map**: 16 slices in 4 quadrants (Craft / Build / Run / Lead). Radius = business complexity (Rule of 3 and 10, field `complexity_level`), roads = authored `prereqs` (monotonic), tiers = skill mastery — three separate channels (see `docs/skills.md`). **In progress (2026-06-04): the skills are being rebuilt level by level (L0 outward); the 16 slices are currently empty (`skills: []`).** Before doing curriculum work, read `memory/skill-map-current-state-and-resume.md` (the resume note), then `docs/skills.md`. Every slice README carries YAML frontmatter.
- `viz/` is the dynamic skill-tree visualization. Two build scripts: `viz/build-skills-json.py` walks `skills/`, parses frontmatter, and emits `viz/skills.json`; `viz/build-viz.py` reads `viz/skills.json` and emits `viz/index.html` with the data embedded inline (opens as a plain `file://` URL — no server needed). Run both after any Skill/branch frontmatter change and commit the results in the same change.
- `game/` holds a faithful Python recreation of the 1979 Apple II *Lemonade Stand* (`game/lemonade.py`) plus `game/play-by-chat.md` (the same rules, Python-free, so any AI can run the game conversationally in onboarding). The Python version is the historical inspiration; don't wire it into Skills/drills. The chat version IS used by the onboarding opening — keep the two rule sets in sync if either changes.
- **Reference repo content, don't relay it.** Markdown renders natively in Claude Code, Chat, and Cowork. When the learner needs to read a pre-written file, point at the path and let the interface render it — don't reproduce the file verbatim in chat. Quoting a single relevant paragraph to answer a focused question is fine.
