---
name: onboarding-front-door
description: The learner onboarding model — paste the repo link into any AI chat and the README runs the experience. Agreed flow and decisions.
metadata:
  type: project
---

**Agreed 2026-06-04.** Major pivot in how learners get started.

## The model: the repo link IS the onboarding

No more zipped folder + getting-started PDF. The new front door: a learner pastes the **GitHub repo link into any AI chat** (Claude, ChatGPT, Gemini — any provider, any tool) and says something like *"Read this repo and be my guide. Let's begin."* The AI reads the **root README**, which doubles as **instructions the AI follows to run the onboarding**. The repo is self-orchestrating. Only **later** (after Git basics are established) does it prompt the learner to clone locally and move to Claude Code.

## Settled decisions
- **Entry point = root README.** Must be self-sufficient so an AI that fetches only the README can run the whole opening; deeper files (skill map, game rules) are progressive enhancement. README tells the AI to ask the user to paste files it can't reach.
- **Provider-agnostic, soft-steer to Claude.** Works on any provider; recommend Claude for the advanced AI/automation modules (built first) and flag when it's worth switching. Not a wall.
- **Game as the organizing device (not a detour).** The 1979 lemonade game is the whole curriculum in miniature. Play one day, then reveal that each decision maps to a real slice, which introduces the map.
- **Minimal upfront questions.** One steering question (which AI am I in?), then learn about the learner *through doing*; place them on the map after they've played.
- **Light narrative framing** ("You've inherited a lemonade stand…").
- **No Python dependency for the game** — rules live in markdown (`game/play-by-chat.md`) so any AI runs it from text.

## The agreed opening flow
1. **Cold open** — warm, in-character: you've inherited a stand; this is the whole game of running a business; and you're already doing it *with an AI* — that's lesson one.
2. **One steering question** — which AI am I talking to? (soft Claude note if not Claude).
3. **Play one day** of the stand (chat, zero setup).
4. **The reveal** — map each decision to a slice → introduce the wheel (16 slices, 4 quadrants, the stand at center):
   - price → Marketing/Pricing · signs → Marketing · glasses-to-make → Operations/Inventory + Finance/Unit economics · weather & storms → Decision-making + Risk · did you profit → Finance/**Accounting**.
5. **Place yourself on the map** — "what do you already do well?" (*you are here*) + "what do you want to get better at?" (*destination*) → feeds the Google-Maps routing.
6. **Chart the route** — recommend a first skill/step.
7. **Later milestone** — after Git basics: "let's get this on your own machine" → clone → Claude Code (the chat→local graduation).

## Build artifacts
- Rework root `README.md` into the dual-audience front door (human intro + AI-guide instructions encoding the flow; compact game loop inline for self-sufficiency).
- `game/play-by-chat.md` — Python-free game ruleset for any AI to run.
- Move/trim contributor content (currently in README) to a short pointer.
- Later: `llms.txt` for discoverability; update prelude + docs to match.

## Delivery architecture (decided 2026-06-04)

The hard problem isn't kickoff, it's *ongoing* content access: most AI tools can't reliably fetch raw GitHub files, and cached/search results go stale. Resolution — a **staged, browser/mobile-first** model:

- **Phase 1 (long-lived, any AI, browser + mobile):** learner pastes a *tiny* prompt that points to a **GitHub Pages site** (`nateveldkamp.github.io/lemonade-stand`). Pages is a normal indexable website, so browsing/search-capable tools (incl. the Claude/ChatGPT/Gemini mobile apps) reach it far more reliably than raw-file links. Depth lives on the page; copy-paste stays minimal. **Keep learners in the browser/mobile app as long as possible.**
- **Phase 2 (much later, on a computer):** clone the repo into an agentic tool (Claude Code, Codex, etc.) for full reliable repo access. Deferred.
- **Honest caveat:** a tool with web access fully off still can't reach any URL; the tiny prompt then tells the AI to ask the learner to paste the page (one tap from the site). Degrade gracefully.

**Site files added at repo root (GitHub Pages source = root, `.nojekyll`):**
- `index.html` — mobile-friendly landing: "Copy starter prompt" + one-tap "Open in ChatGPT/Claude/Perplexity/Gemini" deep links (deep-link prompt is short and points to start.txt).
- `start.txt` — canonical full AI-guide instructions (beats + game rules + skill map) the prompt points the AI to fetch and follow.
- `llms.txt` — AI-discovery pointer.
- `.nojekyll` — serve files as-is.

**To enable:** repo Settings → Pages → Deploy from a branch → `main` / root. URLs: site `https://nateveldkamp.github.io/lemonade-stand/`, guide `.../start.txt`.

**Duplication note:** the guide content now lives in 3 places (README AI section, `start.txt`, and the inline starter prompt). Consolidate later — `start.txt` is canonical.

## Naming / narrative TODOs (from this discussion)
- Use **"accounting"** not "bookkeeping" everywhere (Finance & accounting slice).
- Weave **engineering & R&D** into the narrative arc as the stand scales (new recipes, building equipment, process engineering) — possibly its own skill/thread later.
