# Conventions

The canonical formatting and structural rules for this repo. Enforced by review today; will be enforced by lightweight CI as soon as Cycle 1 launches.

If you're proposing a change to these rules, do it via PR against this file and update `CLAUDE.md` if the change affects AI-assisted edits.

## Files and directories

- **Filenames:** lowercase kebab-case (e.g. `chat-vs-cowork-vs-code.md`, `curated-links.md`).
- **Directory names:** lowercase kebab-case (e.g. `skills/`, `docs/`, `resources/`).
- **Uppercase exceptions:** `README.md`, `CLAUDE.md`, `CONTRIBUTORS.md`, `LICENSE`, `CHANGELOG`, and any file an external tool *requires* to be uppercase. Don't invent new uppercase files for stylistic reasons.
- **Skill tree layout:** `skills/<branch>/<skill>/`, plus `skills/<branch>/<skill>/drills/<slug>/` for individual drills.
- **Skill directories:** each Skill has a `README.md` with overview + tier map.
- **Frontmatter is mandatory.** Every `README.md` under `skills/` opens with a YAML frontmatter block declaring `kind`, `slug`, `name`, `tagline`, and `build_state` at minimum. Branch READMEs additionally declare their `skills:` list (mixing slugs for authored Skills and inline objects for not-started placeholders). Skill READMEs additionally declare `branch`, `tier_count`, `tier_1_stand_stage`, `prereqs`, and `unlocks`. Full schema in [skills.md](skills.md). The frontmatter is the canonical structured form of the tree; both the markdown experience and the `viz/` visualization read from it.
- **Drill slug format:** `tier-N.<descriptive-name>` (or the full `<branch>.<skill>.tier-N.<descriptive-name>` outside the skill directory). Slugs are stable — once committed, they don't change. If a drill is restructured, the old slug stays as a redirect rather than being deleted, so local learner progress survives course updates. See [skills.md](skills.md).
- **Drill contents:** `README.md` (the drill itself), plus `exercise.md` and `checkpoints.md` where the drill is long enough to warrant them.
- **Prelude:** `skills/prelude.welcome-to-the-stand/` — outside the tree, the one mandatory step.
- **Locations:**
  - Learner-facing content → `skills/`.
  - Planning + contributor context → `docs/`.
  - External resources → `resources/`.
  - Lemonade-stand motif content (datasets, scenarios) → `lemonade-stand/`.
  - Standalone sibling artifacts (e.g. the 1979 game recreation) → top-level named directory (`game/`). Not part of the curriculum; left alone unless the change is explicitly about that artifact.
  - Local-only learner progress → `.progress/` (gitignored).

## Markdown formatting

- **No horizontal rules (`---`).** Use heading levels for visual separation.
- **ATX-style headings** (`# Heading`), not underline style.
- **One H1 per file.** It is the title.
- **Heading hierarchy is logical.** Don't skip levels (no `#` jumping to `###`).
- **Inline links only.** `[label](path)`. No bare URLs in prose.
- **Relative paths for repo-internal links.** Example: `[plan](docs/plan.md)`, not absolute or GitHub URLs.
- **Fenced code blocks** with a language tag (`` ```python ``, `` ```bash ``).
- **Tables** are fine; keep columns narrow enough to read in raw markdown.
- **Don't hard-wrap lines.** Let markdown reflow.
- **No emoji** unless the maintainer explicitly requested them.

## Tone and content

- **Plain English.** Define jargon on first use.
- **Tone is hybrid: professional layout, warm voice.** Not playful (no mascot, no jokes for their own sake), not corporate (no marketing-speak). Think *a friendly senior colleague walking you through it* — clean, present, kind, never condescending.
- **Curate, don't recreate.** When an external doc is canonical (Anthropic, GitHub, etc.), link it. Don't paraphrase reference material that will go stale.
- **Lemonade-stand framing** for every example, dataset, scenario, and exercise.
- **Open with a story beat.** Every cycle's `README.md` opens with one paragraph of narrative anchored in the relevant stage of [narrative-arc.md](narrative-arc.md). Bulleted instructions come after the story, not before it.
- **Voice:** present tense, second person early ("you decide to open a second stand"). Mixed cast appears as the business grows past Cycle 3 — but the learner remains the owner/operator making the decisions.
- **Analogies first, definitions second.** When introducing a concept the audience hasn't seen, lead with an analogy from [analogies.md](analogies.md) (spreadsheets, email, folders, etc.), bridge to the new concept, then explicitly name where the analogy breaks. If you need a new analogy, add it to that doc in the same PR.
- **Name the interface in every cycle step.** Each step in a cycle states which room the learner is in (Cowork, Claude Code, terminal, browser). The Cowork → Code graduation inside Cycle 1 is called out explicitly. See [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md).
- **Mac + Windows both first-class.** Every install or setup step needs parallel instructions for both OSes.

