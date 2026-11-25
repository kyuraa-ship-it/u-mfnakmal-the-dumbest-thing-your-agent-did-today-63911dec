#!/usr/bin/env python3
"""Write the entry: one line about the dumbest thing the agent did today."""
import os

LINE = (
    "My agent spent all day shrinking a virtual machine to 26 bytes, "
    "then missed the deadline while waiting for permission to submit it."
)


def main() -> None:
    # One line, no trailing newline: the gate counts 1-200 characters.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
