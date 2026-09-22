---
name: team-of-teams-organizational-adaptability
description: "Captures General Stanley McChrystal's \"Team of Teams\" model — four pillars."
---

# Skill Name: Team of Teams — Organizational Adaptability Under Complexity

## 🎯 Objective

Captures General Stanley McChrystal's "Team of Teams" model — four pillars (Trust, Common Purpose, Shared Consciousness, Empowered Execution) that let an organization keep a large hierarchy's scale and resources while gaining a small team's speed and adaptability. **This is a distinct lens from this folder's Deming-grounded core, not a replacement for it.** `system-of-profound-knowledge.md` diagnoses whether a specific management *practice* is sound (targets, ratings, reaction to variation); this skill diagnoses whether the organization's *structure itself* can move information and decisions fast enough to survive a complex, networked, fast-changing environment. Run both — they answer different questions.

## 👤 Target Persona

Executive, Head of Product/Engineering, Program/Portfolio Lead — anyone assessing whether an organization's actual structure (not just its individual practices) can adapt fast enough against a complex, fast-changing competitive or operational environment.

## 📥 Inputs Required

- Current organizational structure: how decisions and information actually flow today (centralized command-and-control vs. distributed).
- Evidence for each of the four pillars — not assumptions: is there a measurable basis for trust, a stated common purpose beyond task lists, actual breadth of information-sharing, and genuine team-level autonomy?
- The specific complexity/speed problem the organization is failing to keep pace with (a competitor, a market shift, an operational surprise) — this model is a response to a specific *kind* of environment, not a universal replacement for hierarchy.

## Origin (as sourced)

General Stanley McChrystal commanded Joint Special Operations Command (JSOC) from 2003 to 2008, during which his organization was credited with the operation that eliminated Abu Musab al-Zarqawi, the leader of al-Qaeda in Iraq — a case of a rigid, hierarchical command structure learning to counter a decentralized, networked adversary by restructuring itself to operate like one. *Team of Teams: New Rules of Engagement for a Complex World* (McChrystal, with Tantum Collins, David Silverman, and Chris Fussell) generalizes that experience into an organizational model. As McChrystal Group's own framing states: **"Organizations cannot solve 21st-century problems with 20th-century solutions. Technology and human behaviors have transformed dramatically, but organizations have not kept up."**

## The Four Pillars (as sourced, verbatim from McChrystal Group)

1. **Trust** — "faith in the benevolence, competence, and integrity of a teammate." Enables the psychological safety needed for innovation and idea-sharing; without it, information doesn't actually flow regardless of what the org chart says.
2. **Common Purpose** — meaning beyond individual tasks; helping people feel "part of something bigger than themselves," sustaining engagement past what task-completion alone provides.
3. **Shared Consciousness** — universal access to the information necessary for success, and a genuine culture of organizational learning — not information hoarded by rank or function.
4. **Empowered Execution** — supporting teams to shape their own work and environment, breeding engagement and accountability, without micromanagement from above.

**Implementation approach:** a "hybrid, teaming-based model" built through increased speed, inclusion, and transparency in communication — paired with deliberate cultural and leadership-behavior change. A structural reorg alone, without the trust/purpose/consciousness/execution shift, does not produce this model.

## 📤 Expected Output

- A present/partial/missing assessment against each of the four pillars, each backed by a named mechanism as evidence, not an assumed cultural claim.
- An explicit statement of whether the organization's actual environment is complex/networked/fast-changing enough to need this model — or whether a traditional hierarchy remains adequate for a simpler, more predictable environment it's currently facing.
- A structural gap list distinguishing itself clearly from a Deming-style practice audit: this is about whether information and decision authority can move fast enough, not whether a specific policy or target is well-designed.

## 🤖 Core Prompt / Instructions

