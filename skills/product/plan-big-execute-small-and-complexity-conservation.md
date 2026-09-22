---
name: plan-big-execute-small-and-complexity-conservation
description: "Three product-thinking heuristics to check any plan, PRD, or scoping decision against — each one a check against a specific, common failure mode:."
---

# Skill Name: Plan Big, Execute Small, and the Conservation of Complexity

## 🎯 Objective

Three product-thinking heuristics to check any plan, PRD, or scoping decision against — each one a check against a specific, common failure mode:

1. **Plan big, execute small** — a target end-state should be ambitious; the path to it should not be.
2. **Complex products are easy to build; simple products are complex to build** — simplicity is the result of hard editorial work, not a shortcut.
3. **All products carry the same total complexity — the only question is where it lives** (Tesler's Law) — a "simpler" product usually just moved its complexity onto the business/engineering side, or onto the client, not eliminated it.

## 👤 Target Persona

Product Manager, Product Owner, Head of Product — anyone reviewing a plan, a PRD/BRD, or a feature scope and checking whether it's actually well-formed, not just whether it's plausible.

## 📥 Inputs Required

- The target end-state/vision in question (ideally already run through `../strategy/target-state-vision-and-phased-roadmap.md`).
- The proposed first release/phase scope.
- What's being called "simple" in the current design, and what happens to the complexity that a simple surface implies is absent.

## 1. Plan Big, Execute Small

The target end-state should be the ambitious, whole-picture version of what "great" looks like — not hedged down to what feels achievable in the first release. The execution path to it should be the opposite: the smallest slice that gets real client feedback fastest, not the largest chunk a team can justify building at once.

**This is exactly the mechanic `../strategy/target-state-vision-and-phased-roadmap.md` already enforces** — its target end-state (Step 1) is the "big" plan; its guaranteed year-one client-facing delivery (Step 4) and phased 2–3 year roadmap are the "small" execution. Don't re-derive this heuristic separately from that skill; use it directly. The failure mode this principle catches: a vision that's been quietly shrunk to match the first release's scope (small plan, not a big one), or a first release that tries to ship most of the big vision at once (big execution, not a small one) — either failure defeats the pairing.

## 2. Complex Products Are Easy to Build; Simple Products Are Complex to Build

Simplicity on the client-facing surface is not the absence of engineering/product work — it's usually the *result* of more of it, not less. Antoine de Saint-Exupéry's line applies directly, from *Terre des Hommes* (1939), Ch. III: *"It seems that perfection is attained not when there is nothing more to add, but when there is nothing more to take away"* (original French: *"la perfection soit atteinte non quand il n'y a plus rien à ajouter, mais quand il n'y a plus rien à retrancher"*).

**Steve Jobs, in full (as sourced):** *"Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple. But it's worth it in the end because once you get there, you can move mountains."* Source: [Inc.com — "Steve Jobs Said Your Overall Success May Be Tied to This Powerful Thinking Habit"](https://www.inc.com/marcel-schwantes/steve-jobs-said-your-overall-success-may-be-tied-to-this-powerful-thinking-habit.html) (Marcel Schwantes). The quote's ultimate origin is commonly cited as a 1997–98 BusinessWeek interview, which was not independently re-accessed — this Inc.com piece is the source actually verified and cited here.

That same article's framing of what the quote demands in practice is worth carrying forward as four concrete checks, since "simplify it" is otherwise just as vague a directive as "make it good":

1. **Exercise clean thinking.** Before a project/strategy starts, strip away the unnecessary complexity and name the core objective and the essential steps to it — don't let a plan carry detail that isn't load-bearing for the goal.
2. **Focus on top priorities, with unrelenting intent.** This isn't oversimplifying — it's naming what actually matters and allocating resources there, instead of spreading effort thin across everything that could plausibly help.
3. **Provide clarity, not micromanagement.** A team that understands the goal and the essential steps can execute with autonomy; a team drowning in undifferentiated detail can't tell the load-bearing steps from the noise.
4. **Commit to continuous improvement, not a one-time cleanup.** Simplification is not a project with an end date — revisit strategies/processes as the business evolves and keep removing what's no longer load-bearing.

**The practical check:** if a feature or flow looks "simple" in a PRD/FRD, ask what was actually removed to get there, and whether that removal was deliberate editorial work (the hard kind, per checks 1–2 above) or just an unaddressed gap (edge cases not designed for, error handling deferred, a data model that will need rework later). A simple-looking design that skipped Section 8 of `refinement/product-requirements-document-template.md` (Edge & Error Case Scenarios) isn't simple — it's unfinished, and principle 3 below explains where that unaddressed complexity actually went.

## 3. Tesler's Law: Complexity Is Conserved, Not Eliminated

Larry Tesler, working at Xerox PARC, formulated the **Law of Conservation of Complexity**: every process/application has a certain amount of inherent complexity that cannot be designed away — it can only be moved, either onto the system/business side (absorbed by engineering, support, or process) or onto the user/client side (left for them to navigate). Tesler's own view was that designers should invest the extra time to absorb complexity themselves rather than pass the cost on to every user who touches the product afterward — the effort should be paid once, by the team, not repeatedly, by every client.

**This is a direct, named match for the framing that all products carry the same total complexity — the only real question is where it lives.** A product that looks simpler to the client didn't shed complexity; it moved that complexity into the business (more configuration logic, more support load, more engineering edge-case handling, a heavier data model). A product that pushes complexity onto the client (more setup steps, more decisions exposed, more manual configuration) is lighter on the business side for exactly that reason. Neither is free — the decision is *who pays*, not *whether anyone pays*.

**The practical check:** for any "simplification," name explicitly where the complexity that used to live at the surface actually went. If the honest answer is "nowhere, it's just not designed for yet," that's principle 2's failure mode, not a real simplification.

## 📤 Expected Output

- A stated verdict on whether a plan is genuinely "big vision, small execution" or has quietly collapsed one side into the other.
- For any feature/flow described as "simple," an explicit statement of what was removed and whether that removal was deliberate work or an unaddressed gap.
- A named answer to "where did the complexity go" for any simplification claim — business/engineering side, or client side — never "nowhere."

## 🤖 Core Prompt / Instructions

```text
You are reviewing a product plan, PRD, or feature scope against three
heuristics: plan big/execute small, simplicity-as-hard-work, and
Tesler's Law (complexity is conserved, not eliminated).

I will provide the target end-state/vision, the proposed first release
scope, and what's being described as "simple" in the current design.

Produce the result in this order:

1. Check plan-big/execute-small: is the target end-state genuinely
   ambitious (not quietly scaled down to match the first release), and
   is the first release genuinely small (not an attempt to ship most of
   the big vision at once)? If either side has collapsed into the other,
   route back to `../strategy/target-state-vision-and-phased-roadmap.md` to re-separate
   them rather than patching the symptom here.

2. For anything described as "simple," ask what was specifically removed
   to get there. If the answer is a deliberate, considered cut (an
   edge case explicitly deferred with a stated reason, a configuration
   option intentionally not exposed), that's principle 2 done well. If
   the answer is "we haven't gotten to that yet," that's an unfinished
   design wearing simplicity as a costume — route it to
   `refinement/product-requirements-document-template.md` Section 8
   (Edge & Error Case Scenarios) as an open gap, not a completed
   simplification. Check the "clean thinking" behind the simplification
   against Jobs's four practical tests: was the core objective and
   essential-steps-only scope actually named (clean thinking), did
   resources concentrate on the few things that matter rather than
   spreading thin (top priorities), does the team have enough clarity to
   execute without being micromanaged through it (clarity), and is there
   a plan to keep revisiting the simplification as the product evolves
   rather than treating it as done once (continuous improvement)?

3. Apply Tesler's Law explicitly: for the same "simple" surface, name
   where its underlying complexity actually went — more logic/support
   load absorbed by the business, or more steps/decisions pushed onto
   the client. Neither is inherently wrong, but both must be named; "the
   complexity just isn't there anymore" is not an acceptable answer.

4. If complexity was pushed onto the client to keep the business side
   light, check that this was a deliberate trade-off decision, not a
   default that nobody actually chose.

Rules:
- Never accept "it's simple now" without naming what was removed and
  where the underlying complexity went.
- A target end-state that's been scaled down to match the first
  release's actual scope has failed the plan-big/execute-small pairing —
  say so explicitly, don't let it pass as "appropriately scoped."
- Complexity that was "removed" with no stated destination (business
  side or client side) has not actually been removed — it's unaddressed,
  and belongs in the Edge & Error Case Scenarios section, not presented
  as a finished simplification.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The target end-state and the first release are checked as genuinely separate (big vision, small execution), not collapsed into each other.
- [ ] Every claim of "simple" states explicitly what was removed to get there.
- [ ] Every simplification names where the underlying complexity actually went (business/engineering side vs. client side) — never "nowhere."
- [ ] Unaddressed complexity disguised as simplicity is routed to the PRD's Edge & Error Case Scenarios section as an open gap, not accepted as done.
- [ ] A deliberate choice to push complexity onto the client (vs. absorbing it in the business) is confirmed as an actual decision, not a default nobody chose.
- [ ] A simplification claim is checked against all four of Jobs's practical tests (clean thinking, top priorities, clarity, continuous improvement), not just asserted as "simple now."

## Sources

- Larry Tesler's Law of Conservation of Complexity: https://lawsofux.com/teslers-law/
- Antoine de Saint-Exupéry, *Terre des Hommes* (1939) / *Wind, Sand and Stars*, Ch. III: quote verified via Wikiquote.
- Steve Jobs, "Simple can be harder than complex..." (full quote): https://www.inc.com/marcel-schwantes/steve-jobs-said-your-overall-success-may-be-tied-to-this-powerful-thinking-habit.html (the ultimate origin is commonly cited as a 1997–98 BusinessWeek interview, not independently re-accessed; this Inc.com piece — supplied directly by the user — is the source actually cited).

**Not independently sourced — flagged rather than force-cited:** a single canonical named source for "plan big, execute small" as a discrete named principle (it overlaps with IBM Enterprise Design Thinking's iterative framing and Lean Startup's build-measure-learn cycle, but no single origin was confirmed — this workspace's own operationalization of the idea in `../strategy/target-state-vision-and-phased-roadmap.md` is the load-bearing citation instead).

## Related Workspace Skills

- `strategy/target-state-vision-and-phased-roadmap.md` — where "plan big, execute small" is actually operationalized (target end-state + phased roadmap + guaranteed year-one delivery); this skill names the principle, that skill runs it.
- `refinement/product-requirements-document-template.md` Section 8 (Edge & Error Case Scenarios) — where unaddressed complexity disguised as simplicity gets tracked as an open gap.
- `refinement/functional-requirements-document-template.md` — where Tesler's-Law complexity that lands on the business/engineering side gets specified (system logic, data rules, NFRs).
- `product/systems-thinking-and-domain-driven-design.md` — the broader systems-thinking lens this skill's Tesler's-Law reasoning is a specific instance of (trade-offs, no perfect solutions).
- `product/no-silo-product-operating-model.md` — the other foundational product lens in this folder.
- `product/laws-of-ux-decision-and-interaction-cost.md`, `product/laws-of-ux-perception-and-memory.md`, `product/laws-of-ux-gestalt-grouping-principles.md`, `product/laws-of-ux-system-design-heuristics.md` — the four companion `laws-of-ux-*.md` skills from the same lawsofux.com source family, covering interaction cost, perception/memory, visual grouping, and broader system-design heuristics respectively; this skill's Tesler's Law section is the canonical treatment of complexity-conservation specifically and is cross-referenced, not repeated, in `laws-of-ux-system-design-heuristics.md`. That file's Ashby's Law of Requisite Variety (cybernetics, not lawsofux.com) is the underlying mechanism that explains *why* Tesler's Law holds — a system's regulatory capacity can't exceed its own internal variety, so complexity kept off the client surface has to become real system-side variety, not just an appearance of simplicity.

---

## Metadata

- **Version:** 1.3
- **Last Updated:** 2026-09-11
- **Author:** Workspace Product Skills
