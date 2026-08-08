from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]

PHASES = (
    {
        "runbook": "workflow/run-phase-01-discover.md",
        "agents": ("agents/ux-research-agent.md", "agents/requirements-challenge-agent.md"),
        "gate": "gates/gate-d1-research-review.md",
        "skills": (
            "source-evidence-analysis-skill",
            "advocate-review-skill",
            "cynic-review-skill",
            "debate-synthesis-skill",
            "persona-synthesis-skill",
            "pain-point-extraction-skill",
        ),
        "outputs": (
            "outputs/phase-01/brd-risk-review.md",
            "outputs/phase-01/persona.md",
            "outputs/phase-01/pain-points.md",
            "outputs/phase-01/research-gaps.md",
        ),
    },
    {
        "runbook": "workflow/run-phase-02-define.md",
        "agents": ("agents/ux-definition-agent.md",),
        "gate": "gates/gate-d2-definition-review.md",
        "skills": (
            "problem-framing-skill",
            "journey-mapping-skill",
            "opportunity-prioritization-skill",
            "concept-generation-skill",
            "concept-evaluation-skill",
        ),
        "outputs": (
            "outputs/phase-02/problem-definition.md",
            "outputs/phase-02/journey-map.md",
            "outputs/phase-02/opportunities.md",
            "outputs/phase-02/concept-options.md",
            "outputs/phase-02/selected-concept.md",
        ),
    },
    {
        "runbook": "workflow/run-phase-03-design.md",
        "agents": ("agents/experience-design-agent.md",),
        "gate": "gates/gate-d3-prototype-review.md",
        "skills": (
            "user-flow-skill",
            "information-architecture-skill",
            "screen-specification-skill",
            "interaction-state-skill",
            "prototype-generation-skill",
        ),
        "outputs": (
            "outputs/phase-03/user-flow.md",
            "outputs/phase-03/screen-spec.md",
            "outputs/phase-03/interaction-states.md",
            "outputs/phase-03/prototype-spec.md",
        ),
    },
    {
        "runbook": "workflow/run-phase-04-validate.md",
        "agents": ("agents/ux-validation-audit-agent.md",),
        "gate": "gates/gate-d4-final-validation-review.md",
        "skills": (
            "synthetic-usability-test-skill",
            "cognitive-friction-analysis-skill",
            "accessibility-audit-skill",
            "design-system-audit-skill",
            "requirement-coverage-skill",
            "edge-case-validation-skill",
        ),
        "outputs": (
            "outputs/phase-04/validation-report.md",
            "outputs/phase-04/validation-issues.md",
            "outputs/phase-04/requirement-coverage.md",
            "outputs/phase-04/accessibility-audit.md",
        ),
    },
)


class CrossReferenceTests(unittest.TestCase):
    def test_frozen_source_files_exist(self) -> None:
        expected = {"workflow/orchestrator.md", "project.config.md", "project.state.md", "projects/starter/brief.md"}
        for phase in PHASES:
            expected.update((phase["runbook"], phase["gate"], *phase["agents"]))
            expected.update(f"skills/{skill}.md" for skill in phase["skills"])
        self.assertEqual([path for path in expected if not (ROOT / path).is_file()], [])

    def test_phase_contracts_agree(self) -> None:
        orchestrator = (ROOT / "workflow/orchestrator.md").read_text(encoding="utf-8")
        for phase in PHASES:
            runbook = (ROOT / phase["runbook"]).read_text(encoding="utf-8")
            agents = [(ROOT / path).read_text(encoding="utf-8") for path in phase["agents"]]
            gate = (ROOT / phase["gate"]).read_text(encoding="utf-8")
            for path in (phase["runbook"], *phase["agents"], phase["gate"]):
                self.assertIn(path, orchestrator)
            positions = [orchestrator.index(skill) for skill in phase["skills"]]
            self.assertEqual(positions, sorted(positions))
            for skill in phase["skills"]:
                self.assertIn(skill, runbook)
                self.assertTrue(any(skill in agent for agent in agents))
                self.assertTrue((ROOT / "skills" / f"{skill}.md").is_file())
            for output in phase["outputs"]:
                for text in (orchestrator, runbook, gate):
                    self.assertIn(output, text)

    def test_requirements_challenge_precedes_persona_and_pain_points(self) -> None:
        runbook = (ROOT / "workflow/run-phase-01-discover.md").read_text(encoding="utf-8")
        ordered = (
            "source-evidence-analysis-skill",
            "advocate-review-skill",
            "cynic-review-skill",
            "debate-synthesis-skill",
            "persona-synthesis-skill",
            "pain-point-extraction-skill",
        )
        positions = [runbook.index(name) for name in ordered]
        self.assertEqual(positions, sorted(positions))

    def test_frozen_pipeline_order(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        readme = readme[readme.index("## Workflow Overview"):]
        labels = ("Phase 1 — Discover", "Gate D1", "Phase 2 — Define & Ideate", "Gate D2", "Phase 3 — Design & Prototype", "Gate D3", "Phase 4 — Validate", "Gate D4", "Verified Workable Prototype")
        positions = [readme.index(label) for label in labels]
        self.assertEqual(positions, sorted(positions))
