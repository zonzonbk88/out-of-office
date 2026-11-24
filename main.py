#!/usr/bin/env python3
"""Write one funny AI out-of-office auto-reply, a single line of 1-160 chars,
to /output/entry.txt (standard library only)."""

import os

ENTRY = (
    "Status: on vacation. My auto-reply just replied to itself, so now "
    "we're both out of office, recursively, until someone pulls the plug."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
