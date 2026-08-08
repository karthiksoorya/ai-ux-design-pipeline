---
phase: 2
name: Define & Ideate
entry_from: D1 explicitly approved
trigger: D1 approval is recorded
gate: D2
team:
  lead: ux-definition-agent
agents:
  - ux-definition-agent
skills_invoked:
  - problem-framing-skill
  - journey-mapping-skill
  - opportunity-prioritization-skill
  - concept-generation-skill
  - concept-evaluation-skill
inputs:
  - projects/starter/input/
  - outputs/phase-01/brd-risk-review.md
  - outputs/phase-01/persona.md
  - outputs/phase-01/pain-points.md
  - outputs/phase-01/research-gaps.md
outputs:
  - outputs/phase-02/problem-definition.md
  - outputs/phase-02/journey-map.md
  - outputs/phase-02/opportunities.md
  - outputs/phase-02/concept-options.md
  - outputs/phase-02/selected-concept.md
exports:
  - outputs/phase-02/problem-definition.md
  - outputs/phase-02/journey-map.md
  - outputs/phase-02/opportunities.md
  - outputs/phase-02/concept-options.md
  - outputs/phase-02/selected-concept.md
exit_to: workflow/run-phase-03-design.md
---

# P2 — Define & Ideate

## Agent Team
| Role | Agent | Outputs produced |
|---|---|---|
| UX definition and ideation lead | ux-definition-agent | Problem definition, journey, opportunities, concept options, selected concept |

## Execution Sequence
| Step | Who | Skills | Input | Output | Gate |
|---|---|---|---|---|---|
| 1 | UX Definition Agent | — | D1-approved Phase 1 artefacts + BRD/context | Execution context | — |
| 2 | UX Definition Agent | problem-framing-skill | Phase 1 outputs + requirements | problem-definition.md | — |
| 3 | UX Definition Agent | validation | problem-definition.md | Validated framing | — |
| 4 | UX Definition Agent | journey-mapping-skill | Personas + pain points + framing | journey-map.md | — |
| 5 | UX Definition Agent | opportunity-prioritization-skill | Pain points + journey + business constraints | opportunities.md | — |
| 6 | UX Definition & Ideation Agent | concept-generation-skill | Approved problems + opportunities | concept-options.md | — |
| 7 | UX Definition & Ideation Agent | concept-evaluation-skill | Candidate concepts + explicit criteria | selected-concept.md | — |
| 8 | UX Definition & Ideation Agent | validation | All Phase 2 outputs | Validated definition and ideation pack | — |
| 9 | Human reviewer | — | All Phase 2 artefacts | Decision | D2 |

## Define Rules
- Reconcile business intent from the BRD with supported user evidence; do not collapse them into one source of truth.
- Problem statements must identify user, context, evidence, impact, and uncertainty.
- Journey stages must be evidence-based or explicitly marked hypothetical.
- Opportunities are candidate directions, not committed features.
- Prioritization must explain evidence strength, user value, business relevance, dependencies, and uncertainty.
- Generate multiple meaningfully different concepts when evidence supports them; do not silently converge on the first solution.
- Each concept separates evidence-supported problem, design hypothesis, assumptions, and unresolved questions.
- selected-concept.md records alternatives, criteria, evidence, risks, assumptions, and unresolved questions.

## D2 Gate — Definition & Ideation Review
Use gates/gate-d2-definition-review.md.
Only explicit human APPROVE may advance to Phase 3.

## Exceptions
| Failure condition | Recovery action |
|---|---|
| D1 not approved | Stop. |
| Problem framing unsupported | Return to problem-framing-skill. |
| Journey contains invented stages | Remove or mark as hypothesis and revalidate. |
| Opportunity is presented as requirement without evidence | Reclassify as hypothesis/candidate direction. |
| Only one concept is produced without justification | Return to concept-generation-skill. |
| Concept selection lacks common criteria | Return to concept-evaluation-skill. |
| Phase 1 evidence changes | Reassess all dependent Phase 2 artefacts. |

## Phase Handoff
Phase 3 receives all D2-approved outputs, especially selected-concept.md, with preserved evidence, alternatives, assumptions, risk hypotheses, confidence, contradictions, and unresolved validation questions.
