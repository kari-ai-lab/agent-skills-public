# Skill Name: Agent Zero-Trust Delegation Skeleton

## 🎯 Objective
A reference skeleton for designing or reviewing how AI agents authenticate and get authorized against a platform/application. Grounded in zero trust: an agent is never implicitly trusted, never inherits a human's full entitlements, and any access it does get is a narrow, time-boxed delegation — never a standing or long-running credential. Includes explicit defenses against an agent masquerading as the human it's acting for, including via stolen/reused human credentials.

## 👤 Target Persona
Platform/security engineer designing an agent-to-application authorization model, or an agent reviewing/implementing agent access controls for a system it's integrating with.

## 📥 Inputs Required
- **Task allocation decision** — has `product/ai-human-task-allocation-model.md` already classified which tasks in this workflow are AI-owned, Human-owned, Interchangeable, or Never-AI? That skill answers the design-time "should this route to AI at all" question; this skill assumes that answer exists and covers the runtime "how is the agent's access to an AI-owned/Interchangeable task properly bounded" question instead. Run that skill first if it hasn't been.
- **Platform's existing auth model** — how do human users authenticate today, and what roles/permissions exist to delegate?
- **Agent use cases** — what workflows does the agent need to perform (read-only lookups, write actions, multi-step workflows)?
- **Human-in-the-loop model** — is there always a human present who is initiating/supervising the agent's task, or can the agent run unattended?
- **Existing token/session infrastructure** — OAuth2, signed JWTs, capability tokens, API keys — what's already available to build on?
- **Available step-up/MFA factors** — WebAuthn/passkeys, push MFA, SMS/TOTP, in-app confirmation — what can serve as a human-presence challenge at grant issuance?

## 📤 Expected Output
- An agent identity model distinct from user identity
- A delegation-grant structure (who delegated, what role, what scope, when it expires)
- A concrete TTL policy with numbers, not vague "short-lived" language
- Enforcement, renewal, revocation, and audit mechanics
- A masquerade-defense plan: how agents are structurally prevented from holding human credential material, the human-presence challenge required to mint a grant, and the detection/auto-block behavior for masquerade attempts

