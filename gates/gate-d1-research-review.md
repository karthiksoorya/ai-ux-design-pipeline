# Gate D1 — Research & Requirements Review

## Purpose
Human approval of Phase 1 BRD challenge and evidence synthesis before UX definition and ideation begin.

## Artefacts reviewed in order
1. outputs/phase-01/brd-risk-review.md
2. outputs/phase-01/persona.md
3. outputs/phase-01/pain-points.md
4. outputs/phase-01/research-gaps.md

The reviewer may inspect original sources in projects/starter/input/.

## Review checklist
- Sources were inventoried and source types are correctly distinguished.
- Challenged BRD assumptions and missing requirements are traceable and appropriately classified.
- Edge cases, accessibility risks, and potential user-trust risks avoid unsupported accusations.
- Contradictions, unresolved questions, and items needing human decision are visible.
- BRD/business requirements were not presented as user evidence.
- Requirements Challenge risk hypotheses did not become persona facts or pain points without independent user evidence.
- Persona claims are traceable to evidence or explicitly labeled assumptions.
- Confidence levels are appropriate.
- Contradictions and research gaps are visible.
- Pain points are traceable to personas/evidence.
- Design opportunities are hypotheses, not requirements.
- Validation questions are actionable.

## Human decisions
- APPROVE — clear D1 and allow Phase 2.
- REVISE — provide actionable feedback and rerun only the affected skill plus downstream dependencies.
- REJECT — stop at Phase 1 until adequate evidence or direction is available.

## Dependency logic
- If the BRD or brd-risk-review.md changes materially, determine whether persona.md, pain-points.md, or research-gaps.md are affected and rerun only affected downstream skills.
- If persona.md changes, regenerate pain-points.md and research-gaps.md as needed before review.
- If only pain-points.md changes, rerun pain-point extraction only and refresh research-gaps.md only when its contents are affected.

## Governance
- Agents may revise artefacts but cannot approve D1.
- Silence, agent validation, or a generic request to continue is not approval.
- When a decision is made, record it in outputs/reviews/d1-review.md and update project.state.md.
