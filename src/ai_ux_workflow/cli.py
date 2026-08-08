"""Command-line interface for the frozen workflow runtime."""

import argparse
import json
from pathlib import Path

from .runtime import WorkflowRuntime
from .challenge import render_review


DEMO_BRD = """# Demo Appointment BRD
Goal: Allow customers to book an appointment online.
The customer must provide a name, email, and preferred time.
The system shall show available appointment slots and confirmation.
Cancellation ownership and network-error recovery are not specified.
Marketing consent is pre-selected during booking.
Color indicates whether a slot is available.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-ux-workflow")
    parser.add_argument("command", choices=("validate", "status", "demo"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--brd", type=Path, help="BRD to challenge in demo mode")
    parser.add_argument("--output", type=Path, help="Optional demo report destination")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    runtime = WorkflowRuntime(args.root)
    if args.command == "demo":
        text = args.brd.read_text(encoding="utf-8") if args.brd else DEMO_BRD
        report = render_review(text, str(args.brd) if args.brd else "built-in demo BRD")
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(report, encoding="utf-8")
            print(f"Demo report written to {args.output}")
        else:
            print(report)
        return 0
    result = runtime.validate() if args.command == "validate" else runtime.route()
    payload = result.to_dict()
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for key, value in payload.items():
            print(f"{key}: {value}")
    return 0 if args.command == "status" or payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
