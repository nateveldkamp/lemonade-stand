# Playing the Whole Game — A Teaching Philosophy

This document captures a philosophy of teaching skills: how to take a complex
discipline and make it learnable by playing a "whole game" from the very
beginning. It is written to stand on its own and apply to any domain. The
final section points to how it is being put into practice in this repo, but the
principles do not depend on that instantiation.

## The tree-trunk problem

Most tutorials cover branches and leaves: a particular model, a particular tool,
a particular library, a particular technique. They rarely cover the trunk — how
the work actually gets done, the discovery process that produced the methods, the
story of how a discipline grows from simple to complex. As a result, students
learn to drive specific tools without ever learning to navigate.

The branches and leaves are abundant and easy to find. The trunk is scarce. A
learner who only ever encounters branches accumulates disconnected techniques
with no sense of when, why, or whether to use any of them.

Two analogies guide this philosophy.

### Josh Waitzkin teaching chess

Waitzkin (former child chess prodigy, author of *The Art of Learning*) doesn't
start beginners with rules and opening moves. He clears the board down to three
pieces — a king-and-pawn endgame against a king — and teaches first principles
inside that radically simplified game. Pieces come back gradually. By the time
the full board is restored, the student can derive opening moves from principles
instead of memorizing them.

### David Perkins on "playing the whole game"

In *Making Learning Whole*, Perkins argues we should teach skills the way we
teach baseball: invent a junior version (t-ball), play it immediately, and add
complexity only as the student is ready. Not the way we teach math — sit kids in
a classroom for 12 years memorizing rules and only let them play after they
graduate.

He names the failure modes:
- **Elementitis** — learning the elements of something without the story of how
  it came to be or how the pieces fit together.
- **Abouttitis** — learning *about* something without participating in the
  discovery process that created the knowledge.

Both are rampant across technical education: tutorials drop students straight
into models, equations, or tool features with no context for why the methods
exist or what problems they were invented to solve.

## The principles

These are the goal posts for any course or curriculum built on this philosophy:

- Remember the importance of **play** in skill acquisition.
- Play the **whole game early**.
- Figure out how to create a **junior version** of the game.
- Start with **fundamental principles**, not rules and rote.
- **Add complexity back over time**, not all at once.
- Have students **participate in the discovery process** — don't just hand them
  the answer.
- **Tell the whole story** so context and intuition can develop alongside
  technique.
- **Use a continuous narrative.** A single story, told stage by stage, gives every
  new concept a place to land. Bullet points are forgotten; stories are
  remembered. Story is also a complexity dial — what the business is currently
  doing controls what problems can be motivated next.
- **Use what they already know.** Lead with an analogy to something the learner
  is already fluent in (a spreadsheet, an email thread, a folder of files).
  Bridge from there to the new concept. Then explicitly name where the analogy
  breaks down so the scaffolding doesn't calcify into a permanent
  misunderstanding.
- **Deliver the course through the tools it teaches.** The medium is part of
  the message. A course about modern knowledge work should itself be lived
  inside the tools of modern knowledge work, with the learner experiencing the
  move up the stack — from a chat-style assistant, to a shared workspace, to
  a versioned repository — rather than being told about it. Each interface
  switch is a teaching moment in its own right.
- **Each Skill plays the whole game inside itself.** The whole-game-from-day-one
  principle applies *per Skill*, not just to the course as a whole. The Tier 1
  drill of any Skill is the simplest credible version of that Skill — t-ball
  for Git, t-ball for Planning, t-ball for Data analysis. Complexity is added
  back across tiers within each Skill, the same way it's added back across the
  course as a whole. The curriculum is a skill *tree* precisely because each
  branch grows its own way.

## Designing the junior version

The hardest design problem is the junior version: a simplified form of the game
that is still recognizably the *whole* game, not a disconnected fragment of it.
A good junior version has two properties that off-the-shelf teaching material
usually lacks:

1. **Controllable complexity.** You can dial difficulty up or down to match where
   the student is. If you can't control the game, you can't meet the student
   where they are — you're stuck with whatever difficulty the material happens to
   have.
2. **A continuous storyline.** The same scenario carries through from the
   simplest version to the most advanced, so each new technique arrives as the
   next chapter of one story rather than a paragraph torn from the middle of an
   unrelated book. If you can't control the storyline, you can't control how
   context and intuition accumulate.

When the available material is static and disconnected — as most sample problems,
datasets, and exercises are — the only way to get these two properties is to
**generate the game yourself** from a model you control. Owning the generator
means owning the curriculum: you decide which piece of complexity is introduced
next, and you motivate it with a teaching milestone rather than adding it simply
because you can.

The payoff is that students live through how a discipline came to exist. They
start in t-ball — the simplest tools, the smallest version of the problem,
first-principles reasoning. Each time around the bases, complexity is added back
and a more capable tool is introduced to meet it. By the time a student arrives
at the discipline's advanced techniques, they have re-derived *why* those
techniques exist instead of memorizing that they do.

## The aspirational flywheel

A controllable, story-driven game is also a foundation others can build on, which
creates a flywheel:

- Better teaching material, because the content has narrative and the difficulty
  is tunable.
- More teachers, students, and practitioners using it.
- More contributed material — explanations, walkthroughs, exercises, examples.
- More contributors back to the generator itself, which improves the material
  again.

The aim is for the artifact to become a "machine that builds the machine" — not
just for one course, but for many.

## One instantiation: this repo

This repository applies the philosophy to **teaching modern knowledge work to
non-engineer professionals**. The current acute need is AI fluency — Claude
Code, Git and GitHub, agentic workflows, prompting — so the early cycles weight
heavily toward it. But the broader subject is the full skill stack a modern
knowledge worker depends on: business fundamentals, planning, analytics,
automation, and the AI/system-design skills that increasingly tie them
together. AI is the current frontier of this stack, not the whole of it.

The junior version is a **lemonade stand that grows into a business**. The same
stand carries the learner through every cycle, starting as a card table on a
sidewalk and ending — across many cycles — as a global public company with
manufacturing, software, logistics, and data. At each stage the business
introduces exactly the kind of complexity the cycle is trying to teach, and
nothing more. See [docs/narrative-arc.md](docs/narrative-arc.md) for the canonical
story bible.

The lemonade stand matters not because anyone needs lemonade analytics, but
because it is a low-stakes, infinitely extensible, intuitively familiar
playground. Because the storyline is owned rather than borrowed, its complexity
and direction are fully controllable — exactly the two properties described above
— so the difficulty of the *business* problem and the difficulty of the *skill
being taught* can be tuned independently.

Two further design devices fall out of this philosophy and are first-class in
the repo:

- A **continuous narrative** carries the learner through stages of the business.
  See [docs/narrative-arc.md](docs/narrative-arc.md).
- **Analogies** bridge new concepts to things the audience already knows — most
  importantly, spreadsheets to Git. See [docs/analogies.md](docs/analogies.md).

The sandbox is deliberately a t-ball version at the start. New complexity gets
added back **one piece at a time**, each motivated by a teaching milestone. When
extending it, the question to ask is always: *what teaching story does this
support?* If there isn't one, defer. See the repo's other documentation for the
specifics of the model and how to extend it.