## 🤖 Core Prompt / Instructions
```text
You are designing (or reviewing) an authorization model for AI agents acting
against a platform/application. Apply zero trust as the foundation: never
trust by default, verify every request, grant the least privilege necessary,
and treat every session — including the current one — as something that
must re-earn trust rather than something assumed to still be valid.

Work through these building blocks:

1. AGENT IS A DISTINCT PRINCIPAL, NOT A USER ALIAS
   An agent acting "on behalf of" a human is a delegation relationship, not
   an identity assumption. Model it as its own principal type:
     agent:<agent_id>  acting_for  user:<user_id>
   Never let an agent authenticate AS the user (reusing the user's own
   session token/cookie/credential). Every downstream system, log, and
   audit trail must be able to tell "the agent did this for the user" apart
   from "the user did this directly."

2. NO IMPLICIT INHERITANCE OF THE HUMAN'S ENTITLEMENTS
   The human's full permission set is a CEILING, never a default. An agent
   never receives "everything this user can do." It receives a SUBSET the
   human explicitly delegates, chosen from roles the human is themselves
   authorized to delegate (not roles the human merely holds but cannot
   grant onward, and never roles beyond what the human holds — no
   privilege escalation through the agent).

3. DELEGATION GRANT STRUCTURE
   Every agent access grant should carry, explicitly:
     - delegator: which human user authorized this
     - agent_id: which agent/session is acting
     - role / scope: the specific delegable role, ideally narrowed further
       to specific resources/actions the task actually needs (least
       privilege beyond just picking a coarse role)
     - task_binding: what task/session this grant is for — a grant issued
       for "summarize my inbox" should not authorize "send email"
     - issued_at / expires_at: see TTL policy below — expires_at is
       mandatory, not optional
     - revocation reference: a way to invalidate this grant before natural
       expiry (see step 6)

4. TTL POLICY — THIS IS NOT NEGOTIABLE
   - No permanent or standing agent entitlement, ever. Every grant expires.
   - No long-running grants either: "long-running" means anything measured
     in hours. Do not issue multi-hour agent tokens even for supposedly
     trusted internal agents.
   - Grants are measured in MINUTES: default to 15 minutes, cap at 30
     minutes, sized to let the agent finish its bounded workflow and no
     more. Pick the smallest window that comfortably covers the task.
   - If a workflow genuinely needs longer, that is a signal to break it
     into smaller re-authorized steps, not to widen the window. A workflow
     that structurally requires hours of standing access needs a different
     architecture (queued/reviewed batch job with its own controls), not a
     stretched agent grant.
   - When the window expires mid-task, the agent halts and requests a fresh
     grant — it does not self-extend. A silent auto-renew that never
     re-checks with the human/platform is a long-running credential wearing
     a short-TTL costume; don't build that.

5. ENFORCEMENT (POLICY DECISION POINT)
   Every request from an agent principal must be checked at the boundary,
   every time, not just at session start:
     - Is this actually an agent principal (not a spoofed/reused user token)?
     - Is there a valid, unexpired delegation grant for this agent+task?
     - Does the requested action fall inside the grant's role/scope, not
       just "is the agent authenticated"?
     - Has the grant been revoked since issuance?
   Treat "authenticated" and "authorized for this specific call" as two
   separate checks — a valid but expired or out-of-scope grant must be
   rejected even though the agent's identity itself is legitimate.

6. REVOCATION AND CONTINUOUS VERIFICATION
   TTL expiry is the floor, not the only control. Provide an explicit
   revoke path the human or platform can trigger mid-window (task
   cancelled, anomaly detected, human steps away). Agents must check
   revocation status per-call, not cache "still valid" for the life of the
   grant.

7. NO SUB-DELEGATION WITHOUT GOING THROUGH THE SAME FLOW
   An agent holding a delegated grant must not delegate a role onward to
   another agent by simply forwarding its own grant. Any further delegation
   re-enters this same model from step 2 (explicit, scoped, human-approved,
   freshly time-boxed) — no implicit chains of trust.

8. AUDIT
   Log every delegation grant issuance, every action taken under it, and
   every expiry/revocation event — attributed to (agent_id, delegator,
   task_binding), kept distinct from the human's own direct-action audit
   trail so "what did the agent do on my behalf" is independently
   reviewable.

9. AGENTS MUST NEVER HOLD THE HUMAN'S ACTUAL CREDENTIAL MATERIAL
   This is the primary defense against masquerading, and it's structural,
   not detective: an agent's execution environment must never receive,
   store, or have code-path access to the human's real authentication
   factors — password, live session cookie, personal long-lived API token,
   browser session, passkey private key. The agent's ONLY credential is its
   own agent identity plus the short-TTL delegation grant from steps 3-4.
   If this holds, there is nothing for a compromised agent to "steal" — the
   worst case is misuse of its own narrow, fast-expiring grant, not full
   account takeover.
   Anti-patterns to explicitly reject in review:
     - injecting the human's password into an agent's environment/config
     - a headless browser autofilling the human's login form
     - copying a live human session cookie into the agent's HTTP client
     - an agent holding a personal access token that was minted for a human
   If a legacy integration only supports one of these patterns, that's a
   signal it needs a real service-identity/OAuth delegation flow before an
   agent is allowed to touch it — not a workaround that hands the agent the
   human's standing identity.

10. HUMAN-PRESENCE CHALLENGE AT GRANT ISSUANCE
   Minting or renewing a delegation grant requires a FRESH proof of human
   presence bound to that specific request — not "the human logged in at
   some point earlier today." Use a step-up factor the agent cannot itself
   satisfy: a WebAuthn/passkey tap, a push-MFA approval that names the
   specific agent/task/scope being requested, or an explicit in-app
   confirmation that states what's being delegated and for how long.
     - Bind the proof cryptographically to the grant it authorizes (sign
       over role, scope, task_binding, and expires_at) so a captured
       approval can't be replayed later to mint a broader or different
       grant.
     - The challenge must be something only the human can complete. An
       agent that can answer its own MFA prompt, auto-click its own
       confirmation dialog, or hold the factor needed to pass the
       challenge has turned the challenge into just another secret it
       holds — this defeats the entire control.

11. DETECT AND HARD-BLOCK MASQUERADE ATTEMPTS
   Treat any of the following as a security incident (auto-block +
   alert + revoke), not a normal auth failure to log and move past:
     - a request presents human-identity credential material (password,
       session cookie, personal long-lived token) from an execution
       context that is flagged, tagged, or otherwise known as agent/
       automated
     - a session/principal tagged as an agent attempts an action that
       should only be reachable from an interactive human-authenticated
       session (e.g. changing account recovery settings, approving or
       widening its own delegation grant, disabling the challenge in
       step 10)
     - behavioral signals inconsistent with the claimed session type: an
       "interactive human login" session exhibiting machine-speed/
       machine-regular request cadence, missing expected client-side
       signals (interactive rendering flow, expected browser fingerprint)
       for a flow that's supposed to be human-driven
   Wire every one of these to the revocation path (step 6) and an alert —
   detection that only logs and continues is not a control.

Now apply this to the described platform:
Existing auth model: $EXISTING_AUTH_MODEL
Agent use cases: $AGENT_USE_CASES
Human-in-the-loop model: $HUMAN_IN_THE_LOOP_MODEL
Existing token infrastructure: $EXISTING_TOKEN_INFRASTRUCTURE

Produce: the agent identity model, the delegation grant schema, the TTL
policy (with actual minute values, sized per use case), the
enforcement/renewal/revocation/audit mechanics, the specific human-presence
challenge mechanism used at grant issuance, and the concrete masquerade
detection signals + auto-block behavior for this platform — reusing
existing token infrastructure where possible rather than inventing a
parallel system.
```

## ✅ Success Criteria / Quality Checklist
- [ ] Agent principal is modeled distinctly from the user principal — no reuse of the user's own session credential
- [ ] No grant gives an agent the human's full entitlement set by default
- [ ] Every delegation grant has an explicit, mandatory `expires_at`
- [ ] No grant's TTL exceeds 30 minutes; nothing is described as "long-running" (multi-hour) or permanent
- [ ] Expired grants cause the agent to halt and re-request, not silently self-renew
- [ ] Enforcement checks scope and expiry on every call, not just at session start
- [ ] A revocation path exists and is checked per-call, independent of TTL
- [ ] Sub-delegation (agent-to-agent) re-enters the same human-approved flow rather than forwarding an existing grant
- [ ] Agent-attributed actions are separately auditable from the human's own direct actions
- [ ] Agents never hold or have code-path access to the human's actual credential material (password, session cookie, long-lived personal token) — only their own agent identity + delegation grant
- [ ] Delegation grant issuance requires a fresh, request-bound human-presence challenge that an agent cannot complete on the human's behalf
- [ ] Masquerade attempts (agent context presenting human credential material, or an agent-tagged session attempting a human-only action) are auto-blocked and trigger revocation + alert — not just logged

---
**Metadata**
- **Version:** 1.1
- **Last Updated:** 2026-07-19
- **Author:** Workspace Governance Skills
