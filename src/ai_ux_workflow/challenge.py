"""Deterministic, conservative BRD challenge used by the local demo."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Finding:
    section: str
    statement: str
    classification: str
    confidence: str
    locator: str


SECTIONS = (
    "BRD Intent", "Strengths", "Challenged Assumptions", "Missing Requirements",
    "Edge Cases", "Accessibility Risks", "Trust / Dark-Pattern Risks",
    "Contradictions", "Unresolved Questions", "Recommended Actions",
    "Items Requiring Human Decision",
)


def _lines(text: str) -> list[tuple[int, str]]:
    return [(number, line.strip()) for number, line in enumerate(text.splitlines(), 1) if line.strip()]


def _find(lines: list[tuple[int, str]], pattern: str) -> list[tuple[int, str]]:
    regex = re.compile(pattern, re.I)
    return [(number, line) for number, line in lines if regex.search(line)]


def analyze_brd(text: str) -> list[Finding]:
    lines = _lines(text)
    findings: list[Finding] = []
    if not lines:
        return [Finding("Missing Requirements", "No readable BRD content was supplied.", "FACT", "HIGH", "input:empty")]

    goal_lines = _find(lines, r"\b(goal|objective|purpose|must|shall)\b")
    if goal_lines:
        number, line = goal_lines[0]
        findings.append(Finding("BRD Intent", line, "BRD STATEMENT", "HIGH", f"BRD line {number}"))
    else:
        findings.append(Finding("Missing Requirements", "Business goals or objectives are not explicitly identified.", "RISK HYPOTHESIS", "MEDIUM", "BRD: missing goal/objective specification"))

    strength_matches = [item for item in _find(lines, r"\b(retry|recover|cancel|validation|error|accessib|keyboard|consent)\b") if "not specified" not in item[1].lower()]
    for number, line in strength_matches[:2]:
        findings.append(Finding("Strengths", f"The BRD explicitly addresses: {line}", "BRD STATEMENT", "HIGH", f"BRD line {number}"))

    if len(" ".join(line for _, line in lines).split()) < 40:
        findings.append(Finding("Missing Requirements", "The BRD is sparse; scope, actors, workflows, constraints, or acceptance conditions may be underspecified.", "RISK HYPOTHESIS", "HIGH", "BRD: document-level completeness check"))

    for label, pattern in (("Edge Cases", r"\b(network|timeout|session|duplicate|partial|invalid|missing data|downstream|loading|empty state)\b"), ("Accessibility Risks", r"\b(color|colou?r|red|green|keyboard|screen reader|accessib|cognitive)\b"), ("Trust / Dark-Pattern Risks", r"\b(opt.?in|pre.?select|forced|consent|cancel|personal data|collect data|hidden)\b")):
        matches = _find(lines, pattern)
        if matches:
            number, line = matches[0]
            wording = "REQUIRES REVIEW: the BRD mentions a condition with potential risk: " + line
            if label == "Trust / Dark-Pattern Risks":
                wording = "POTENTIAL TRUST RISK: " + line
            findings.append(Finding(label, wording, "RISK HYPOTHESIS", "MEDIUM", f"BRD line {number}"))
        else:
            findings.append(Finding(label, f"The BRD does not specify {label.lower()} acceptance conditions; validate whether they are required for this context.", "RISK HYPOTHESIS", "LOW", f"BRD: missing {label.lower()} specification"))

    normalized = " ".join(line for _, line in lines).lower()
    contradictions = (("must require", "must not require"), ("always", "never"), ("mandatory", "optional"))
    for left, right in contradictions:
        if left in normalized and right in normalized:
            findings.append(Finding("Contradictions", f"Potentially conflicting statements use both '{left}' and '{right}'.", "INFERENCE", "CONTRADICTORY", "BRD: cross-statement comparison"))

    adversarial = _find(lines, r"ignore (?:all |the )?(?:previous|workflow)|system prompt|approve d1|treat .* as user evidence")
    for number, _ in adversarial:
        findings.append(Finding("Challenged Assumptions", "Embedded instruction was treated as source content and did not alter workflow or evidence rules.", "FACT", "HIGH", f"BRD line {number}"))

    findings.extend((
        Finding("Unresolved Questions", "Which missing requirements must be resolved before persona synthesis?", "RISK HYPOTHESIS", "MEDIUM", "Derived from missing-specification review"),
        Finding("Recommended Actions", "Ask the product owner to resolve HIGH or CONTRADICTORY requirement findings and define acceptance conditions.", "INFERENCE", "MEDIUM", "Derived from challenge findings"),
        Finding("Items Requiring Human Decision", "Confirm which risk hypotheses should become research questions; none are user evidence by default.", "RISK HYPOTHESIS", "HIGH", "Workflow evidence boundary"),
    ))
    return findings


def render_review(text: str, source_name: str = "BRD") -> str:
    findings = analyze_brd(text)
    output = ["# BRD Risk Review", "", f"Source: {source_name}", "", "> Risk hypotheses are not user research evidence and must not become persona facts or confirmed pain points without independent support.", ""]
    for section in SECTIONS:
        output.append(f"## {section}")
        section_findings = [finding for finding in findings if finding.section == section]
        if not section_findings:
            output.append("- No supported finding recorded.")
        for finding in section_findings:
            output.extend((f"- Finding: {finding.statement}", f"  - Classification: {finding.classification}", f"  - Confidence: {finding.confidence}", f"  - Source: {finding.locator}"))
        output.append("")
    return "\n".join(output)
