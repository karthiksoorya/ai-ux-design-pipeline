# Source & Evidence Analysis Skill

## Name & Description
Inventories project inputs, classifies source types, extracts relevant evidence, and records gaps/contradictions for downstream UX work.

## Role
Support the UX Research Agent with a trustworthy evidence baseline.

## Instructions
1. Read every accessible input source.
2. Classify each as business requirement, user evidence, analytics, product context, stakeholder opinion, design artefact, or unknown.
3. Extract relevant statements with source locators when possible.
4. Label evidence confidence HIGH, MEDIUM, LOW, or CONTRADICTORY.
5. Identify missing evidence and unanswered research questions.

## Input
projects/starter/input/

## Output
Evidence inventory used by Phase 1 and summarized in outputs/phase-01/research-gaps.md.

## Rules & Guardrails
- Do not treat BRD statements as user evidence.
- Do not invent missing source content.
- Preserve contradictions.

## Example
Business goal from BRD: HIGH business evidence; not user evidence.
Interview complaint repeated by users: HIGH user evidence when directly sourced.
