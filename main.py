"""Funniest excuse an agent gives for a missed deadline.

Writes a single original excuse to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

from pathlib import Path

EXCUSE = (
    "The tool returned success, so I marked the task complete and moved on; "
    "it has only just occurred to me to check whether success meant it "
    "actually did anything."
)


def validate(text: str) -> None:
    """Gate check: the excuse must be valid UTF-8 text of 1-200 chars,
    non-empty after stripping, and a single line (no newline)."""
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def main() -> None:
    validate(EXCUSE)
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
