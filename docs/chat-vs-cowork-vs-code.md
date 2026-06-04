# Claude Chat vs. Claude Cowork vs. Claude Code

Three different ways to work with Claude. Each is appropriate in different contexts. This document explains the differences in plain terms, then makes the case for why **this repo lives in Code + GitHub**, not in Chat or Cowork.

## The simple version

Imagine three different rooms in a workshop:

- **Claude Chat** is your personal desk. You sit down, work on something, get help. When you're done, the work is yours. Nobody else watches over your shoulder, and nothing leaves the desk unless you carry it out by hand.
- **Claude Cowork** is a shared studio. You and your teammates are in the same room. Claude is in there with you. You have shared whiteboards, shared tools, and shared connections to the things your team uses. It's collaborative — but the studio is still the workplace itself. The work *is* in the room.
- **Claude Code** is the factory floor. Everything that happens is recorded. Every change is signed and timestamped. Materials come in through one door, finished goods leave through another, and you can trace any product back to the exact change that produced it. Nothing important is in someone's head or on a sticky note — it's all in the system.

All three are useful. The question is *what kind of work belongs in which room.*

## What each one actually is

### Claude Chat

The web/desktop chat interface at claude.ai. A single user has a conversation with Claude. You can attach files, work iteratively, save snippets — but the artifacts of the conversation (the messages, the files generated) live in a chat history. They're not naturally version-controlled. They're not naturally shareable except as links or copy-pastes. They don't naturally compose with the rest of your tools.

**Best at:** quick lookups, one-off questions, drafting, exploratory thinking, anything where the value is in the answer you get *right now* and you don't need it to be reused, audited, or built upon by others.

### Claude Cowork

A team-oriented workspace product. Multiple people share an environment, with Claude integrated in. Plugins connect to common tools (Slack, Drive, calendar, etc.); skills can be installed; the workspace becomes a place where a team operates together with AI in the loop.

**Best at:** team coordination, real-time collaboration on documents or tasks, shared context across people who already work together, day-to-day operational work that doesn't need to outlive the workspace itself.

### Claude Code

A CLI agent that operates on files in a Git repository. Everything Claude Code touches is a file in your repo. Every change is a Git commit. Every commit is reviewable, attributable, reversible, and inspectable forever. The repo is the artifact, and the repo is portable — it can move between people, teams, machines, companies, and remain identical.

**Best at:** anything that needs to be versioned, reviewed, accumulated, audited, shared across organizational boundaries, or used as input to other systems.

## Why the difference matters

Look at it through three lenses:

### Where the work lives

| | Chat | Cowork | Code |
|---|---|---|---|
| Artifacts stored as | chat history + files | workspace objects | files in a Git repo |
| Survives independent of the platform? | partially | partially | **yes** |
| Portable across teams/companies? | no | limited | **yes** |
| Inspectable by another tool? | limited | limited | **yes** — it's just files |

### How changes are tracked

| | Chat | Cowork | Code |
|---|---|---|---|
| Versioned? | no | platform-dependent | **yes (Git)** |
| Diffable? | no | limited | **yes** |
| Reviewable as a PR? | no | no | **yes** |
| Has an audit trail with who/when/why? | partial | partial | **yes** |
| Can you experiment on a branch without breaking main? | no | no | **yes** |

### How knowledge compounds

| | Chat | Cowork | Code |
|---|---|---|---|
| Does one person's work make the next person's easier? | only if they share manually | within the team | **yes — automatically** |
| Does the asset get better as more people contribute? | no | within the team | **yes** |
| Can it be built upon five years from now? | unlikely | platform-dependent | **yes** |

Chat is a private session. Cowork is a shared session. **Code is a shared, durable, version-controlled artifact.** That difference is the whole point.

## A spreadsheet bridge

