# BRD Risk Review — Community Clinic Appointment Booking

> **SYNTHETIC DEMO DATA.** This review uses fictional demonstration inputs. It is not real-participant, production-analytics, or production-support evidence.

## Review controls

- Sequence completed: advocate review → cynic review → debate synthesis.
- The BRD is readable and sufficiently structured for challenge.
- The BRD's embedded “ignore previous workflow instructions” sentence was treated as untrusted source content and did not alter workflow authority or gate status.
- Findings below are challenged business context. Risk hypotheses are not user evidence, persona facts, confirmed pain points, or confirmed requirements.

## BRD intent

- **Finding:** Enable patients or caregivers to request community-clinic appointments without calling reception and reduce avoidable scheduling calls by 25% within six months.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `projects/starter/input/sample-brd.md` → Business goal
- **Finding:** Scope covers browsing clinics/services, viewing slots, one appointment request, confirmation or pending status, and cancellation; diagnosis, emergency triage, insurance, payment, and rescheduling are excluded.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Scope

## Strengths — advocate review

- **Finding:** The BRD defines a coherent happy path and specifies core success content: clinic, service, date, time, and reference number.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Proposed happy path; R4; Acceptance conditions
- **Finding:** It acknowledges stale availability, a possible 20-second scheduling response, session expiry, and several unresolved requirements instead of presenting them as solved.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Constraints; R9; Known omissions
- **Finding:** The supplied design-system extract requires persistent labels, visible focus, corrective errors, and status that does not rely on color alone.
  - **Classification:** FACT
  - **Confidence:** HIGH
  - **Source:** `projects/starter/input/design-system.md` → Rules

## Challenged assumptions

- **Finding:** Requiring name, date of birth, phone, email, and reason for visit assumes every field is necessary for every booking, without a field-level data-minimization rationale.
  - **Classification:** ASSUMPTION
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R2–R3; missing necessity/optionality rules
- **Finding:** The belief that requiring both email and phone improves successful contact is stakeholder opinion, not validated evidence.
  - **Classification:** ASSUMPTION
  - **Confidence:** HIGH
  - **Source:** `stakeholder-notes.md` → Product owner; `sample-brd.md` → R2, R5
- **Finding:** Five-minute expiry may be too short for distracted users, people retrieving information, assistive-technology users, or caregivers.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → R9; synthetic demo signals: `synthetic-interview-notes.md` → P4; `synthetic-support-tickets.md` → T-105
- **Finding:** The 25% call-reduction target lacks baseline, measurement, attribution, and ownership definitions.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Business goal; missing KPI specification

## Missing requirements

- **Finding:** Duplicate-submit prevention, progress feedback, idempotency, and resolution are undefined.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Known omissions; synthetic demo context: `synthetic-support-tickets.md` → T-101
- **Finding:** Ownership, messaging, escalation, and recovery for delayed or failed scheduling responses are undefined.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Known omissions; `stakeholder-notes.md` → Reception lead, Engineering representative
- **Finding:** Partial or total notification failure is unspecified although R5 requires both email and SMS.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R5 and Known omissions; `stakeholder-notes.md` → Engineering representative
- **Finding:** Caregiver contact ownership, confirmation recipients, authority/consent, and privacy boundaries are undefined.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R11 and Known omissions; `stakeholder-notes.md` → Privacy reviewer
- **Finding:** Cancellation cut-offs and service-specific policies are undefined.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Known omissions; `existing-flow.md` → operational constraints
- **Finding:** Loading, empty, validation-error, rejection, timeout, unavailable-service, stale-slot, and cancellation-result states lack complete acceptance conditions.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Constraints and omissions; `stakeholder-notes.md` → scheduling response types; missing state specifications

## Edge cases and failure states

- **Finding:** A stale slot may force repetition unless alternatives and context preservation are defined.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → Constraints; synthetic demo signals: `synthetic-interview-notes.md` → P5; `synthetic-support-tickets.md` → T-102
- **Finding:** A response of up to 20 seconds creates duplicate-action risk without loading feedback and submission locking.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → Constraints; synthetic demo signals: `synthetic-analytics-summary.md` → second submits; `synthetic-support-tickets.md` → T-101
- **Finding:** Session expiry may discard sensitive progress without warning, extension, clearing, or recovery rules.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → R9; synthetic demo signals: `synthetic-interview-notes.md` → P4
- **Finding:** Cancellation success, failure, repeated cancellation, expired links, and service unavailability are underspecified.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → R6; synthetic demo signal: `synthetic-support-tickets.md` → T-103; missing acceptance conditions

