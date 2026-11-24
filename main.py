#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes a single sentence -- a pitch for the worst, most useless app
imaginable -- to entry.txt inside $ENTRY_OUTPUT_DIR (default /output).
Standard library only, no network, deterministic.
"""

import os

PITCH = "PebblePal: an app that scans your driveway pebbles, assigns each one a personality, and sends a daily mood report on which pebble is thriving and which one needs space, for homeowners who refuse to let a single stone go unmonitored."


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 240, f"pitch must be 1-240 chars, got {len(text)}"
    assert text.strip(), "pitch must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
