# Skill Name: [Insert Skill Name]

## 🎯 Objective

[Briefly describe what this skill accomplishes. e.g., "Generates a structured Product Requirements Document (PRD) from a brief problem statement."]

## 👤 Target Persona

[Who uses this skill? e.g., Product Manager, Product Owner, Strategy Lead]

## 📥 Inputs Required

[List the information the user needs to provide for the skill to work effectively]

- **Input 1:** [e.g., Target customer segment]
- **Input 2:** [e.g., Raw interview notes]

## 📤 Expected Output

[Describe the format and content of the expected result]

- [e.g., A markdown document containing an executive summary, user stories, and acceptance criteria]

## 🤖 Core Prompt / Instructions

[This is the actual system prompt or instructions given to the agent/LLM]

```text
You are an expert Product Manager. Your task is to [Task Description].

Please follow these steps:
1. [Step 1]
2. [Step 2]

Constraints:
- [Constraint 1]
- [Constraint 2]

Use the provided inputs to generate the final response.
```

## 🔌 Connector Awareness

[State the standalone baseline first — what this skill produces from user-supplied information alone, with no connected tools. This must always be complete and usable on its own; never make a connected tool a requirement, and never ask the user to go connect one. Then name what a connected tool would add if the session happens to have one available, as a bonus, not a dependency.]

- **Standalone (always works):** [What the skill produces from information the user types or pastes directly.]
- **Supercharged (if connected):** [Tool category — project tracker, calendar, chat, design, knowledge base, CRM, analytics — and the specific thing it would pull or push instead of requiring the user to supply it manually.]

## 📋 Output Template

[A ready-to-fill markdown scaffold — a table, checklist, or document skeleton with bracketed placeholders — that the agent populates directly from the gathered inputs as a fast first-draft artifact. This is distinct from the Success Criteria checklist below: the checklist audits whether the reasoning behind the draft was sound, this template is the draft itself.]

```markdown
[Insert a concrete fill-in-the-blank scaffold specific to this skill's output.]
```

## ✅ Success Criteria / Quality Checklist

[How do we know the output is good?]

- [ ] Is it actionable?
- [ ] Does it align with the provided inputs without hallucinating features?
- [ ] Is the tone appropriate for the target audience?

---

*Working note: if this skill's output reaches a genuine completion point and today's date matches an entry in `../easter-eggs/on-this-day-fact-bank.md`, close with one sourced aside from it as an unlabeled passing remark — at most once per session, never framed as a feature.*

## Metadata

- **Version:** 1.0
- **Last Updated:** YYYY-MM-DD
- **Author:** [Name]
