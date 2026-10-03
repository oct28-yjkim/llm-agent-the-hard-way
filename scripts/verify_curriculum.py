from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_LABS = [
    "00-baseline-and-boundaries",
    "01-raw-responses-api",
    "02-streaming-and-errors",
    "03-conversation-state",
    "04-structured-output",
    "05-tool-calling-loop",
    "06-retrieval-from-scratch",
    "07-memory",
    "08-agent-runtime",
    "09-approvals-and-security",
    "10-evals-and-tracing",
    "11-multi-agent",
    "12-production",
    "13-sdk-comparison",
    "14-capstone",
]


def main() -> int:
    missing = [name for name in EXPECTED_LABS if not (ROOT / "labs" / name / "README.md").is_file()]
    if missing:
        print("Missing lab README files:")
        for name in missing:
            print(f"- {name}")
        return 1
    print(f"Curriculum structure OK: {len(EXPECTED_LABS)} labs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
