# Prototype Specification — Availability-First Guided Request

> **SYNTHETIC DEMO DATA.** This D3 artefact is not validated, verified, production-ready, or evidence of WCAG compliance.

## Scope

The local dependency-free prototype implements Search, Availability, Role/details, Review, Request outcome, and a scenario selector for confirmed, pending, stale, rejected, timeout, unavailable, and partial-notification states. It uses fictional in-memory values, makes no network request, stores no personal data, disables repeated submission, and clears on restart/reload.

It does not implement accounts, payment, diagnosis, insurance, emergency triage, rescheduling, real scheduling/notifications, slot holding, persistent recovery, caregiver authorization, cancellation policy, or backend guarantees.

## Files

- `outputs/phase-03/prototype/index.html`
- `outputs/phase-03/prototype/styles.css`
- `outputs/phase-03/prototype/app.js`

Open `index.html` locally. Scenario controls are explicitly labelled simulated.

## Acceptance checks

- Availability appears before personal data.
- Required fields block progression with corrective text.
- Processing blocks duplicate activation.
- Pending/timeout never imply confirmation.
- Stale slot returns to availability.
- Partial notification does not change booking status.
- Status is understandable without color alone.
- Every implemented view/state maps to the flow, screen specification, and interaction-state matrix.

Marketing consent is unselected in the demo pending decision. Static outcomes demonstrate UI behavior only, not backend feasibility. D3 may approve completeness; Phase 4 performs audits, and only D4 APPROVE may permit **Verified Workable Prototype**.

