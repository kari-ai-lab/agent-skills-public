# Credits

Sources, specifications, and people whose work enriched the skills in this repo, with links back to the specific files that cite them.

## Systems Thinking & Management Theory

### The Systems Thinker
**https://thesystemsthinker.com/systems-thinking-what-why-when-where-and-how/**
Source for the Iceberg Framework (Events → Patterns → Structure → Mental Models) and the "no perfect solutions" framing.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### MIT Open Learning
**https://openlearning.mit.edu/news/ask-mit-professor-what-system-thinking-and-why-it-important**
Edward Crawley's systems-as-entities-and-relationships framing ("the cognitive skill of the 21st century").
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Wikipedia — Systems Thinking
**https://en.wikipedia.org/wiki/Systems_thinking**
Source for reinforcing/balancing feedback loops, stocks and flows, emergence, causal loop diagrams, and Donella Meadows' leverage-points hierarchy.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Domain Language (Eric Evans)
**https://www.domainlanguage.com/ddd/**
Primary source for Domain-Driven Design's ubiquitous language, strategic design, and context mapping.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### Wikipedia — Domain-Driven Design
**https://en.wikipedia.org/wiki/Domain-driven_design**
Source for DDD's three pillars, tactical patterns, and the nine Context Mapping patterns (Partnership, Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Open-Host Service, Published Language, Separate Ways, Big Ball of Mud).
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md)

