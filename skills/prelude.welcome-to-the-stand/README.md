---
kind: prelude
slug: prelude.welcome-to-the-stand
name: Welcome to the stand
tagline: The one mandatory step. Get oriented, then pick your first Skill from the tree.
build_state: complete
---

# Prelude — Welcome to the stand

You've just inherited a tiny lemonade stand on the corner of your block. A folding table, a pitcher, paper cups, and a hand-drawn sign. You don't know how much it sold last weekend, or how many lemons it'll need next weekend, or even who used to run it. Today is the day you get oriented.

## What this is

The prelude is the welcome. No installs, no terminal, no commits — just you, Claude, and a quick tour of where you are. Plan on 15 to 30 minutes. By the end of it, you'll know what's in the folder, you'll have had your first real interaction with Claude on a real project, and you'll be ready to pick your first Skill from the tree.

This is the only required step in the course. Everything after the prelude is choose-your-own-adventure.

## The room you're in

You're reading this inside **Claude Cowork**. Claude is sitting in the side panel on the right.

Cowork is the easiest room to start in, because there's nothing to install — it's just a tab in your browser. Some Skills (Git, in particular) will later have you graduate to a more powerful room called **Claude Code**, which you'll install when the right Skill calls for it. You don't need to worry about that now. If you're curious, take a look at [docs/chat-vs-cowork-vs-code.md](../../docs/chat-vs-cowork-vs-code.md). Otherwise, keep going.

## Take the tour

Four files to look at, in order. Each one is short — open it, skim it, then come back here.

### 1. The story

Open [docs/narrative-arc.md](../../docs/narrative-arc.md).

This is the trajectory the lemonade stand follows across the whole course — from a card table on a sidewalk all the way to a global public company with manufacturing, software, and data. We're at the very beginning. You don't have to read every stage in detail; just notice that there's a destination, and that the complexity of the business is what motivates the complexity of the Skills you'll learn.

### 2. The roadmap

Open [docs/roadmap.md](../../docs/roadmap.md).

This is your map. The prelude (you, right now) is at the top. Below it, nine *branches* of a skill tree — Foundations, Data, Operations, Customer, Systems, Automation, Communication, People, Strategy. Each branch contains several Skills. Each Skill has its own tiers of difficulty. Most cells are empty on day one; this curriculum is being built deliberately, one Skill at a time. The build state of every Skill is visible on the roadmap.

### 3. The framework

Open [docs/skills.md](../../docs/skills.md).

This is the brief explanation of how the tree works — Branches, Skills, Tiers, Drills. The most important idea: there is **no required order** after the prelude. You can go deep on one Skill (vertical progression) or broad across many Skills at the foundational tier (horizontal progression), or both. The tree is designed to reward either path.

### 4. The stand

Open [lemonade-stand/README.md](../../lemonade-stand/README.md).

This is the business itself. Right now it's an empty room — that's intentional. Your first Skill drill is when you start putting things in it.

## Try Claude on something real

Open the side panel and ask Claude a question that requires it to actually look at the repo. Try this one verbatim:

> Given my background and what I do at work, which Skill from the tree should I probably try first?

You'll need to tell Claude what your background actually is — what you do, what you already know, what you'd like to be better at. Treat this as a real conversation. Claude can read every file in the repo; you can read every file too. Use that.

That conversation is what working with Claude on a real project looks like: not a chat with a clever stranger, but a working session with a collaborator who can read everything you can read.

## When you're ready

Open `docs/roadmap.md` and pick a Skill that looks interesting. The Skills currently with authored overviews (look for **stub** in the build state) are:

- **[Git](../foundations/git/)** (Foundations) — versioned text, first commit, first PR. Smallest possible first change to a real repo.
- **[Spreadsheets](../foundations/spreadsheets/)** (Foundations) — the tool you already half-know, taken to fluent.
- **[Planning](../operations/planning/)** (Operations) — making a one-page plan for next weekend, then comparing it to what happened.
- **[Data management](../data/data-management/)** (Data) — taking scattered records and putting them in one place.
- **[Data analysis](../data/data-analysis/)** (Data) — looking at last weekend's numbers and writing three sentences about what you saw.
- **[Spreadsheet automation](../automation/spreadsheet-automation/)** (Automation) — handing a recurring spreadsheet task to Claude and watching it shrink.

Each Skill's `README.md` describes what its tiers are about and which Tier-1 drill is the entry point. None of the Tier-1 drills themselves are authored yet — the course is mid-build. But the Skills are real, the Skills' overviews are real, and the roadmap will get filled in over time. When a drill you want to do shows up as authored on the roadmap, it's ready.

Welcome to the stand.
