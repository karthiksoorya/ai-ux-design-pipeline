---
phase: 3
name: Design & Prototype
entry_from: D2 explicitly approved
trigger: D2 approval is recorded
gate: D3
team:
  lead: experience-design-agent
agents:
  - experience-design-agent
skills_invoked:
  - user-flow-skill
  - information-architecture-skill
  - screen-specification-skill
  - interaction-state-skill
  - prototype-generation-skill
inputs:
  - outputs/phase-02/problem-definition.md
  - outputs/phase-02/journey-map.md
  - outputs/phase-02/opportunities.md
  - outputs/phase-02/selected-concept.md
  - projects/starter/input/
outputs:
  - outputs/phase-03/user-flow.md
  - outputs/phase-03/screen-spec.md
  - outputs/phase-03/interaction-states.md
  - outputs/phase-03/prototype-spec.md
exports:
  - outputs/phase-03/user-flow.md
  - outputs/phase-03/screen-spec.md
  - outputs/phase-03/interaction-states.md
  - outputs/phase-03/prototype-spec.md
exit_to: workflow/run-phase-04-validate.md
---

# P3 — Design & Prototype

## Agent Team
| Role | Agent | Outputs produced |
|---|---|---|
| Experience design lead | experience-design-agent | User flow, information architecture when applicable, screens, interaction states, prototype |

## Execution Sequence
| Step | Who | Skills | Input | Output | Gate |
|---|---|---|---|---|---|
| 1 | Experience Design Agent | — | D2-approved outputs | Execution context | — |
| 2 | Experience Design Agent | user-flow-skill | Problem definition + journey + opportunities | user-flow.md | — |
| 3 | Experience Design Agent | validation | user-flow.md | Validated flow | — |
| 4 | Experience Design Agent | information-architecture-skill | Selected concept + validated flow | IA decisions or NOT APPLICABLE | — |
| 5 | Experience Design Agent | screen-specification-skill | Validated flow + IA + constraints | screen-spec.md | — |
| 6 | Experience Design Agent | interaction-state-skill | Flow + screen spec | interaction-states.md | — |
| 7 | Experience Design Agent | prototype-generation-skill | Flow + screen spec + states | prototype-spec.md and runnable prototype when available | — |
| 8 | Experience Design Agent | validation | All Phase 3 outputs | Design and prototype pack | — |
| 9 | Human reviewer | — | Design pack + runnable prototype if available | Decision | D3 |

## Design Rules
- Every major screen or interaction must map back to an approved problem, journey stage, opportunity, requirement, or clearly labeled hypothesis.
- Include happy path plus relevant error, empty, loading, permission, and recovery states when applicable.
- Do not invent backend capabilities, policies, pricing, or business rules.
- Prototype generation must preserve traceability to screen-spec.md and user-flow.md.
- Preserve traceability from BRD through research, problem definition, selected concept, and every major design decision.
- Loading, empty, error, validation error, cancellation, timeout, unavailable-service, permission, recovery, and exit states are included when relevant or marked NOT APPLICABLE with rationale.
- Phase 3 does not claim the prototype is validated or verified.
- First-level Markdown submission may end with prototype-spec.md; runnable UI implementation is the next implementation layer.

## D3 Gate — Design & Prototype Review
Use gates/gate-d3-prototype-review.md.
Only explicit human APPROVE advances to Phase 4.

## Exceptions
| Failure condition | Recovery action |
|---|---|
| D2 not approved | Stop. |
| Flow contains unsupported feature | Return to user-flow-skill or Phase 2 if definition is wrong. |
| Screen specification misses required state | Revise screen-specification-skill and regenerate dependent prototype spec. |
| Prototype conflicts with approved flow | Regenerate prototype only after fixing mismatch. |
| Requirement is unclear | Mark decision/validation need; do not invent. |

## Phase Handoff
After D3 approval, Phase 4 receives the complete approved design/prototype pack and all traceability, assumptions, risks, and unresolved validation needs.
