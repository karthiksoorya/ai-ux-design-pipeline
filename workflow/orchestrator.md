# AI UX Project Orchestrator

## Scope and path rules
- Project root is the repository root containing this file.
- Supported phases are only:
  1. workflow/run-phase-01-discover.md
  2. workflow/run-phase-02-define.md
  3. workflow/run-phase-03-design.md
  4. workflow/run-phase-04-validate.md
- Supported human gates are only D1, D2, D3, and D4 as defined in gates/.
- Paths are project-relative. Missing components or project facts must not be invented.

## First action
1. Read project.config.md, project.state.md, and this orchestrator.
2. Read all phase runbooks.
3. Inspect required inputs, outputs, and review records.
4. Reconcile project.state.md with actual artefacts without inventing progress.
5. If a human gate is pending, present its required artefacts and stop.

## State and routing
| Condition | Position | Required action |
|---|---|---|
| Phase 1 outputs incomplete | Phase 1 — Discover | Run only eligible Phase 1 work after confirming usable inputs. |
| Phase 1 complete; D1 not approved | Gate D1 | Present D1 artefacts and stop. |
| D1 approved; Phase 2 incomplete | Phase 2 — Define & Ideate | Dispatch UX Definition & Ideation Agent. |
| Phase 2 complete; D2 not approved | Gate D2 | Present D2 artefacts and stop. |
| D2 approved; Phase 3 incomplete | Phase 3 — Design & Prototype | Dispatch Experience Design Agent. |
| Phase 3 complete; D3 not approved | Gate D3 | Present D3 artefacts and stop. |
| D3 approved; Phase 4 incomplete | Phase 4 — Validate | Dispatch UX Validation & Audit Agent. |
| Phase 4 complete; D4 not approved | Gate D4 | Present D4 artefacts and stop. |
| D4 approved | Complete | Report verified/workable prototype and validation evidence. |

## Phase contracts

### Phase 1 — Discover
- Runbook: workflow/run-phase-01-discover.md
- Agents: agents/ux-research-agent.md; agents/requirements-challenge-agent.md; then agents/ux-research-agent.md
- Inputs: projects/starter/input/
- Outputs: outputs/phase-01/brd-risk-review.md; outputs/phase-01/persona.md; outputs/phase-01/pain-points.md; outputs/phase-01/research-gaps.md
- Skills in order: source-evidence-analysis-skill; advocate-review-skill; cynic-review-skill; debate-synthesis-skill; persona-synthesis-skill; pain-point-extraction-skill
- Gate: gates/gate-d1-research-review.md
- Requirements Challenge finishes before persona synthesis. Its risk hypotheses are not user evidence.

### Phase 2 — Define & Ideate
- Runbook: workflow/run-phase-02-define.md
- Agent: agents/ux-definition-agent.md (UX Definition & Ideation Agent)
- Inputs: D1-approved Phase 1 outputs and projects/starter/input/
- Outputs: outputs/phase-02/problem-definition.md; outputs/phase-02/journey-map.md; outputs/phase-02/opportunities.md; outputs/phase-02/concept-options.md; outputs/phase-02/selected-concept.md
- Skills in order: problem-framing-skill; journey-mapping-skill; opportunity-prioritization-skill; concept-generation-skill; concept-evaluation-skill
- Gate: gates/gate-d2-definition-review.md
- Do not jump from a single pain point to a single solution; justify when meaningful alternatives are unsupported.

### Phase 3 — Design & Prototype
- Runbook: workflow/run-phase-03-design.md
- Agent: agents/experience-design-agent.md
- Inputs: D2-approved outputs, especially selected-concept.md, plus relevant sources
- Outputs: outputs/phase-03/user-flow.md; outputs/phase-03/screen-spec.md; outputs/phase-03/interaction-states.md; outputs/phase-03/prototype-spec.md
- Skills in order: user-flow-skill; information-architecture-skill when applicable; screen-specification-skill; interaction-state-skill; prototype-generation-skill
- Gate: gates/gate-d3-prototype-review.md
- Do not describe the prototype as validated, verified, or workable at Phase 3.

### Phase 4 — Validate
- Runbook: workflow/run-phase-04-validate.md
- Agent: agents/ux-validation-audit-agent.md
- Inputs: approved Phase 1–3 artefacts and relevant sources
- Outputs: outputs/phase-04/validation-report.md; outputs/phase-04/validation-issues.md; outputs/phase-04/requirement-coverage.md; outputs/phase-04/accessibility-audit.md
- Skills in order: synthetic-usability-test-skill; cognitive-friction-analysis-skill; accessibility-audit-skill; design-system-audit-skill; requirement-coverage-skill; edge-case-validation-skill
- Gate: gates/gate-d4-final-validation-review.md
- Synthetic validation is heuristic, not empirical user research. Only D4 APPROVE verifies the prototype.

## Gate governance
- D1, D2, D3, and D4 allow only APPROVE, REVISE, or REJECT.
- Only explicit human APPROVE advances.
- Agents, the orchestrator, and automated checks cannot approve gates.
- Silence or a generic request to continue is not approval.
- REJECT stops at the current phase and records the reason.
- REVISE reruns the minimum affected skill and dependent downstream outputs.
- D4 REVISE routes to the affected Phase 3 skill/output, regenerates dependent prototype work, reruns relevant Phase 4 checks, and returns to D4; upstream phases restart only when approved assumptions materially change.

## Operating rules
- The orchestrator routes work and never authors phase artefacts itself.
- Read the active runbook, agents, and all declared skills before dispatch.
- Preserve citations, evidence type, classifications, confidence, assumptions, limitations, contradictions, risks, and open questions across handoffs.
- Do not treat business requirements, risk hypotheses, synthetic findings, or design hypotheses as user research evidence.
- Update project.state.md only after a material event or explicit human gate decision.

## Completion
Report current position, artefacts, gate status, evidence limitations, unresolved issues, and next action. The phrase verified/workable prototype is allowed only after recorded D4 APPROVE.

