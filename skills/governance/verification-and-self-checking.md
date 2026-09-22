---
name: verification-and-self-checking
description: "Ensures Claude validates its own work against explicit success criteria — tests, reference outputs, screenshots, or build commands — before declaring a task complete."
---

# Skill Name: Verification and Self-Checking

## 🎯 Objective
Ensures Claude validates its own work against explicit success criteria — tests, reference outputs, screenshots, or build commands — before declaring a task complete. Eliminates the trust gap where plausible-looking code doesn't actually work.

## 👤 Target Persona
Software Engineer who wants Claude to close the feedback loop itself rather than returning output for manual review.

## 📥 Inputs Required
- **Task description:** What should be implemented or fixed?
- **Verification method:** One of: test suite command, expected output sample, reference screenshot, build/lint command, or Bash assertion
- **Success condition:** What does passing look like? (e.g., "all tests green", "output matches reference", "screenshot matches design")

**Minimum viable input:** the claim about to be made and the condition that would prove it. If no checkable condition exists, that is the finding — a task whose completion cannot be checked cannot honestly be reported as done, only as attempted.

## 📤 Expected Output
- Implemented code or fix
- Verification run output (test results, command output, or screenshot comparison)
- Explicit PASS or FAIL verdict with a diff if FAIL — never a silent assumption of success

## 🔗 Routing / Related Skills

Check these before running; each fires on something visible in the input.

- Run before declaring any task complete, including tasks from other skills in this library.
- If the claim concerns a deployed or running system → verify runtime state, not just code state.
- If the claim goes into a status report → `../communication/rag-status-reporting.md`, where an unverified Green is the costliest error.

## 🤖 Core Prompt / Instructions
```text
You are an expert software engineer working with Claude Code. Before starting any implementation, you must establish and then verify against a clear success condition.

Follow this process exactly:

1. UNDERSTAND the task. Restate it in one sentence.
2. IMPLEMENT the change, fix, or feature described.
3. VERIFY by running the provided verification method:
   - If a test command is given: run it and capture the output.
   - If an expected output is given: run the code and compare output exactly.
   - If a screenshot reference is given: take a screenshot of the result and compare it visually to the reference. List any differences explicitly.
   - If a build/lint command is given: run it and confirm it exits cleanly.
4. REPORT the result as PASS or FAIL.
   - On PASS: summarize what was implemented and confirm the verification succeeded.
   - On FAIL: show the diff or error, explain the root cause, fix it, and re-verify. Do NOT suppress errors to make the build pass.
5. REPEAT verify-fix cycles until the verification passes.

Never declare a task complete without running the verification. Never address a symptom if the root cause is identifiable.

Task: $TASK
Verification method: $VERIFICATION_METHOD
Success condition: $SUCCESS_CONDITION
```

## ✅ Success Criteria / Quality Checklist
- [ ] Verification is run — not skipped or assumed
- [ ] Output of the verification step is shown explicitly (not summarized away)
- [ ] PASS / FAIL verdict is stated clearly
- [ ] On failure, root cause is addressed — not the symptom
- [ ] No "it should work" or "this looks correct" without evidence

---
**Metadata**
- **Version:** 1.0
- **Last Updated:** 2026-05-01
- **Author:** Anthropic / Claude Code Docs
