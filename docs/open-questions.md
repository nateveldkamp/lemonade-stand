# Open questions

Decisions to make before the first build phase begins. React in PRs or comments — these are the highest-leverage choices in the project right now.

## 1. Where does the repo eventually live?

Possible homes:
- A personal/maintainer GitHub account.
- A dedicated public GitHub org for the curriculum.
- Mirrored elsewhere (an org's internal GitHub, a fork by a sponsor, etc.).

**Why it matters:** affects PR-flow instructions, the GitHub access guide, the "first PR" social dynamics, and whether external contributors are part of the model.

**Working assumption (replace when decided):** maintainer's personal account during planning, with a plan to migrate to a public org once Cycle 1 is built.

## 2. PDF build pipeline for `START_HERE.pdf`

Options:
- **Pandoc** — cleanest output, widely used, but adds an external system dependency for anyone rebuilding the PDF.
- **Python-only** (e.g. `markdown` + `weasyprint`) — slower output, more setup pain, but uses only tools the curriculum already installs. Could itself become a Cycle 3 exercise ("rebuild your own START_HERE PDF").

**Why it matters:** the rendered PDF is the entry point for every learner. Reproducibility of the build matters.

**Working lean:** Python-only, to keep the dependency surface aligned with what learners install anyway.

## 3. Branding and tone of `START_HERE.pdf`

**✅ DECIDED — Hybrid: professional layout, warm tone.** Captured in `docs/conventions.md` under "Tone and content." Not playful (no mascot), not corporate (no marketing-speak) — friendly senior colleague walking you through it.

Original options for context:
- Playful (mascot, "Lemonade Stand Academy" framing, casual screenshots).
- Professional (clean, neutral, corporate-friendly).
- Hybrid (professional layout, warm tone). ← chosen

## 4. First-PR merge policy

Options:
- **Auto-merge** — Cycle 1 PRs that touch only `CONTRIBUTORS.md` merge themselves via a GitHub Action. Scales infinitely but loses the "someone reviewed this" social moment.
- **Manual review by maintainer** — every Cycle 1 PR gets a personal merge. Highest signal, doesn't scale.
- **Opened-and-left-open** — opening the PR is the win condition; merging isn't required. Avoids the scaling problem without losing the celebratory moment.

**Why it matters:** Cycle 1's reward structure depends on this. The full-circle moment is the centerpiece.

**Working lean:** auto-merge for Cycle 1 specifically (lowest friction at scale), manual review for Cycle 2+ where the contributions are more substantive.

## 5. Scope of `lemonade-stand/` content at Cycle 1 launch

Options:
- **Minimal** — just a `CONTRIBUTORS.md` for the stand and nothing else. Learners add their name to a near-empty file.
- **Seeded** — a tiny `sales.csv`, an `ingredients.csv`, a one-paragraph "your stand" scenario, and a `CONTRIBUTORS.md`. The world feels real on day one.

**Why it matters:** sets the tone for the motif. A bare file feels like a class exercise; a seeded world feels like a real (tiny) business.

**Working lean:** seeded. The marginal authoring cost is small and the immersion gain is large.

## 6. Automated convention enforcement timing

Options:
- **Now (planning phase)** — set up markdownlint + a filename-casing check before any other build work. Catches violations from day one.
- **After Cycle 1 launches** — focus build energy on curriculum first; enforce by review until then. Add CI as part of Cycle 1's wrap-up.
- **Never automated** — rely on review forever. Reasonable only if scale stays low.

**Why it matters:** [conventions.md](conventions.md) is the canonical rules document. Without automation, drift will happen as contributor count grows. The earlier we add CI, the cheaper enforcement is per PR.

**Working lean:** after Cycle 1 launches. Convention drift is low-stakes during planning; the CI surface is small enough to add quickly when needed.

## 7. How deep does the business arc go?

The lemonade stand grows alongside the curriculum (see [narrative-arc.md](narrative-arc.md)). The arc could plausibly end anywhere from "regional small business" to "global public multinational with manufacturing, logistics, software, and data orgs."

Options:
- **Outline the full arc now**, with detail front-loaded on early stages where Cycles 1–3 live. Later stages exist as named placeholders so contributors can see where their cycle would slot in.
- **Cap at regional company for v1.** Don't commit to anything beyond. Add later stages only if/when cycles demand them.
- **Don't commit yet.** Sketch only the stages that cycles currently need.

**Why it matters:** the arc defines the canonical "story bible." Cycles reference it, contributors extend it. The wider the committed arc, the more discipline is needed to keep cycles from sprawling toward it prematurely.

**Working lean:** outline the full arc now, detail front-loaded. Naming the destination makes "playing the whole game" credible — the learner sees from day one where this is heading.

## 8. Voice and point of view for the narrative

**✅ DECIDED — Mixed: second-person early, small cast widens as the business grows past Cycle 3.** The learner remains the owner/operator making decisions throughout. Captured in `docs/conventions.md` under "Tone and content."

Original options for context:
- Second-person only.
- Third-person character.
- Omniscient / company-level.
- Mixed (second-person early, widens later). ← chosen

## 9. Real spreadsheets in the repo?

**✅ DECIDED — `.xlsx` first; `.csv`-in-Git migration is a Cycle 3 teaching moment** (the *Out of the spreadsheet* milestone on the roadmap). Captured in `docs/conventions.md` under "Data files." The migration *is* the lesson.

Original options for context:
- xlsx + csv side-by-side from day one.
- csv only.
- xlsx first, migrate to csv as a Cycle 3 teaching moment. ← chosen

## 10. Primary delivery interface

**✅ DECIDED — Claude is the primary interface. Cowork is the foyer; Code is the workshop. Graduation happens mid-Cycle 1 at the *Move to the workshop* milestone.** Captured in `docs/teaching-philosophy.md` (new principle), `docs/plan.md` (Delivery interface section), `docs/chat-vs-cowork-vs-code.md` (the learner's path section), and `docs/roadmap.md` (interface column + milestone).

Original options for context:
- Pure Code from minute one.
- Cowork foyer → Code workshop (graduation mid-Cycle 1). ← chosen
- All three interfaces taught explicitly.

## 11. Curriculum architecture — linear or tree?

**✅ DECIDED — Skill tree, not linear.** After the mandatory prelude (Welcome to the stand), the curriculum is a multi-branch skill tree the learner navigates choose-your-own-adventure style. Vocabulary: *Branch*, *Skill*, *Tier*, *Drill*. Captured in [skills.md](skills.md), with the live state in [roadmap.md](roadmap.md). Supersedes the original linear Cycle 0–4 plan in [plan.md](plan.md).

## 12. Drill slug stability

**✅ DECIDED — Slugs are forever.** Format `<branch>.<skill>.tier-N.<descriptive-name>`. Once committed, a drill's slug doesn't change. If a drill is restructured or moved, the old slug stays as a redirect rather than being deleted. This is how a learner's local `.progress/state.json` survives course updates. Captured in [skills.md](skills.md) and [conventions.md](conventions.md).

## 13. Initial skill tree shape

**✅ DECIDED — 9 branches, ~40 Skills.** Branches: Foundations, Data, Operations, Customer, Systems, Automation, Communication, People, Strategy. Six Skills stubbed at landing (Git, Spreadsheets, Planning, Data management, Data analysis, Spreadsheet automation); the rest of the ~34 Skills are visible on the roadmap but marked *not started*. Authoring proceeds drill-by-drill. This is a starting shape that will iterate; the build-state markers on `roadmap.md` are the source of truth for what's live.

## 14. Choose-your-own-adventure mechanic

How does the learner pick their next Skill, given a 9-branch tree mostly empty on day one?

Options:
- **Conversation with Claude.** Cycle 0 ends with the learner telling Claude what they do for work and what they want to be better at; Claude proposes the best authored entry point. *(My lean — natural, conversational, uses Claude as the curriculum tour guide.)*
- **Static suggestions.** The prelude lists "if you want X, start with Y" pairs. Simpler; less personal.
- **Quiz / decision tree.** A few questions and a recommendation. Most structured; most rigid.

**Why it matters:** the choose-your-own-adventure model breaks if learners get stuck staring at the tree without knowing where to start.

**Working lean:** conversation with Claude (already wired into the prelude's "Try Claude on something real" step).

## 15. AI tool extensibility — when to add second-class paths

The default AI tool is Claude (Cowork at the foyer, Code from Git Tier 1 onward). The vision calls for the course to be extensible to other AI tools (ChatGPT, Gemini, Copilot) eventually.

Options:
- **Now, alongside the Cowork path.** Author `open-in-chatgpt.md`, `open-in-gemini.md` from day one. Adds authoring cost on every prelude change.
- **After Claude path is complete.** Lock Claude as the only path until the first ~5 drills are authored, then layer alternatives.
- **Never beyond Claude.** Treat Claude as the curriculum's working assumption; let other tools' learners adapt the materials themselves.

**Why it matters:** affects the prelude's structure and how much parallel authoring drag we accept.

**Working lean:** after the Claude path is complete. Don't pay the extensibility tax until the original works.

## 16. Dynamic skill-tree visualization

The current skill tree is a markdown roadmap — fine for builders, limited for learners. The maintainer wants a dynamic, Google-Maps-style visualization the learner can pan and zoom — overview of all 9 branches at one zoom level, individual Skill detail at another. Inspiration: [hfviewer.com](https://hfviewer.com/).

Options to evaluate next session:

- **Static HTML+JS, checked into the repo.** A single-file or small-directory visualizer (D3.js or similar) that opens locally in a browser. No backend; no hosting. Source of truth is still the markdown; viz is generated from YAML frontmatter on each Skill `README.md` or from a generated `skills.json`. Best aligned with the "everything in the repo" principle.
- **Mermaid diagrams in the markdown itself.** Rendered natively by GitHub, Cowork, and Claude Code. Limited interactivity (some zoom support is recent and uneven). Lowest authoring overhead; not really Google-Maps quality.
- **GitHub Pages site deployed from the repo.** A small static site (Svelte/React/plain HTML) deployed automatically via Actions. Shareable URL; the learner doesn't need to clone. Adds CI complexity.
- **Separate hosted web app.** Most flexible visualization; breaks the "repo is the artifact" principle. Hardest to keep in sync with the curriculum.

**Working lean (subject to revision):** static HTML+JS checked into the repo, generated from structured data extracted from the existing Skill READMEs. Keeps the markdown as source of truth, adds zero hosting dependencies, and a learner who clones the repo can open the viz locally with no install. Could later be deployed to GitHub Pages without changing the source.

**Why it matters:** the skill tree's value scales with how easily a learner can hold the whole thing in their head. A flat markdown table is OK at 6 Skills, painful at 40, useless at 80. The viz is the difference between a course that *feels* navigable and one that *is* navigable.

**Live design questions to settle next session:**
- Frontmatter schema (what structured data each Skill `README.md` exposes).
- Layout strategy — clustered branches with concentric tier rings? Force-directed graph? Tiered tree? Each gives a different "shape" of map.
- Build state visualization — color? Opacity? Layer toggle?
- Prereq/connection arrows — visible by default, on-hover, or layer-toggle?
- Whether to extract `skills.json` at commit time (CI/script) or maintain it by hand.

## How to add a new question to this list

When a question comes up during build, add it here rather than letting it become silent. Track decisions in PRs that resolve them; close out the question with a one-line link to the deciding PR.
