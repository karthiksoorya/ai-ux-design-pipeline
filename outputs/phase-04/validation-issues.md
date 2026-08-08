# Phase 4 Validation Issues

> **SYNTHETIC / HEURISTIC FINDINGS.** Severity represents potential impact inferred from inspected artefacts and interactive checks, not observed participant harm or production incidence.

| ID | Severity | Finding | Evidence / traceability | Minimum revision route |
|---|---|---|---|---|
| V-01 | HIGH | Cancellation is in the approved flow, screens, and state matrix but absent from the runnable prototype. | `user-flow.md` F12–F13; `screen-spec.md` S06–S07; `interaction-states.md` ST-16–ST-20; BRD R6; no matching code in `prototype/app.js`. | Phase 3 prototype-generation work; regenerate prototype and rerun synthetic usability, accessibility, coverage, and edge-case checks. |
| V-02 | HIGH | Five-minute inactivity warning/expiry is not implemented, so privacy clearing and user interruption behavior cannot be validated. | BRD R9; `interaction-states.md` ST-14–ST-15; no timer/warning/expiry code in `prototype/app.js`. | Phase 3 interaction-state/prototype-generation work; rerun relevant Phase 4 checks. |
| V-03 | MEDIUM | Required-field error handling does not focus the first invalid field, identify individual fields, associate errors programmatically, or announce an alert. | Interactive check left focus on `#go`; `#err` has no role; inputs have no `aria-describedby`; design-system error rule; ST-04. | Phase 3 screen specification and prototype-generation work; rerun accessibility and usability checks. |
| V-04 | MEDIUM | Whole-view replacement does not deliberately move focus to the new step heading; the entire application region is `aria-live="polite"`, which may produce excessive or inconsistent announcements. | `index.html` `#app`; `app.js` `set()`; interactive step transitions. | Phase 3 interaction-state/prototype-generation work; verify with keyboard and screen-reader users/tools. |
| V-05 | MEDIUM | Empty availability, loading, unavailable-service-at-search, and session states are specified but not exercisable in the runnable prototype. | ST-01–ST-03, ST-11, ST-14–ST-15; fixed availability code in `app.js`. | Phase 3 prototype-generation work; rerun synthetic usability and edge-case validation. |
| V-06 | MEDIUM | Caregiver booking is selectable but supplies no authority, consent, contact ownership, or notification-recipient behavior. | BRD R11; PD-03; role option says policy is unresolved. | Human product/privacy decision, then minimum affected Phase 2/3 artefacts and prototype behavior. |
| V-07 | MEDIUM | R2 says reason for visit is required, but the prototype allows it to be empty. | BRD R2; `app.js` validates name, DOB, phone, email only. | Phase 3 prototype-generation work; confirm data-minimization decision before enforcing collection. |
| V-08 | LOW | DOB, phone, and email controls use generic text inputs with no autocomplete metadata, reducing input assistance and validation semantics. | Interactive DOM inspection and `app.js` input template. | Phase 3 screen specification/prototype-generation work; rerun accessibility check. |
| V-09 | MEDIUM | Notification delivery and the 20-second scheduling response are simulated; backend timing, idempotency, delivery, and recovery cannot be validated. | BRD R5 and constraint; `prototype-spec.md` limitations; no network calls. | Engineering feasibility/integration work outside this local demo; retain explicit simulation labels. |

## D4 attention

- Unresolved HIGH issues: V-01 and V-02.
- Human decisions still required: marketing default/legality, caregiver authority and recipients, R12/R13 preservation meaning, notification guarantees, and cancellation cut-offs.
- An APPROVE decision would explicitly accept the listed limitations for this deliverable; an agent cannot make that decision.

