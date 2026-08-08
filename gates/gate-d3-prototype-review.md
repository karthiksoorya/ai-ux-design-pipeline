# Gate D3 — Design & Prototype Review

## Purpose
Human approval that the experience design and prototype are sufficiently complete to enter validation.

## Artefacts reviewed in order
1. outputs/phase-03/user-flow.md
2. outputs/phase-03/screen-spec.md
3. outputs/phase-03/interaction-states.md
4. outputs/phase-03/prototype-spec.md
5. Runnable prototype, when implementation exists

## Review checklist
- User flow addresses D2-approved problems/opportunities.
- Major steps trace back to approved evidence/requirements or labeled hypotheses.
- Screen specification covers required states and edge conditions.
- Prototype specification matches the flow and screens.
- The D2-approved selected concept is represented correctly.
- Important loading, empty, error, validation, cancellation, timeout, and unavailable-service states exist when relevant.
- No unsupported business rule or product capability was invented.
- Open design decisions and validation needs remain visible.

## Human decisions
- APPROVE — clear D3 and allow Phase 4 validation.
- REVISE — rerun only the affected skill plus downstream dependencies.
- REJECT — stop at Phase 3.

## Dependency logic
- If user-flow.md changes, reassess screen-spec.md and prototype-spec.md.
- If screen-spec.md changes, regenerate prototype-spec.md and runnable prototype when present.
- If interaction-states.md changes, reassess screen-spec.md and regenerate dependent prototype work.

## Governance
- Agents cannot approve D3.
- Only explicit human APPROVE advances to Phase 4.
- Record a decision in outputs/reviews/d3-review.md and update project.state.md.
