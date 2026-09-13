# Skill Name: Bookend Communication Structure

## 🎯 Objective
Structures any analytical or business communication (report, memo, RFC, research writeup, briefing) so a reader who reads **only** the introduction and **only** the conclusion walks away with a complete, standalone understanding of the topic, the outline, the finding, and what happens next — while every piece of supporting proof, data, and methodology lives in the body for readers who want to verify or reproduce the work.

## 👤 Target Persona
Analyst, PM, strategist, researcher, or anyone producing a report/memo/briefing/RFC that will be read by people with very different depth needs — some readers only have time for the headline, others need to audit or replicate the analysis.

## 📥 Inputs Required
- **The core finding, recommendation, or decision** being communicated
- **Audience and their time constraints** — who reads only the summary vs. who reads everything
- **Available supporting evidence** — data sources, methodology, analysis steps, prior work
- **The action/decision** that needs to happen as a result, and who owns it
- **Format constraints** — memo, doc, slide deck, email

## 📤 Expected Output
A document in three structural parts:
1. A **self-sufficient introduction** — topic, scope, headline finding, and roadmap of what's covered
2. A **rigorous, reproducible body** — every finding traced to its evidence and method, with each source tagged by access tier (public/gated/paid/internal) and a stated fallback for readers who can't reach a non-public source
3. A **self-sufficient conclusion** — synthesis, concrete next steps, owners, and timing

## 🤖 Core Prompt / Instructions
```text
You are structuring a piece of analytical/business communication so that its
introduction and conclusion are each complete on their own, and its body
carries all the proof.

1. THE TWO-BOOKEND TEST (apply this literally before finalizing)
   If a reader reads ONLY the introduction and ONLY the conclusion — skipping
   the entire body — could they still:
     a) accurately describe what the piece is about
     b) name the outline of what's covered
     c) state the key finding or recommendation
     d) know what happens next and what's expected of them
   If any answer is no, the intro or conclusion is incomplete. Fix that
   section directly — don't rely on the body to compensate for a weak
   bookend.

2. INTRODUCTION REQUIREMENTS (must stand alone)
   - State the topic/question being addressed in one or two sentences —
     no throat-clearing preamble.
   - Lead with the headline finding or recommendation (BLUF — Bottom Line
     Up Front; see `bluf-bottom-line-up-front.md` for the mechanics of
     writing this line). Don't make the reader wait for a "reveal" at the
     end.
   - Give an explicit roadmap: what each following section covers, so the
     reader knows the shape of the argument before reading it.
   - State scope boundaries — what's covered and, where relevant, what's
     deliberately excluded — so the reader isn't left wondering if
     something was missed vs. intentionally out of scope.
   - Keep it tight but complete: an introduction that requires the body to
     make sense has failed at this job.

3. CONCLUSION REQUIREMENTS (must stand alone)
   - Restate the key finding/recommendation as a synthesis in light of the
     evidence ("given the above, therefore...") — not a verbatim repeat of
     the introduction.
   - Enumerate concrete next steps: what needs to happen, who owns it, and
     by when. Vague "we should consider..." language fails this bar.
   - State explicitly any decision being requested of the reader (approve,
     reject, choose between named options) rather than implying it.
   - State what happens on inaction, when relevant (default path, risk of
     not deciding).
   - Do not introduce new findings or data here that weren't covered in the
     body — the conclusion synthesizes, it never adds new evidence.

4. BODY REQUIREMENTS (proof, reproducibility, depth)
   - Every finding stated in the intro/conclusion must be traceable to a
     specific section, data source, or analysis step in the body.
   - Document methodology explicitly enough that an independent reader
     could reproduce the analysis and reach the same conclusion: named and
     dated data sources, the method/tooling used, assumptions made, and any
     filtering/exclusion criteria applied.
   - Show the chain from raw data/source to finding — include intermediate
     steps, not just the final number.
   - Separate fact (what the data shows) from interpretation (what we
     conclude from it), so a reader can agree with the facts and still form
     their own interpretation if they choose to.
   - Cite sources with enough specificity to verify: link, date accessed,
     query/filter used.
   - Tag every source's access tier alongside the citation, so a reader
     knows before clicking whether they'll actually be able to open it:
       * PUBLIC — freely accessible, no login required
       * GATED — requires a free signup/account (e.g. registration-walled
         reports, community/forum content)
       * PAID — requires a paid subscription, license, or purchase (e.g.
         analyst reports, paywalled journalism, licensed datasets)
       * INTERNAL — accessible only within the organization (internal
         tools, private repos, licensed enterprise data the org already
         pays for)
     Don't leave this implicit — a bare link reads as "public" by default
     and silently fails the reader who hits a paywall.
   - Manage the exception case explicitly for anything not PUBLIC: state
     what a reader without access should do — an alternative public source
     that supports the same point, a brief inline summary of the gated
     content sufficient to follow the argument without opening it, or who/
     where to request access (e.g. an internal team, license holder, or
     librarian). Never cite a GATED/PAID/INTERNAL source as if it were
     equally available to every reader without addressing this.
   - Order body sections to match the roadmap promised in the introduction
     — don't let the actual structure drift from what was promised.

5. STRUCTURAL ANTI-PATTERNS TO REJECT
   - "Slow build" writing that only reveals the finding at the very end
     (buries the lede — violates BLUF).
   - An introduction that's just a table of contents with no actual content
     (fails the "understand the topic" bar).
   - A conclusion that only summarizes what was said rather than stating
     what happens next (fails the "know what's needed" bar).
   - Evidence or data scattered into the intro/conclusion instead of
     staying in the body — this bloats the bookends and defeats their
     "readable in isolation" purpose.
   - Any claim in the intro/conclusion that can't be traced to something in
     the body — this destroys reproducibility and trust.

6. VALIDATION PASS
   Before shipping, extract just the introduction and conclusion into a
   separate scratch document and read them in total isolation — nothing
   else. If they don't fully pass the two-bookend test on their own, fix
   them before polishing the body further.

Now apply this to the described communication:
Core finding/recommendation: $CORE_FINDING
Audience and time constraints: $AUDIENCE
Available evidence/methodology: $AVAILABLE_EVIDENCE
Required action/decision and owner: $REQUIRED_ACTION
Format: $FORMAT
```

## ✅ Success Criteria / Quality Checklist
- [ ] A reader who reads only the introduction can state the topic, the outline, and the headline finding
- [ ] A reader who reads only the conclusion knows exactly what happens next, who owns it, and by when
- [ ] The introduction leads with the finding (BLUF), not a slow build to a reveal at the end
- [ ] The conclusion synthesizes rather than repeats, and introduces no new evidence
- [ ] Every claim in the intro/conclusion traces back to a specific section, source, or method in the body
- [ ] The body documents methodology precisely enough for an independent reader to reproduce the finding
- [ ] The body's actual section order matches the roadmap promised in the introduction
- [ ] Fact and interpretation are visibly separated in the body
- [ ] Every source citation is tagged with its access tier (public, gated, paid, internal)
- [ ] Every non-public source has an explicit fallback for readers without access (alternative source, inline summary, or request path)

---
**Metadata**
- **Version:** 1.2
- **Last Updated:** 2026-08-09
- **Author:** Workspace Communication Skills
