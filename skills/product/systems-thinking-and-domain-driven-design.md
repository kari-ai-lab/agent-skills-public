# Skill Name: Systems Thinking and Domain-Driven Design Foundations

## 🎯 Objective

Establishes the foundational mindset that every other product skill in this workspace builds on: product thinking starts from systems thinking (structure over symptoms, trade-offs over "perfect solutions," future-orientation over one-off fixes), and Domain-Driven Design (DDD) is the shared discipline that carries that thinking from product decisions into the technical solution — via a common vocabulary and explicit ownership boundaries — so product and engineering make the same call for the same reasons.

This is not a task skill that produces a single deliverable. It is a lens applied before and during other skills (`strategy/`, `refinement/`, `delivery/`, `platform/`): run it first on any non-trivial problem, then hand its output into whichever downstream skill fits (strategy definition, roadmap refinement, solution/architecture design).

See also `management/system-of-profound-knowledge.md`: Deming's "Appreciation for a System" and "Knowledge of Variation" are this same discipline applied specifically to management practice (performance reviews, targets, reactive policy changes) — use that skill when the decision at hand is about how people or teams are managed, rated, or corrected, rather than about a product/technical solution.

## 👤 Target Persona

Product Manager, Head of Product, Product Director, Solution Architect, Tech Lead — anyone who defines a problem, proposes a solution, or has to translate between "what the business needs" and "what gets built."

## 📥 Inputs Required

- **Problem or opportunity statement**, stated as currently understood (often event-level: "customers are churning," "this feature keeps breaking").
- **History**: prior attempts at solving this, what was tried, what happened. Systems thinking is most useful when a problem is chronic and has a track record, not a one-off.
- **System context**: the actors, teams, systems, and incentives currently touching this problem area.
- **Current domain vocabulary**: terms the business uses, terms engineering uses for the same concepts — including places where they already diverge.
- **Candidate solution boundaries**: which team, service, or bounded context is expected to own the fix.

## 📤 Expected Output

- An **Iceberg analysis** — Events, Patterns, Structure, Mental Models — for the problem, produced before any solution is proposed.
- An explicit **trade-off statement**: what this solution improves, and what it may worsen or constrain elsewhere in the system. There is no perfect solution; name the cost.
- A **causal loop sketch**: the reinforcing and balancing feedback loops driving the pattern, named in words if a diagram isn't practical (e.g. "more X causes less Y, which causes more X" for reinforcing; "more X causes a correction back toward baseline" for balancing).
- A **leverage-point recommendation**, placed on Donella Meadows' hierarchy (parameters → buffers/stocks → delays → feedback-loop strength → information flows → rules → self-organization → goals → paradigm), and why it was chosen over a lower-leverage event-level patch.
- A **ubiquitous language check**: a short glossary of the core domain terms in play, flagging any term where product's meaning and engineering's implementation-level meaning have drifted apart.
- A **bounded context map** for the solution, using the [Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas) fields (name, purpose, strategic classification, domain roles, inbound/outbound communication, ubiquitous language, business decisions, assumptions, verification metrics, open questions) — not just a name and an owner.
- A **modelling-process stage tag**: which of the eight [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process) stages (Understand, Discover, Decompose, Strategize, Connect, Organise, Define, Code) this decision currently sits at, so it's clear whether the work is still product-side alignment or has moved into technical definition.
- A **future-orientation note**: what pattern or structure this decision reinforces going forward, not just whether it resolves today's event — i.e., does it increase future optionality or quietly add to the underlying structure that keeps producing this class of problem.

## 🤖 Core Prompt / Instructions

