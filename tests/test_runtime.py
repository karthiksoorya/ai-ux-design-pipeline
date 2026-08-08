from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from ai_ux_workflow.runtime import WorkflowRuntime


ROOT = Path(__file__).parents[1]


class RuntimeTests(unittest.TestCase):
    def test_validate_reports_a_clean_frozen_workflow(self) -> None:
        report = WorkflowRuntime(ROOT).validate()
        self.assertTrue(report.ok, report.errors)
        self.assertEqual(report.markdown_files_inspected, len(tuple(ROOT.rglob("*.md"))))
        self.assertEqual(report.skills_validated, 22)

    def test_current_route_does_not_mutate_state(self) -> None:
        state_before = (ROOT / "project.state.md").read_bytes()
        route = WorkflowRuntime(ROOT).route()
        self.assertIn(route.action, {"await-inputs", "run-phase", "human-review", "report-completion"})
        self.assertEqual((ROOT / "project.state.md").read_bytes(), state_before)

    def test_future_output_paths_are_contracts_not_broken_references(self) -> None:
        report = WorkflowRuntime(ROOT).validate()
        self.assertFalse(any("outputs/phase" in error for error in report.errors))

    def test_routes_through_all_four_phases_and_d4(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "project"
            shutil.copytree(ROOT, project, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            for generated in (project / "outputs").rglob("*.md"):
                generated.unlink()
            (project / "projects/starter/input/demo-brd.md").write_text("Goal: demo", encoding="utf-8")
            runtime = WorkflowRuntime(project)
            for index, phase in enumerate((
                ("phase-01", ("brd-risk-review.md", "persona.md", "pain-points.md", "research-gaps.md"), "d1-review.md"),
                ("phase-02", ("problem-definition.md", "journey-map.md", "opportunities.md", "concept-options.md", "selected-concept.md"), "d2-review.md"),
                ("phase-03", ("user-flow.md", "screen-spec.md", "interaction-states.md", "prototype-spec.md"), "d3-review.md"),
                ("phase-04", ("validation-report.md", "validation-issues.md", "requirement-coverage.md", "accessibility-audit.md"), "d4-review.md"),
            ), 1):
                route = runtime.route()
                self.assertEqual(route.action, "run-phase")
                for output in phase[1]:
                    (project / "outputs" / phase[0] / output).write_text("# Test artefact", encoding="utf-8")
                self.assertEqual(runtime.route().position, f"Gate D{index}")
                (project / "outputs/reviews" / phase[2]).write_text("Decision: APPROVE", encoding="utf-8")
            self.assertEqual(runtime.route().position, "Complete")
