---
kind: branch
slug: automation
name: Automation
tagline: Turning recurring work into systems that run themselves.
build_state: stub
skills:
  - slug: automation.spreadsheet-automation
  - slug: automation.document-automation
    name: Document automation
    tagline: Auto-generating documents and reports from data and templates.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 2
  - slug: automation.workflow-automation
    name: Workflow automation
    tagline: Multi-step automation across tools.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 3
  - slug: automation.agentic-workflows
    name: Agentic workflows
    tagline: Recurring tasks done by Claude without being asked each time.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 3
  - slug: automation.skill-engineering
    name: Skill engineering
    tagline: Building reusable Claude skills.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 4
  - slug: automation.eval-design
    name: Eval design
    tagline: Testing AI outputs so automation can be trusted at scale.
    build_state: not-started
    tier_count: 5
    tier_1_stand_stage: 4
---

# Branch: Automation

*Turning recurring work into systems that run themselves.*

This is the branch where the "factory not artifact" idea actually lands. Every Skill here takes something the learner has been doing by hand — a weekly summary, a status update, a forecast — and turns it into something they *build* once and *run* repeatedly.

The audience meets automation at the most familiar entry point: a spreadsheet they already maintain. From there, automation broadens to documents, then to multi-step workflows, then to agentic patterns where Claude does work without being asked each time. By the end of this branch (at high tiers), the learner is engineering reusable Claude skills the same way an engineer engineers reusable libraries.

## Skills in this branch

| Skill | Status | Tier-1 stand stage | What it covers |
|---|---|---|---|
| [Spreadsheet automation](spreadsheet-automation/) | **stub** | 1 — recurring weekend stand | Using Claude to take a recurring spreadsheet task and make it run itself. The factory moment in its most immediate form. |
| Document automation | not started | 2 — family helps out | Auto-generating documents and reports from data and templates. |
| Workflow automation | not started | 3 — multiple locations | Multi-step automation across tools. |
| Agentic workflows | not started | 3–4 | Recurring tasks done by Claude without being asked each time. |
| Skill engineering | not started | 4+ | Building reusable Claude skills. The thing this curriculum's later cycles produce. |
| Eval design | not started | 4+ | Testing AI outputs so automation can be trusted at scale. |

## How this branch relates to the others

Automation is the *culmination* branch — almost every other branch feeds into it at higher tiers. Spreadsheet automation needs **Spreadsheets** + **AI fluency** + (eventually) **Coding**. Workflow automation needs **APIs and integrations**. Agentic workflows need **System design** + **Eval design**. Skill engineering needs **Documentation** (Communication) so that what you build is reusable by others.

The Naval "build the factory" line in [vision.md](../../docs/vision.md) lives here. The transition from doing a task to building the thing that does the task lands inside this branch's first few tiers.

See the [skill tree framework](../../docs/skills.md) and the [roadmap](../../docs/roadmap.md).
