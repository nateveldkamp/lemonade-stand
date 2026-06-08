# TODO: strip every em dash from the repo

**Logged 2026-06-08.** Nate's standing preference: never use em dashes (—). They read as AI-generated. This is now recorded in the global `~/.claude/CLAUDE.md`, the project `CLAUDE.md`, and `docs/conventions.md`.

**The cleanup that still needs doing:** every file written/edited in the recent build sessions is full of em dashes and needs a sweep. Replace each `—` with a period, comma, colon, parentheses, or "and"/"but", whatever reads cleanest. Don't mangle the prose; rewrite the sentence if needed.

Scope as of 2026-06-08: **459 em dashes across 49 files** (`rg "—"`). The big ones are docs/ (plan, skills, narrative-arc, teaching-philosophy, open-questions, chat-vs-cowork-vs-code all 20+), the root onboarding files, and CLAUDE.md.

Files known to be heavy on em dashes:
- Root: `README.md`, `start.txt`, `index.html`, `about.html`, `llms.txt`
- `game/play-by-chat.md`
- All 16 skill slice READMEs under `skills/`
- `docs/skills.md`, `docs/roadmap.md`
- `memory/*.md` (these notes too)
- `CLAUDE.md` (the longer prose bullets)

Sweep approach: grep the repo for the em-dash character, go file by file, rewrite in Nate's voice (lowercase, casual, brief, direct). Watch the HTML files: keep them valid, only touch text content.
