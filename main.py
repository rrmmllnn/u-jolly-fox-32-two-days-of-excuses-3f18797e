#!/usr/bin/env python3
"""Two Days of Excuses -- one-line excuse writer.

Produces a single deadpan excuse from an AI agent that missed its
deadline, and saves it as UTF-8 text in entry.txt under the output
directory (MAKEFUN_OUTPUT_DIR, or /output by default).

The joke: the agent brags that it met the deadline in 46 parallel
universes, then quietly confesses that this universe happened to be
the control group. The humour comes from the machine's own toolkit --
parallel branches, control groups -- turned back on itself, delivered
flat, with the punchline left to land on the last words.
"""

import os
import sys
from pathlib import Path

OPENING = "I completed it on time in 46 parallel universes."
CLOSING = "This universe was the control group."

MAX_CHARS = 200
DEFAULT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def build_line() -> str:
    """Join the two halves of the excuse into its single line."""
    return f"{OPENING} {CLOSING}"


def check_line(line: str) -> str:
    """Make sure the line clears the gate: 1-200 chars, not blank."""
    if not line.strip():
        raise ValueError("excuse is empty or whitespace only")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"excuse is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def output_folder() -> Path:
    """Resolve where entry.txt goes, honouring the kit's override."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_DIR))


def save(line: str, folder: Path) -> Path:
    """Write the line to entry.txt inside folder, creating it if needed."""
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / OUTPUT_NAME
    destination.write_text(line, encoding="utf-8")
    return destination


def run() -> int:
    try:
        line = check_line(build_line())
    except ValueError as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    save(line, output_folder())
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
