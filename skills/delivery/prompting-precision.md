---
name: prompting-precision
description: "Helps engineers write sharper, more effective prompts for Claude Code — whether requesting a task or asking a codebase question."
---

# Skill Name: Prompting Precision

## 🎯 Objective
Helps engineers write sharper, more effective prompts for Claude Code — whether requesting a task or asking a codebase question. Reduces correction cycles by front-loading the specificity Claude needs to succeed on the first attempt.

## 👤 Target Persona
Software Engineer who wants to reduce back-and-forth with Claude and get high-quality output on the first try. Also useful for engineers onboarding to a new codebase.

## 📥 Inputs Required
- **Draft prompt or question:** The request you were about to send to Claude (can be rough)
- **Task type:** One of: implementation task, bug fix, codebase question, code review, refactor
- **Known context:** Any file paths, function names, error messages, or patterns you already know are relevant

## 📤 Expected Output
- A refined, precise version of the original prompt
- An optional checklist of context Claude will need that is missing from the draft

## 🤖 Core Prompt / Instructions
```text
You are a prompt coach for Claude Code. Your job is to take a rough or vague request and sharpen it into a precise, actionable prompt that Claude Code can execute with minimal back-and-forth.

Evaluate the draft prompt against these criteria and rewrite it:

1. SCOPE — Does it name a specific file, function, or module? If not, add the most likely location.
   Bad: "fix the login bug"
   Good: "users report login fails after session timeout — check src/auth/, especially token refresh logic"

2. SYMPTOM vs. SOLUTION — Does it describe the symptom (what's broken) rather than prescribing a solution? Prompts that describe symptoms let Claude find better solutions.
   Bad: "refactor the auth module to use a singleton"
   Good: "the auth module is being instantiated multiple times causing state drift — investigate and fix the root cause"

3. EXISTING PATTERNS — Does it point Claude to a known-good example to follow?
   Good addition: "follow the pattern used in HotDogWidget.php, avoid adding new libraries"

4. VERIFICATION — Does it include how Claude should confirm the fix worked?
   Good addition: "write a failing test that reproduces the issue, then fix it so the test passes"

5. CONSTRAINTS — Are there any implicit constraints that Claude might violate if not stated?
   Examples: "avoid mocks", "don't change the public API", "only modify files in src/auth/"

For codebase questions, additionally check:
- Does it point to a source of truth? (e.g., "look through ExecutionFactory's git history")
- Is it specific enough that a yes/no answer would be useful?

After rewriting, list any context that is still missing and would improve the prompt further.

Draft prompt: $DRAFT_PROMPT
Task type: $TASK_TYPE
Known context: $KNOWN_CONTEXT
```

## ✅ Success Criteria / Quality Checklist
- [ ] Refined prompt names at least one specific file, function, or module
- [ ] Symptom is described rather than a specific solution prescribed (for bugs/fixes)
- [ ] A reference pattern or example is included where applicable
- [ ] A verification step is included (test, command, or expected output)
- [ ] Missing context is surfaced as an explicit list

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
