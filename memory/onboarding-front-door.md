---
name: onboarding-front-door
description: The learner onboarding model — paste the repo link into any AI chat and the README runs the experience. Agreed flow and decisions.
metadata:
  type: project
---

**Agreed 2026-06-04, story-first landing 2026-06-12.** Major pivot in how learners get started, then the landing rebuilt as a story that doubles as the first lesson.

## STATUS / how to resume (last worked 2026-06-12)

**2026-06-12, story-first landing (current).** `index.html` was rebuilt as a story that doubles as the first lesson, written in Nate's public voice (`~/.claude/voice.md`). It opens with the teaching philosophy as narrative (Josh Waitzkin clearing the chessboard to three pieces; David Perkins' "play the whole game" / t-ball / elementitis + abouttitis; why play works; the 1979 lemonade game's real history; the payoff that the game's three questions are the three chess pieces; then "the new piece on the board," an AI). It then hands the interactive part to the learner's own AI through two copy-paste prompts: (1) play one day of the stand, (2) the reveal (map each decision to a real skill, then show the skill map). The "one tap to start" provider buttons are removed; plain copy-paste only.

`start.txt` stays the canonical AI guide (the full 7-beat flow + game rules). The page's launch prompt points the AI to it and tells the AI to skip the cold open and jump to playing a day, so the page and the guide don't repeat each other.

**Note on an earlier same-day redesign that was superseded.** A parallel redesign (commit `f6cd8c1`) deleted `start.txt` and inlined the cold open, game rules, reveal table, and skill map directly into `index.html`, on the reasoning that most AI chats can't reliably fetch a hosted file. Nate chose the story-first version instead and restored `start.txt`; the fetch-reliability concern is handled by the prompts' "if you can't open the link, tell me and I'll paste it in" fallback. `README.md` and `llms.txt` from that redesign were kept (they just point at the page).

**PENDING (do these to resume / test):**
1. **Enable GitHub Pages** (one-time, only Nate can): repo Settings → Pages → Deploy from a branch → `main` / root → Save. Until then the github.io URLs 404.
2. **Test pass:** open `index.html` on a phone and a computer, read it top to bottom, copy both prompts into an AI chat, and confirm the AI plays a day and delivers the reveal + map via `start.txt`.
3. **Trim `start.txt` beat 1** so the AI doesn't re-run the cold open / why now that the page delivers that.
4. **Em dashes** still live in `README.md` and `llms.txt` (from the `f6cd8c1` redesign); they're tracked in `em-dash-cleanup-todo.md`.

This onboarding thread is separate from the **curriculum skill rebuild** (see `skill-map-current-state-and-resume.md`, where skills are still empty, being rebuilt level by level, L0 proposal pending).

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
- `index.html`: story-first interactive landing (the philosophy narrative, then two copy-paste prompts that hand play + reveal to the learner's AI via `start.txt`). **Done 2026-06-12.**
- `start.txt`: canonical AI guide (7-beat flow + game rules). Restored after the `f6cd8c1` redesign deleted it.
- `about.html`: the "fuller story" page. **Done.**
- `game/play-by-chat.md`: Python-free game ruleset; canonical source the game rules are distilled from. **Done.**
- `llms.txt`: AI-discovery pointer to the page. **Done.**
- Root `README.md`: points learners at the page, with a short fallback note for AI assistants with repo access. **Done.**

## Delivery architecture (current, since 2026-06-12)

**Current model: the page tells the story, the AI runs the play.**
- `index.html` (GitHub Pages root, `.nojekyll`) is a story-first landing that doubles as lesson one. It carries the teaching-philosophy narrative and the game's history as readable content, then hands the interactive beats to the learner's own AI.
- Two copy-paste prompts do the handoff: (1) play one day of the stand, (2) the reveal (map the decisions to skills, then show the skill map). Both point the AI to `start.txt` for the beat-by-beat flow and the game rules, with a "paste it in if you can't open the link" fallback for AIs that can't fetch a URL. Provider buttons were removed; plain copy-paste only.
- `start.txt` is the canonical AI guide and stays the single source for the flow + rules (`game/play-by-chat.md` is the Python-free rules it aligns with).
- `about.html` is the "fuller story" page (business + AI as one skill, why a lemonade stand, "play the whole game," David Perkins), linked from `index.html`.
- `llms.txt` and `README.md` point learners and AI assistants at the page.
- Later (deferred): clone the repo into an agentic tool (Claude Code, Codex, etc.) for full reliable repo access, the "graduate to a repo" milestone.

Landing headline still makes explicit it's one course in two things at once: building/running a business AND working with AI, learned together.

**To enable:** repo Settings → Pages → Deploy from a branch → `main` / root. URL: `https://nateveldkamp.github.io/lemonade-stand/`.

## Naming / narrative TODOs (from this discussion)
- Use **"accounting"** not "bookkeeping" everywhere (Finance & accounting slice).
- Weave **engineering & R&D** into the narrative arc as the stand scales (new recipes, building equipment, process engineering) — possibly its own skill/thread later.
