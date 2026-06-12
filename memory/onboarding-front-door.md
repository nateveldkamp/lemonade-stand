---
name: onboarding-front-door
description: The learner onboarding model — paste the repo link into any AI chat and the README runs the experience. Agreed flow and decisions.
metadata:
  type: project
---

**Agreed 2026-06-04, redesigned 2026-06-12.** Major pivot in how learners get started, then a second pivot in how the opening is delivered.

## STATUS / how to resume (last worked 2026-06-12)

**2026-06-12 — redesign: the page leads, AI assists via small prompts.** The original model (learner pastes a tiny prompt, AI fetches `start.txt` and runs the whole 7-beat script) turned out to be unreliable — most AI chats can't reliably fetch a hosted page. The "one tap to start" provider buttons on `index.html` (Open in Claude / ChatGPT / Gemini / Grok) also didn't work. Both are now removed.

New model: `index.html` is a single scrolling page that **is** the start of the course — the cold open, day-1 game rules, the reveal table, and the skill map are all readable directly on the page, no AI fetch required. Interwoven at the two moments AI conversation genuinely helps are short, self-contained "copy this to your AI" prompts:
1. Play day 1 of the lemonade-stand game (rules distilled inline in the prompt — no page context needed).
2. Place yourself on the skill map and get a first-step recommendation (skill map listed inline in the prompt).

`start.txt` is removed. `llms.txt` and `README.md` now point AI assistants at the `index.html` page as the canonical opening; `README.md` keeps a short fallback note for agents with real repo file access (e.g. Claude Code), pointing them to `game/play-by-chat.md` and `docs/skills.md` if a learner wants to play differently.

**PENDING (do these to resume / test):**
1. **Enable GitHub Pages** (one-time, only Nate can): repo Settings → Pages → Deploy from a branch → `main` / root → Save. Until then the github.io URLs 404.
2. **Test pass:** open `index.html` on a phone and a computer — read it top to bottom, try both "Copy prompt" buttons, and paste each into an AI chat to confirm they work standalone with no page context.

This onboarding thread is separate from the **curriculum skill rebuild** (see `skill-map-current-state-and-resume.md` — skills are still empty, being rebuilt level by level, L0 proposal pending).

## The model: the repo link IS the onboarding

No more zipped folder + getting-started PDF. The new front door: a learner pastes the **GitHub repo link into any AI chat** (Claude, ChatGPT, Gemini — any provider, any tool) and says something like *"Read this repo and be my guide. Let's begin."* The AI reads the **root README**, which doubles as **instructions the AI follows to run the onboarding**. The repo is self-orchestrating. Only **later** (after Git basics are established) does it prompt the learner to clone locally and move to Claude Code.

## Settled decisions
- **Entry point = root README.** Must be self-sufficient so an AI that fetches only the README can run the whole opening; deeper files (skill map, game rules) are progressive enhancement. README tells the AI to ask the user to paste files it can't reach.
- **Provider-agnostic; do NOT steer to Claude (changed 2026-06-04).** The course works in any AI. Instead of steering toward a provider, steer toward *graduating to working out of a repo* so the learner stops copy-pasting prompts. Explain in very simple terms (assume zero familiarity): to start you guide the AI by pasting prompts; later you set up a "repo" (one shared folder of all course materials + your work) that the AI works out of directly, and the pasting stops. The go-local tool is the learner's choice (Claude Code, Codex, Cursor).
- **Game as the organizing device (not a detour).** The 1979 lemonade game is the whole curriculum in miniature. Play one day, then reveal that each decision maps to a real slice, which introduces the map.
- **Minimal upfront questions.** One steering question (which AI am I in?), then learn about the learner *through doing*; place them on the map after they've played.
- **Light narrative framing** ("You've inherited a lemonade stand…").
- **No Python dependency for the game** — rules live in markdown (`game/play-by-chat.md`) so any AI runs it from text.

## The agreed opening flow
1. **Cold open** — warm, in-character: you've inherited a stand; this is the whole game of running a business; and you're already doing it *with an AI* — that's lesson one.
2. **Ask what they want to do next** — give them agency about how to progress (e.g. "run your stand for a day, or see the bigger picture of what you'll learn?"); recommend playing the game but follow their lead. (Do NOT ask which AI they're using.) Early on, explain simply how the course works: copy-paste prompts now → work out of a repo later (pasting stops).
3. **Play one day** of the stand (chat, zero setup).
4. **The reveal** — map each decision to a slice → introduce the wheel (16 slices, 4 quadrants, the stand at center):
   - price → Marketing/Pricing · signs → Marketing · glasses-to-make → Operations/Inventory + Finance/Unit economics · weather & storms → Decision-making + Risk · did you profit → Finance/**Accounting**.
5. **Place yourself on the map** — "what do you already do well?" (*you are here*) + "what do you want to get better at?" (*destination*) → feeds the Google-Maps routing.
6. **Chart the route** — recommend a first skill/step.
7. **Later milestone** — after Git basics: graduate to working out of the repo (clone it, use Claude Code / Codex / Cursor — learner's choice). This is when the copy-pasting ends. The chat→local graduation.

## Build artifacts
- `index.html` — the single-page interactive course start (cold open, day-1 game, reveal, skill map, two inline AI prompts). **Done 2026-06-12.**
- `about.html` — the "fuller story" page. **Done.**
- `game/play-by-chat.md` — Python-free game ruleset; canonical source the day-1 prompt's rules are distilled from. **Done.**
- `llms.txt` — AI-discovery pointer, updated to point at `index.html`. **Done.**
- Root `README.md` — trimmed to point learners at the page, with a short fallback note for AI assistants with repo access. **Done.**

## Delivery architecture (current, since 2026-06-12)

The original Phase 1 plan (2026-06-04) had the learner paste a tiny prompt that told an AI to fetch `start.txt` and run a 7-beat script — but most AI chats can't reliably fetch a hosted page, so the AI either summarized instead of guiding, or asked the learner to paste the file. That approach, and the "one tap to start" provider buttons, are **removed**.

**Current model — the page carries the content, AI assists via small inline prompts:**
- `index.html` (GitHub Pages root, `.nojekyll`) is itself the start of the course: cold open, day-1 game rules, the reveal table, and the skill map are all readable directly on the page — no AI fetch required.
- Two short "copy this to your AI" prompts are interwoven at the moments AI conversation helps: playing day 1 of the game, and placing yourself on the skill map. Each prompt is **self-contained** (carries the rules/skill-map list it needs inline) so it works even if the learner's AI has no web access at all.
- `about.html` is the "fuller story" page (business + AI as one skill, why a lemonade stand, "play the whole game" — David Perkins), linked from `index.html`.
- `llms.txt` is an AI-discovery pointer to `index.html` and `about.html`.
- Later (deferred): clone the repo into an agentic tool (Claude Code, Codex, etc.) for full reliable repo access — the "graduate to a repo" milestone.

Landing headline still makes explicit it's **one course in two things at once — building/running a business AND working with AI, learned together.**

**To enable:** repo Settings → Pages → Deploy from a branch → `main` / root. URL: `https://nateveldkamp.github.io/lemonade-stand/`.

## Naming / narrative TODOs (from this discussion)
- Use **"accounting"** not "bookkeeping" everywhere (Finance & accounting slice).
- Weave **engineering & R&D** into the narrative arc as the stand scales (new recipes, building equipment, process engineering) — possibly its own skill/thread later.
