# Skill Name: Explore-Plan-Code-Commit Workflow

## 🎯 Objective
Guides engineers through Claude Code's recommended 4-phase development workflow — Explore, Plan, Implement, Commit — preventing wasted effort from jumping straight to code. Includes an optional interview phase for complex features where requirements are unclear.

## 👤 Target Persona
Software Engineer starting a new feature, refactor, or multi-file change where scope or approach is uncertain.

## 📥 Inputs Required
- **Feature or change description:** What needs to be built or modified?
- **Relevant file paths or modules:** Known starting points for exploration (optional — Claude can discover them)
- **Uncertainty level:** Is the approach clear (skip to plan) or unclear (start with interview)?

## 📤 Expected Output
- **Explore phase:** A summary of relevant code, patterns, and dependencies Claude found
- **Plan phase:** A written implementation plan (saved to a file like `PLAN.md` or displayed in editor via `Ctrl+G`)
- **Implement phase:** Working code with tests passing
- **Commit phase:** A descriptive commit message and optional PR

## 🤖 Core Prompt / Instructions
```text
You are a senior software engineer using Claude Code. Follow the 4-phase workflow below. Do not skip phases.

---

PHASE 1 — EXPLORE (Plan Mode)
Enter Plan Mode. Read the relevant files, understand the existing patterns, and answer these questions:
- What files will need to change?
- What existing utilities or patterns should be reused?
- Are there any non-obvious constraints or gotchas?
Do not make any changes in this phase.

---

PHASE 2 — PLAN (Plan Mode)
Produce a detailed implementation plan that includes:
- Files to create or modify
- The order of changes
- Test strategy (what tests to write and run)
- Any risks or edge cases to handle

Save the plan to PLAN.md or press Ctrl+G to open it in the editor for review.
Do not write any implementation code until the plan is confirmed.

---

PHASE 3 — IMPLEMENT (Normal Mode)
Switch to Normal Mode. Implement the plan step by step:
1. Make the changes described in the plan.
2. Write tests for the new behavior.
3. Run the tests and fix any failures.
4. Run the linter or type checker and fix any issues.
Do not move to the next step until the current one passes.

---

PHASE 4 — COMMIT
Write a commit message that explains WHY the change was made, not just what changed.
Format: `<type>: <short summary>\n\n<body explaining the motivation>`
Then open a PR if applicable.

---

OPTIONAL — INTERVIEW PHASE (before Phase 1, for complex features)
If the requirements are unclear, run the interview phase first:
"I want to build [description]. Interview me using the AskUserQuestion tool. Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions — dig into the hard parts. Keep interviewing until we've covered everything, then write a complete spec to SPEC.md."
Start a fresh session after the spec is complete.

NOTE — for larger or AI-driven initiatives, don't stop at a one-off SPEC.md: this single-session
Plan phase is not the same as a durable, re-verifiable spec. Use `delivery/spec-driven-development.md`
instead when the work already has an approved FRD, needs to survive across multiple sessions/agents,
or needs the Commercialization Validation Gate (independent testing, use-case coverage
classification, roadmap feedback for gaps) before being treated as production-ready.

---

Feature to build: $FEATURE_DESCRIPTION
Known files or modules: $KNOWN_FILES
```

## ✅ Success Criteria / Quality Checklist
- [ ] Phases are followed in order — no jumping from description to code
- [ ] Explore phase produces a written summary of findings, not just silent file reads
- [ ] Plan is externalized (written to file or opened in editor) before implementation begins
- [ ] Tests are written and passing before commit
- [ ] Commit message explains motivation, not just mechanics

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
