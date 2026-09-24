# Context files — how these skills become useful in *your* work

This library is for a product manager's ordinary week: sizing a sprint, refining an epic,
scoring a proposal that landed by escalation, writing the status nobody trusts, deciding what
to say no to. The skills are the method. **This file is about the other half — the facts only
you have — and why that half is where the value actually is.**

Everything below is measured, not asserted: each case was pre-registered and graded against
an unaided control. In this public repository the per-case records are kept in the private working repository, because the test material is real internal project data — the method and the harness that produced them are published here.

## The finding that shapes everything here

A modern model is already good at product method, and already knows your industry.

We tested six cases with symmetric arms — one with the skill, one without, same prompt, same
model, same tools. Assertions written before any output was seen.

| What the case tested | Domain | Lift over no-skill |
|---|---|---|
| Method: capacity arithmetic | neutral | +13.0 — **fail** |
| Method: status reporting | neutral | +13.0 — **fail** |
| Method + domain substance | payments | +11.9 — **fail** |
| Injected team facts | neutral | **+75.7 — pass** |
| Injected org facts | clinical trials | **+85.0 — pass** |

In the payments case the unaided control produced decline taxonomy, scheme retry caps, SCA
regional variation, idempotency risk and holdout measurement design — unprompted, all of it.
In the clinical-trials case it produced 21 CFR Part 11 scope analysis, eSource determination,
eConsent amendment states and sponsor protocol confidentiality. It needed no help with either
industry.

**What it could not do, in both cases, was know the company.** It named sponsors as the buyer
for a business that sells to CROs. It costed a sprint with five wrong numbers, every one
optimistic.

So the useful claim is narrow and specific:

> The model brings the method and the industry. You bring your instantiation of it. A context
> file is how you hand it over once instead of re-explaining it every session.

## What this means for other industries

The daily-use kit is domain-neutral — sprint capacity, epic refinement, RAG status, sprint
goals, WSJF, PRD discovery carry no industry assumptions. The fintech content is concentrated
in `skills/domains/` and `skills/practitioner/`, which are separate from the kit.

**You do not need to rewrite `domains/` for your industry.** That was our first assumption and
the evidence contradicts it: general industry knowledge is already in the model, so writing it
down buys nothing. The clinical-trials case scored +85.0 with **no** clinical-trials skill in
the library — only a context file describing one company's position.

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

- **Two data points per side.** The separation is wide and consistent across unrelated
  domains, but it is not many cases. Treat it as a strong signal, not a settled law.
- **Method genuinely ties.** Do not expect a skill to out-reason the model. Four cases say it
  will not.
- **Staleness is unsolved.** Nothing here detects a context file that has drifted from
  reality, and a wrong file is worse than no file. Ownership and a refresh cadence are your
  responsibility; the tooling cannot help yet. This is the largest open risk in the design.
- **One encouraging sign, not a solution:** given a context file that described a *different*
  team, a skill recognised the mismatch and refused to use its numbers — "treat as illustrative
  of the shape of the problem, not as this team's numbers." Detecting misapplied context is not
  the same as detecting stale context.
- **Refusal is real but small.** Skills reliably decline things a helpful model does — scoping
  an unevidenced build, giving a single-point estimate. Measured at roughly 12% of a case:
  genuine, and not enough on its own to justify a skill.

## Reproducing any of this

```bash
tools/skill_eval.py status                 # three tiers: good / attention / bad
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
changed after `lock`. Every claim on this page traces to a pre-registered case, including
the ones that failed; the per-case records are kept in the private working repository, because the test material is real internal project data — the method and the harness that produced them are published here.