For most knowledge workers the closest existing mental model for a "shared, durable, version-controlled artifact" is a heavily-used shared workbook — the team's quarterly model, the company's pricing sheet, the operations dashboard that everyone opens on Monday morning. A Git repository is the next version of that idea, with the things spreadsheets have always lacked bolted on: real history, real diffs, real branching, real review. See [analogies.md](analogies.md) for the full mapping (workbook ↔ repo, tab ↔ file, "Save As v2_FINAL_final" ↔ branch, track-changes ↔ commit log, cell comment ↔ PR review) and — just as importantly — where the analogy breaks.

## Why this training lives in Code + GitHub

Recall the central argument from [vision.md](vision.md): the next wave of AI value depends on closing the **context gap** between software engineering (where everything lives in repos) and the rest of knowledge work (where context lives in heads, emails, decks, SaaS). Knowledge work is shifting from "produce the artifact" to "design the factory that produces artifacts." The factory needs a place to live, a way to be improved over time, and a way for many people to contribute.

A repo gives you exactly that:

- **Versioning** — every change tracked.
- **Diffs** — you can see exactly what changed.
- **Branches** — experiment without breaking the main artifact.
- **Pull-request review** — changes go through structured approval.
- **Audit trail** — every modification has a who, when, and why.
- **Compounding** — every contribution accumulates; nothing falls out when someone leaves the team.

These are the same primitives that made software development scalable across millions of contributors. They are what knowledge work has always needed and rarely had.

A training built in Chat would be private to one user. A training built in Cowork would be private to one workspace. **A training built in Code + GitHub is portable, reviewable, contributable, and lives longer than any individual learner, team, or product cycle.** It can be cloned, forked, mirrored, genericized, translated, branched for a new audience, and folded back into a single canonical source. Each cycle a learner contributes — even just adding their name — becomes part of the asset the next learner inherits.

This repo is, in itself, the first concrete example of what it teaches: a knowledge-work artifact built like software. The lesson begins the moment a learner clones it.

## When to use which (practical guide)

- **Use Chat** for quick personal lookups, drafts, exploratory thinking, one-off help. Anything where the conversation itself is the product.
- **Use Cowork** for live team work, where multiple people need to coordinate with Claude in the loop and the work is operational rather than archival.
- **Use Code** for anything you want to outlive a session — anything that will be reviewed, reused, audited, compounded, or contributed to by others. Anything that *is* an artifact, not just a conversation about one.

For the training you're holding in your hands: it's a Code project, by design.

## The learner's path through these rooms

The course doesn't just explain the difference between the three rooms. It walks the learner through them in a deliberate order, so the difference is *experienced*.

| Phase | Room | What the learner does there |
|---|---|---|
| Pre-Cycle 0 | None — file explorer + browser | Unzip the folder. Read the thin `START_HERE.pdf`. The only ask: open Cowork in a browser. |
| Cycle 0 — Welcome to the stand | **Cowork** | Create a Cowork project, drop the unzipped folder in, read Cycle 0 with Claude already alongside. No CLI, no install. The lowest-friction "Claude is in the room" experience. |
| Cycle 1 — Your name on the stand (first half) | **Cowork** | Read the cycle README. Install VS Code, Git, Python, and Claude Code from inside Cowork's guided steps. Still no terminal-first work. |
| Cycle 1 — Your name on the stand (graduation) | **🛠 Move to the workshop — Cowork → Code** | Open the same folder in Claude Code from the terminal. Same files, same `CLAUDE.md`, same `docs/` — but now versioned, branchable, reviewable. Side-by-side screenshot in the cycle materials. |
| Cycle 1 — Your name on the stand (second half) | **Code** | Make the first real change to a tracked file (`CONTRIBUTORS.md`). Commit, branch, push, open the first PR. |
| Cycle 2 onward | **Code** | Steady state. The workshop the rest of the curriculum lives in. |

The shape is intentional. The learner spends a comfortable amount of time in Cowork before being moved to Code — long enough to like it, short enough to feel the difference. Then they make the move, and the chat-vs-cowork-vs-code distinction stops being abstract.

**Chat is not on the learner's path.** It's the room they probably already know, mentioned in this doc so they can place it relative to the other two. The course starts one room up.
