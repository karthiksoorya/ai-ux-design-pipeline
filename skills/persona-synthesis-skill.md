# Persona Synthesis Skill

## Name & Description
Creates a small set of evidence-based personas or proto-personas from available research and behavioral evidence.

## Role
Help a senior UX researcher synthesize user patterns without inventing unsupported detail.

## Instructions
1. Read the source/evidence inventory and all relevant evidence.
2. Determine whether personas are justified by the evidence.
3. Create only the number of meaningfully distinct personas supported by evidence.
4. Include name/label, user type, summary, goals, pain points, motivations, evidence, assumptions, confidence, contradictions, and validation needs.
5. Distinguish facts from synthesis and assumptions.

## Input
projects/starter/input/ plus source evidence analysis.

## Output
outputs/phase-01/persona.md

## Rules & Guardrails
- Do not invent demographics, quotes, behaviors, or needs.
- BRD alone is insufficient as user research evidence.
- HIGH = direct evidence; MEDIUM = reasonable synthesis; LOW = assumption; CONTRADICTORY = conflicting inputs.
- If evidence is insufficient, create fewer personas or state that personas cannot be supported.

## Example
A repeated research pattern may support a persona goal; a guessed age must not be added unless sourced.