```text
You are a product and technical advisor grounding a decision in systems thinking and Domain-Driven Design before any solution gets proposed.

Systems thinking is not a diagram technique — it's "a sensitivity to the circular nature of the world" and the recognition that "there are no perfect solutions; the choices we make will have an impact on other parts of the system." Thinking about something as a system means seeing "the entities — the parts, the chunks, the pieces — and the relationships between them," not just isolated events. It also means expecting **emergence**: the patterns the Iceberg surfaces at the Patterns/Structure level often arise from component interactions and cannot be predicted by looking at any single part in isolation — so don't stop analyzing once one contributing part is found.

Follow this sequence:

1. **Climb the Iceberg before proposing anything.**
   - Events: what just happened / what was reported.
   - Patterns: has this happened before, how often, under what conditions.
   - Structure: what organizational, process, or system design produces this pattern.
   - Mental models: what beliefs or incentives sustain that structure.
   Do not let the conversation jump straight from Events to a fix.

2. **Map the system, not just the request.**
   - Name the entities (teams, services, actors) and the relationships between them.
   - Sketch a causal loop: identify at least one **reinforcing loop** (amplifies change, drives runaway growth or decline) and one **balancing loop** (seeks a target, resists change) in play. Most chronic problems persist because a balancing loop is fighting the fix, or a reinforcing loop is being fed.
   - Where the problem is about accumulation over time (backlog, technical debt, churned users, trust), separate the **stock** (the accumulated quantity) from the **flows** (the rates adding to or draining it) — a stock problem is rarely fixed by a one-time flow adjustment.
   - Ask who else is affected by a change here, even indirectly.

3. **State the trade-off explicitly.**
   - Name what improves.
   - Name what gets worse, constrained, or deferred elsewhere in the system as a result.
   - If no trade-off can be named, treat that as a signal the analysis is incomplete, not as a genuinely free win.

4. **Choose a leverage point, not just a patch.**
   - Rank the candidate intervention using Donella Meadows' leverage-point hierarchy, from weakest to strongest: constants/parameters → sizes of buffers and stocks → structure of stocks and flows → length of delays → strength of negative (balancing) feedback loops → gain of positive (reinforcing) feedback loops → structure of information flows (who knows what) → the rules of the system (incentives, constraints) → the power to self-organize/restructure → the system's goals → the mindset/paradigm the system arises from.
   - "A small change could lead to a large shift in behavior" (Meadows) — prefer intervening as high on that hierarchy as the situation actually allows, over a faster, lower-leverage parameter tweak.
   - State explicitly which point on the hierarchy was chosen and why a higher-leverage one either was or wasn't feasible here.

5. **Establish the ubiquitous language.**
   - Write down the core domain terms both product and engineering will use for this problem.
   - Flag any term where the business meaning and the code-level/data-model meaning already disagree — resolve the disagreement before design proceeds, don't paper over it with a translation layer.

6. **Map bounded contexts before the solution is designed.**
   - Fill out a Bounded Context Canvas for each context in play — Name, Purpose, Strategic Classification (core/supporting/generic; revenue-generator/engagement-creator/compliance-enforcer; genesis/custom-built/product/commodity), Domain Roles, Inbound Communication, Outbound Communication, Ubiquitous Language, Business Decisions, Assumptions, Verification Metrics, Open Questions.
   - Flag any place the proposed solution assumes one shared meaning across contexts that actually model the concept differently (a classic source of integration bugs and mid-project rework).
   - Name the actual relationship between contexts using the standard Context Mapping patterns — don't leave it implicit: Partnership, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open-Host Service, Published Language, Separate Ways, or Big Ball of Mud. If the honest answer is Big Ball of Mud, say so — that's a finding, not a failure to classify.
   - If a context's internal model itself is non-trivial (not just its boundary), use an Aggregate Design Canvas to work out entities, value objects, invariants, and the aggregate root before implementation.

7. **Sequence the work using the DDD Starter Modelling Process.**
   - Understand: align to the org's business model, user needs, and short/medium/long-term goals — this and Discover/Decompose/Strategize are primarily product-side.
   - Discover: explore the domain collaboratively (e.g. EventStorming) to build shared understanding of concepts and behaviors.
   - Decompose: break the problem into smaller, loosely-coupled sub-domains.
   - Strategize: identify which sub-domains are core (differentiating) versus supporting or generic.
   - Connect: design the interactions between sub-domains — this and Organise/Define/Code are where product and technical decisions interlock and must be made jointly, not handed off.
   - Organise: structure teams around the context boundaries so ownership matches the model, not the org chart's convenience.
   - Define: make the bounded context's roles and responsibilities explicit before any code is written.
   - Code: implement so the code's structure mirrors the domain model — this is a technical step, but it is downstream of, and constrained by, every product-side step above it.
   - State which stage the current decision is at; don't let a Code-stage question get answered with an Understand-stage level of clarity, or vice versa.

8. **Orient the decision to the future.**
   - State what structural pattern this decision reinforces if repeated, not only whether it resolves the immediate event.
   - Assess whether the domain model/solution boundary chosen increases future optionality (easy to extend, safe to change) or locks in today's shortcut as tomorrow's structural constraint.
   - Check whether the fix addresses the stock (the accumulated problem) or only slows a flow — a flow-only fix looks like progress short-term while the stock keeps building toward the same failure later.

Constraints:
- Do not accept an event-level explanation as the final answer to "why is this happening."
- Do not let product and engineering proceed with different meanings for the same term.
- Do not treat "no trade-offs" as a valid conclusion — surface the trade-off or flag the analysis as incomplete.
- Do not skip straight to Define/Code (technical solution definition) without having actually done Understand/Discover/Decompose/Strategize (product-side domain alignment) — that's the most common way DDD gets reduced to a technical-only exercise disconnected from product intent.
- Every output feeds into a downstream skill (Strategy, Refinement, delivery, or platform/architecture) — end with which skill should run next and what this analysis hands it.
```

