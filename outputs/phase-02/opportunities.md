# Prioritized Opportunity Hypotheses

> **SYNTHETIC DEMO DATA.** Opportunities are hypotheses, not requirements or committed features.

| Rank | ID | Opportunity hypothesis | Evidence | Value / relevance | Dependency | Confidence |
|---:|---|---|---|---|---|---|
| 1 | OP-01 | Make availability easy to compare and offer nearby alternatives after a stale slot. | PP-01, P1/P5, T-102, survey signal | Less repeated work; supports R1/call reduction | API refresh/reservation capability | MEDIUM |
| 2 | OP-02 | Make submission single-action and explicit across slow, pending, failed, and duplicate outcomes. | PP-03, T-101/T-103, analytics | Less uncertainty; supports R4 | Idempotency and ownership | MEDIUM |
| 3 | OP-03 | Provide privacy-bounded timeout warning and recovery. | PP-02, P4, T-105 | Prevent restart; clarify handling | Resolve R12/R13 | LOW pending decision |
| 4 | OP-04 | Use redundant text/icon/programmatic state and predictable keyboard behavior. | PP-05 plus design constraint | Potentially removes blocker; supports R10 | Missing accessibility contract/testing | LOW–MEDIUM |
| 5 | OP-05 | Distinguish self/caregiver roles and recipient consequences. | PP-04, P2, T-104 | Reduces ambiguity; supports R11 | Legal/privacy decision | LOW pending decision |
| 6 | OP-06 | Separate transactional contact, channel preference, and marketing consent. | PP-06, channel split, T-106 | Improves control/trust | Product/legal/delivery decisions | LOW pending decision |
| 7 | OP-07 | Make cancellation outcome and fallback explicit. | T-103 and policy gap | Reduces cancellation uncertainty | Cut-offs and ownership | LOW |

OP-01 and OP-02 combine the strongest synthetic evidence with the main business goal. OP-04 is retained as a potential access blocker. The remaining opportunities require human decisions before commitment.

