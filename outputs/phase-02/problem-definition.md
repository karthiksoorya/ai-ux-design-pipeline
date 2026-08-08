# Problem Definition — Community Clinic Appointment Booking

> **SYNTHETIC DEMO DATA.** This definition is for workflow demonstration, not validated evidence about real clinic users.

## Boundaries

- BRD requirements are business evidence, not user evidence.
- Synthetic interviews, surveys, tickets, and analytics retain their stated limitations.
- D1 approval permits definition work but does not resolve R12/R13, caregiver policy, notification policy, marketing consent, cancellation rules, or accessibility criteria.

## PD-01 — Efficient discovery and resilient slot selection

- **User/context:** Time-Constrained Self-Booker seeking a routine appointment.
- **Problem:** Comparing availability may require excess exploration, and a selected slot can disappear before submission.
- **Evidence:** `persona.md` Persona 1; `pain-points.md` PP-01; synthetic P1/P5 and T-102.
- **Impact:** Repeated work, abandonment, or return to telephone booking.
- **Business relevance:** Call-reduction goal; R1; changing-availability constraint.
- **Confidence:** MEDIUM.
- **Assumption:** Consolidated or nearby availability reduces effort.
- **Validation:** Test comparison and stale-slot recovery with representative users.

## PD-02 — Clear, recoverable submission outcomes

- **User/context:** Self-booker submitting while the scheduling service is slow or unavailable.
- **Problem:** Unclear feedback can cause duplicate submissions, uncertain outcomes, and lost progress.
- **Evidence:** Persona 1; PP-02/PP-03; synthetic T-101/T-103/T-105 and second-submit signal.
- **Impact:** Duplicate references, support demand, restart, and uncertainty.
- **Business relevance:** R4, R9, R12, R13; latency constraint.
- **Confidence:** MEDIUM.
- **Contradiction:** R12 forbids incomplete storage; R13 asks to preserve details.
- **Validation:** Define idempotency/outcome states and resolve permissible recovery first.

## PD-03 — Unambiguous caregiver booking

- **User/context:** Caregiver Coordinator booking for another person.
- **Problem:** Patient data, caregiver data, authority, consent, and recipients are not distinguished.
- **Evidence:** Persona 2; PP-04; synthetic P2, T-104, and caregiver survey signal; R11 is business scope only.
- **Impact:** Incorrect contact, coordination failure, or privacy concern.
- **Confidence:** MEDIUM for ambiguity; LOW for any policy solution.
- **Validation:** Authorized decision on role, consent, field ownership, and recipients.

## PD-04 — Perceivable and operable status

- **User/context:** Access-and-Clarity-Dependent Booker.
- **Problem:** Slot and outcome states may be ambiguous when conveyed by color or without focus/announcement rules.
- **Evidence:** Persona 3; PP-05; synthetic P3/P5; supplied design-system rules.
- **Impact:** Potential inability to select, correct, or understand an outcome.
- **Business relevance:** R8 and R10.
- **Confidence:** LOW.
- **Contradiction:** Green/grey status conflicts with the design-system rule.
- **Validation:** Keyboard, screen-reader, contrast, focus, error, and date-control evaluation; no WCAG claim.

## PD-05 — Proportionate contact and consent

- **User/context:** Self-bookers and caregivers with differing channel preferences.
- **Problem:** Both channels are required despite differing preferences and uncertain delivery; marketing consent is preselected.
- **Evidence:** PP-06; synthetic P1/P4, survey split, T-106; stakeholder opinion.
- **Impact:** Unwanted contact, unnecessary collection, or unclear confirmation.
- **Confidence:** MEDIUM for conflict; LOW for prevalence.
- **Validation:** Product/privacy/legal decisions on fields, notification semantics, and marketing default.

## Priority

PD-01 and PD-02 have the strongest combined evidence/business relevance. PD-04 may be a task blocker but has limited evidence. PD-03 and PD-05 remain constrained by unresolved policy.