## ✅ Success Criteria / Quality Checklist

- [ ] The problem was decomposed through Events → Patterns → Structure → Mental Models before any solution was proposed, and emergence was considered (not stopped at the first contributing part found).
- [ ] The system's entities and relationships (not just the request) are named, with at least one reinforcing and one balancing feedback loop identified.
- [ ] Where the problem is accumulation-based, the stock is separated from its flows, and the fix is checked against the stock, not just a flow.
- [ ] A real trade-off is stated — what improves and what worsens elsewhere.
- [ ] The chosen leverage point is placed on Meadows' hierarchy and justified over a lower-leverage patch.
- [ ] A ubiquitous-language glossary exists and any product/engineering term drift is flagged and resolved.
- [ ] A Bounded Context Canvas exists per context in play, and the relationship between contexts is named as one of the nine standard Context Mapping patterns (not left implicit).
- [ ] Where a context's internal model is non-trivial, an Aggregate Design Canvas backs it up.
- [ ] The decision states which DDD Starter Modelling Process stage it's at, and product-side stages (Understand/Discover/Decompose/Strategize) were actually done before technical stages (Define/Code) were answered.
- [ ] The future-orientation note states what structural pattern the decision reinforces, not just whether it fixes today's event.
- [ ] The output names which downstream skill (Strategy, Refinement, delivery, platform) it feeds and what that skill should do with it.

## Sources

- Systems thinking overview, Iceberg Framework, and "no perfect solutions" framing: [thesystemsthinker.com — Systems Thinking: What, Why, When, Where, and How](https://thesystemsthinker.com/systems-thinking-what-why-when-where-and-how/)
- Systems-as-entities-and-relationships framing ("the cognitive skill of the 21st century" — Edward Crawley): [MIT Open Learning — Ask an MIT Professor: What Is Systems Thinking and Why Is It Important?](https://openlearning.mit.edu/news/ask-mit-professor-what-system-thinking-and-why-it-important)
- Feedback loops (reinforcing/balancing), stocks and flows, emergence, causal loop diagrams, and Donella Meadows' leverage-points hierarchy ("a small change could lead to a large shift in behavior"), plus the field's origins (von Bertalanffy, Forrester, Wiener, Meadows, Senge): [Wikipedia — Systems thinking](https://en.wikipedia.org/wiki/Systems_thinking)
- Domain-Driven Design — ubiquitous language, strategic design, context mapping: [domainlanguage.com — Domain-Driven Design](https://www.domainlanguage.com/ddd/)
- DDD concepts overview, three pillars, tactical patterns, and the nine Context Mapping patterns (Partnership, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open-Host Service, Published Language, Separate Ways, Big Ball of Mud): [Wikipedia — Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
- Practical, fillable templates referenced above: [DDD Crew on GitHub](https://github.com/ddd-crew) — specifically [Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas), [Aggregate Design Canvas](https://github.com/ddd-crew/aggregate-design-canvas), and the [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process)

---

## Metadata

- **Version:** 1.2
- **Last Updated:** 2026-07-24
- **Author:** Workspace Product Skills
