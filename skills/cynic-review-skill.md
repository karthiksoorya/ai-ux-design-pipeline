# Cynic Review Skill

## Name & Description
Challenges the BRD as a Devil's Advocate across usability pressure, failure states, accessibility, trust, and requirement quality.

## Role
Support the Requirements Challenge Agent by exposing risks and missing specifications without turning suspicions into facts.

## Instructions
1. Apply the Rushed / Distracted User Test: unnecessary steps, cognitive load, excessive fields, unclear recovery, and time-sensitive risks.
2. Review edge cases and failure states: network failure, partial completion, invalid or missing data, duplicate actions, timeout/session expiry, cancellation, unavailable downstream services, and relevant empty/error/loading states.
3. Review accessibility and inclusivity: color-only meaning, keyboard access, text clarity, cognitive accessibility, potential exclusion, and missing accessibility requirements.
4. Review trust risks: forced actions, hidden choices, default opt-ins, misleading hierarchy, difficult cancellation, unnecessary data collection, and unclear consequences.
5. Review requirement quality: ambiguity, contradiction, missing acceptance conditions, undefined ownership, undefined business rules, and unsupported assumptions.
6. Attach classification, confidence, and source locator or missing-specification locator to every substantive finding.

## Input
Readable BRD, relevant source material, and advocate analysis.

## Output
Cynic analysis consumed by debate-synthesis-skill and represented in outputs/phase-01/brd-risk-review.md.

## Rules & Guardrails
- Use FACT, BRD STATEMENT, INFERENCE, ASSUMPTION, or RISK HYPOTHESIS classifications only.
- Use HIGH, MEDIUM, LOW, or CONTRADICTORY confidence only.
- Do not claim a WCAG violation without sufficient evidence; otherwise label an accessibility risk requiring validation.
- Do not accuse a product of a dark pattern without explicit evidence; use POTENTIAL TRUST RISK or REQUIRES REVIEW.
- Absence of a requirement supports a missing-specification finding, not a claim that the failure occurs.
- Never invent user evidence, product behavior, requirements, or facts.

