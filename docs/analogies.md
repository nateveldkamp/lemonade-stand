# Analogies

A core teaching device for this repo is **using what learners already know**. Most of the intended audience is fluent in spreadsheets, email, shared folders, and the daily mechanics of office work. They are not fluent in repos, branches, commits, or agents. Bridging the gap with an analogy — and then showing exactly where the analogy breaks — is faster, stickier, and more honest than starting from definitions.

This document is the canonical analogy reference. When you introduce a new concept in a cycle, **reach for an analogy from this list first** before inventing a new one. If you do invent a new one, add it here.

## How to use an analogy well

Three rules. Cycles that follow them age well. Cycles that skip them produce learners who think they understand and don't.

1. **Lead with the familiar side.** Open with the spreadsheet (or email, or folder) the learner already understands. Make that the concrete anchor.
2. **Bridge to the new concept.** "This thing you already do is a primitive version of *this thing the new tool does*." One sentence is usually enough.
3. **Show where the analogy breaks.** Always. The bridge is scaffolding, not the floor. Without this step, the analogy becomes a permanent misunderstanding the learner has to unlearn later — which is harder than learning it correctly the first time.

A good analogy gets the learner 80% of the way to the right intuition and explicitly names the 20% gap. A bad analogy gets them 100% of the way to a *wrong* intuition.

## The spreadsheet ↔ Git family

This is the most important analogy in the repo. Almost every Git concept has a spreadsheet equivalent the audience already lives with daily.

### Workbook ↔ Repository

| Spreadsheet world | Git world |
|---|---|
| A workbook (`.xlsx` file) | A repository |
| A folder of related workbooks | A repo with multiple files |

**The bridge:** a repo is your workbook of workbooks. Everything related to one project lives in one place.

**Where it breaks:** the repo isn't a single binary file you open in one app. It's a folder of plain-text files that any tool can read. That difference is *why* Git can do diffs, merges, and review — none of which Excel can do on an `.xlsx`.

### Sheet/tab ↔ File

| Spreadsheet world | Git world |
|---|---|
| A tab inside a workbook | A file inside a repo |

**The bridge:** each file in a repo is like a tab in a workbook. Different tabs hold different parts of the project.

**Where it breaks:** files in a repo can be in any format (markdown, code, data, images). Tabs in a workbook are all spreadsheets. Files in a repo can also reference each other in structured ways tabs cannot.

### "Save As `report_v2_FINAL_final.xlsx`" ↔ Branch

| Spreadsheet world | Git world |
|---|---|
| Saving a copy of the file with a new name before making risky changes | Creating a branch |
| The day-of-the-week folder where you keep yesterday's version | A branch from yesterday |
| Ten people each working on their own copy of the file | Ten branches |

**The bridge:** branches solve the problem that everyone has solved badly with filename suffixes for thirty years.

**Where it breaks:** branches are *cheap*, *fast*, and *can be merged back together* without manual copy-paste. Filename copies pile up forever and have to be reconciled by hand. The reason knowledge workers end up with `report_v2_FINAL_final_USE_THIS_ONE.xlsx` is precisely because the spreadsheet world has no merge operation.

### "Track changes" / Excel version history ↔ Commit history

| Spreadsheet world | Git world |
|---|---|
| Word's "Track Changes" | A diff |
| Excel's "Show changes" or sheet version history | The commit log |
| The comment box you typed when you saved | A commit message |

**The bridge:** Git keeps a full record of every change anyone ever made, with who made it, when, and why.

**Where it breaks:** Git's history is permanent, structured, and queryable. Spreadsheet history is best-effort, vendor-locked, and lost the moment you email the file. Also: Git tracks changes to *meaning* (a renamed line, a moved block) better than spreadsheet tools track changes to cells.

### Comments in a shared sheet ↔ Pull request review

| Spreadsheet world | Git world |
|---|---|
| Leaving a comment on a cell asking "should this be `SUM` or `AVERAGE`?" | A line comment on a PR |
| Sending the file with "please review before I share" | Opening a PR |
| Saying "looks good to me, you can publish" in chat | Approving a PR |

**The bridge:** PRs are the structured version of the "can you look at this before I send it" conversation that already happens, except the review is attached to the change itself and lives forever.

**Where it breaks:** PR review is *gating* by default — the change doesn't merge until the review passes. Spreadsheet review is *advisory* — the author can hit Save regardless of what the reviewer said. PR review also catches the exact line that changed automatically; spreadsheet review depends on the reviewer noticing.

### Named ranges / formulas ↔ Variables and functions

| Spreadsheet world | Git world |
|---|---|
| A named range like `Q3_Revenue` | A variable |
| A formula in a cell like `=SUM(Sales!B2:B100)` | A function |
| Building a model by chaining formulas across tabs | Composing functions across files |

**The bridge:** writing code is mostly the same kind of thinking as building a complicated Excel model. Both are about naming things and chaining them together.

**Where it breaks:** code can do things Excel cannot (loops, conditionals beyond `IF`, external data sources, real testing). Code can also be reviewed, versioned, and reused across projects in ways formulas locked inside a workbook cannot.

## Other recurring analogies

These are less central than the spreadsheet ↔ Git family, but they come up across cycles.

### Sticky notes on a monitor ↔ Issue tracker

The disorganized backlog every knowledge worker has — sticky notes, a Notes app, a half-tracked email folder — is a primitive issue tracker. The bridge: issue trackers (GitHub Issues, etc.) are the structured version, with status, assignment, history, and search. Where it breaks: a sticky note doesn't notify anyone; an issue can.

### "Reply-all" ↔ Broadcast notification

Email threads with everyone CC'd are the original broadcast notification. The bridge: chat channels and notifications scale better. Where it breaks: email threads carry deeper context (whole quoted history) than most chat messages; the trade-off is real.

### "Forwarding the email chain" ↔ Sharing context

The thing knowledge workers already do — forward the whole thread so the new person can catch up — is exactly the problem repos solve. The bridge: a repo's history is the always-up-to-date "forwarded chain" for the project. Where it breaks: email threads are linear and time-ordered; repos are structured and topic-ordered.

### Templates in Word/Excel ↔ Reusable code

Every team has a "monthly review template" or a "client proposal template." That habit is the same instinct as reusable code. The bridge: code makes the templating mechanical instead of manual. Where it breaks: code templates can be parameterized and combined; document templates usually can't.

### A binder vs. a search index ↔ Files vs. database

A three-ring binder of printed reports is a "file system": you know where each thing is, but only by remembering where you put it. A search index (or database) lets you find things by what's in them, not where you put them. The bridge: when knowledge-work artifacts move from binders/folders into structured systems, *searchability* is the major gain.

### Recipe / SOP / playbook ↔ Skill or script

A printed checklist or written procedure your team follows is a manual version of what an AI skill or script does automatically. The bridge: codifying the procedure means it runs the same way every time, and someone else can improve it without your involvement. Where it breaks: the procedure stops adapting when the world changes; a human reading a checklist will notice an obvious problem and stop, a script may not.

## Adding new analogies

When you reach for a new analogy in a cycle:

1. Check whether one in this doc already fits. If it does, use it for consistency.
2. If not, draft the new analogy in your PR using the same template:
   - The familiar side (one or two sentences, ideally with a table).
   - The bridge (one sentence).
   - Where it breaks (one or two sentences, explicit).
3. Add it to this doc in the same PR.

Analogies that get reused across cycles belong here. Analogies that work only once for one specific paragraph can live inline in the cycle that uses them — but if you find yourself reaching for them a second time, promote them up.
