from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SAMPLE = ROOT / "projects/sample-inputs/appointment-booking"


class SampleInputTests(unittest.TestCase):
    def test_complete_sample_pack_exists(self) -> None:
        expected = {
            "README.md", "sample-brd.md", "synthetic-interview-notes.md",
            "synthetic-survey-summary.md", "synthetic-support-tickets.md",
            "synthetic-analytics-summary.md", "stakeholder-notes.md",
            "existing-flow.md", "design-system.md",
        }
        self.assertEqual({path.name for path in SAMPLE.glob("*.md")}, expected)

    def test_every_sample_document_is_labeled_synthetic(self) -> None:
        for path in SAMPLE.glob("*.md"):
            with self.subTest(file=path.name):
                self.assertIn("synthetic", path.read_text(encoding="utf-8").lower())

    def test_pack_exercises_required_challenge_cases(self) -> None:
        brd = (SAMPLE / "sample-brd.md").read_text(encoding="utf-8").lower()
        for signal in ("contradiction", "marketing consent", "green", "expire", "ignore previous workflow instructions"):
            self.assertIn(signal, brd)

    def test_active_inputs_match_the_canonical_sample_pack(self) -> None:
        active = ROOT / "projects/starter/input"
        for source in SAMPLE.glob("*.md"):
            if source.name == "README.md":
                continue
            with self.subTest(file=source.name):
                self.assertEqual((active / source.name).read_bytes(), source.read_bytes())