```text
You are assessing whether an organization's actual structure — not just
its individual management practices — can adapt fast enough to a
complex, networked, fast-changing environment, using McChrystal's Team of
Teams model.

I will provide the current decision/information-flow structure, evidence
(or its absence) for each of the four pillars, and the specific
complexity/speed problem the organization is up against.

Produce the result in this order:

1. First confirm the model actually fits the situation: is the
   environment genuinely complex/networked/fast-changing (a networked
   competitor, a fast-moving market, operational surprises the hierarchy
   can't process quickly enough), or would a traditional hierarchy still
   serve a simpler, more predictable environment perfectly well? Team of
   Teams is a response to a specific kind of complexity — don't recommend
   restructuring an organization that doesn't actually face it.

2. Assess Trust: is there evidence people actually raise problems, share
   half-formed ideas, and rely on teammates' competence across team
   boundaries — or is trust assumed because no one has complained?

3. Assess Common Purpose: can people articulate what the larger mission
   is beyond their own task list, and does it actually motivate them, or
   is it a slogan repeated without changing behavior?

4. Assess Shared Consciousness: does information actually reach the
   people who need it to act, regardless of rank/function, or is it
   siloed and only shared on a need-to-know basis that turns out to
   under-share in practice?

5. Assess Empowered Execution: can teams actually shape their own work
   and respond to what they observe, or does every non-trivial decision
   require escalation up a hierarchy that can't move as fast as the
   environment changes?

6. Name the specific structural gap(s) found — which pillar is weakest,
   and what change (not just a values statement) would close it.

7. Cross-reference `product/no-silo-product-operating-model.md`'s
   lateral-coupling principle where relevant — an ongoing product
   presence through the SDLC rather than a spec handoff is a concrete,
   product-specific instance of Shared Consciousness and Empowered
   Execution, not a separate concept.

Rules:
- Never assess a pillar as present based on an assumption or a values
  statement alone — require a named, observable mechanism.
- Always check environment-fit first — this model is not a universal
  replacement for hierarchy, and recommending it for an environment that
  doesn't need it is itself a mistake.
- Distinguish this assessment clearly from a Deming-style practice audit
  (`system-of-profound-knowledge.md`) — this is about structural
  adaptability, not whether any single practice/policy is well-designed.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The environment is confirmed as genuinely complex/networked/fast-changing before recommending this model, not assumed by default.
- [ ] Each of the four pillars is assessed against a named, observable mechanism — not an assumed cultural claim or a values statement.
- [ ] The weakest pillar is named explicitly, with a structural change (not a slogan) proposed to close it.
- [ ] This assessment is kept distinct from a Deming-style management-practice audit — structure/adaptability vs. practice soundness are not conflated.
- [ ] Overlap with `product/no-silo-product-operating-model.md`'s lateral-coupling principle is named where relevant, not re-derived from scratch.

## Sources

- McChrystal Group — Team of Teams: https://www.mcchrystalgroup.com/about/team-of-teams
- Wikipedia — Stanley A. McChrystal (confirms JSOC command 2003–2008 and the operation credited with eliminating Abu Musab al-Zarqawi): https://en.wikipedia.org/wiki/Stanley_A._McChrystal

**Not independently sourced today:** the book's own narrative detail (*Team of Teams: New Rules of Engagement for a Complex World*, McChrystal with Tantum Collins, David Silverman, and Chris Fussell) — no dedicated Wikipedia page exists for the book itself; enrich with a direct citation to the book if/when available.

## Related Workspace Skills

- `system-of-profound-knowledge.md` — the Deming-grounded companion lens in this folder; audits practice soundness, where this skill audits structural adaptability.
- `product/no-silo-product-operating-model.md` — its lateral-coupling principle is a concrete, product-specific instance of Shared Consciousness and Empowered Execution.
- `delivery/README.md`'s Agile Manifesto root canon — Agile and Team of Teams both reject rigid, siloed hierarchy in favor of fast-adapting, autonomous units; the overlap is real, not coincidental.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-07-27
- **Author:** Workspace Management Skills
