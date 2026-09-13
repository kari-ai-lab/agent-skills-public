# Skill Name: Agent Memory Architecture and Consolidation

## 🎯 Objective

Covers **persistent, cross-session** agent memory — facts and preferences an agent should still know tomorrow — which is a different problem from two related concerns: `orchestration/shared-context-and-state-ownership.md` covers ephemeral, mid-workflow context between a live orchestrator and its subagents (gone when the workflow ends); `platform/context-management.md` covers a single Claude Code session's own working-context hygiene (`/compact`, `/clear`, one human operating one agent). This skill is the third, often-missing leg: what an agent remembers *after* the session or workflow that created the memory is over, how that memory is stored safely, who's allowed to write to it, and what happens when two agents' persisted memories disagree.

## 👤 Target Persona

Engineer architecting an agent's long-term memory (preferences, learned facts, episodic recall of past interactions); an orchestrator deciding whether multiple agents may read/write the same persistent memory store.

## 📥 Inputs Required

- What the agent needs to remember across sessions: user preferences, learned facts, or episodic recall of past interactions (they have different storage/retrieval shapes — don't force all three into one mechanism).
- Whether more than one agent will read from or write to the same memory store.
- Sensitivity of the stored content (PII, financial, health, or otherwise regulated data changes the encryption-at-rest and retention requirements).
- Any existing storage already in place (vector DB, relational store, key-value store) this workflow should extend rather than duplicate.

## 📤 Expected Output

- A tiered memory model (working / episodic / semantic-preference), each with its own storage and retrieval mechanism — never a single undifferentiated blob.
- A write policy: exactly one writer of record per memory collection, with every write against a validated schema, not free-form key/value.
- A confidence-and-source field on every stored fact — no persisted "memory" without a traceable origin.
- An encryption-at-rest requirement for sensitive stored content, with retrieval still functioning on encrypted content.
- A forgetting/review policy distinct from an authorization grant's TTL.
- A conflict path for when two agents' persisted memories disagree, routed to `orchestration/conflict-and-consensus-resolution.md` rather than silent overwrite.

## Why Tiered Memory, Not One Big Context Blob

MemGPT's own framing names the underlying constraint directly: LLMs have **"limited context windows, hindering their utility in tasks like extended conversations and document analysis."** Its fix draws explicit inspiration from operating systems — **"hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory"** — so that the system **"intelligently manages different memory tiers in order to effectively provide extended context within the LLM's limited context window."** Applied here: don't try to keep everything an agent has ever learned in its live context (that's `shared-context-and-state-ownership.md`'s problem, and it will lose). Instead, split what's remembered into tiers with different storage and retrieval shapes: **working** (live session context — out of scope here, covered by `platform/context-management.md` and `shared-context-and-state-ownership.md`), **episodic** (past interactions, retrieved by relevance via a vector store when the current context needs them), and **semantic/preference** (structured facts and preferences, retrieved directly by key rather than by similarity search).

## Recommendation (Portable)

- **Episodic memory**: a vector store (Chroma, pgvector, or a managed vector DB) indexed on embeddings of past interaction content, retrieved by semantic similarity to the current query — not a flat log an agent re-reads in full.
- **Semantic/preference memory**: a structured store (relational or document) where every record carries the preference/fact itself **plus a confidence value and a source** — never assert persisted knowledge without a traceable origin. The same fabrication-prohibition rule that applies to any AI-generated numeric or factual claim (never invent, extrapolate, or round a value without a traceable source) applies identically to a "learned" memory fact.
- **Encryption at rest for sensitive content**: encrypt the stored document/fact content, but compute embeddings from the plaintext *before* encryption, so semantic retrieval keeps working without ever storing plaintext sensitive content at rest. This is a generic technique (any authenticated-encryption scheme — Fernet, AES-GCM, or your platform's existing field-encryption helper), not something novel to name after one implementation.
- **Write policy**: exactly one writer of record per memory collection or table (extending `orchestration/shared-context-and-state-ownership.md`'s single-writer rule to the persistent-store case). Every write must validate against a defined schema/allowlist for that agent — an agent should not be able to write an arbitrary free-form key into long-term memory. Any other agent that wants to add or change a memory does so by proposing it through `orchestration/inter-agent-handoff-contract.md` to the writer of record, not by writing directly.
- **Consolidation**: run extraction/consolidation as a periodic or post-interaction background pass, not inline in the critical path of a user-facing response — new memories get merged/deduplicated against existing ones rather than accumulating unbounded near-duplicates.
- **Forgetting/review, not a fixed short TTL**: an agent's authorization-grant TTL discipline (short-lived, minutes-scale, because standing access is the risk) does not transfer to persisted *knowledge* — a true fact doesn't stop being true after 30 minutes. Instead of a fixed expiry, apply a periodic staleness/relevance review (does this preference still reflect current behavior? has this fact been contradicted since?) and prune or re-confirm on that basis. Reusing an authorization TTL for memory content misapplies a security control to a knowledge-quality problem.
- **Multi-agent conflict**: when two agents' persisted memories disagree about the same fact, that is a conflict, not a race to overwrite — route it through `orchestration/conflict-and-consensus-resolution.md`'s independence-check-then-resolve procedure rather than last-write-wins.

## Worked Example

A production implementation of this pattern typically looks like:

- **Episodic**: a ChromaDB (or pgvector) collection with document content **encrypted at rest** (e.g. Fernet/AES) while **embeddings are computed from the plaintext before encryption, so semantic search still works — only the stored document content is opaque.**
- **Semantic/preference**: a per-agent context builder that combines learned preferences (a structured table, each row carrying a confidence value and a source) with categorized facts and episodic memories retrieved from the vector store, returned as one enriched-context object to the calling agent.
- **Write policy**: a background extraction pass runs after each interaction (non-blocking, off the response critical path) and validates every extracted preference against a per-agent allowlist of valid keys — e.g. an email-handling agent may only write `vip_sender`, `ignored_sender`, `summary_style`, `focus_keyword`, nothing else — the concrete implementation of "every write validates against a schema, not free-form key/value."
- **Working-tier boundary**: session-level conversation history gets trimmed/summarized by a separate mechanism — this is the working tier this skill deliberately excludes, already covered by `platform/context-management.md`.

## 🤖 Core Prompt / Instructions

```text
You are designing (or reviewing) an agent's persistent memory. Do not store
everything the agent has ever seen in one undifferentiated blob, and do not
let more than one process write the same memory collection without a
defined owner.

1. SPLIT BY TIER
   - Working (live session context): out of scope here — use
     platform/context-management.md and orchestration/shared-context-and-
     state-ownership.md instead.
   - Episodic (past interactions): store in a vector store, retrieve by
     relevance to the current query, not by re-reading a full log.
   - Semantic/preference (learned facts/preferences): store in a structured
     table/collection, retrieved directly by key.

2. REQUIRE CONFIDENCE + SOURCE ON EVERY STORED FACT
   No record is written to semantic/preference memory without a source
   (where this was learned) and a confidence value. A "memory" with no
   traceable origin is a hallucination risk wearing a persistence layer.

3. ENCRYPT SENSITIVE CONTENT AT REST WITHOUT BREAKING RETRIEVAL
   If stored content is sensitive (PII, financial, health, or otherwise
   regulated), encrypt the document content at rest, but compute the
   embedding from the plaintext BEFORE encryption — this keeps semantic
   search working without ever persisting plaintext sensitive content.

4. ENFORCE A SINGLE WRITER OF RECORD, SCHEMA-VALIDATED
   Exactly one agent/process owns writes to a given memory collection.
   Every write validates against a defined schema or key allowlist for
   that writer — reject or flag a write that doesn't match. Any other
   agent proposing a memory change does so through orchestration/inter-
   agent-handoff-contract.md to the writer of record, never by writing
   directly.

5. CONSOLIDATE, DON'T ACCUMULATE
   Run extraction/consolidation as a background pass (not inline in a
   user-facing response path), merging new observations against existing
   records rather than piling up near-duplicates.

6. REVIEW FOR STALENESS — DO NOT REUSE AN AUTHORIZATION TTL
   Persisted knowledge decays by relevance/contradiction, not by a fixed
   short clock. Do not apply an agent-authorization grant's minutes-scale
   TTL to memory content — that TTL protects against standing unauthorized
   access, a different risk than a fact going stale. Apply a periodic
   staleness/relevance review instead.

7. ROUTE MULTI-AGENT DISAGREEMENT TO CONFLICT RESOLUTION
   If two agents' persisted memories disagree about the same fact, do not
   silently overwrite. Run orchestration/conflict-and-consensus-
   resolution.md's independence check and resolution procedure, and log
   the disagreement per that skill's requirements.

Now design memory for:
Agent(s): $AGENTS
What must be remembered across sessions: $MEMORY_CONTENT
Sensitivity: $SENSITIVITY_LEVEL
Shared across how many agents: $SHARED_WRITERS
```

## ✅ Success Criteria / Quality Checklist

- [ ] Working, episodic, and semantic/preference memory are stored and retrieved through distinct mechanisms, not one undifferentiated blob.
- [ ] Every semantic/preference record carries a confidence value and a source.
- [ ] Sensitive stored content is encrypted at rest, with embeddings computed from plaintext before encryption so retrieval still works.
- [ ] Exactly one writer of record exists per memory collection, and every write validates against a defined schema/allowlist.
- [ ] Consolidation runs as a background pass, not inline in the user-facing critical path, and deduplicates against existing records.
- [ ] A staleness/relevance review policy exists for memory content, distinct from and never conflated with an authorization grant's TTL.
- [ ] Multi-agent disagreement about a persisted fact routes through `orchestration/conflict-and-consensus-resolution.md`, never silent last-write-wins.

## Sources

- [Sun, Chen, Zhu, et al. — "MemGPT: Towards LLMs as Operating Systems"](https://arxiv.org/abs/2310.08560) (arXiv 2310.08560) — the OS-inspired hierarchical/tiered memory framing and its "extended context within the LLM's limited context window" objective. The fetched abstract did not itself name specific tier labels (e.g. "main context" vs. "archival storage") or the exact eviction/paging decision rule, so this skill's tier names and write/consolidation mechanics beyond the OS-paging analogy are original design, not a verbatim restatement of MemGPT's internal architecture.

## Related Workspace Skills

- `orchestration/shared-context-and-state-ownership.md` — the ephemeral, mid-workflow counterpart to this skill's persistent, cross-session scope; its single-writer rule is extended here to persistent memory collections.
- `platform/context-management.md` — owns single-session working-context hygiene, explicitly out of scope for this skill's tiered model.
- `orchestration/conflict-and-consensus-resolution.md` — the required path when two agents' persisted memories disagree, rather than a silent overwrite.
- `orchestration/inter-agent-handoff-contract.md` — the only sanctioned channel for a non-owning agent to propose a memory change to the writer of record.
- `domains/agent-zero-trust-delegation.md` — source of the TTL discipline this skill explicitly declines to reuse for memory content, naming why the two risk shapes differ.
- `governance/privacy-law-awareness-for-product-development.md` — the applicable regime-triage skill when persisted memory contains regulated personal data.
- `orchestration/harness-selection-and-mapping.md` — a harness decision governs execution, not persistent memory; the two are complementary, not substitutes for each other.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-09-09
- **Author:** Workspace Orchestration Skills
