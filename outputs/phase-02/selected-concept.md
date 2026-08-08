# Selected Concept Recommendation

> **SYNTHETIC DEMO DATA.** This is a D2 recommendation, not proof of usability, feasibility, accessibility compliance, or validation.

## Common evaluation

Scores are design judgments from 1 (weak) to 5 (strong).

| Criterion | Weight | A | B | C |
|---|---:|---:|---:|---:|
| Traceability to supported problems | 25% | 5 | 4 | 4 |
| High-priority opportunity coverage | 20% | 5 | 4 | 3 |
| Low dependence on unconfirmed capability/policy | 20% | 4 | 1 | 2 |
| Accessibility/cognitive-risk posture | 15% | 4 | 2 | 3 |
| Alignment with call reduction | 10% | 4 | 5 | 2 |
| Failure/recovery representation | 10% | 4 | 4 | 5 |
| **Weighted result** | **100%** | **4.45** | **3.25** | **3.30** |

## Recommendation

Recommend **Concept A — Availability-First Guided Request** for D2 review.

It addresses the best-supported problems without assuming a slot-hold API, exposes availability before personal data, accommodates explicit processing/recovery states, and can apply redundant status and keyboard patterns without claiming compliance.

## Alternatives considered

- **B:** Potentially faster, but its defining hold behavior is unsupported and its timer/density add risk.
- **C:** Strong fallback, but depends on an undefined support model and may conflict with call reduction.
- Explicit fallback and non-stranding failure states from C may be tested within A.

## Phase 3 boundaries

Phase 3 may specify availability-first exploration, staged role/details/review/outcome, redundant state, submission locking, processing feedback, and confirmed/pending/stale/rejected/timeout/unavailable/partial-notification states.

Phase 3 must not assume slot holding, persistent incomplete-detail recovery, caregiver/consent policy, optional contact fields, guaranteed delivery, approved default marketing consent, cancellation cut-offs, verified usability, or WCAG compliance.

## Required decisions

1. Resolve R12/R13.
2. Define idempotency and service response states.
3. Decide caregiver ownership, consent, and recipients.
4. Decide contact requirements, notification semantics, and marketing default.
5. Define timeout warning, extension, clearing, and shared-device behavior.
6. Validate with representative users, including keyboard and assistive-technology users.

**Status: RECOMMENDED FOR HUMAN D2 REVIEW — NOT VALIDATED OR APPROVED**

