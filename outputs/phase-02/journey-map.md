# Target-Hypothesis Journey — Appointment Request

> **SYNTHETIC DEMO DATA.** This is design framing, not an observed real-user journey.

| Stage | User goal/action | Evidence/basis | Friction or risk | Confidence | Validation need |
|---|---|---|---|---|---|
| 1. Start | Find clinic/service without calling | BRD; existing flow | Choice effort | MEDIUM | Observe real selection behavior |
| 2. Compare | See suitable times before personal data | P1/P5; synthetic survey; PP-01 | Exploration, stale slots, color-only state | MEDIUM | Test comparison and keyboard use |
| 3. Select | Choose a slot knowing it may change | R1; P5; T-102 | Slot becomes unavailable | MEDIUM | Confirm refresh capability and recovery |
| 4. Role | Identify self or caregiver booking | R11; P2; T-104 | Ownership and consent undefined | LOW / HYPOTHETICAL | Resolve policy and test comprehension |
| 5. Details | Provide only necessary information | R2/R3; P4; PP-02 | Mandatory fields, timeout, privacy | MEDIUM | Validate necessity, wording, warning, clearing |
| 6. Review | Check details and communication choices | Existing read-back; R7 | Marketing/channel consequences unclear | LOW / HYPOTHETICAL | Obtain policy decision and test choice |
| 7. Submit | Send once and understand processing | Latency; T-101; synthetic analytics | Duplicate action and long wait | MEDIUM | Confirm idempotency and progress feedback |
| 8. Outcome | Understand confirmed, pending, rejected, stale, or unavailable | R4; T-102/T-103 | Pending and recovery undefined | MEDIUM risk / LOW recovery | Define state contract |
| 9. Notify | Retain reference and know channel result | R5; T-106 | Partial delivery and recipients unresolved | MEDIUM | Define on-screen source of truth |
| 10. Cancel | Cancel and understand result | R6; T-103 | Cut-offs and failure unclear | MEDIUM gap | Define policy and outcome states |

Required states include loading, validation error, pending, rejection, timeout, unavailable service, stale slot, duplicate submit, notification failure, expiry, and cancellation outcomes. Persistent recovery remains blocked by R12/R13.

