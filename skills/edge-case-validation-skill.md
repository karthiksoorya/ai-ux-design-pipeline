# Edge Case Validation Skill

## Name & Description
Rechecks relevant failure states and Phase 1 BRD risks against the approved design and prototype.

## Role
Support the UX Validation & Audit Agent in closing the risk-to-design loop.

## Input
outputs/phase-01/brd-risk-review.md and approved Phase 3 flow, screen, state, and prototype artefacts.

## Output
Edge-case dispositions in outputs/phase-04/validation-report.md and issues in outputs/phase-04/validation-issues.md.

## Rules & Guardrails
- Classify each relevant risk as ADDRESSED, PARTIALLY ADDRESSED, UNRESOLVED, or NO LONGER APPLICABLE.
- Preserve original classification, confidence, and source locator.
- Missing design evidence cannot support an ADDRESSED result.

