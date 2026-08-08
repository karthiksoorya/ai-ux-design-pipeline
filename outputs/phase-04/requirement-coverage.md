# Requirement Coverage — D3-Approved Clinic Appointment Demo

> Coverage is limited to inspected documentation and the local synthetic prototype. It does not demonstrate backend feasibility, production behavior, real notification delivery, empirical usability, or legal/accessibility compliance.

| Requirement | BRD source | Status | Design/prototype locator | Rationale / gap |
|---|---|---|---|---|
| R1 — Show scheduling-service slots | `sample-brd.md` R1 | COVERED | `user-flow.md` F02–F04; prototype steps 1–2 | The demo visibly presents fictional availability. No live scheduling-service integration is claimed. |
| R2 — Require name, DOB, phone, email, reason | `sample-brd.md` R2 | PARTIALLY COVERED | `screen-spec.md` S03; prototype step 3 | The UI contains all fields, but code does not require reason for visit and applies no content-format rules. |
| R3 — Block submission until required fields complete | `sample-brd.md` R3 | COVERED | `interaction-states.md` ST-04; prototype steps 3–4 | Empty coded-required fields and missing privacy consent block progress/submission, although error accessibility is deficient. |
| R4 — On-screen outcome | `sample-brd.md` R4 | COVERED | `screen-spec.md` S05; prototype step 5 | Confirmed, pending, rejected, timeout, unavailable, stale, and partial-notification outcomes are simulated and shown. |
| R5 — Send email and SMS confirmation | `sample-brd.md` R5 | PARTIALLY COVERED | `user-flow.md` F11; prototype simulated outcome selector | Notification status is demonstrated only; no email/SMS is sent and the BRD/engineering contradiction remains. |
| R6 — Cancel through confirmation link | `sample-brd.md` R6 | NOT COVERED | Design only: F12–F13, S06–S07, ST-16–ST-20 | No cancellation entry, authentication, processing, or result exists in the runnable prototype. |
| R7 — Marketing selected by default | `sample-brd.md` R7 | REQUIRES HUMAN DECISION | `screen-spec.md` S04; prototype step 4 | Demo intentionally leaves marketing unchecked to avoid implementing an unresolved potential trust/legal risk. This does not amend R7. |
| R8 — Green available / grey unavailable | `sample-brd.md` R8 | COVERED | Prototype step 2; `design-system.md` non-color rule | Availability is distinguishable with text and disabled state, not color alone, resolving the presentation risk in the demo while preserving status meaning. |
| R9 — Five-minute inactivity expiry | `sample-brd.md` R9 | NOT COVERED | Design only: ST-14–ST-15 | No timer, warning, continuation, clearing, or expiry behavior exists in the runnable prototype. |
| R10 — Accessible and WCAG compliant | `sample-brd.md` R10 | PARTIALLY COVERED | `accessibility-audit.md`; prototype HTML/CSS | Several accessible patterns exist, but error/focus issues remain and the broad compliance claim lacks sufficient criteria and human/assistive-technology verification. |
| R11 — Caregiver may book for another person | `sample-brd.md` R11 | PARTIALLY COVERED | F05; S03; prototype role selector | “Someone else” is selectable, but authority, consent, field ownership, and recipients are intentionally unresolved. |
| R12 — Never store incomplete details | `sample-brd.md` R12 | PARTIALLY COVERED | `prototype-spec.md`; in-memory `app.js` data | No persistence or analytics is implemented and reload clears the demo, but live-session data exists in memory and no production storage evidence exists. |
| R13 — Preserve entered details after scheduling failure | `sample-brd.md` R13 | REQUIRES HUMAN DECISION | F14; ST-24; `prototype-spec.md` exclusions | Persistent recovery is not implemented because R12/R13 contradict each other; the required preservation scope, duration, and security need a human decision. |

## Coverage conclusion

The appointment-request happy path is substantially represented, but cancellation and inactivity expiry are missing from the runnable prototype. Notification delivery, caregiver rules, marketing default, accessibility compliance, and R12/R13 recovery cannot be declared complete from the available evidence.

