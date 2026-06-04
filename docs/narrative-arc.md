# The narrative arc

The lemonade stand is not just a recurring example. It is a **business that grows** across the curriculum, and the curriculum grows with it. Each cycle drops the learner into a new stage of that business and teaches the knowledge-work skills that stage demands.

This document is the story bible. Cycles reference it. Contributors extend it. When in doubt about where a new exercise belongs, find the stage that motivates it.

## Why narrative

Knowledge work is hard to teach abstractly. People remember stories; they forget bullet points. A continuous storyline gives every new concept a place to land: not "here is a thing called variance analysis," but "the stand now has three locations and the numbers don't match — here is how to figure out why."

The story is also the **complexity dial**. By controlling which stage of the business the learner is in, we control which problems are realistic to introduce. You can't credibly motivate a "weekly stand report" agent for a kid with a card table. You can credibly motivate it the moment there are four locations and a parent who wants visibility.

See [teaching-philosophy.md](teaching-philosophy.md), especially the "junior version" and "continuous storyline" sections, for the philosophical grounding.

## Voice and point of view

**Default voice:** second person. *You* started the stand. *You* are figuring out what's broken. As the business grows past what one person can do (around Cycle 3), the narrative widens to a small cast — but the learner remains the owner/operator making the decisions. See open question [#8 in open-questions.md](open-questions.md) for the live discussion.

**Tense:** present. The stand is happening now, not as a case study from the past.

**Tone:** warm, observational, occasionally wry. Never cute. The business is real to the learner.

## The arc

