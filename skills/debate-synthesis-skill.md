# Debate Synthesis Skill

## Name & Description
Compares advocate and cynic analyses and produces a concise, traceable BRD risk review.

## Role
Support the Requirements Challenge Agent in reconciling strengths and challenges into an actionable handoff.

## Instructions
1. Compare the advocate and cynic findings rather than choosing a rhetorical winner.
2. Structure the review as BRD intent, strengths, challenged assumptions, missing requirements, edge cases, accessibility risks, trust/dark-pattern risks, contradictions, unresolved questions, recommended actions, and items requiring human decision.
3. For every substantive finding include classification, confidence, and an evidence/source locator where available.
4. Preserve contradictions and distinguish an absent specification from contrary evidence.
5. Validate that risk hypotheses cannot be read as user research findings.

## Input
Advocate analysis, cynic analysis, readable BRD, relevant sources, and the source/evidence inventory.

## Output
outputs/phase-01/brd-risk-review.md

## Rules & Guardrails
- Allowed classifications: FACT, BRD STATEMENT, INFERENCE, ASSUMPTION, RISK HYPOTHESIS.
- Allowed confidence: HIGH, MEDIUM, LOW, CONTRADICTORY.
- Never invent user evidence, facts, requirements, findings, quotations, or source locators.
- Unsupported accusations must be removed or reframed as labeled risks requiring validation.
- Risk hypotheses may feed research gaps, validation questions, or human decisions only; they cannot become persona facts or confirmed pain points.