## Data files

- **`.xlsx` is the default ship format for lemonade-stand data.** The audience opens spreadsheets daily; meeting them there is the on-ramp.
- **The `.csv`-in-Git migration is a Cycle 3 teaching moment**, not an authoring shortcut. Don't pre-emptively convert `.xlsx` files to `.csv` in early cycles — that gives away the lesson.
- **One canonical dataset per scenario.** When a cycle needs new numbers, extend the existing dataset rather than introducing a parallel one.

## Drill authoring

- **Every drill justifies itself against `teaching-philosophy.md`** (sibling file in `docs/`). New material is added only when a teaching milestone motivates it.
- **Every Skill plays the whole game.** Tier 1 of any Skill is the simplest credible version of that Skill — t-ball for Git, t-ball for Planning, t-ball for Data analysis. Drill authors check the existing Tier 1 drills for tone before writing a new one.
- **The five-phase shape** — Hook → Setup → Play → Ship → Reflect — applies at the drill level for drills long enough to warrant it. Short drills can collapse phases. See `docs/plan.md` for the original framing.
- **Last interaction is celebratory**, not "now go read these docs."
- **No prerequisites that delay the play loop.** Foundational drills should be playable from the prelude with no intermediate setup beyond what their Skill README says is required.
- **Reference content, don't relay it.** Markdown renders natively in Claude Code, Chat, and Cowork. When a drill wants the learner to read something pre-written, the instruction points at the file (e.g. "open `skills/data/data-analysis/drills/tier-1.../exercise.md`") and the interface renders it. Claude may quote a single relevant paragraph to answer a focused question, but should not reproduce whole docs the learner could open directly. This keeps drills fast, the rendering crisp, and avoids wasteful verbatim regeneration.
- **Slugs are forever.** A drill's slug is committed when the drill lands. If the drill is later renamed or restructured, the slug stays as a redirect (the directory may be empty except for a pointer file). This is how local learner progress survives course updates.

## Curated resources

- Each entry in `resources/curated-links.md` answers three questions: *what it is*, *why we link it* (instead of writing our own), *when in the curriculum to read it*.
- **Inclusion bar:** "would I genuinely recommend this to a colleague at this point in the curriculum?" If not, leave it out.
- Mark URLs *to confirm* rather than guess them.

## Contribution flow

- **One topic per PR.** Don't bundle unrelated changes.
- **PR descriptions reference relevant docs** (`docs/vision.md`, `docs/plan.md`, `docs/teaching-philosophy.md`, this file).
- **Open decisions tracked** in `docs/open-questions.md`. Resolve via PR; close out the question with a one-line link to the deciding PR.
- **Sweep the index files when structure changes.** When a commit lands or removes a Skill, a Drill, a top-level file, or a major directory, review and update — in the *same* commit — the status lines and read-first lists in `README.md`, `CLAUDE.md`, the structure diagram in `docs/plan.md`, and the build-state markers in `docs/roadmap.md` and the relevant Skill/branch `README.md`. These files go stale faster than any others; treat them as part of every structural change. Until automated, this is review-enforced.
- **Regenerate `viz/skills.json` when frontmatter changes.** Any edit to a Skill or branch README's YAML frontmatter (add, rename, change prereqs/unlocks, promote build state) requires running `python3 viz/build-skills-json.py` and committing the updated `viz/skills.json` in the same change. The script validates symmetry of `prereqs`/`unlocks` edges and warns on dangling references; resolve those before committing.
- **No direct commits to `main`** once Cycle 1 launches. Until then, the maintainer may push directly during planning.

## Enforcement

- **Today:** manual review against this document. `CLAUDE.md` instructs AI-assisted edits to follow it automatically.
- **Planned:** lightweight CI when Cycle 1 launches — at minimum a markdownlint config (catches horizontal rules, emoji, heading hierarchy) and a filename-casing check. Tracked in `docs/open-questions.md`.
- **Until automated checks exist**, contributors and reviewers are the enforcement mechanism. If a PR violates a rule, link this doc in the review comment rather than rewriting the rule each time.
