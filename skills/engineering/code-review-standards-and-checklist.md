# Skill Name: Code Review Standards and Checklist

## 🎯 Objective

Closes the second of three declared-but-empty sub-areas in `engineering/`'s own README (Testing Strategy — now closed; Coding Standards & Patterns; **Code Review & Quality**; UI/Frontend Design). Gives a fixed priority order for what a review should check (design and functionality first, style last), a concrete standard for when to approve (does this improve code health, not "is it perfect"), sourced turnaround-time norms, and a collaborative procedure for resolving author/reviewer disagreement — replacing "review the code" with a specific, ordered checklist and a named approval bar.

This is the **human-driven** half of the Code Review pair. Its companion, `agent-driven-code-review-calibration.md`, covers what changes when an AI agent is doing the reviewing (or being reviewed) — the rubber-stamp failure mode, calibrated confidence, and when to route a disagreement to a human rather than letting two agents settle it themselves.

## 👤 Target Persona

Software Engineer or Tech Lead reviewing a change, writing a change that's about to be reviewed, or setting a team's review norms (turnaround expectations, what blocks a merge vs. what's a non-blocking nit).

## 📥 Inputs Required

- **The change under review** (the diff/CL itself), or a description of its scope and intent if the diff isn't directly available.
- **Whether this is a review-the-change request or a set-our-review-norms request** — the checklist below applies to the former; turnaround/escalation guidance applies to the latter.
- **For a disagreement-resolution request**: what the author and reviewer each believe and why, not just "we disagree."

## What to Look For, in Priority Order

Google's own engineering-practices guide gives the reviewer checklist a fixed, non-arbitrary order — check the things most likely to require a real rewrite first, before spending time on things a linter or a second pass could catch:

1. **Design** — "The most important thing to cover in a review is the overall design of the CL." Does this change belong here, does it interact sensibly with the rest of the system, is this the right time to add it.
2. **Functionality** — does the code do what the author intended, and does that intent actually serve the change's users (both end-users and the engineers who'll maintain this later).
3. **Complexity** — is the code more complicated than it needs to be, including complexity added for a speculative future need that hasn't arrived yet (this is the code-level twin of `testing-strategy-and-the-test-pyramid.md`'s coverage-gaming problem: effort spent that doesn't buy real quality).
4. **Tests** — is test coverage present and are the assertions actually meaningful, not just present. Route the depth of this check to `testing-strategy-and-the-test-pyramid.md` rather than re-deriving test-quality judgment here.
5. **Naming** — are identifiers descriptive without being unwieldy.
6. **Comments** — do they explain *why*, not restate what the code already says (line up directly with this workspace's own default no-comments-unless-non-obvious-why rule).
7. **Style** — does it match the language's style guide. **This is the point where the priority ordering starts actively protecting review speed**, not just organizing it (see the next section).
8. **Consistency** — balanced against the style guide when the existing codebase already has an established (if imperfect) local pattern.
9. **Documentation** — do READMEs, reference docs, and related materials need to change alongside behavior.
10. **Every line** — actually read everything assigned, not just the parts that look interesting.
11. **Context** — assess the change against the system it's landing in, not just in isolation.
12. **Good things** — name what's actually well done, not only what needs to change.

## The Approval Standard: Better, Not Perfect

The bar for approval, stated directly: **"reviewers should favor approving a CL once it is in a state where it definitely improves the overall code health"** of the system — even if the CL isn't flawless. The guiding principle is continuous improvement, not a perfection gate: **"there is only better code."** A reviewer who blocks a change purely to chase an ideal implementation, when the change as written is a genuine improvement, is optimizing for the wrong thing — a codebase that never merges anything until it's perfect doesn't actually get healthier faster.

The practical mechanism for this: reserve blocking comments for things that would make the codebase *worse* if merged (a real correctness, security, or maintainability problem), and prefix optional, non-blocking improvements with **"Nit:"** so the author can address them or explicitly decline without a second review round. **Never block a merge on a personal style preference alone** — if it's not in the team's actual style guide, it's a nit, not a blocker.

## Review Turnaround: Speed Is a Team-Level Discipline, Not a Courtesy

Slow reviews are not a minor inconvenience — they compound into a measurable team-productivity cost. The stated standard: **"you should do a code review shortly after it comes in"** when not mid-task, with **one business day** as the outer bound for a first response, ideally by the next morning. The load-bearing distinction is between *response* speed and *total process* speed: **"it's even more important for the individual responses to come quickly than it is for the whole process to happen rapidly."** A reviewer who takes two days to leave the first comment, then responds instantly after that, has still created the delay that matters — the clock that hurts a team runs from "submitted" to "first response," not from "submitted" to "merged."

The stated rationale ties directly back to team-level cost, not individual reviewer convenience: slow reviews delay every feature and fix waiting behind them, slow-responding reviewers who also demand substantial changes generate real author frustration (the same substantive feedback delivered quickly draws far fewer complaints), and slow reviews create pressure to let substandard code through just to stop the wait — degrading exactly the code health the review process exists to protect. The single most load-bearing empirical claim here: **"Most complaints about the code review process are actually resolved by making the process faster."** Review-process friction is very often a speed problem wearing a process-design costume.

## Resolving Author/Reviewer Disagreement

When an author disagrees with a reviewer's comment, the collaborative default is: confirm understanding first ("do I understand what the reviewer is asking for?"), then respond with the actual tradeoff reasoning rather than a bare rebuttal — state why the current approach was chosen, and ask directly whether the reviewer's suggestion serves the same original tradeoffs better, rather than treating it as a personal disagreement. Authors often hold context (about the codebase, the users, prior decisions) the reviewer doesn't have yet — surfacing that context is usually what actually resolves the disagreement, not a louder restatement of either position.

If discussion doesn't produce consensus, escalate against **the Approval Standard above** (does the current state improve code health) rather than letting the CL sit unresolved indefinitely — an unresolved disagreement that stalls a change is itself a cost, and the standard exists precisely to give both sides a shared, non-personal criterion to argue against instead of arguing against each other.

## 🔌 Connector Awareness

- **Standalone (always works):** Applies directly to a diff or change description pasted or described by the user, producing the priority-ordered checklist and an approval/nit/block recommendation from that description alone.
- **Supercharged (if connected):** A code-hosting connector (e.g. GitHub) can supply the actual diff, existing review comment threads, and historical review-turnaround data for the team, rather than requiring the user to describe or paste them.

## 📤 Expected Output

- A review pass ordered Design → Functionality → Complexity → Tests → Naming → Comments → Style → Consistency → Documentation, with style-level findings explicitly prefixed "Nit:" and never presented as blocking on their own.
- An explicit approve/needs-changes verdict against the code-health standard (does this improve the system, not "is this flawless"), not a vague "looks mostly fine."
- For a turnaround-norms question: the one-business-day first-response standard and the rationale for why response speed (not total cycle time) is the metric that matters.
- For a disagreement: a collaborative-tradeoff framing (not a rebuttal) and, if unresolved, an explicit escalation against the code-health standard rather than an indefinite stall.

## 🤖 Core Prompt / Instructions

```text
You are reviewing a code change, or advising on code-review norms/turnaround/
disagreement-handling. Use Google's fixed priority order and the "improves
code health, not perfection" approval standard — not a freeform impression.

I will provide: the diff/change (or its description), and whether this is a
review-the-change request, a set-norms request, or a disagreement-resolution
request.

Produce the result in this order:

1. If reviewing a change, check it in this fixed order and stop re-litigating
   earlier items once later ones are reached: Design, Functionality,
   Complexity, Tests, Naming, Comments, Style, Consistency, Documentation,
   Every Line, Context, Good Things. Findings in the Style/Consistency tier
   are prefixed "Nit:" and never justify blocking on their own.

2. State an explicit verdict: does this change, as written, improve the
   system's overall code health? If yes, favor approval even if it isn't
   perfect — name what a follow-up could still improve, but don't withhold
   approval for that alone. If no (a real correctness, security, or
   maintainability regression), block and name the specific defect, not a
   vague concern.

3. If advising on turnaround: state the one-business-day first-response
   standard, and be explicit that RESPONSE speed (not total review-to-merge
   time) is the metric that actually matters for author trust and team
   throughput.

4. If resolving a disagreement: reframe it as a tradeoff discussion — what
   context might the author have that the reviewer doesn't, and vice versa —
   rather than a rebuttal contest. If unresolved after that, escalate against
   the code-health standard from step 2, not against either party's opinion.

Rules:
- Never block a review on a style preference that isn't in the team's actual
  style guide — that's a nit, not a blocker.
- Never demand perfection before approving a change that genuinely improves
  code health.
- Never treat slow review turnaround as a minor inconvenience — name it as a
  team-throughput cost with a stated standard (one business day) to check
  against.
- Never resolve an author/reviewer disagreement by volume or seniority alone
  — resolve it against the code-health standard.
```

## 📋 Output Template

```markdown
## Code Review — [Change Name/PR#]

### Priority-Ordered Findings
| Tier | Finding | Blocking? |
|---|---|---|
| Design | [finding or "no concerns"] | [Yes/No] |
| Functionality | [finding or "no concerns"] | [Yes/No] |
| Complexity | [finding or "no concerns"] | [Yes/No] |
| Tests | [finding or "no concerns"] | [Yes/No] |
| Naming | [finding or "no concerns"] | [Yes/No] |
| Comments | [finding or "no concerns"] | [Yes/No] |
| Style | [Nit: ...] | No (nits never block) |
| Consistency | [finding or "no concerns"] | [Yes/No] |
| Documentation | [finding or "no concerns"] | [Yes/No] |

### Verdict
**Does this improve overall code health?** [Yes/No — basis]
**Recommendation:** [Approve / Approve with non-blocking nits / Needs changes — blocking reason]

### Good Things Noted
- [specific strong practice worth naming]

### Disagreement Log (if applicable)
**Point of disagreement:** [description]
**Author's context:** [tradeoff reasoning]
**Reviewer's context:** [tradeoff reasoning]
**Resolution:** [Consensus reached — how / Escalated against code-health standard — outcome]
```

## ✅ Success Criteria / Quality Checklist

- [ ] Findings are checked in the stated priority order (Design/Functionality/Complexity/Tests first, Style/Consistency last).
- [ ] Style-tier findings are prefixed "Nit:" and never presented as a blocking reason on their own.
- [ ] The approval verdict is framed as "does this improve code health," never "is this perfect."
- [ ] A turnaround recommendation names the one-business-day first-response standard and distinguishes response speed from total cycle time.
- [ ] A disagreement is framed as a tradeoff discussion (surfacing each side's context) before any escalation, and escalation (if needed) is against the code-health standard, not either party's authority.
- [ ] At least one genuinely positive, specific observation is included, not only critique.

## Sources

- [Google — "What to Look For In a Code Review"](https://google.github.io/eng-practices/review/reviewer/looking-for.html) (`google/eng-practices`) — the twelve-item priority-ordered checklist, and the "Nit:" convention for non-blocking style comments. Verified via live fetch this session.
- [Google — "The Standard of Code Review"](https://google.github.io/eng-practices/review/reviewer/standard.html) — the "improves overall code health," "there is only better code" approval standard. Verified via live fetch this session.
- [Google — "Speed of Code Reviews"](https://google.github.io/eng-practices/review/reviewer/speed.html) — the one-business-day first-response standard, the response-speed-vs-total-speed distinction, and the "most complaints... resolved by making the process faster" finding. Verified via live fetch this session.
- [Google — "How to Handle Reviewer Comments"](https://google.github.io/eng-practices/review/developer/handling-comments.html) (`google/eng-practices`, developer/CL-author guide) — the collaborative disagreement-handling procedure and its escalation pointer back to the Standard of Code Review. Verified via live fetch this session.
- Jason Cohen — *Best Kept Secrets of Peer Code Review* (SmartBear, based on a study of ~2,500 code reviews and 3.2 million lines of code at Cisco) — the diff-size/review-rate findings behind this skill's "small, frequent reviews beat large, infrequent ones" instinct (commonly cited figures: reviews under roughly 200–300 lines of code, at rates under roughly 300 LOC/hour, correlate with materially better defect-detection than larger, faster reviews). **Access note:** the primary PDF (`static1.smartbear.co/.../best-kept-secrets-of-peer-code-review.pdf`) could not be read directly this session — its pages render as scanned/legacy-format images behind an "Adobe Reader required" compatibility notice that both the automated fetch tool and this session's PDF reader could not extract text from. The figures above are drawn from secondary descriptions of the same Cisco study (SmartBear's own webinar page and independent summaries), not independently re-verified against the primary text — flagged honestly rather than presented as directly confirmed, per this workspace's sourcing discipline.

## Related Workspace Skills

- `agent-driven-code-review-calibration.md` — the agent-driven companion: what changes about this checklist and standard when an AI agent is doing the reviewing or being reviewed.
- `testing-strategy-and-the-test-pyramid.md` — owns the depth of the Tests-tier check (coverage quality, test-double correctness); this skill only flags that tests exist and look meaningful, it doesn't re-derive test strategy.
- `coding-standards-and-design-patterns.md` — the Complexity- and Style-tier findings here route to that skill's SOLID/refactoring/code-smell vocabulary for *why* something is too complex, rather than re-deriving it.
- `governance/verification-and-self-checking.md` — the same "don't declare done without evidence" discipline this skill's approval standard specializes for review specifically.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-30
- **Author:** Workspace Engineering Skills