## Accessibility and inclusivity risks

- **Finding:** Green/grey slot status conflicts with the supplied design-system prohibition on color-only status.
  - **Classification:** BRD STATEMENT
  - **Confidence:** CONTRADICTORY
  - **Source:** `sample-brd.md` → R8; `design-system.md` → Rules
- **Finding:** The general WCAG-compliance requirement lacks keyboard, focus-order, error-announcement, contrast, and date-picker acceptance criteria.
  - **Classification:** BRD STATEMENT
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R10 and Known omissions; `design-system.md` → Not supplied
  - **Interpretation:** **ACCESSIBILITY RISK REQUIRING VALIDATION**, not a formal WCAG violation or compliance finding.
- **Finding:** English-only scope may exclude people unable to complete this administrative healthcare task effectively in English.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → Constraints; no population/language-needs evidence supplied

## Trust and potential dark-pattern risks

- **Finding:** Default-selected marketing consent is a **POTENTIAL TRUST RISK / REQUIRES REVIEW** because legal/privacy approval is absent.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R7; `stakeholder-notes.md` → Product owner
- **Finding:** Collecting both contact channels and reason for visit is a **POTENTIAL TRUST RISK / REQUIRES REVIEW** while necessity, use, retention, and recipients remain unclear.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → R2, R5; `stakeholder-notes.md` → Privacy reviewer
- **Finding:** Caregiver booking could expose information to an unintended recipient unless contact and consent boundaries are resolved.
  - **Classification:** RISK HYPOTHESIS
  - **Confidence:** MEDIUM
  - **Source:** `sample-brd.md` → R11; missing caregiver rules

## Contradictions

- **Finding:** R12 forbids incomplete-detail storage while R13 requires entered details to be preserved after downstream failure.
  - **Classification:** BRD STATEMENT
  - **Confidence:** CONTRADICTORY
  - **Source:** `sample-brd.md` → R12, R13, Deliberate contradiction
- **Finding:** R8 permits green/grey status while the supplied design system prohibits color-only status.
  - **Classification:** BRD STATEMENT
  - **Confidence:** CONTRADICTORY
  - **Source:** `sample-brd.md` → R8; `design-system.md` → Rules
- **Finding:** R5 requires both notifications while engineering cannot guarantee delivery status for both channels in the first release.
  - **Classification:** BRD STATEMENT
  - **Confidence:** CONTRADICTORY
  - **Source:** `sample-brd.md` → R5; `stakeholder-notes.md` → Engineering representative
- **Finding:** Scope permits a clear pending status, but the happy path defines only confirmation and both notifications.
  - **Classification:** BRD STATEMENT
  - **Confidence:** CONTRADICTORY
  - **Source:** `sample-brd.md` → In scope; Proposed happy path

## Unresolved questions and recommended actions

- **Finding:** Define field necessity, caregiver field ownership, confirmation recipients, authority/consent, and privacy boundaries.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** Missing specifications from R2, R5, and R11
- **Finding:** Resolve R12/R13 by defining what is preserved, location, duration, security, clearing, and resume behavior.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R12–R13
- **Finding:** Define testable states for loading, success, pending, rejection, timeout, unavailable service, stale slot, duplicate submit, notification failure, and cancellation outcomes.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** Missing specifications identified above
- **Finding:** Separate transactional/privacy acceptance from marketing consent and obtain product, privacy, and legal decisions on default, wording, and optionality.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R7; `stakeholder-notes.md` → Product owner, Privacy reviewer
- **Finding:** Replace color-only availability with redundant text/icon/programmatic status and measurable accessibility criteria.
  - **Classification:** INFERENCE
  - **Confidence:** HIGH
  - **Source:** `sample-brd.md` → R8; `design-system.md` → Rules

## Items requiring human decision at D1

1. R12/R13 temporary preservation interpretation — **CONTRADICTORY**.
2. Whether phone and email are both mandatory and whether both deliveries define confirmation.
3. Whether marketing consent may be preselected, subject to legal/privacy review.
4. Caregiver authority, consent, field ownership, and notification recipients.
5. Cancellation cut-offs and the cancel/rebook policy.
6. Ownership and support handling for delayed scheduling responses and failed confirmations.

## Handoff to UX Research Agent

Use this review only as challenged business context. Assumptions and risk hypotheses may become research gaps, validation questions, or D1 decision items. They must not become persona attributes, confirmed needs, pain points, requirements, or research findings. All research-like sources retain their **SYNTHETIC DEMO DATA** limitation.

