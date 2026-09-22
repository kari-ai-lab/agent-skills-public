---
name: quality-monitoring-model
kind: reference
description: "To ensure the Agentic PM Skills Library remains highly effective, accurate, and relevant, we must treat the \"Skills\" (prompts and workflows) as product features."
---

# Skill Quality & Governance Model

To ensure the Agentic PM Skills Library remains highly effective, accurate, and relevant, we must treat the "Skills" (prompts and workflows) as product features. They require monitoring, user feedback, and iterative improvement.

## 1. Quality Monitoring Metrics

How do we measure if a skill is performing well?

### A. Quantitative Metrics (Usage & Efficiency)
*   **Adoption Rate:** How often is the skill being invoked by the PM team per week/month? (High usage implies high value).
*   **Completion Rate:** Does the user take the output and use it (e.g., copy/pasting the Jira epic), or do they abandon it and write it manually?
*   **Time-to-Task Completion:** Compare the time it takes a PM to complete a task using the skill vs. doing it manually.

### B. Qualitative Metrics (Output Quality)
*   **User Rating (CSAT):** Implement a simple 1-5 star rating or Thumbs Up/Down after a skill generates an output.
*   **Hallucination / Error Rate:** How often does the user report that the skill fabricated information or failed to follow constraints?
*   **Edit Distance:** How heavily does the PM have to edit the output before it is usable? (High edit distance = poor prompt quality).

---

## 2. Triggers for Skill Updates

Skills should not remain static. They need updates when underlying models change or business context shifts. A skill should be flagged for review and update when:

### 🌟 Performance-Based Triggers
1.  **Feedback Drop:** The average user rating falls below 4.0/5.0, or the Thumbs Down rate exceeds 15% over a two-week period.
2.  **Abandonment:** Usage drops significantly (e.g., a 30% drop month-over-month), indicating the skill is no longer solving a core problem.
3.  **High Edit Distance:** Users report they are rewriting more than 30% of the generated output.

### 🏢 Context-Based Triggers (Business Changes)
1.  **Process Changes:** E.g., The engineering team switches from User Stories to "Jobs To Be Done" framework. The `jira_epic_builder.md` skill must be updated to reflect the new format.
2.  **Product Pivot/Strategy Shift:** If the company shifts focus (e.g., from B2C to Enterprise B2B), the tone and constraints in the prompts must be updated to match the new persona.
3.  **New LLM Versions:** When switching underlying models (e.g., moving from GPT-4 to Claude 3, or updating to a new Gemini version), skills should be regression-tested as different models interpret prompts differently.

---

## 3. Maintenance Workflow

To maintain the library, implement the following Agile-style governance:

1.  **Quarterly Skill Audit:** A designated "AI Operations" lead or Lead PM reviews all skills quarterly. 
2.  **Deprecation:** Skills with zero usage in 60 days should be archived to reduce clutter.
3.  **Version Control:** Always bump the version number in the metadata (`Version: 1.1`) when modifying the core prompt so teams know the logic has changed.
4.  **Feedback Loop:** Maintain a dedicated Slack channel or internal ticketing queue (e.g., `#ai-pm-skills`) where users can report bugs or request new skills.
