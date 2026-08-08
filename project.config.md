# Project Configuration

## Project
- Project name: AI UX Discovery-to-Prototype Pipeline
- Active project: projects/starter
- Source input location: projects/starter/input/

## Workflow
- Orchestrator: workflow/orchestrator.md
- Supported phases:
  - workflow/run-phase-01-discover.md
  - workflow/run-phase-02-define.md
  - workflow/run-phase-03-design.md
  - workflow/run-phase-04-validate.md
- Human review gates:
  - gates/gate-d1-research-review.md
  - gates/gate-d2-definition-review.md
  - gates/gate-d3-prototype-review.md
  - gates/gate-d4-final-validation-review.md
- Agent locations:
  - agents/requirements-challenge-agent.md
  - agents/ux-research-agent.md
  - agents/ux-definition-agent.md
  - agents/experience-design-agent.md
  - agents/ux-validation-audit-agent.md
- Skill location: skills/

## Constraints
- BRD expresses business intent; it must not be treated as user research evidence.
- User research evidence, business requirements, synthesis, assumptions, and contradictions must remain distinguishable.
- Do not invent users, quotes, pain points, requirements, journeys, screens, priorities, or validation results.
- Unsupported findings must be marked as assumptions or validation needs.
- Every major insight must include evidence traceability where a source exists.
- Confidence convention:
  - HIGH — directly supported by source evidence.
  - MEDIUM — reasonable synthesis from multiple supported facts.
  - LOW — assumption or weakly supported inference requiring validation.
  - CONTRADICTORY — sources conflict and human resolution is required.
- Human gates cannot be approved by agents or automated validation.
- Synthetic usability findings are heuristic analysis, not empirical user evidence.
- Do not claim full WCAG compliance without sufficient testable evidence and human validation.
- A prototype becomes verified/workable only after explicit D4 APPROVE.

## Canonical paths
- Input folder: projects/starter/input/
- Phase 1 outputs: outputs/phase-01/
  - Required BRD risk review: outputs/phase-01/brd-risk-review.md
- Phase 2 outputs: outputs/phase-02/
- Phase 3 outputs: outputs/phase-03/
- Phase 4 outputs: outputs/phase-04/
- Review-record folder: outputs/reviews/

## Configuration governance
- This file is stable configuration, not runtime status.
- Change it only when the user explicitly changes scope, workflow structure, constraints, or canonical paths.
- Record phase progress, gate decisions, and next actions in project.state.md.
