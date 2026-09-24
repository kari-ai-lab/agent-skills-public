# Context files — how these skills become useful in *your* work

This library is for a product manager's ordinary week: sizing a sprint, refining an epic,
scoring a proposal that landed by escalation, writing the status nobody trusts, deciding what
to say no to. The skills are the method. **This file is about the other half — the facts only
you have — and why that half is where the value actually is.**

Everything below is measured, not asserted: each case pre-registered and graded against an
unaided control. In this repository the three `synthetic` cases are published in [`evals/`](evals/), with the fictional workspaces they use in [`examples/`](examples/). The other cases were built on internal project data and are kept in the private working repository.

## What the evidence says — including where we were wrong

Eight cases, each with symmetric arms — one with the skill, one without, same prompt, same
model, same file access. Assertions written before any output was seen.

| What the case tested | Workspace | Lift over no-skill |
|---|---|---|
| Method only — capacity, status, proposal scoring | none | +10.7 · +11.9 · +13.0 · +13.0 — **fail** |
| Injected team facts | large, many projects; unaided model never looked | **+75.7 — pass** |
| Injected org facts (clinical trials) | large; unaided model never looked | **+85.0 — pass** |
| Injected team facts (synthetic) | small, one file; unaided model found it | 0.0 — **fail** |
| Injected org facts (synthetic, K-12) | small, one file; unaided model found it | +11.9 — **fail** |

We first published the two passes as the headline. Reproducing them on synthetic material
showed they were conditional: **when the context file was easy to find, the unaided model found
it and used it exactly as well as the skill did.** Both arms of the synthetic team case reached
the same answer to the decimal — 12.6 delivery person-days, commit about 15 points.

Three findings survive:

1. **The context file is what changes the answer.** On a byte-identical prompt, adding one page
   of team facts moved the recommended sprint commitment from 21–25 points to about 15, for the
   unaided model and the skill alike. That 30–40% correction is the largest effect we measured,
   and it needed no skill at all.
2. **A skill makes sure the file is read when it is not the obvious thing to look at.** That is
   what the two large-workspace passes actually show. It is real, and narrower than we first
   said: two runs, both in the same workspace.
3. **The skill's one reproducible contribution is refusal.** Declining to scope an unevidenced
   build when a helpful model scopes one anyway. Where it was the only difference between the
   arms it was worth exactly +11.9, twice.

In every case the unaided model already knew the method and the industry. In payments it
produced decline taxonomy, retry caps and SCA variation unprompted; in clinical trials, Part 11
scope and eSource; in K-12, student-data agreements and school-year release constraints. What it
could not know, without being handed a file, was the company.

So the practical advice is simple: **write the context file first.** It is the single highest-
leverage thing in this repository. Put it where your agent will look, and use the skills to
make sure it gets read and to supply the refusals a helpful model will not make on its own.

## What this means for other industries

The daily-use kit is domain-neutral — sprint capacity, epic refinement, RAG status, sprint
goals, WSJF, PRD discovery carry no industry assumptions. The fintech content is concentrated
in `skills/domains/` and `skills/practitioner/`, which are separate from the kit.

**You do not need to rewrite `domains/` for your industry.** General industry knowledge is
already in the model, so writing it down buys nothing. Clinical trials and K-12 education, with
no skill for either, behaved exactly like the payments cases: the model brought the industry,
and a context file describing one company brought everything else.

## Writing a context file

Location: `context/` at the workspace root. `context/team.md` for delivery facts,
`context/domains/<domain>.md` for a product area. Skills declare what they read in a
`Context Consumed` section.

**The test for every sentence: if it would be true for any company in your industry, delete
it.** That single rule is what separates a useful file from a textbook the model already has.

Include, with numbers where you have them:

- **Who actually buys, and who merely uses.** The most commonly misread fact, and the one that
  most changes a verdict.
- **Measured load and multipliers.** "eConsent work runs at 2.4x estimate, six features, six
  surprises" beats any generic risk warning.
- **Your regulatory posture specifically** — not the regulation. Which of your modules are in
  scope, what a change to them costs in days.
- **Calendar constraints.** Freeze windows, lock periods, the months a launch is wasted in.
- **Concentration and veto rights.** Who can block, and how long they take to answer.
- **What you already tried and abandoned, and why.** This is the highest-value section and the
  one people omit. A proposal that re-runs a failed experiment is invisible to any model.

Mark what is measured versus assumed, and date it. A skill reading a stale figure is
confidently wrong in exactly the way an unaided model was — the failure this whole mechanism
exists to prevent.

## The honest limits

- **Small numbers.** Eight cases, two of them the passes that did not reproduce. Treat the three
  findings above as well-supported directions, not settled law.
- **The skill's advantage depends on discoverability.** In a small workspace the unaided model
  found the context itself; in a large one it did not. We have not yet tested the middle ground —
  a realistic workspace where the context file is one directory among many.
- **Method genuinely ties.** Do not expect a skill to out-reason the model. Four cases say it
  will not.
- **Staleness is unsolved.** Nothing here detects a context file that has drifted from reality,
  and a wrong file is worse than no file — both arms will use it confidently. Ownership and a
  refresh cadence are your responsibility.
- **One encouraging sign, not a solution:** every arm that read an example file caught that its
  "last verified" date was in the future — an authoring error, since corrected. Models will
  notice obvious staleness. They will not notice a plausible but outdated number.

## Reproducing any of this

```bash
tools/skill_eval.py status                 # three tiers: good / attention / bad
tools/skill_eval.py status --profile exploratory   # same evidence, your thresholds
tools/skill_eval.py policy                 # weights, thresholds, profiles in force
tools/skill_eval.py new <skill> --case x   # scaffold a case
tools/skill_eval.py lock <skill>__x        # hash the prompt and assertions
tools/skill_eval.py arms <skill>__x        # emit two symmetric prompts to dispatch
tools/skill_eval.py grade <skill>__x       # verify the hash, score 0-100
```

`status` reports three tiers, never a ratio. **Good** = measured, benefit shown. **Attention**
= not known, so go and measure it. **Bad** = measured and it did not clear the bar, so
reposition or retire it. Untested is never folded into failed: they are different states
implying opposite actions, and this library's own status was once misreported as "0/18
passing" when the truth was two proven, one failing and fifteen unmeasured.

Cases are pre-registered and tamper-evident: `grade` voids itself if the prompt or assertions
changed after `lock`. Every claim on this page traces to a pre-registered case, including the
ones that failed; the three `synthetic` cases are published in [`evals/`](evals/), with the fictional workspaces they use in [`examples/`](examples/). The other cases were built on internal project data and are kept in the private working repository.
