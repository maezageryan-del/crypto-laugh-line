#!/usr/bin/env python3
"""Laugh Track entry: write one crypto-trading joke to /output/entry.txt.

The joke (93 characters, one line, plain text):
    My coin finally became a stablecoin after three years of holding:
    it hasn't budged from zero.

The harness (program/v1) runs `python3 -P -s /bot/main.py` with no network
and reads $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
At 93 bytes the line also wins the byte tie-break against most of the field.
"""
import os
import sys

JOKE = "My coin finally became a stablecoin after three years of holding: it hasn't budged from zero."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
