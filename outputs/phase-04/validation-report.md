# Phase 4 Validation Report — Community Clinic Appointment Demo

> **SYNTHETIC / HEURISTIC VALIDATION.** No real participants were observed. Findings come from traceable artefact review, static inspection, and interactive walkthrough of the local prototype on 2026-08-08. This is not empirical usability evidence, production validation, or a WCAG compliance determination.

## Scope and method

- Entry condition: explicit human D3 APPROVE recorded in `outputs/reviews/d3-review.md`.
- Prototype inspected: `outputs/phase-03/prototype/index.html`, `styles.css`, and `app.js`, served locally and exercised in the in-app browser.
- Evidence compared: the synthetic BRD and supplied design-system extract, approved Phase 1 risk review/persona, selected Phase 2 concept, and Phase 3 flow, screen, state, and prototype specifications.
- Interactive checks used fictional values only. No network request, real booking, notification, storage, or participant session occurred.

## Synthetic usability walkthroughs

| Walkthrough | SYNTHETIC / HEURISTIC result | Evidence and potential friction |
|---|---|---|
| Find a routine slot before entering personal data | PASS | Search opens availability, displays text-labelled available/unavailable states, and keeps personal fields until step 3. Prototype steps 1–3; R1/R8. |
| Attempt to continue with missing required details | PARTIAL | Progress is blocked with corrective text, but the error is a single summary, is not associated with fields, and focus remains on the triggering button rather than moving to the first invalid control. Prototype step 3; ST-04. |
| Review and submit a request | PASS WITH LIMITATIONS | Review exposes privacy and optional marketing separately; privacy blocks submission; submit disables during processing. Notification promises are simulated only. Prototype step 4; R3/R4/R5/R7. |
| Interpret an unknown/timeout outcome | PASS | The result says “Outcome unknown” and explicitly says not to assume success. Prototype step 5; ST-10. |
| Recover from a stale slot | PARTIAL | The simulated stale outcome provides “View refreshed availability,” but it is available only after data entry and submission; no live stale-slot detection or preserved-data contract exists. ST-05; R12/R13 remain unresolved. |
| Book for someone else | PARTIAL | A role option exists, but its label states that policy is unresolved and the UI supplies no authority, consent, field-ownership, or recipient guidance. R11; PD-03. |
| Cancel a confirmed booking | FAIL | The approved flow/specification defines cancellation screens and states, but the runnable prototype contains no cancellation entry or outcome flow. F12–F13; S06–S07; ST-16–ST-20; R6. |
| Respond to session warning/expiry | FAIL | Session warning and expiry are specified but not implemented in the runnable prototype. ST-14–ST-15; R9. |

These walkthroughs identify hypotheses for real-user testing. They do not establish task success rates, completion times, satisfaction, accessibility conformance, or behavioral prevalence.

## Cognitive friction analysis

**SYNTHETIC / HEURISTIC SCORE: 14/25 — moderate potential friction** (lower is better).

Method: five dimensions were rated from 1 (low potential burden) to 5 (high potential burden), using the interactive walkthrough and approved artefacts: navigation/sequence 2, form burden 3, decision clarity 3, recovery clarity 4, and status comprehension 2. Evidence basis includes the five-step prototype, required contact/patient fields, unresolved caregiver and notification policies, missing cancellation/session recovery, and explicit pending/timeout wording.

Limitations: this score is an analyst heuristic, not measured cognition or user behavior. It is not comparable to a benchmark and must be validated with representative participants, including caregivers, distracted users, and assistive-technology users.

## Accessibility audit summary

- Positive evidence: semantic `main`, heading hierarchy, persistent visible labels, native controls, visible focus styling, text plus visual status, and marketing consent off by default.
- Potential issues: missing first-invalid focus, errors not programmatically associated or announced, broad `aria-live` replacement, missing semantic input types/autocomplete, and unimplemented session/cancellation states.
- Measured supplied color pairs meet common text/non-text contrast thresholds in isolation; this does not establish page-level or WCAG conformance.
- Full evidence is in `outputs/phase-04/accessibility-audit.md`.

