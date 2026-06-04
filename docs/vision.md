# Vision

## What this repo is

A flywheel for retraining and upskilling existing employees (and onboarding new ones) on the full skill stack modern knowledge work depends on — **business fundamentals, planning, analytics, automation, and AI/system-design** — taught through a single continuous story of a lemonade stand that grows from a card table on a sidewalk to a global public company.

It is not a static course. It is a controllable, story-driven, recursive set of "whole game" cycles a learner moves through asynchronously, on their own machine, starting from zero tools installed. The AI fluency that anchors the early cycles (Claude Code, Git, GitHub, agentic workflows) is the current frontier of the stack, not the whole of it — later cycles use those same tools to teach business operations, finance, analytics, planning, and the rest of the work.

The achievement that defines "completing" Cycle 1 of the training is a real merged pull request to this repo. A learner who started with a zipped folder ends as a contributor to the same artifact. That full-circle moment is teased from the first page and tracked along the way.

The continuous narrative and the spreadsheet-to-Git analogy family are first-class design devices. See [narrative-arc.md](narrative-arc.md) and [analogies.md](analogies.md).

## Who it is for

Knowledge workers who need to develop AI and system-design fluency — at any organization, in any role where the work product is a document, a decision, an analysis, or a plan rather than shipped code.

The learner is assumed to start with **zero** background in Claude Code, Git, GitHub, Python, or VS Code. They are, however, assumed to be fluent in the everyday tools of office work — spreadsheets, email, shared folders, slide decks. That existing fluency is leaned on heavily as the on-ramp into less familiar territory (see [analogies.md](analogies.md)).

Getting access, installing the tools, and using them is part of the training, not a prerequisite.

## Why this matters

Software engineering has been reshaped most quickly by AI because code repositories already contain everything an AI needs to do the work: source, tests, configuration, deployment specs, and the version-controlled history of every change and why it was made. The context is structured and reviewable.

This is **not** the case for most other knowledge work. The context lives in people's heads, in emails, in slide decks, in private folders, and in SaaS tools that don't talk to each other. The next wave of AI value depends on closing that gap.

Each time a frontier lab announces a vertical product — "agents for financial services," "agents for legal," "agents for healthcare" — it makes headlines. If you look at what the product actually is, it's a GitHub repo with organized context for a domain. It is surprisingly simple, and surprisingly sparse. A public accounting-journal-entry skill captures generic steps, but a public company has hundreds of accrual entry types. Millions of workflows are still not captured. Some generalize across companies. Many are company-specific. Every organization will still need its own repo to connect generalizable skills to its specific systems, workflows, people, and history.

## What knowledge work becomes

Naval Ravikant described the shift in software engineering this way:

> "You used to ship the output directly, and everything inside the company was, you know, how good is person A at shipping output B? And now what's happening is the way that I'm judging you as an engineer is like, are you producing the factory that will produce multiplicative outputs B through Z, right?"

Knowledge work in all domains will trend the same direction. The deliverable is no longer the accrual entry, the variance analysis, the monthly business review deck, the pricing study, the headcount plan, or the board update. The deliverable is **the factory** — the system that produces those things on demand, at scale, from established context. The work moves from authoring artifacts to designing, maintaining, and improving the systems that produce them.

This is why the best practices and tooling primitives of software engineering will expand to all knowledge work. Git already provides what knowledge artifacts have always needed:

- **Versioning** — every change is tracked.
- **Diffs** — you can see exactly what changed.
- **Branches** — you can experiment without breaking the main artifact.
- **Pull-request-style review** — changes go through structured approval.
- **Audit trails** — every modification has a who, when, and why.

Evaluation suites and feedback loops, originally developed to train frontier models, will increasingly capture, structure, and maintain institutional-knowledge repositories so AI can use them reliably. The discipline that used to belong only to software teams — continuous integration, observability, refactoring, code review — becomes the discipline of every team that does knowledge work.

## How this repo embodies the shift

This repo is itself an example of what it teaches. It is:

- A GitHub repository, not a slide deck or LMS course.
- Version-controlled, with every change reviewable.
- Open to PR-style contribution from the people learning from it.
- Designed to compound over time as cycles, exercises, and curated resources accumulate.

Static training material would go stale within months, because the tools are moving that fast. Treating the training itself as a repo — a living, version-controlled, collaboratively edited system — is the only way to keep up. It is also, deliberately, the first concrete example a learner sees of "the factory."

For the pedagogical foundation, see [teaching-philosophy.md](teaching-philosophy.md). For the architecture, see [plan.md](plan.md). For the story of the lemonade stand as it grows, see [narrative-arc.md](narrative-arc.md). For the canonical analogies the curriculum leans on, see [analogies.md](analogies.md). For why this lives in a repo instead of in Claude Chat or Claude Cowork, see [chat-vs-cowork-vs-code.md](chat-vs-cowork-vs-code.md).
