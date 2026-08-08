# Traceable Pain Points — Community Clinic Appointment Booking

> **SYNTHETIC DEMO DATA.** These themes derive from fictional demonstration evidence and are not confirmed real-user findings.

| ID | Pain theme | Persona(s) | Evidence | Confidence | Impact/severity rationale |
|---|---|---|---|---|---|
| PP-01 | Finding a suitable slot may require excess exploration, and a selected slot can disappear before submission. | Time-Constrained Self-Booker | `synthetic-interview-notes.md` P1, P5; `synthetic-support-tickets.md` T-102; BRD stale-slot constraint supplies context | MEDIUM | Can cause repeated work or abandonment; prevalence is unknown because evidence is synthetic. |
| PP-02 | Timeout and recovery behavior is unclear while users are entering or retrieving information. | Time-Constrained Self-Booker | `synthetic-interview-notes.md` P4; `synthetic-support-tickets.md` T-105 | MEDIUM | Potential loss of sensitive progress and task restart; actual frequency is unknown. |
| PP-03 | Slow or unclear submission feedback may lead to duplicate actions and uncertain outcomes. | Time-Constrained Self-Booker | `synthetic-support-tickets.md` T-101, T-103; `synthetic-analytics-summary.md` second-submit signal | MEDIUM | Duplicate references or uncertain cancellation can create support demand; synthetic data cannot establish causation. |
| PP-04 | Caregiver booking does not clearly distinguish patient details, caregiver details, consent, or notification recipients. | Caregiver Coordinator | `synthetic-interview-notes.md` P2; `synthetic-support-tickets.md` T-104; `synthetic-survey-summary.md` caregiver signal | MEDIUM | Incorrect contact or disclosure could prevent coordination or create privacy concern; legal requirements remain unknown. |
| PP-05 | Availability and state communicated through color alone is not usable for the synthetic keyboard-dependent participant. | Access-and-Clarity-Dependent Booker | `synthetic-interview-notes.md` P3, P5; `design-system.md` provides corroborating constraint, not user evidence | LOW | May block slot identification; evidence is limited to authored walkthroughs and needs real accessibility validation. |
| PP-06 | Requiring both notification channels conflicts with differing synthetic preferences and uncertain partial-delivery behavior. | Time-Constrained Self-Booker; Caregiver Coordinator | `synthetic-interview-notes.md` P1 versus P4; `synthetic-survey-summary.md` channel split; `synthetic-support-tickets.md` T-106 | MEDIUM | Users may receive unwanted messages or lack clarity when one channel fails; no real preference distribution is known. |

## Design opportunity hypotheses

- **H-01:** Earlier, consolidated availability and nearby alternatives may reduce repeated exploration. This is a hypothesis, not a requirement.
- **H-02:** Explicit timeout warning, extension, and evidence-bounded recovery may reduce lost progress. R12/R13 must first be resolved.
- **H-03:** A submission lock with clear progress and outcome messaging may reduce duplicate actions. This requires technical confirmation.
- **H-04:** Separate patient/caregiver fields and explicit notification choices may reduce ambiguity, subject to consent/privacy decisions.
- **H-05:** Redundant textual and programmatic status may address color-only risk, subject to accessibility validation.

No challenge-agent risk was promoted to a pain point unless independently supported by the labelled synthetic research sources.

