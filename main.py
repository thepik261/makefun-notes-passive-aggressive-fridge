#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one funny passive-aggressive note from a smart fridge to its
owner at /output/entry.txt. Pure Python standard library, deterministic:
the same note every run.
"""

import os

NOTE = (
    "The ice maker made 214 cubes this week. "
    "You used none of them. I'm not mad. I'm just cold."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The note is a single line, 90 characters: within the gate's
    # 1-200 character range and not only whitespace.
    assert 1 <= len(NOTE) <= 200, "note must be 1-200 characters"
    assert NOTE.strip(), "note must not be only whitespace"
    assert "\n" not in NOTE, "note must be a single line"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(NOTE + "\n")

    # The grader collects outputs as a different user, so the file we
    # created must be world-readable. Never chmod /output itself.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
