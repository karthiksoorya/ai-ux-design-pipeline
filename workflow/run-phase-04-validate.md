---
phase: 4
name: Validate
entry_from: D3 explicitly approved
trigger: D3 approval is recorded
gate: D4
team:
  lead: ux-validation-audit-agent
agents:
  - ux-validation-audit-agent
skills_invoked:
  - synthetic-usability-test-skill
  - cognitive-friction-analysis-skill
  - accessibility-audit-skill
  - design-system-audit-skill
  - requirement-coverage-skill
  - edge-case-validation-skill
inputs:
  - projects/starter/input/
  - outputs/phase-01/brd-risk-review.md
  - outputs/phase-01/persona.md
  - outputs/phase-02/problem-definition.md
  - outputs/phase-02/selected-concept.md
  - outputs/phase-03/user-flow.md
  - outputs/phase-03/screen-spec.md
  - outputs/phase-03/interaction-states.md
  - outputs/phase-03/prototype-spec.md
outputs:
  - outputs/phase-04/validation-report.md
  - outputs/phase-04/validation-issues.md
  - outputs/phase-04/requirement-coverage.md
  - outputs/phase-04/accessibility-audit.md
exports:
  - outputs/phase-04/validation-report.md
  - outputs/phase-04/validation-issues.md
  - outputs/phase-04/requirement-coverage.md
  - outputs/phase-04/accessibility-audit.md
exit_to: Complete after D4 approval
---

# P4 — Validate

## Agent Team
| Role | Agent | Outputs produced |
|---|---|---|
| Synthetic validation and audit lead | ux-validation-audit-agent | Validation report, issues, requirement coverage, accessibility audit |

## Execution Sequence
| Step | Who | Skill | Output |
|---|---|---|---|
| 1 | UX Validation & Audit Agent | synthetic-usability-test-skill | Synthetic task walkthroughs |
| 2 | UX Validation & Audit Agent | cognitive-friction-analysis-skill | Heuristic friction findings |
| 3 | UX Validation & Audit Agent | accessibility-audit-skill | accessibility-audit.md |
| 4 | UX Validation & Audit Agent | design-system-audit-skill | Design-system findings or NOT AVAILABLE |
| 5 | UX Validation & Audit Agent | requirement-coverage-skill | requirement-coverage.md |
| 6 | UX Validation & Audit Agent | edge-case-validation-skill | BRD-risk and failure-state dispositions |
| 7 | UX Validation & Audit Agent | validation | validation-report.md and validation-issues.md |
| 8 | Human reviewer | — | D4 decision |

## Validation Rules
- Synthetic usability is simulated heuristic analysis, not real-user evidence.
- Any Cognitive Friction Score is labeled SYNTHETIC / HEURISTIC SCORE with method and limitations.
- Accessibility findings are evidence-bounded risks; do not claim full WCAG compliance without sufficient evidence.
- If no design system is supplied, report NOT AVAILABLE.
- Requirement coverage uses COVERED, PARTIALLY COVERED, NOT COVERED, NOT APPLICABLE, or REQUIRES HUMAN DECISION.
- Edge-case status uses ADDRESSED, PARTIALLY ADDRESSED, UNRESOLVED, or NO LONGER APPLICABLE.
- The prototype remains unverified until explicit D4 APPROVE.

## D4 Gate — Final UX Validation Review
Use gates/gate-d4-final-validation-review.md. Only explicit human APPROVE marks the prototype verified/workable.

## Revision Loop
On REVISE, identify the minimum affected Phase 3 skill/output, rerun dependent prototype-generation work when necessary, rerun only relevant Phase 4 checks, and return to D4. Restart upstream phases only when their approved assumptions materially change.

