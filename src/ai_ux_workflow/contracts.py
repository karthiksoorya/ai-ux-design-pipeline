"""Immutable runtime representation of the frozen Markdown contracts."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PhaseContract:
    number: int
    name: str
    runbook: str
    agents: tuple[str, ...]
    gate: str
    gate_id: str
    review: str
    skills: tuple[str, ...]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]


PHASES = (
    PhaseContract(
        1,
        "Discover",
        "workflow/run-phase-01-discover.md",
        ("agents/ux-research-agent.md", "agents/requirements-challenge-agent.md"),
        "gates/gate-d1-research-review.md",
        "D1",
        "outputs/reviews/d1-review.md",
        ("source-evidence-analysis-skill", "advocate-review-skill", "cynic-review-skill", "debate-synthesis-skill", "persona-synthesis-skill", "pain-point-extraction-skill"),
        ("projects/starter/input/",),
        ("outputs/phase-01/brd-risk-review.md", "outputs/phase-01/persona.md", "outputs/phase-01/pain-points.md", "outputs/phase-01/research-gaps.md"),
    ),
    PhaseContract(
        2,
        "Define & Ideate",
        "workflow/run-phase-02-define.md",
        ("agents/ux-definition-agent.md",),
        "gates/gate-d2-definition-review.md",
        "D2",
        "outputs/reviews/d2-review.md",
        ("problem-framing-skill", "journey-mapping-skill", "opportunity-prioritization-skill", "concept-generation-skill", "concept-evaluation-skill"),
        ("projects/starter/input/", "outputs/phase-01/brd-risk-review.md", "outputs/phase-01/persona.md", "outputs/phase-01/pain-points.md", "outputs/phase-01/research-gaps.md"),
        ("outputs/phase-02/problem-definition.md", "outputs/phase-02/journey-map.md", "outputs/phase-02/opportunities.md", "outputs/phase-02/concept-options.md", "outputs/phase-02/selected-concept.md"),
    ),
    PhaseContract(
        3,
        "Design & Prototype",
        "workflow/run-phase-03-design.md",
        ("agents/experience-design-agent.md",),
        "gates/gate-d3-prototype-review.md",
        "D3",
        "outputs/reviews/d3-review.md",
        ("user-flow-skill", "information-architecture-skill", "screen-specification-skill", "interaction-state-skill", "prototype-generation-skill"),
        ("outputs/phase-02/problem-definition.md", "outputs/phase-02/journey-map.md", "outputs/phase-02/opportunities.md", "outputs/phase-02/selected-concept.md", "projects/starter/input/"),
        ("outputs/phase-03/user-flow.md", "outputs/phase-03/screen-spec.md", "outputs/phase-03/interaction-states.md", "outputs/phase-03/prototype-spec.md"),
    ),
    PhaseContract(
        4,
        "Validate",
        "workflow/run-phase-04-validate.md",
        ("agents/ux-validation-audit-agent.md",),
        "gates/gate-d4-final-validation-review.md",
        "D4",
        "outputs/reviews/d4-review.md",
        ("synthetic-usability-test-skill", "cognitive-friction-analysis-skill", "accessibility-audit-skill", "design-system-audit-skill", "requirement-coverage-skill", "edge-case-validation-skill"),
        ("projects/starter/input/", "outputs/phase-01/brd-risk-review.md", "outputs/phase-01/persona.md", "outputs/phase-02/problem-definition.md", "outputs/phase-02/selected-concept.md", "outputs/phase-03/user-flow.md", "outputs/phase-03/screen-spec.md", "outputs/phase-03/interaction-states.md", "outputs/phase-03/prototype-spec.md"),
        ("outputs/phase-04/validation-report.md", "outputs/phase-04/validation-issues.md", "outputs/phase-04/requirement-coverage.md", "outputs/phase-04/accessibility-audit.md"),
    ),
)

FROZEN_FILES = (
    "README.md",
    "project.config.md",
    "project.state.md",
    "projects/starter/brief.md",
    "workflow/orchestrator.md",
    *(phase.runbook for phase in PHASES),
    *(agent for phase in PHASES for agent in phase.agents),
    *(phase.gate for phase in PHASES),
    *(f"skills/{skill}.md" for phase in PHASES for skill in phase.skills),
)
