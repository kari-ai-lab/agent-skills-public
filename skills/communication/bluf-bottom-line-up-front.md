---
name: bluf-bottom-line-up-front
description: "Use when writing any email, memo or status update that needs a reader to know something or act: puts the conclusion, the required action and the deadline in the first line, with supporting context after."
---

# Skill Name: BLUF (Bottom Line Up Front)

## 🎯 Objective

Structures the opening of any message, email, memo, or status update so the reader gets the conclusion, the required action, and the deadline before any supporting context — a sentence-to-paragraph-level discipline that `communication/bookend-communication-structure.md` already assumes ("lead with the headline finding... BLUF") but never defined on its own. This skill is that definition: how to actually write a BLUF line, distinguished from an executive summary or abstract by being blunter and shorter — closer to a thesis statement than a synopsis.

## 👤 Target Persona

Anyone writing an email, Slack message, status update, memo, or the opening of a longer document where the reader may be time-constrained, skimming, or need to act on the message without reading the rest of it.

## 📥 Inputs Required

- **The core message or finding** being communicated.
- **The required action**, if any — what the reader needs to do.
- **The deadline or timing**, if the action is time-bound.
- **The five Ws context** (who, what, where, when, why) available to support the bottom line, for use in the body/follow-up, not the BLUF line itself.

**Minimum viable input:** the fact to convey and who reads it. A full draft is not required — BLUF applies to the opening, so it can be written before the body exists. If there is genuinely no deadline, write "no deadline" explicitly rather than omitting the line; a missing deadline reads as an oversight, a stated absence reads as a decision.

## 📤 Expected Output

- A single BLUF statement (labeled `BLUF:` or structurally equivalent) placed as the very first line of the message, stating what needs to be known, what needs to be done, and when — before any narrative, background, or scene-setting.
- Supporting context, background, and the five-Ws detail following the BLUF line, in descending order of importance (mirroring journalism's inverted pyramid).

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- If the message reports initiative or milestone health → `rag-status-reporting.md` for the status line itself.
- If it announces a delay, re-sequence or scope change → `roadmap-change-communication.md`.
- If it names risks the reader must act on → `roam-risk-communication.md` so each ends with an owner.

## 🤖 Core Prompt / Instructions

```text
You are structuring a message so its bottom line comes first, not last.

1. FIND THE ACTUAL BOTTOM LINE.
   Ask: if the reader only reads one sentence, what must that sentence say?
   It is the conclusion, decision, or request — never the setup, background,
   or how you got there. If you can't state it in one or two sentences, you
   haven't found it yet; keep compressing.

2. WRITE THE BLUF LINE FIRST, AS THE FIRST LINE OF THE MESSAGE.
   State explicitly, in this order:
   a. What needs to be known (the finding, status, or fact).
   b. What needs to be done (the specific action requested, if any).
   c. When it needs to be done (the deadline, if time-bound).
   Label it if the format allows ("BLUF:") — the label itself signals to the
   reader that everything they need is right there, and trains recipients
   over time to expect and rely on the pattern.

3. DO NOT BURY THE LEDE.
   Reject any draft that builds up to the point through narrative
   background, chronological retelling, or a "let me walk you through how we
   got here" structure before stating the conclusion. That structure is the
   exact failure mode BLUF exists to prevent — this is the same anti-pattern
   `bookend-communication-structure.md` flags as "slow build" writing.

4. PUT EVERYTHING ELSE AFTER, IN DESCENDING ORDER OF IMPORTANCE.
   After the BLUF line, provide supporting context, the five Ws (who, what,
   where, when, why), background, and methodology — mirroring journalism's
   inverted pyramid, where a reader can stop at any point and still have the
   most important information already in hand. Do not require the reader to
   finish the message to understand the bottom line; the BLUF line already
   gave it to them.

5. DISTINGUISH BLUF FROM AN EXECUTIVE SUMMARY OR ABSTRACT.
   A BLUF line is blunter and shorter than either — closer to a thesis
   statement. An executive summary can run several sentences or a short
   paragraph recapping multiple points; a BLUF line is one to two sentences
   naming the single most important conclusion and action. If the draft BLUF
   line is doing the job of a summary (recapping several findings), compress
   it further to the single most decision-relevant one and move the rest to
   the body.

6. MATCH TO HIGH-STAKES / TIME-CONSTRAINED CONTEXTS ESPECIALLY.
   BLUF matters most where miscommunication is costly or the reader is
   time-constrained: incident updates, approval requests, status reports to
   leadership, handoffs (e.g. clinical/operational handoffs where an unclear
   handoff is a documented source of downstream errors), and any message
   competing for a busy reader's attention. Apply the discipline by default
   in these contexts, not just when explicitly asked to "be more concise."

7. VALIDATION PASS.
   Read only the first line of the drafted message in isolation. If a reader
   who stopped there would not know what happened, what's being asked of
   them, and by when (where applicable), the BLUF line has failed — fix it
   before polishing anything else in the message.

Now apply this to the message:
Core message/finding: $CORE_MESSAGE
Required action (if any): $REQUIRED_ACTION
Deadline/timing (if any): $DEADLINE
Supporting context/five Ws for the body: $SUPPORTING_CONTEXT
```

## ✅ Success Criteria / Quality Checklist

- [ ] The very first line states what needs to be known, what needs to be done, and when — before any background or narrative.
- [ ] The BLUF line is one to two sentences, not a multi-sentence executive-summary-style recap.
- [ ] A reader who stops after the first line still knows the conclusion and any required action/deadline.
- [ ] Supporting detail (five Ws, background, methodology) follows in descending order of importance, not scattered ahead of the bottom line.
- [ ] No "slow build" structure remains where the point is only revealed at the end.
- [ ] For high-stakes or time-constrained contexts (incidents, approvals, handoffs, leadership updates), the BLUF discipline was applied by default, not only on request.

## Sources

- [The Persimmon Group — "BLUF: How These 4 Letters Simplify Communication"](https://thepersimmongroup.com/bluf-how-these-4-letters-simplify-communication/) — the military-leadership origin, the three-part structure (what needs to be known / done / when), the "state it immediately, then support it" example format, organizational-adoption tips (label email templates, train leadership, recognize good examples), and the cited cost of poor communication (Grammarly/Harris Poll: ~$12,500 lost per employee; the 47%-higher-shareholder-return figure for effective-communication organizations).
- [Wikipedia — BLUF (communication)](https://en.wikipedia.org/wiki/BLUF_(communication)) — the formal military origin in U.S. Army Regulation 25-50 ("main point at the beginning of the correspondence"), Defense Secretary Jim Mattis's 2017 reinforcement of the standard for Congressional correspondence, the explicit distinction from an executive summary/abstract (BLUF is blunter, shorter, closer to a thesis statement), the parallel to journalism's inverted pyramid, and applications beyond military use (healthcare handoffs, intelligence analysis, project management, policy papers) including the cited finding that communication failures contribute to a documented share of medical malpractice claims.

---

## Metadata

- **Version:** 1.0
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
