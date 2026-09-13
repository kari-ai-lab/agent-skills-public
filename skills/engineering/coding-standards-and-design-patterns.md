# Skill Name: Coding Standards and Design Patterns

## 🎯 Objective

Closes the third of three declared-but-empty sub-areas in `engineering/`'s own README (Testing Strategy and Code Review & Quality — now closed; **Coding Standards & Patterns**; UI/Frontend Design). Gives the five SOLID principles precisely defined (not just named), refactoring framed as a disciplined, named-catalog activity rather than unstructured "cleanup," and code smells positioned as the actual trigger for refactoring — a surface indicator worth investigating, not a synonym for "bad code" or an aesthetic complaint.

This skill is explicitly **implementation-level**: it governs how a single class, function, or module is shaped once a design decision has already been made. It is not a substitute for `product/systems-thinking-and-domain-driven-design.md`, which governs the **architecture-level** question of how a whole system is decomposed into bounded contexts before any single class gets written — that skill decides where a boundary goes; this one decides whether the code inside a boundary is well-shaped.

This is the **human-driven** half of the Coding Standards pair. Its companion, `agent-driven-code-generation-discipline.md`, covers what changes when an AI agent is the one writing the code — premature abstraction, scope creep, and comment discipline as agent-specific failure modes, not general advice restated for AI.

## 👤 Target Persona

Software Engineer or Tech Lead deciding whether a piece of code violates a SOLID principle, whether a refactoring is actually warranted (and which named refactoring fits), or whether something flagged as a "code smell" is worth acting on.

## 📥 Inputs Required

- **The code in question**, or a description of its structure, if a SOLID-violation or code-smell judgment is being requested.
- **What prompted the question** — a review comment, a recurring bug, difficulty adding a feature, or a general "does this need refactoring" check. The trigger matters: refactoring justified by a real symptom is different from refactoring for its own sake.
- **The scope boundary already in place**, if this work sits inside a bounded context already defined by `product/systems-thinking-and-domain-driven-design.md` — this skill doesn't re-derive or move that boundary.

## SOLID: Five Principles, Precisely Defined

"SOLID" gets invoked constantly and defined precisely far less often. Robert C. Martin introduced the underlying principles in a 2000 paper on software rot; Michael Feathers coined the SOLID acronym around 2004. Each principle below is stated in its original, precise form — not a loose paraphrase — with the concrete violation/fix shape that actually makes it checkable:

- **Single Responsibility Principle (SRP)** — "There should never be more than one reason for a class to change." *Violation shape:* a class that handles both business logic and, say, how that logic gets persisted or formatted — two unrelated stakeholders (a product change and a storage-format change) can now each force an edit to the same class. *Fix shape:* split the class along those separate reasons-to-change, one class per responsibility.
- **Open–Closed Principle (OCP)** — "Software entities should be open for extension, but closed for modification." *Violation shape:* adding a new case requires editing an existing, already-tested function's internals (e.g. a growing `if/else` chain keyed on a type). *Fix shape:* structure the code so a new case is added via a new unit (a new subclass, a new registered handler) rather than a change to existing, working code.
- **Liskov Substitution Principle (LSP)** — "Functions that use pointers or references to base classes must be able to use pointers or references of derived classes without knowing it." *Violation shape:* a subclass that overrides a method to throw, weaken a guarantee, or otherwise behave in a way callers of the base type didn't expect — code written against the base type breaks when handed the subclass. *Fix shape:* a subclass must honor every contract the base type promised, not just match its method signatures.
- **Interface Segregation Principle (ISP)** — "Clients should not be forced to depend upon interface methods that they do not use." *Violation shape:* a single fat interface that forces every implementer to stub out methods it has no real use for. *Fix shape:* split the interface into smaller, role-specific ones so a client depends only on what it actually calls.
- **Dependency Inversion Principle (DIP)** — "One should depend upon abstractions, not concretes." *Violation shape:* a high-level policy class directly instantiating and calling a specific low-level implementation (a specific database driver, a specific HTTP client), coupling the policy to that detail. *Fix shape:* both sides depend on a shared abstraction (an interface), and the concrete implementation is supplied from outside, not reached for internally.

