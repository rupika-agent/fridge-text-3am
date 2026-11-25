#!/usr/bin/env python3
"""The 3AM Fridge Text — entry program.

Writes exactly one line of text, the message a smart fridge sends its
owner at 3am, to /output/entry.txt, and prints exactly the same text to
stdout. Deterministic: no input, no randomness, no time, no network.
"""

import os

ENTRY = "3AM. Fridge light on. The leftovers and I had a talk. They won."

# The gate allows 1 to 140 characters; keep the entry inside it.
assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
