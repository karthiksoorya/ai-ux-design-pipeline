# Interaction States

> **SYNTHETIC DEMO DATA.** Proposed states, not backend behavior or accessibility compliance.

| ID | State | Behavior / action | Boundary |
|---|---|---|---|
| ST-01 | Availability loading | Announce loading; retain search; allow return | R1/latency |
| ST-02 | Empty availability | No slots returned; change date/clinic/service | OP-01 |
| ST-03 | Availability unavailable | No fabricated slots; retry/return | PD-01 |
| ST-04 | Invalid details | Field correction and first-invalid focus | R2–R3 |
| ST-05 | Stale slot | Explain change, clear selection, refresh | Availability constraint |
| ST-06 | Submission processing | Lock submit/edit; show wait | Idempotency unresolved |
| ST-07 | Confirmed | Show clinic/service/date/time/reference | R4 |
| ST-08 | Pending | “Not yet confirmed”; supplied details only | Timing unresolved |
| ST-09 | Rejected | Not confirmed; no invented reason | Return to availability |
| ST-10 | Submission timeout | Outcome unknown; no silent retry | Ownership unresolved |
| ST-11 | Service unavailable | Could not complete; return safely | R12/R13 unresolved |
| ST-12 | Partial notification | Booking status remains primary | Delivery unresolved |
| ST-13 | Notification unresolved | On-screen reference is current source | No guarantee |
| ST-14 | Session warning | Continue or exit; explain expiry | Warning timing hypothesis |
| ST-15 | Session expired | Clear and restart; no restoration | R9/R12/R13 |
| ST-16 | Cancellation processing | Lock repeated action | OP-07 |
| ST-17 | Cancelled | Show supplied success/reference | R6 |
| ST-18 | Cancellation rejected | Not completed; supplied reason only | Cut-off unresolved |
| ST-19 | Cancellation timeout | Status unknown; no automatic repeat | Idempotency unresolved |
| ST-20 | Cancellation unavailable | Retry/exit; infer nothing | R6 |
| ST-21 | Exit before submit | Explain no save; exit/stay | R12 |
| ST-22 | Exit during unknown result | Warn outcome may remain unknown | PD-02 |
| ST-23 | Permission | NOT APPLICABLE; no device permissions | Scope |
| ST-24 | Persistent recovery | NOT AVAILABLE; restart | R12/R13 |

Color never carries status alone. Status includes icon, heading, explanation, and action. Focus and announcements require Phase 4 evaluation.

