"""Session-scoped execution helpers for the public pipeline demo."""

from __future__ import annotations

from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path
from typing import Callable, Mapping
from zipfile import ZIP_DEFLATED, ZipFile

from .contracts import PHASES, PhaseContract


DECISIONS = ("APPROVE", "REVISE", "REJECT")


@dataclass
class PipelineSession:
    """Mutable state belonging to one browser session only."""

    current_phase: int = 1
    phase_status: dict[int, str] = field(default_factory=lambda: {p.number: "NOT STARTED" for p in PHASES})
    gate_status: dict[int, str] = field(default_factory=lambda: {p.number: "PENDING" for p in PHASES})
    artifacts: dict[str, str] = field(default_factory=dict)
    logs: list[str] = field(default_factory=list)


def phase_by_number(number: int) -> PhaseContract:
    return next(phase for phase in PHASES if phase.number == number)


def run_phase(
    state: PipelineSession,
    number: int,
    generator: Callable[[PhaseContract, Mapping[str, str]], Mapping[str, str]],
) -> None:
    if number != state.current_phase:
        raise ValueError(f"Phase {number} is not eligible; Phase {state.current_phase} is current.")
    if state.phase_status[number] == "REJECTED":
        raise ValueError(f"Gate D{number} rejected the workflow; reset the session to restart.")
    if number > 1 and state.gate_status[number - 1] != "APPROVE":
        raise ValueError(f"Gate D{number - 1} requires explicit APPROVE.")
    phase = phase_by_number(number)
    state.logs.append(f"Phase {number}: dispatched {', '.join(phase.agents)}")
    generated = dict(generator(phase, state.artifacts))
    missing = [path for path in phase.outputs if not generated.get(path, "").strip()]
    extras = [path for path in generated if path not in phase.outputs]
    if missing or extras:
        raise ValueError(f"Invalid phase output. Missing={missing}; unexpected={extras}")
    state.artifacts.update(generated)
    state.phase_status[number] = "READY FOR REVIEW"
    state.gate_status[number] = "PENDING"
    state.logs.extend(f"Phase {number}: completed skill {skill}" for skill in phase.skills)
    state.logs.append(f"Gate {phase.gate_id}: awaiting explicit human decision")


def record_gate(state: PipelineSession, number: int, decision: str) -> None:
    decision = decision.upper()
    if decision not in DECISIONS:
        raise ValueError(f"Decision must be one of {DECISIONS}.")
    if state.phase_status[number] != "READY FOR REVIEW":
        raise ValueError(f"Phase {number} is not ready for gate review.")
    state.gate_status[number] = decision
    state.logs.append(f"Gate D{number}: human decision recorded as {decision}")
    if decision == "APPROVE":
        state.phase_status[number] = "APPROVED"
        state.current_phase = min(number + 1, len(PHASES))
        return
    state.phase_status[number] = "REVISION REQUIRED" if decision == "REVISE" else "REJECTED"
    for phase in PHASES[number - 1 :]:
        if phase.number > number:
            state.phase_status[phase.number] = "NOT STARTED"
            state.gate_status[phase.number] = "PENDING"
            for path in phase.outputs:
                state.artifacts.pop(path, None)
    state.current_phase = number


def repository_generator(root: Path) -> Callable[[PhaseContract, Mapping[str, str]], Mapping[str, str]]:
    """Load the checked-in synthetic demonstration artifacts without changing files."""

    def generate(phase: PhaseContract, _: Mapping[str, str]) -> Mapping[str, str]:
        return {path: (root / path).read_text(encoding="utf-8") for path in phase.outputs}

    return generate


def artifact_zip(state: PipelineSession) -> bytes:
    buffer = BytesIO()
    with ZipFile(buffer, "w", ZIP_DEFLATED) as archive:
        for path, content in sorted(state.artifacts.items()):
            archive.writestr(path, content)
        archive.writestr("execution-log.txt", "\n".join(state.logs))
    return buffer.getvalue()