### DDD Crew
**https://github.com/ddd-crew**
Source for the practical, fillable DDD templates.
- [`skills/product/systems-thinking-and-domain-driven-design.md`](skills/product/systems-thinking-and-domain-driven-design.md) — [Bounded Context Canvas](https://github.com/ddd-crew/bounded-context-canvas), [Aggregate Design Canvas](https://github.com/ddd-crew/aggregate-design-canvas), [DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process)

### The W. Edwards Deming Institute
**https://deming.org/**
Primary source for the entire `Management/` skillset.
- [`skills/Management/system-of-profound-knowledge.md`](skills/Management/system-of-profound-knowledge.md) — [Deming the Man](https://deming.org/deming-the-man/), [SoPK](https://deming.org/explore/sopk/)
- [`skills/Management/fourteen-points-for-management.md`](skills/Management/fourteen-points-for-management.md) — [Fourteen Points](https://deming.org/explore/fourteen-points/)
- [`skills/Management/seven-deadly-diseases.md`](skills/Management/seven-deadly-diseases.md) — [Seven Deadly Diseases](https://deming.org/explore/seven-deadly-diseases/)
- [`skills/Management/pdsa-improvement-cycle.md`](skills/Management/pdsa-improvement-cycle.md) — [PDSA](https://deming.org/explore/pdsa/)
- [`skills/Management/red-bead-experiment.md`](skills/Management/red-bead-experiment.md) — [Red Bead Experiment](https://deming.org/explore/red-bead-experiment/)
- [`skills/Management/funnel-experiment.md`](skills/Management/funnel-experiment.md) — [The Funnel Experiment](https://deming.org/explore/the-funnel-experiment/)

## Specifications & Standards

### OpenAPI Specification
**https://swagger.io/specification/**
Primary source for the OpenAPI/Swagger document-mechanics sub-recipes.
- [`skills/platform/api-builder.md`](skills/platform/api-builder.md)
- [`skills/recipes/api-builder-document-structure-recipe.md`](skills/recipes/api-builder-document-structure-recipe.md) — [`#openapi-object`](https://swagger.io/specification/#openapi-object), [`#info-object`](https://swagger.io/specification/#info-object)
- [`skills/recipes/api-builder-paths-operations-recipe.md`](skills/recipes/api-builder-paths-operations-recipe.md) — [`#paths-object`](https://swagger.io/specification/#paths-object), [`#operation-object`](https://swagger.io/specification/#operation-object)
- [`skills/recipes/api-builder-schemas-recipe.md`](skills/recipes/api-builder-schemas-recipe.md) — [`#components-object`](https://swagger.io/specification/#components-object), [`#schema-object`](https://swagger.io/specification/#schema-object)
- [`skills/recipes/api-builder-security-recipe.md`](skills/recipes/api-builder-security-recipe.md) — [`#security-scheme-object`](https://swagger.io/specification/#security-scheme-object), [`#security-requirement-object`](https://swagger.io/specification/#security-requirement-object)
- [`skills/recipes/api-builder-webhooks-examples-recipe.md`](skills/recipes/api-builder-webhooks-examples-recipe.md) — [`#callback-object`](https://swagger.io/specification/#callback-object), [`#example-object`](https://swagger.io/specification/#example-object)

### Google API Design Guide (AIPs)
**https://docs.cloud.google.com/apis/design** (canonical home: **https://google.aip.dev/**)
Source for resource-oriented design, standard methods, pagination, and error-model guidance.
- [`skills/platform/api-builder.md`](skills/platform/api-builder.md)
- [`skills/recipes/api-builder-google-resource-naming-recipe.md`](skills/recipes/api-builder-google-resource-naming-recipe.md) — [AIP-121](https://google.aip.dev/121) (resource-oriented design), [AIP-122](https://google.aip.dev/122) (resource names), [AIP-190](https://google.aip.dev/190) (naming conventions)
- [`skills/recipes/api-builder-google-standard-methods-recipe.md`](skills/recipes/api-builder-google-standard-methods-recipe.md) — [AIP-130](https://google.aip.dev/130) (standard methods), [AIP-131](https://google.aip.dev/131) (Get), [AIP-132](https://google.aip.dev/132) (List), [AIP-133](https://google.aip.dev/133) (Create), [AIP-134](https://google.aip.dev/134) (Update), [AIP-135](https://google.aip.dev/135) (Delete), [AIP-136](https://google.aip.dev/136) (custom methods), [AIP-193](https://google.aip.dev/193) (errors)

### LeSS (Large-Scale Scrum)
**https://less.works/**
- [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md) — [framework/introduction](https://less.works/less/framework/introduction), [principles](https://less.works/less/principles/index), [rules](https://less.works/less/rules)

### SAFe (Scaled Agile Framework)
**https://scaledagile.com/** / **https://framework.scaledagile.com/**
- [`skills/delivery/scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md) — [Lean-Agile principles](https://framework.scaledagile.com/safe-lean-agile-principles/), [Big Picture](https://framework.scaledagile.com/#big-picture)

### Prioritization Frameworks (WSJF and related)
- [`skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md`](skills/Refinement/future-workstream-prioritization-wsjf-and-techniques.md) — [SAFe WSJF](https://framework.scaledagile.com/wsjf/), [Fibery: Agile Prioritization Techniques](https://fibery.com/blog/product-management/agile-prioritization-techniques/), [Atlassian: Prioritization Framework](https://www.atlassian.com/agile/product-management/prioritization-framework)

### PCI-DSS v4.0
Publicly published payment-card industry data security standard (PCI Security Standards Council). No specific clause URL is cited in-file; referenced by requirement number.
- [`skills/domains/pci-dss-req-3-4.md`](skills/domains/pci-dss-req-3-4.md) — Requirement 3.4

### SMART Goals
- [`skills/Strategy/annual-goals-and-quarterly-objectives.md`](skills/Strategy/annual-goals-and-quarterly-objectives.md) — [Atlassian: How to write SMART goals](https://www.atlassian.com/blog/productivity/how-to-write-smart-goals), [SNHU: What are SMART goals](https://www.snhu.edu/about-us/newsroom/education/what-are-smart-goals), [UCOP: How to write SMART Goals (PDF)](https://www.ucop.edu/local-human-resources/_files/performance-appraisal/How+to+write+SMART+Goals+v2.pdf), [Harvard Health: Get SMART about your goals](https://www.health.harvard.edu/blog/get-smart-about-your-goals-this-strategy-can-help-you-stay-focused-and-on-track-at-any-age-2017090112113).

### INVEST (User Story / Initiative Quality Checklist)
Originated by Bill Wake (2003); reference definition via the Agile Alliance glossary.
- [`skills/Strategy/annual-goals-and-quarterly-objectives.md`](skills/Strategy/annual-goals-and-quarterly-objectives.md) — [Agile Alliance: INVEST](https://agilealliance.org/glossary/invest/)

### Agile Manifesto — 12 Principles
**https://agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/**
Root canon underneath every framework-specific delivery skill (SAFe, LeSS) — these are implementations of the 12 principles, not replacements for them.
- [`skills/delivery/scaled-agile-delivery-guidance.md`](skills/delivery/scaled-agile-delivery-guidance.md), [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md)

### FIRST.org Standards
**https://www.first.org/standards/**
Forum of Incident Response and Security Teams — CVSS, EPSS, the PSIRT/CSIRT Services Frameworks and PSIRT Maturity Document, and the Traffic Light Protocol.
- [`skills/governance/vulnerability-severity-and-exploit-prioritization.md`](skills/governance/vulnerability-severity-and-exploit-prioritization.md) — [CVSS](https://www.first.org/cvss), [EPSS](https://www.first.org/epss)
- [`skills/governance/product-security-incident-response-readiness.md`](skills/governance/product-security-incident-response-readiness.md) — [PSIRT Services Framework](https://www.first.org/standards/frameworks/psirts/psirt_services_framework_v1.1), [PSIRT Maturity Document](https://www.first.org/standards/frameworks/psirts/psirt_maturity_document), [CSIRT Services Framework](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1), [TLP](https://www.first.org/tlp)

### NIST Information Technology Laboratory (ITL)
**https://www.nist.gov/itl**
US federal standards body for cybersecurity, cryptography, AI standards, and biometrics; home of FIPS and the National Vulnerability Database.
- [`skills/governance/README.md`](skills/governance/README.md) — root-canon reference for software security standards generally.

### Wikipedia — Privacy Law
**https://en.wikipedia.org/wiki/Privacy_law**
Jurisdiction-by-jurisdiction survey (GDPR, US Privacy Act/HIPAA/COPPA, PIPEDA/CASL, LGPD, UK DPA/UK-GDPR, China's Cybersecurity Law, APPI, India's DPDP Act, Singapore's PDPA, POPI, and more) and the principles common across nearly all of them.
- [`skills/governance/privacy-law-awareness-for-product-development.md`](skills/governance/privacy-law-awareness-for-product-development.md)

### Cucumber Documentation
**https://cucumber.io/docs/**
Canonical source for Gherkin syntax and BDD (Behaviour-Driven Development) practice.
- [`skills/delivery/gherkin-syntax-and-writing-guide.md`](skills/delivery/gherkin-syntax-and-writing-guide.md) — [Gherkin reference](https://cucumber.io/docs/gherkin/reference/), [writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/)
- [`skills/delivery/behavior-driven-development-and-model-integration.md`](skills/delivery/behavior-driven-development-and-model-integration.md) — [What is BDD](https://cucumber.io/docs/bdd/), [who does what](https://cucumber.io/docs/bdd/who-does-what/)

### SDLC Sources (reconciled across four)
- [`skills/delivery/software-development-life-cycle-modeling.md`](skills/delivery/software-development-life-cycle-modeling.md) — [Atlassian](https://www.atlassian.com/agile/software-development/sdlc), [IBM](https://www.ibm.com/think/topics/sdlc), [AWS](https://aws.amazon.com/what-is/sdlc/), [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/software-development-life-cycle-sdlc/)

### PDLC Sources
- [`skills/product/product-development-life-cycle-modeling.md`](skills/product/product-development-life-cycle-modeling.md) — [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/product-development-life-cycle-and-its-stages/), [Atlassian](https://www.atlassian.com/agile/product-management/product-development)

### Product School
**https://productschool.com/**
Blog and 25-item template library — role clarity (PM vs. PMM), AI-native operating-model guidance, and ready-to-use product templates.
- [`skills/product/ai-operating-model-for-product-teams.md`](skills/product/ai-operating-model-for-product-teams.md) — [The AI Operating Model](https://productschool.com/blog/digital-transformation/the-ai-operating-model-why-product-teams-are-stuck)
- [`skills/product/pm-vs-pmm-role-clarity.md`](skills/product/pm-vs-pmm-role-clarity.md) — [PM vs PMM](https://productschool.com/blog/job-search/pm-vs-pmm-landing-the-right-role-for-you)
- [`skills/product/product-school-template-toolkit.md`](skills/product/product-school-template-toolkit.md) — [Template Library](https://productschool.com/resources/templates)

## Multi-Agent Systems & Agentic AI Engineering

Primary sources for the `orchestration/` and `journeys/` skillsets — each verified via live fetch against the source's own page, not cited from memory.

### Anthropic — "How we built our multi-agent research system"
**https://www.anthropic.com/engineering/multi-agent-research-system**
The lead-agent decompose-and-spawn pattern, the four-field subtask specification (objective, output format, tool guidance, boundaries), the named duplicate-search failure mode from vague task descriptions, the compounding-error/trajectory-shift failure mode and its resumability/graceful-adaptation mitigations, and the 1,000-2,000 token distilled-summary return-value figure.
- [`skills/orchestration/task-decomposition-and-routing.md`](skills/orchestration/task-decomposition-and-routing.md), [`skills/orchestration/conflict-and-consensus-resolution.md`](skills/orchestration/conflict-and-consensus-resolution.md), [`skills/orchestration/agent-chain-failure-and-escalation.md`](skills/orchestration/agent-chain-failure-and-escalation.md), [`skills/orchestration/agent-memory-architecture-and-consolidation.md`](skills/orchestration/agent-memory-architecture-and-consolidation.md)

### Anthropic — "Effective context engineering for AI agents"
**https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents**
Context as a finite resource, the orchestrator/clean-subagent-context-window ownership split, and the compaction mechanism.
- [`skills/orchestration/shared-context-and-state-ownership.md`](skills/orchestration/shared-context-and-state-ownership.md)

### A2A Protocol (Google)
**https://a2a-protocol.org/latest/topics/what-is-a2a/**
The Agent Card discovery mechanism, the Task object's `id`/`status`/`artifacts` fields, the full `TaskState` lifecycle enum, and the Message object's `role`/`parts` fields.
- [`skills/orchestration/inter-agent-handoff-contract.md`](skills/orchestration/inter-agent-handoff-contract.md), [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### Microsoft — Azure Architecture Center, Circuit Breaker Pattern
**https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker**
The Retry-vs-Circuit-Breaker distinction, the Closed/Open/Half-Open state machine, and the increasing-timeout recovery guidance.
- [`skills/orchestration/agent-chain-failure-and-escalation.md`](skills/orchestration/agent-chain-failure-and-escalation.md)

### Du, Li, Torralba, Tenenbaum & Mordatch — "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
**https://arxiv.org/abs/2305.14325**
The multi-round agent-debate mechanism and its factuality/hallucination-reduction result.
- [`skills/orchestration/conflict-and-consensus-resolution.md`](skills/orchestration/conflict-and-consensus-resolution.md)

### LangGraph — Persistence
**https://docs.langchain.com/oss/python/langgraph/persistence**
The checkpointer/thread-scoped state-persistence model and its named use cases (conversation continuity, human-in-the-loop, time travel, fault tolerance).
- [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### OpenAI Agents SDK — Handoffs
**https://openai.github.io/openai-agents-python/handoffs/**
The tool-based agent delegation pattern and the `HandoffInputData` context-carrying mechanism.
- [`skills/orchestration/harness-selection-and-mapping.md`](skills/orchestration/harness-selection-and-mapping.md)

### Sun, Chen, Zhu, et al. — "MemGPT: Towards LLMs as Operating Systems"
**https://arxiv.org/abs/2310.08560**
The OS-inspired hierarchical/tiered memory framing. The fetched abstract did not itself name specific tier labels or an eviction/paging decision rule — the skill's tier design beyond the OS-paging analogy is original, not a verbatim restatement.
- [`skills/orchestration/agent-memory-architecture-and-consolidation.md`](skills/orchestration/agent-memory-architecture-and-consolidation.md)

### Enterprise Integration Patterns — Process Manager
**https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html** (Gregor Hohpe & Bobby Woolf)
The centralized-orchestration pattern, its hub-and-spoke mechanism, and its named bottleneck trade-off.
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Temporal — Understanding Temporal
**https://docs.temporal.io/evaluate/understanding-temporal**
The Workflow Definition as executable business logic, the durable Event History mechanism, and Temporal's own stated fit ("order fulfillment, customer onboarding, and payment processing").
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### W3C Trace Context
**https://www.w3.org/TR/trace-context/**
The cross-vendor trace-correlation problem and the `traceparent`/`tracestate` header mechanism (trace-id, parent-id).
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Pact
**https://pact.io/**
Consumer-driven contract testing's own framing — verifying compatibility in isolation rather than via full end-to-end environments.
- [`skills/journeys/journey-orchestration-and-verification.md`](skills/journeys/journey-orchestration-and-verification.md)

### Alberto Brandolini — EventStorming
**https://www.eventstorming.com/**
The collaborative-workshop-format definition and its four styles (Improve, Envision, Explore, Design).
- [`skills/journeys/end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md)

### John Ferguson Smart — Feature Mapping
**https://johnfergusonsmart.com/feature-mapping-a-lightweight-requirements-discovery-practice-for-agile-teams/**
The sticky-note structure (blue/rules, green/examples, yellow/steps, purple/consequences) bridging a business goal to Given-When-Then BDD scenarios.
- [`skills/journeys/end-to-end-journey-specification.md`](skills/journeys/end-to-end-journey-specification.md)

### IBM — Principles for Trust and Transparency
**https://www.ibm.com/policy/trust-transparency**
Human-accountability grounding for classifying which tasks should route to AI at all.
- [`skills/product/ai-human-task-allocation-model.md`](skills/product/ai-human-task-allocation-model.md)

## Software Engineering Practice

Primary sources for the `engineering/` skillset.

### Martin Fowler — "TestPyramid" / "Mocks Aren't Stubs" / "CodeSmell" / Refactoring Catalog
**https://martinfowler.com/**
Pyramid shape and ice-cream-cone anti-pattern (Mike Cohn/Jason Huggins attribution); precise dummy/fake/stub/spy/mock definitions and state-vs-behavior verification; code smells framed as an investigation trigger, not an automatic verdict; the named-refactoring vocabulary (Extract Function, Rename Variable, and others).
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Google Testing Blog — "Test Sizes"
**https://testing.googleblog.com/2010/12/test-sizes.html** (Simon Stewart, 2010)
Enforceable Small/Medium/Large test-size definitions.
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md)

### Wikipedia — "Test-driven development" / "SOLID"
**https://en.wikipedia.org/**
Kent Beck attribution and the red-green-refactor cycle, with TDD's own named real limits; the five SOLID principles' precise definitions (Robert C. Martin / Michael Feathers attribution).
- [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md)

### Google — `eng-practices`
**https://google.github.io/eng-practices/review/**
The twelve-item review-priority checklist, the "improves code health, not perfection" approval standard, the one-business-day turnaround norm, and the collaborative disagreement-handling procedure.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### Google — AIP-192: Documentation
**https://google.aip.dev/192**
"Documentation... will be the only things a user has" — grounds the Design-for-the-Human-Reader-First principle applied to naming, interfaces, and comments.
- [`skills/engineering/coding-standards-and-design-patterns.md`](skills/engineering/coding-standards-and-design-patterns.md), [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md), [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### Jason Cohen — *Best Kept Secrets of Peer Code Review*
SmartBear/Cisco study on diff-size vs. defect-detection rate. The primary PDF is an unreadable legacy scanned format for automated tools — cited via secondary description, flagged honestly in the skill's own Sources rather than presented as directly verified.
- [`skills/engineering/code-review-standards-and-checklist.md`](skills/engineering/code-review-standards-and-checklist.md)

### InfoQ
**https://www.infoq.com/**
Several specific reports: "AI Code Review at Scale: LinkedIn's Multi-Agent Approach" (Sergio De Simone, 2026-08-22 — hallucination/low-signal/missing-context failure modes, multi-independent-reviewer architecture, a 63.9% acceptance-rate data point); "Taming Flaky Tests" (Trisha Gee podcast, 2025-04-18 — four named flaky-test cause categories); "The AI Productivity Paradox in Test Automation" (Chowdhury & Gummadavelli, 2026-06-01 — Ghost Click, State Reversion Race, Timeout Spiral failure modes); "Meta Applies Mutation Testing with LLM..." (2026-01-06 — Meta's ACH system, 73% engineer-acceptance result); "AI-Generated Code Creates New Wave of Technical Debt" (2025-11-18 — Ox Security's "Comments Everywhere"/"Over-Specification" anti-pattern frequencies).
- [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md), [`skills/engineering/testing-strategy-and-the-test-pyramid.md`](skills/engineering/testing-strategy-and-the-test-pyramid.md), [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md), [`skills/engineering/agent-driven-code-generation-discipline.md`](skills/engineering/agent-driven-code-generation-discipline.md)

### Anthropic — "Best practices for Claude Code"
**https://code.claude.com/docs/en/best-practices**
The "reviewer prompted to find gaps will usually report some, even when the work is sound" rubber-stamp warning, its corrective, and the fresh-subagent-context independence framing.
- [`skills/engineering/agent-driven-test-generation-and-verification.md`](skills/engineering/agent-driven-test-generation-and-verification.md), [`skills/engineering/agent-driven-code-review-calibration.md`](skills/engineering/agent-driven-code-review-calibration.md)

## Agile & Lean Thought Leadership

Practitioner/primary sources for the `delivery/` and `Strategy/` skillsets — several are the actual co-creators of the methods those skills guide on, cited alongside (not instead of) the frameworks' own official sites.

- **Ron Jeffries** — XP co-founder, Agile Manifesto co-author. **https://ronjeffries.com/**
- **Craig Larman** — LeSS co-creator (with Bas Vodde). **https://www.craiglarman.com/wiki/index.php?title=Main_Page** — cited in [`skills/delivery/less-delivery-guidance.md`](skills/delivery/less-delivery-guidance.md) alongside less.works.
- **Lean Manufacturing (Wikipedia)** — **https://en.wikipedia.org/wiki/Lean_manufacturing** — Lean's lineage: Deming → Ohno/Shingo's Toyota Production System → Womack/Jones's five principles.
- **Lean Enterprise Institute** — **https://www.lean.org/**
- **Mary Poppendieck / Lean Essays** — **https://www.leanessays.com/** — first applied lean-manufacturing principles to software development.
- **Agileism — "12 Agile Thought Leaders to Follow"** — **https://agileism.com/12-agile-thought-leaders-to-follow** — a discovery index, not a primary source in itself.
- **KPI Fire — "House of Lean"** — **https://www.kpifire.com/continuous-improvement/house-of-lean/** — a distinct model from SAFe's House of Lean; cited in [`skills/Strategy/house-of-lean-for-product-strategy.md`](skills/Strategy/house-of-lean-for-product-strategy.md) as complementary background, not a substitute source.
- **MIT Sloan — "10 Agile Ideas Worth Sharing"** — **https://mitsloan.mit.edu/ideas-made-to-matter/10-agile-ideas-worth-sharing**

All cited in [`skills/delivery/README.md`](skills/delivery/README.md)'s Reference Sources section.

## People

### Anthropic / Claude Code Docs
Several platform, delivery, and governance skills are adapted from or attributed to Anthropic's own Claude Code documentation and guidance.
- [`skills/platform/claude-md-configuration.md`](skills/platform/claude-md-configuration.md)
- [`skills/platform/context-management.md`](skills/platform/context-management.md)
- [`skills/platform/session-management-and-failure-patterns.md`](skills/platform/session-management-and-failure-patterns.md)
- [`skills/platform/tooling-and-mcp-servers.md`](skills/platform/tooling-and-mcp-servers.md)
- [`skills/governance/permissions-and-safety.md`](skills/governance/permissions-and-safety.md)
- [`skills/governance/verification-and-self-checking.md`](skills/governance/verification-and-self-checking.md)
- [`skills/delivery/prompting-precision.md`](skills/delivery/prompting-precision.md)
- [`skills/delivery/explore-plan-code-commit.md`](skills/delivery/explore-plan-code-commit.md)

### Kari Hytoenen
Credited as the originating author of the rich-context-input technique.
- [`skills/delivery/rich-context-input.md`](skills/delivery/rich-context-input.md)

## Internal Authorship (non-external, listed for completeness)

Several skills carry a generic internal-team byline rather than a named external source — these were authored in-house rather than adapted from a public source, so there's no external link to credit:

- "Workspace Delivery Skills", "Workspace Strategy Skills", "Workspace Refinement Skills", "Workspace Governance Skills", "Workspace Product Skills", "Workspace Orchestration Skills", "Workspace Journeys Skills", "Workspace Engineering Skills" — internal authoring placeholders across `skills/delivery/`, `skills/Strategy/`, `skills/Refinement/`, `skills/governance/`, `skills/product/`, `skills/orchestration/`, `skills/journeys/`, `skills/engineering/`
- [`skills/product/no-silo-product-operating-model.md`](skills/product/no-silo-product-operating-model.md) — a workspace-authored operating principle (cross-functional coupling + four-lens awareness), not adapted from an external source; it routes to the specific external/internal sources listed elsewhere in this file for each of its component checks.
- "PM Team" — `skills/product/competitor-analysis-synthesizer.md`, `skills/delivery/jira-epic-builder.md`, `skills/governance/defect-triage-assistant.md`

---

*If you contributed a source, technique, or correction to a skill in this repo and aren't credited here, please open an issue or PR.*
