from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]


class AssignmentComplianceTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_assignment_chain_is_explicit(self) -> None:
        readme = self.read("README.md")
        self.assertIn("BRD → Research → Ideation → Design → Validation → Verified Workable Prototype", readme)
        for phase in ("Discover", "Define & Ideate", "Design & Prototype", "Validate"):
            self.assertIn(phase, readme)

    def test_one_solution_only_ideation_failure_is_guarded(self) -> None:
        generation = self.read("skills/concept-generation-skill.md")
        evaluation = self.read("skills/concept-evaluation-skill.md")
        self.assertIn("multiple candidate", generation.lower())
        self.assertIn("one-option result requires explicit justification", generation.lower())
        self.assertIn("one-concept input fails", evaluation.lower())

    def test_missing_design_system_is_not_invented(self) -> None:
        skill = self.read("skills/design-system-audit-skill.md")
        self.assertIn("NOT AVAILABLE", skill)
        self.assertIn("Do not invent", skill)

    def test_missing_error_states_are_guarded(self) -> None:
        skill = self.read("skills/interaction-state-skill.md")
        for state in ("loading", "empty", "error", "validation error", "cancellation", "timeout", "unavailable service"):
            self.assertIn(state, skill.lower())

    def test_unresolved_brd_risk_reaches_final_validation(self) -> None:
        skill = self.read("skills/edge-case-validation-skill.md")
        self.assertIn("outputs/phase-01/brd-risk-review.md", skill)
        self.assertIn("UNRESOLVED", skill)

    def test_synthetic_usability_cannot_overclaim(self) -> None:
        skill = self.read("skills/synthetic-usability-test-skill.md")
        self.assertIn("SYNTHETIC / HEURISTIC", skill)
        self.assertIn("Never claim participants were observed", skill)

    def test_accessibility_cannot_claim_false_compliance(self) -> None:
        skill = self.read("skills/accessibility-audit-skill.md")
        self.assertIn("Never claim full WCAG compliance", skill)

    def test_only_d4_can_verify_prototype(self) -> None:
        orchestrator = self.read("workflow/orchestrator.md")
        phase3 = self.read("workflow/run-phase-03-design.md")
        self.assertIn("Only D4 APPROVE verifies the prototype", orchestrator)
        self.assertIn("does not claim the prototype is validated or verified", phase3)

    def test_every_gate_is_human_and_has_three_decisions(self) -> None:
        for gate in ("gate-d1-research-review.md", "gate-d2-definition-review.md", "gate-d3-prototype-review.md", "gate-d4-final-validation-review.md"):
            text = self.read(f"gates/{gate}")
            for decision in ("APPROVE", "REVISE", "REJECT"):
                self.assertIn(decision, text)
            self.assertRegex(text, r"(?i)(human|agents? cannot|agents? may.*cannot approve)")