Stages are sized so that each one motivates roughly one cycle's worth of new complexity. Later stages are intentionally sparse — they exist so the destination is visible from day one, not because we've built them yet. See open question [#7](open-questions.md) for the live discussion on how far to commit.

### Stage 0 — The card table (pre-business)

A kid with a folding table, a pitcher, paper cups, and a hand-drawn sign. No employees, no books, no plans. Decisions are made in the moment. Inventory is "however many lemons mom bought."

**New complexity introduced:** none. This is the t-ball baseline — the simplest possible "business."

**Skills relevant here:** the **Prelude** (Welcome to the stand) sits at this stage. The Tier-1 entry point of **Git** (in the Foundations branch) — *Your name on the stand* — also lands here. The learner's *interface* mirrors this stage: just as the stand starts simple, the learner starts in Cowork — no install, no terminal — and graduates to Claude Code inside the Git Tier-1 drill. The stand and the learner level up together.

### Stage 1 — The recurring weekend stand

The stand runs every weekend. You start tracking what you sold, how much you spent, and what the weather was like — initially on a single sheet of paper, then in a spreadsheet. The first real planning happens here: deciding how many lemons to buy for next weekend.

**New complexity introduced:** repeated operations, basic record-keeping, the first forecast, the first "what should we change next time?" feedback loop.

**Skills relevant here:** Tier-1 entry points for **Spreadsheets**, **Data management**, **Data analysis**, **Planning**, **Spreadsheet automation**, and (less centrally) **Writing**, **Customer understanding**, **Pricing**, **Finance and accounting**. Most of the curriculum's foundational drills live at this stage — it's where a recurring business problem first motivates each Skill.

### Stage 2 — Family helps out

A sibling, a parent, or a friend starts helping at the stand. Now there is a *team*, however small. Suddenly you need a shared way to remember things — what's in inventory, who's working which weekend, what last week's sales were. The spreadsheet stops being yours; it has to be everyone's.

**New complexity introduced:** shared context, handoffs, the first time something falls through the cracks because two people each thought the other was doing it. This is also where the **Excel-to-Git migration** lands most naturally — see [analogies.md](analogies.md).

**Skills relevant here:** Tier-2/3 of **Data management** (the **Out of the spreadsheet** milestone — `.xlsx` records migrating into the repo as `.csv` — lives here), Tier-2+ of **Spreadsheet automation** (the first report generator — the factory moment), Tier-2 of **Process design**, Tier-1 of **Coding**, **Collaboration**, **Feedback**, **Document automation**, and **Documentation**.

### Stage 3 — Multiple locations

A second weekend stand opens across town. Then a third. You can't physically be at all of them. You need numbers from each, you need to compare them, and you need to make decisions about where to invest more lemons next week.

**New complexity introduced:** comparison across units, aggregation, the first real analytics question ("which location is doing better, and why?"), the first real automation question ("who is going to pull these numbers every Sunday — or what is?").

**Skills relevant here:** Tier-3+ of **Spreadsheet automation**, Tier-1 of **Workflow automation**, Tier-1 of **Agentic workflows**, Tier-1 of **APIs and integrations**, Tier-3 of **Stakeholder updates**, Tier-1 of **System design**.

### Stage 4 — Wholesale and the first hire

You start selling lemonade to a local coffee shop in bulk. The shop pays on net-30 terms. You hire your first non-family employee for the weekend stands. There are now contracts to remember, payroll to run, and the first month where money goes out before it comes in.

**New complexity introduced:** B2B vs. B2C, accounts receivable, payroll, cash-flow timing, the first compliance touch points (sales tax, employer identification).

**Skills relevant here:** Tier-1 of **Sales** (the first B2B contract), Tier-1 of **Coaching and management** and **Hiring** (the first non-family employee), Tier-1 of **Strategy**, Tier-2+ of **Finance and accounting**, **Risk and compliance**, **Pricing** (now with two pricing models — retail and wholesale).

### Stage 5 — Product lines

You launch a second flavor. Then a sparkling version. Then a "stand kit" that other people can buy. The single product becomes a portfolio, and "how is the lemonade business doing?" stops having one answer.

**New complexity introduced:** SKU management, segment-level P&L, marketing as a discipline (not just a sign), the first real conflict between products competing for the same shelf space.

**Cycle alignment:** later cycles, TBD.

### Stage 6 — Regional company

A handful of stands becomes a small chain. You have a tiny back office. There is a person whose only job is operations, another whose only job is finance, and you spend most of your time deciding what *not* to do. Hiring, firing, vendor management, real estate, and the first leadership team meetings happen here.

**New complexity introduced:** functional org structure, delegation, the first time a decision is made without your direct input, "the business runs without you in the room."

**Cycle alignment:** later cycles, TBD.

### Stage 7 — Manufacturing and supply chain

You start producing bottled lemonade in a small facility and shipping it. Now there is real inventory, real logistics, real quality control, real food-safety regulation, and a fundamentally different cost structure. Software starts to matter as more than a spreadsheet — there are systems of record.

**New complexity introduced:** physical operations at scale, multi-step supply chains, regulatory complexity, the first ERP-like system, the first real data engineering problem.

**Cycle alignment:** later cycles, TBD.

### Stage 8 — National brand

The product is on shelves in stores across the country. There is a sales org, a marketing org, a finance org, a people org, a tech org, and a legal team on retainer. Decisions are made through processes, not in the moment.

**New complexity introduced:** organizational scale, process design, internal politics, the planning calendar, the first acquisitions, the first time the org chart is itself a designed artifact.

**Cycle alignment:** later cycles, TBD.

### Stage 9 — Global, public, multi-segment

International operations. Public-company reporting. Multiple business segments. Manufacturing, software, data, and services. Quarterly earnings, board governance, investor relations, regulatory filings across jurisdictions.

**New complexity introduced:** everything a Fortune-500 leader actually deals with. This stage is sparse on purpose. It exists so the learner sees the trajectory; we will only ever build cycles here when a teaching milestone demands it.

**Cycle alignment:** outline only.

## How to use this document

**For cycle authors:**
- Open every cycle with a one-paragraph story beat anchored in the relevant stage.
- Don't invent new stages in the middle of a cycle. If the story you need isn't here yet, propose an extension to this doc in the same PR.
- The complexity introduced in your cycle must be motivated by something in its stage. If you have to reach down to a later stage to motivate it, the cycle probably belongs later in the curriculum.

**For contributors more broadly:**
- This is a living document. Stages can split, merge, or get renamed as we learn what teaches well.
- Treat the "later stages, TBD" sections as scaffolding. They are not promises. They are seats reserved for future work.

For the canonical analogies that bridge each stage to skills the audience already has (Excel → Git, sticky notes → tickets, etc.), see [analogies.md](analogies.md).