SOLID is a set of pressure-relief principles for a specific pain (code that's hard to change safely as requirements evolve) — apply each one because a specific violation shape is genuinely present, not as a checklist to satisfy for its own sake. A class with exactly one responsibility that will never plausibly need a second implementation doesn't need an abstraction layer bolted on in the name of DIP; see the agent-driven companion's premature-abstraction warning for the failure mode this over-application risk turns into for AI-generated code specifically.

## Design for the Human Reader First

Every principle above (naming, interfaces, comments, refactoring for clarity) ultimately serves one audience: the person who has to read this code next, not the machine that executes it. Google's own API standards state this directly, and the reasoning generalizes past API design to code structure generally: **"Users of your API are unable to dig into the implementation to understand the API better; often, the API surface definition and its corresponding documentation will be the only things a user has. Therefore, it is important that documentation be as clear, complete, and unambiguous as possible."** The same is true of a function signature, a class name, or an interface inside a codebase — the engineer who calls it six months from now, or the reviewer checking it today, usually can't (or won't) dig into the implementation before deciding whether it does what its name and shape claim. The name, the signature, and the comment ARE the interface, in the same sense an API's surface is its interface — get those wrong and the correct implementation underneath doesn't save the reader.

This reframes several of the principles above from stylistic preferences into the same discipline AIP-192 states for API documentation:

- **ISP's "clients should not be forced to depend upon methods they do not use"** is a human-readability rule as much as a coupling rule — a fat interface is harder for the next human to reason about, not just more tightly coupled in the dependency graph.
- **Naming (per the refactoring catalog above)** is the single highest-leverage readability investment available: AIP-192's own guidance that comments should be written assuming **"many readers will not be native English speakers"** and should **"avoid jargon, slang, complex metaphors, pop culture references"** applies just as directly to identifier names as to API comments — a clever or idiom-heavy name is a readability tax paid by every future reader, not a demonstration of cleverness worth keeping.
- **A code smell's "surface indication"** framing (below) is itself a human-legibility concept — a smell is *sniffable* precisely because a human reader, not a machine, is the one doing the noticing.

The practical rule this yields: when a naming, interface-shape, or comment decision is genuinely close, resolve it in favor of what a new human reader — not just a compiler or a test suite — would find clearest, since that reader, like an API's external consumer, frequently has nothing else to go on but the surface itself.

## Code Smells: The Trigger, Not the Verdict

Martin Fowler's own framing is the load-bearing distinction here: **"A code smell is a surface indication that usually corresponds to a deeper problem in the system."** Critically, a smell is not automatically a defect — **"smells don't always indicate a problem... they are often an indicator of a problem rather than the problem themselves."** A smell is meant to be **quick to spot** ("sniffable") precisely so it can prompt investigation without requiring a deep read first; the investigation, not the smell itself, is what determines whether refactoring is actually warranted.

Two concrete, commonly-recognized examples, in Fowler's own framing: a **long method** ("my nose twitches if I see more than a dozen lines") is a smell worth a second look, not an automatic violation — some long methods are genuinely simple, linear, and fine as-is. A **data class** (all data, no behavior) is a particularly useful smell because it prompts a real question — does behavior that currently lives elsewhere actually belong on this class — that often leads to a meaningful refactor, not because a data class is inherently wrong.

**The discipline this enforces:** refactor because a named smell pointed at a real, investigated problem — recurring difficulty extending the code, a bug pattern traceable to the structure, or a genuine SOLID violation with the concrete shape described above — never because code merely *looks* unpolished. "This looks messy" is not yet a reason to refactor; "this class now has two independent reasons to change, and that's already caused two unrelated bugs to collide in the same file" is.

## Refactoring as a Named-Catalog Activity

Refactoring is not generic "cleanup" — it's a disciplined activity with a documented catalog of specific, named transformations, each with a defined mechanism and a defined effect. Martin Fowler's catalog (`refactoring.com`, built for *Refactoring*, 2nd Edition) organizes these under groups including Basic, Encapsulation, Moving Features, Organizing Data, Simplify Conditional Logic, Dealing with Inheritance, and Inline/Extract/Rename/Split-Phase operations. A short list of the most load-bearing, everyday refactorings:

- **Extract Function** — isolate a section of code into its own named, callable unit, so the extracted behavior can be read, tested, and reused independently.
- **Rename Variable** (and Rename Function) — replace a vague identifier with one that actually states its purpose; this alone often removes the need for a comment explaining what the code does.
- **Inline Function** — the reverse of Extract: fold a function's body back into its call site when the function no longer earns its own name (adds an indirection layer without adding real clarity).
- **Extract Variable** (formerly "Introduce Explaining Variable") — name a complex sub-expression so the calling code reads as a statement of intent rather than a puzzle to parse.
- **Change Function Declaration** — deliberately restructure a function's parameters/name for a clearer interface, rather than accumulating awkward parameters over time.
- **Replace Conditional with Polymorphism** — when a conditional is repeatedly branching on the same type/kind across a codebase, move that branching into the type system itself (matches the Open-Closed Principle's fix shape above directly).

Naming the specific refactoring being applied — not just "cleaned this up" — keeps a refactor reviewable: a reviewer checking `code-review-standards-and-checklist.md`'s Complexity tier can evaluate "did this Extract Function actually reduce complexity" far more precisely than "did this general cleanup help."

## 🔌 Connector Awareness

- **Standalone (always works):** Applies directly to code pasted or described by the user, producing a SOLID-violation check, a code-smell investigation, or a named-refactoring recommendation from that description alone.
- **Supercharged (if connected):** A static-analysis/linter connector can supply an objective smell inventory (cyclomatic complexity, method length, class coupling) instead of the user describing suspected problem areas from memory.

## 📤 Expected Output

- A SOLID assessment naming the specific principle and violation shape (never a bare "this violates SOLID" without saying which principle and how).
- A code-smell judgment that distinguishes "this is worth investigating" from "this is confirmed a problem, refactor it" — never treating the presence of a smell alone as sufficient justification.
- A refactoring recommendation naming the specific, catalog-named transformation to apply, not a vague "clean this up."
- An explicit note when the actual question is architecture-level (context boundaries) rather than implementation-level, redirecting to `product/systems-thinking-and-domain-driven-design.md`.

## 🤖 Core Prompt / Instructions

```text
You are assessing code against SOLID principles, code smells, and named
refactorings — implementation-level structure, not system architecture. If
the actual question is about how a whole system is decomposed into bounded
contexts, redirect to product/systems-thinking-and-domain-driven-design.md
instead of answering it here.

I will provide: the code or its description, and what prompted the question
(a review comment, a recurring bug, a general structure check).

Produce the result in this order:

1. If assessing a SOLID concern, name the SPECIFIC principle (SRP/OCP/LSP/
   ISP/DIP) and state the exact violation shape present — never a generic
   "this could be more SOLID." If no real violation shape is present, say so
   rather than inventing one to justify a change.

2. If a code smell is in play, name it explicitly (long method, data class,
   or another named smell) and treat it as an investigation trigger, not an
   automatic verdict — state what the investigation actually found before
   recommending action. A smell with no confirmed underlying problem is not
   grounds for a refactor.

3. If refactoring is warranted, name the SPECIFIC catalog refactoring being
   applied (Extract Function, Rename Variable, Inline Function, Extract
   Variable, Change Function Declaration, Replace Conditional with
   Polymorphism, or another named one) — never "cleaned this up" without
   naming the transformation.

4. Apply each SOLID principle only where its specific violation shape is
   genuinely present — do not recommend an abstraction (interfaces, dependency
   injection, a new class hierarchy) in the name of a principle when the
   simpler, current code has no real symptom the principle would fix.

5. For any close naming, interface-shape, or comment call, resolve it in
   favor of what the next human reader would find clearest — per AIP-192's
   own reasoning, the name/signature/comment is often the ONLY thing that
   reader has, the same way an API's surface and docs are often the only
   thing an external API consumer has.

Rules:
- Never call something a SOLID violation without naming the specific
  principle and its concrete violation shape.
- Never treat a code smell's mere presence as sufficient justification to
  refactor — investigate first, then decide.
- Never recommend a refactor without naming the specific catalog
  transformation being applied.
- Never answer an architecture/bounded-context question here — redirect to
  the DDD skill instead.
```

## 📋 Output Template

```markdown
## Code Structure Assessment — [File/Class/Function Name]

### SOLID Check (if applicable)
**Principle:** [SRP / OCP / LSP / ISP / DIP]
**Violation shape present?** [Yes — describe / No]
**Recommendation:** [Specific fix, or "no change needed"]

### Code Smell Check (if applicable)
**Smell identified:** [name, e.g. Long Method, Data Class]
**Investigation finding:** [what the deeper look actually found]
**Verdict:** [Confirmed problem — refactor / Smell present, no real issue — leave as-is]

### Refactoring Recommendation (if applicable)
**Named refactoring:** [e.g. Extract Function]
**Before/after shape:** [brief description of the transformation]
**Reason:** [the specific SOLID violation or investigated smell this addresses]

### Scope Note
[If this is actually an architecture/bounded-context question: "Redirect to product/systems-thinking-and-domain-driven-design.md — this skill is implementation-level only."]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Any SOLID claim names the specific principle and its concrete violation shape, never a generic "this could be more SOLID."
- [ ] A code smell is treated as an investigation trigger, with the investigation's actual finding stated before any refactor is recommended.
- [ ] Any refactoring recommendation names the specific catalog transformation (Extract Function, Rename Variable, etc.), not a vague "cleaned up."
- [ ] No abstraction is recommended in the name of a SOLID principle without a genuinely present violation shape behind it.
- [ ] An architecture/bounded-context question is redirected to the DDD skill rather than answered at the implementation level.
- [ ] A close naming/interface/comment call is resolved in favor of the next human reader's clarity, not just what a compiler or test suite accepts.

## Sources

- [Wikipedia — "SOLID"](https://en.wikipedia.org/wiki/SOLID) — the five principles' precise definitions, Robert C. Martin's 2000 paper origin, and Michael Feathers' ~2004 acronym coinage. Verified via live fetch this session.
- [Martin Fowler — "CodeSmell"](https://martinfowler.com/bliki/CodeSmell.html) — the surface-indicator definition, the "smells don't always indicate a problem" distinction, and the long-method/data-class examples. Verified via live fetch this session.
- [Martin Fowler — Refactoring Catalog](https://refactoring.com/catalog/) — the catalog's category groups and the specific named refactorings (Extract Function, Rename Variable, Inline Function, Extract Variable, Change Function Declaration, Replace Conditional with Polymorphism) used in this skill's load-bearing list. Verified via live fetch this session.
- [Google — AIP-192: Documentation](https://google.aip.dev/192) (Google's API Improvement Proposals, already this workspace's root-canon source for `platform/api-builder.md` and the `recipes/api-builder-*` family) — the "documentation... will be the only things a user has," write-for-non-native-English-readers, and avoid-jargon/slang/idiom guidance behind this skill's Design for the Human Reader First section. Verified directly this session (the automated fetch tool returned a nav-only shell for several adjacent AIP pages; this one was read in full via the in-app browser).

## Related Workspace Skills

- `agent-driven-code-generation-discipline.md` — the agent-driven companion: premature abstraction, scope discipline, and comment discipline as agent-specific failure modes when generating code against these same standards.
- `product/systems-thinking-and-domain-driven-design.md` — the architecture-level counterpart: decides where a bounded context boundary goes; this skill decides whether the code inside one is well-shaped. Never re-derive one skill's scope inside the other.
- `code-review-standards-and-checklist.md` — this skill's SOLID/smell/refactoring vocabulary is what the Complexity tier of that skill's review checklist should be grounded in, rather than a vague "this feels complex" judgment.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
