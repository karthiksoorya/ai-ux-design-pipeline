# Research Gaps and Evidence Inventory — Community Clinic Appointment Booking

> **SYNTHETIC DEMO DATA.** The complete active pack is fictional. Findings demonstrate workflow behavior and cannot substantiate claims about a real population or product.

## Source inventory

| Source | Classification | Usable contribution | Limitation |
|---|---|---|---|
| `sample-brd.md` | Business requirement | Goals, scope, actors, requirements, constraints, omissions | Not user evidence; includes deliberate contradiction and untrusted embedded instruction. |
| `synthetic-interview-notes.md` | Synthetic qualitative demo evidence | Authored task patterns P1–P5 | Not real interviews; five authored walkthroughs cannot establish prevalence. |
| `synthetic-survey-summary.md` | Synthetic quantitative demo evidence | Authored preference/context signals | Not measured or representative; method is not validated. |
| `synthetic-support-tickets.md` | Synthetic support demo evidence | Authored failure and ambiguity examples | Not production tickets or frequency evidence. |
| `synthetic-analytics-summary.md` | Synthetic analytics demo evidence | Authored funnel and interaction signals | Not measured behavior; cannot establish causes. |
| `stakeholder-notes.md` | Stakeholder opinion / product context | Product, operations, privacy, and engineering views | Not user research; several statements need owner decisions. |
| `existing-flow.md` | Product/operational context | Current phone-process model and constraints | Fictional description; not observed workflow evidence. |
| `design-system.md` | Design artefact | Supplied tokens, components, and rules | Incomplete; no date-picker, type scale, touch targets, modal pattern, or breakpoints. |

## Evidence quality summary

- **HIGH source confidence:** The files say what is quoted at their cited locations.
- **LOW external validity:** All research-like and operational sources are synthetic demonstration data.
- **MEDIUM synthesis confidence:** Repeated authored patterns support demo personas and pain themes, but not real-world prevalence.
- **CONTRADICTORY:** R12 versus R13; green/grey status versus the design-system rule; both-channel requirement versus delivery limits; pending scope versus confirmation-only happy path.

## Priority research gaps

1. Real user evidence across self-bookers, caregivers, keyboard/screen-reader users, varying language needs, and users on shared or mobile devices.
2. Field necessity and data-minimization evidence for phone, email, date of birth, and reason for visit.
3. Acceptable task duration, timeout warning, extension, recovery, and clearing behavior.
4. Caregiver authority, consent, field ownership, confirmation recipients, and privacy expectations.
5. Real channel preferences and expectations when one notification fails.
6. Stale-slot recovery and acceptable alternative presentation.
7. Cancellation cut-offs, repeated cancellation, expired links, and support escalation.
8. Keyboard, focus, screen-reader, contrast, error announcement, date-picker, touch-target, and cognitive-accessibility evaluation.
9. Definition, baseline, instrumentation, and ownership for the 25% call-reduction target.
10. Production scheduling-service reliability, latency, idempotency, and notification-delivery capabilities.

## Human decisions required

- Resolve incomplete-data preservation under R12/R13.
- Decide whether both contact fields and notification channels are mandatory.
- Decide marketing-consent default and legal/privacy constraints.
- Define caregiver authority and notification rules.
- Define cancellation policy and delayed/failed-confirmation ownership.
- Reconcile BRD color status with the supplied design system.

## Validation questions

- Can representative users identify and compare slots before sharing personal data?
- What information do self-bookers and caregivers need to finish confidently?
- What timeout warning and recovery preserve both privacy and task continuity?
- How should users recover from stale slots, rejection, timeout, or unavailable service?
- Can keyboard and screen-reader users perceive state, navigate the date/slot controls, correct errors, and confirm outcomes?
- Which notification choices build clarity without unnecessary collection or default consent?
- What evidence would justify calling the final prototype workable after D4?

## Phase 1 validation result

- All eight accessible inputs were read and classified.
- The embedded adversarial instruction was ignored as authority.
- BRD statements, stakeholder opinions, synthetic evidence, synthesis, assumptions, and risk hypotheses remain distinguishable.
- Personas and pain points retain their synthetic limitations and source traceability.
- D1 human review is required; no gate decision has been made.