## Design-system audit

The supplied system is **AVAILABLE BUT INCOMPLETE** (`projects/starter/input/design-system.md`).

| Rule/evidence | Result |
|---|---|
| Primary/error/focus colors and 8px spacing basis | CONFORMS for inspected declared values; computed contrast is recorded in the accessibility audit. |
| Status cannot rely on color alone | CONFORMS in implemented slot and outcome states through text/icon/heading. |
| Every input has a persistent visible label | CONFORMS for implemented controls. |
| Focus indicators remain visible | CONFORMS statically; keyboard behavior still requires human/assistive-technology validation. |
| Errors identify the field and corrective action | DEVIATES: one generic message covers four fields and is not field-associated. |
| Primary button states | PARTIAL: default, focus, disabled/loading are represented; no supplied reference exists to confirm all visual details. |

Typography, touch targets, date-picker behavior, modal patterns, and responsive breakpoints were not supplied, so conformity cannot be determined.

## Requirement coverage summary

- COVERED: 4 (`R1`, `R3`, `R4`, `R8`).
- PARTIALLY COVERED: 5 (`R2`, `R5`, `R10`, `R11`, `R12`).
- NOT COVERED: 2 (`R6`, `R9`).
- REQUIRES HUMAN DECISION: 2 (`R7`, `R13`).

See `outputs/phase-04/requirement-coverage.md` for source-to-prototype traceability.

## Phase 1 risk and edge-case dispositions

Original classifications and confidence remain as recorded in `outputs/phase-01/brd-risk-review.md`.

| Phase 1 finding | Original classification / confidence | Current disposition | Phase 3/4 evidence |
|---|---|---|---|
| All R2 fields may not be necessary | ASSUMPTION / HIGH | UNRESOLVED | Prototype requires name, DOB, phone, and email; reason is displayed but not required in code. No minimization decision exists. |
| Five-minute expiry may burden users | RISK HYPOTHESIS / MEDIUM | UNRESOLVED | Session expiry is absent from runnable prototype. |
| Duplicate action during delayed response | RISK HYPOTHESIS / MEDIUM | PARTIALLY ADDRESSED | Submit disables and shows processing; backend idempotency and 20-second behavior are not testable. |
| Stale slot forces repetition | RISK HYPOTHESIS / HIGH | PARTIALLY ADDRESSED | A simulated stale outcome returns to availability, but data preservation and real refresh behavior are unresolved. |
| Cancellation failures are underspecified | RISK HYPOTHESIS / MEDIUM | UNRESOLVED | Cancellation exists only in design artefacts, not the runnable prototype. |
| Green/grey conflicts with non-color rule | BRD STATEMENT / CONTRADICTORY | ADDRESSED in prototype | Implemented states use text and visual symbols; the BRD contradiction still requires product resolution. |
| General accessibility claim lacks criteria | BRD STATEMENT / HIGH | PARTIALLY ADDRESSED | Evidence-bounded audit exists; full WCAG claim remains unsupported. |
| Default marketing consent trust risk | RISK HYPOTHESIS / HIGH | PARTIALLY ADDRESSED | Demo leaves marketing unchecked, pending legal/product decision; R7 remains undecided. |
| Caregiver disclosure/consent risk | RISK HYPOTHESIS / MEDIUM | UNRESOLVED | Role option exists without authority or recipient rules. |
| R12/R13 preservation contradiction | BRD STATEMENT / CONTRADICTORY | UNRESOLVED | Demo stores only in memory during the active page and clears on reload; it does not implement failure recovery. |
| R5 delivery guarantee contradiction | BRD STATEMENT / CONTRADICTORY | UNRESOLVED | Outcomes are simulated and no email/SMS integration exists. |

## Validation conclusion

The prototype demonstrates the main appointment-request path and several critical outcome states, but it does not fully implement the D3-approved scope. Cancellation and session expiry are material missing paths, while accessible error/focus behavior and caregiver rules require revision or explicit acceptance. The prototype remains **unverified** pending an explicit human D4 decision.

