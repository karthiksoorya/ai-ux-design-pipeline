from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]

SKILLS = {
    "source-evidence-analysis-skill": "outputs/phase-01/research-gaps.md",
    "advocate-review-skill": "outputs/phase-01/brd-risk-review.md",
    "cynic-review-skill": "outputs/phase-01/brd-risk-review.md",
    "debate-synthesis-skill": "outputs/phase-01/brd-risk-review.md",
    "persona-synthesis-skill": "outputs/phase-01/persona.md",
    "pain-point-extraction-skill": "outputs/phase-01/pain-points.md",
    "problem-framing-skill": "outputs/phase-02/problem-definition.md",
    "journey-mapping-skill": "outputs/phase-02/journey-map.md",
    "opportunity-prioritization-skill": "outputs/phase-02/opportunities.md",
    "concept-generation-skill": "outputs/phase-02/concept-options.md",
    "concept-evaluation-skill": "outputs/phase-02/selected-concept.md",
    "user-flow-skill": "outputs/phase-03/user-flow.md",
    "information-architecture-skill": "outputs/phase-03/screen-spec.md",
    "screen-specification-skill": "outputs/phase-03/screen-spec.md",
    "interaction-state-skill": "outputs/phase-03/interaction-states.md",
    "prototype-generation-skill": "outputs/phase-03/prototype-spec.md",
    "synthetic-usability-test-skill": "outputs/phase-04/validation-report.md",
    "cognitive-friction-analysis-skill": "outputs/phase-04/validation-report.md",
    "accessibility-audit-skill": "outputs/phase-04/accessibility-audit.md",
    "design-system-audit-skill": "outputs/phase-04/validation-report.md",
    "requirement-coverage-skill": "outputs/phase-04/requirement-coverage.md",
    "edge-case-validation-skill": "outputs/phase-04/validation-report.md",
}


class SkillContractTests(unittest.TestCase):
    def test_each_skill_has_a_complete_contract(self) -> None:
        for skill_name, expected_output in SKILLS.items():
            with self.subTest(skill=skill_name):
                text = (ROOT / "skills" / f"{skill_name}.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "))
                for heading in ("Name & Description", "Role", "Input", "Output", "Rules & Guardrails"):
                    self.assertIn(f"## {heading}", text)
                self.assertIn(expected_output, text)

    def test_exactly_the_frozen_twenty_two_skills_exist(self) -> None:
        actual = {path.stem for path in (ROOT / "skills").glob("*.md")}
        self.assertEqual(actual, set(SKILLS))

    def test_every_skill_is_declared_once_by_an_agent(self) -> None:
        agent_text = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "agents").glob("*.md")
        )
        for skill_name in SKILLS:
            self.assertEqual(agent_text.count(f"  - {skill_name}\n"), 1)
