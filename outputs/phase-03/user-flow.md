# User Flow — Availability-First Guided Request

> **SYNTHETIC DEMO DATA.** This flow is not validated, verified, or evidence of WCAG compliance.

## Constraints

No account, payment, diagnosis, rescheduling, emergency triage, slot holding, persistent recovery, caregiver policy, cancellation cut-off, or delivery guarantee is assumed. R12/R13 remains unresolved.

| ID | Step | Result/decision | Traceability |
|---|---|---|---|
| F01 | Open booking | Search or exit | Concept A; journey 1 |
| F02 | Select clinic/service | Both required | R1; PD-01 |
| F03 | Request availability | Loading, results, empty, unavailable | OP-01 |
| F04 | Compare/select slot | Continue, change search, exit | PD-01; OP-04 |
| F05 | Select self/someone else | Caregiver policy remains unresolved | R11; PD-03 |
| F06 | Enter BRD-required details | Field validation | R2–R3 |
| F07 | Review details, privacy, notifications, marketing | Edit or accept privacy | R5, R7; PD-05 |
| F08 | Submit once | Controls lock; processing appears | R4; OP-02 |
| F09 | Receive outcome | Confirmed, pending, rejected, stale, timeout, unavailable | Journey 8 |
| F10 | View confirmation details/reference | Finish or exit | Acceptance condition |
| F11 | View notification status | Both/partial/unresolved | R5; OP-06 |
| F12 | Open cancellation link | Enter reference and DOB | R6 |
| F13 | Process cancellation | Cancelled, rejected, timeout, unavailable | OP-07 |
| F14 | Exit | No restoration promise | R9; R12/R13 |

## Recovery rules

- Empty results allow changing date, clinic, or service.
- Stale slots clear selection and refresh availability.
- Invalid fields retain values in the active session and receive corrective text.
- Submission locks after first activation; backend idempotency remains unresolved.
- Pending and unknown outcomes are never called confirmed.
- Session expiry clears active interaction; persistent restoration is unavailable.
- Cancellation failure never implies whether the appointment remains or was cancelled.

