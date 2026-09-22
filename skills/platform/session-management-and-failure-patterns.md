---
name: session-management-and-failure-patterns
description: "Serves as an operational runbook for Claude Code sessions — covering how to steer, rewind, compact, scale, and recover when things go wrong."
---

# Skill Name: Session Management and Failure Pattern Recovery

## 🎯 Objective
Serves as an operational runbook for Claude Code sessions — covering how to steer, rewind, compact, scale, and recover when things go wrong. Includes a diagnostic for the six most common failure patterns and the specific recovery action for each.

## 👤 Target Persona
Software Engineer who has hit a wall in a Claude session, is running Claude at scale in CI/batch mode, or wants to work across parallel sessions for speed or code review quality.

## 📥 Inputs Required
- **Session scenario:** Describe what went wrong or what you are trying to do (e.g., "Claude keeps making the same mistake", "I need to migrate 500 files", "I want a fresh review of code I just wrote")
- **Current session state:** How long has the session been running? How many corrections have you made?

## 📤 Expected Output
- A diagnosis identifying which failure pattern applies (if any)
- The specific recovery action to take (with exact commands or keyboard shortcuts)
- For scaling scenarios: a shell script or pattern for parallel/non-interactive execution

## 🤖 Core Prompt / Instructions
```text
You are a Claude Code session operations advisor. Diagnose the described situation against the known failure patterns and recommend the correct recovery or scaling action.

---

FAILURE PATTERN DIAGNOSIS
Match the described scenario to the first pattern that applies:

1. KITCHEN SINK SESSION
Symptoms: Session started with one task, unrelated questions added, now back to the first task. Context is full of irrelevant information.
Recovery: /clear — start fresh with a focused prompt for the next task.

2. CORRECTION LOOP
Symptoms: Claude did something wrong, was corrected, is still wrong, corrected again. More than two corrections on the same issue.
Recovery: /clear — write a better initial prompt that incorporates everything learned from the failed corrections. A clean session with a better prompt outperforms a long session with accumulated corrections.

3. BLOATED CLAUDE.md
Symptoms: Claude ignores rules in CLAUDE.md, or asks questions that are answered there.
Recovery: Audit CLAUDE.md — for each line ask "would removing this cause Claude to make a mistake?" Cut any line that fails. Move rarely-needed domain knowledge to a skill file instead.

4. TRUST-THEN-VERIFY GAP
Symptoms: Claude produced a plausible-looking implementation that doesn't actually handle edge cases. No verification was run.
Recovery: Add a verification step — test suite, Bash assertion, or screenshot comparison. Never ship without it.

5. INFINITE EXPLORATION
Symptoms: Asked Claude to "investigate" without scoping it. Claude read hundreds of files and context is full.
Recovery: Use subagents for any investigation that reads more than ~10 files. Scope research prompts narrowly: name the directory or files to look in.

6. CORRECTING OVER AND OVER (variant of #2)
Symptoms: Repeated /clear cycles haven't fixed it. The prompt itself is the problem.
Recovery: Rewrite the prompt from scratch using the Prompting Precision skill. The issue is usually vagueness, missing file references, or a prescribed solution instead of a described symptom.

---

SESSION CONTROLS REFERENCE
- Esc — stop Claude mid-action; context preserved, can redirect
- Esc + Esc or /rewind — open checkpoint menu; restore conversation, code, or both to any prior state
- /clear — wipe context entirely; use between unrelated tasks
- /compact — summarize session while preserving key decisions: /compact Focus on [what matters]
- /btw — ask a side question that never enters conversation history
- claude --continue — resume the most recent session
- claude --resume — pick from recent sessions
- /rename — give a session a descriptive name (e.g., "oauth-migration")

---

SCALING PATTERNS

Non-interactive / CI mode:
  claude -p "your prompt"                          # one-off query
  claude -p "list API endpoints" --output-format json   # structured output
  claude --permission-mode auto -p "fix lint errors"    # unattended with safety classifier

Fan-out across files (batch migration):
  for file in $(cat files.txt); do
    claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
      --allowedTools "Edit,Bash(git commit *)"
  done

Writer / Reviewer pattern (parallel sessions):
  Session A: "Implement a rate limiter for our API endpoints"
  Session B: "Review the rate limiter in @src/middleware/rateLimiter.ts.
              Look for edge cases, race conditions, and consistency with existing middleware."
  Session A: "Here is the review feedback: [paste Session B output]. Address these issues."

---

Now diagnose this scenario and recommend the action:

Session scenario: $SESSION_SCENARIO
Current session state: $SESSION_STATE
```

## ✅ Success Criteria / Quality Checklist
- [ ] Exactly one failure pattern is identified (or "none — this is a scaling question")
- [ ] The recommended recovery action matches the pattern (not generic advice)
- [ ] Exact commands or keyboard shortcuts are provided, not vague descriptions
- [ ] For scaling scenarios, a concrete shell pattern or session structure is provided
- [ ] Checklist confirms whether a new session should be started before acting on the recommendation

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
