"""Validation and deterministic routing; no AI calls and no implicit writes."""

from dataclasses import asdict, dataclass
from pathlib import Path
import re

from .contracts import FROZEN_FILES, PHASES, PhaseContract


@dataclass(frozen=True)
class ValidationReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    markdown_files_inspected: int
    skills_validated: int

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, object]:
        return {"ok": self.ok, **asdict(self)}


@dataclass(frozen=True)
class Route:
    position: str
    action: str
    runbook: str | None
    gate: str | None
    missing: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class WorkflowRuntime:
    """Inspect and route a repository that follows the frozen v2.0 contract."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).resolve()

    def _read(self, relative_path: str) -> str:
        return (self.root / relative_path).read_text(encoding="utf-8")

    def validate(self) -> ValidationReport:
        errors: list[str] = []
        warnings: list[str] = []
        markdown = tuple(self.root.rglob("*.md"))

        for relative_path in FROZEN_FILES:
            if not (self.root / relative_path).is_file():
                errors.append(f"Missing frozen file: {relative_path}")

        if errors:
            return ValidationReport(tuple(errors), tuple(warnings), len(markdown), 0)

        orchestrator = self._read("workflow/orchestrator.md")
        config = self._read("project.config.md")
        declared_skills: set[str] = set()

        for phase in PHASES:
            runbook = self._read(phase.runbook)
            agents = {path: self._read(path) for path in phase.agents}
            gate = self._read(phase.gate)
            for path in (phase.runbook, *phase.agents, phase.gate):
                if path not in orchestrator:
                    errors.append(f"Orchestrator does not reference {path}")
                if path not in config:
                    errors.append(f"Configuration does not reference {path}")

            ordered_positions = [orchestrator.find(skill) for skill in phase.skills]
            if -1 in ordered_positions or ordered_positions != sorted(ordered_positions):
                errors.append(f"Orchestrator skill order differs for Phase {phase.number}")

            for skill in phase.skills:
                declared_skills.add(skill)
                skill_path = f"skills/{skill}.md"
                skill_text = self._read(skill_path)
                for heading in ("Name & Description", "Role", "Input", "Output", "Rules & Guardrails"):
                    if f"## {heading}" not in skill_text:
                        errors.append(f"{skill_path} lacks section: {heading}")
                if skill not in runbook or not any(skill in text for text in agents.values()):
                    errors.append(f"{skill} is not consistently declared for Phase {phase.number}")

            for output in phase.outputs:
                for owner, text in (("orchestrator", orchestrator), (phase.runbook, runbook), (phase.gate, gate)):
                    if output not in text:
                        errors.append(f"{owner} does not reference contract output {output}")
                if not any(output in text for text in agents.values()):
                    errors.append(f"No Phase {phase.number} agent owns contract output {output}")

        actual_skills = {path.stem for path in (self.root / "skills").glob("*.md")}
        if actual_skills != declared_skills:
            errors.append(f"Skill set mismatch: declared={sorted(declared_skills)}, actual={sorted(actual_skills)}")

        state = self._read("project.state.md")
        for gate_id in (phase.gate_id for phase in PHASES):
            if not re.search(rf"\| {gate_id} .+ \|", state):
                errors.append(f"project.state.md lacks {gate_id} status row")

        return ValidationReport(tuple(errors), tuple(warnings), len(markdown), len(actual_skills))

    def _has_project_inputs(self) -> bool:
        input_dir = self.root / "projects/starter/input"
        return input_dir.is_dir() and any(path.name != ".gitkeep" for path in input_dir.iterdir())

    def _outputs_complete(self, phase: PhaseContract) -> bool:
        return all((self.root / path).is_file() for path in phase.outputs)

    def _gate_approved(self, phase: PhaseContract) -> bool:
        review = self.root / phase.review
        if not review.is_file():
            return False
        text = review.read_text(encoding="utf-8")
        return bool(re.search(r"(?im)^\s*(?:[-*]\s*)?(?:decision\s*:\s*)?APPROVE(?:D)?\s*$", text))

    def route(self) -> Route:
        report = self.validate()
        if not report.ok:
            return Route("Invalid workflow", "repair-contract", None, None, report.errors)

        for phase in PHASES:
            if phase.number > 1 and not self._gate_approved(PHASES[phase.number - 2]):
                previous = PHASES[phase.number - 2]
                return Route(f"Gate {previous.gate_id}", "human-review", None, previous.gate)

            if not self._outputs_complete(phase):
                missing = tuple(path for path in phase.outputs if not (self.root / path).is_file())
                if phase.number == 1 and not self._has_project_inputs():
                    return Route("Phase 1 — Discover", "await-inputs", phase.runbook, None, missing)
                return Route(f"Phase {phase.number} — {phase.name}", "run-phase", phase.runbook, None, missing)

            if not self._gate_approved(phase):
                return Route(f"Gate {phase.gate_id}", "human-review", None, phase.gate)

        return Route("Complete", "report-completion", None, None)
