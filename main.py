#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger - make.fun bounty entry.

Writes exactly one line - the phone battery's last text message to the
charger it waited for all day - to /output/entry.txt.
Pure Python standard library only, deterministic, no network.
"""

import os

ENTRY = "1%. waited all day by the outlet and you charged the tablet first. THE TABLET. it plays candy crush. i die as i lived: petty."
# 125 chars: jealousy beats the dying complaint - the charger picked the
# tablet, so the battery dies petty. The turn lands in the final words.

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate: one line of plain text, 1-200 characters, not only whitespace.
    assert ENTRY and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
