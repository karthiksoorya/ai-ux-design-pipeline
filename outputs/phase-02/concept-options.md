# Candidate Concept Options

> **SYNTHETIC DEMO DATA.** These are unvalidated design hypotheses, not approved features.

## Concept A — Availability-First Guided Request

- **Direction:** Linear steps: availability → role → details → review → submit → outcome.
- **Traces to:** PD-01–PD-05; OP-01, OP-02, OP-04.
- **Evidence-supported problem:** Early availability, recovery, and status clarity.
- **Design hypothesis:** Progressive disclosure, review, and explicit outcomes reduce load and uncertainty.
- **Distinctive elements:** Early comparison; step progress; review/read-back; locked loading submit; state-specific outcomes and alternatives.
- **Assumptions:** Linear flow suits the task; review does not add unacceptable effort.
- **Dependencies:** Scheduling states, idempotency, role/contact/consent decisions, accessible controls.
- **Risks:** Extra steps may frustrate rushed users; unresolved policy may complicate role flow.
- **Confidence:** MEDIUM as a candidate, not a validated solution.

## Concept B — Slot Hold and Compact Single Page

- **Direction:** Temporarily hold a slot while availability and details share a compact page.
- **Traces to:** PD-01, PD-02, PD-04; OP-01–OP-04.
- **Design hypothesis:** A hold plus compact form reduces stale-slot loss and completion time.
- **Distinctive elements:** Hold timer; inline errors; immediate alternatives; single submit state.
- **Assumptions:** The scheduling service supports holds; density reduces rather than increases load.
- **Dependencies:** Unsupported hold API; timer accessibility; R12/R13; idempotency.
- **Risks:** Invented capability, time pressure, cognitive density.
- **Confidence:** LOW.

## Concept C — Assisted Request with Escalation

- **Direction:** Guided request with clear support/fallback at caregiver, downstream, confirmation, and cancellation failures.
- **Traces to:** PD-02, PD-03, PD-05; OP-02, OP-05–OP-07.
- **Design hypothesis:** Contextual explanation and escalation prevent users becoming stranded.
- **Distinctive elements:** Role guidance; no-save reception fallback; support reference; partial-notification and cancellation messages.
- **Assumptions:** Reception can absorb escalation and receive safe context.
- **Dependencies:** Operating ownership, privacy decisions, hours, support-reference contract.
- **Risks:** Conflicts with call reduction; shifts complexity; possible disclosure.
- **Confidence:** LOW–MEDIUM.

These are structural alternatives: A optimizes staged comprehension, B speed and stale-slot prevention through unconfirmed capability, and C resilience through human escalation.

