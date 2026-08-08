# Pain Point Extraction Skill

## Name & Description
Extracts traceable pain themes from validated personas and direct evidence.

## Role
Help the UX Research Agent identify user problems without prematurely prescribing features.

## Instructions
1. Require a validated persona output unless the request is explicitly direct-evidence-only pain analysis.
2. Identify repeated frustrations, barriers, unmet needs, and breakdowns.
3. Link every pain point to persona(s) and/or direct evidence.
4. Assign confidence and severity/impact rationale where supported.
5. Suggest design opportunities only as hypotheses.

## Input
outputs/phase-01/persona.md plus project evidence.

## Output
outputs/phase-01/pain-points.md

## Rules & Guardrails
- Do not invent pain points.
- Do not turn an opportunity into a requirement.
- If no supported frustrations exist, say so.
