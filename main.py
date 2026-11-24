#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry (program/v1 harness).

Writes a single line of horror to /output/entry.txt: one sentence,
under 200 characters, plain ASCII. The line is a fixed string, so the
program is fully deterministic; it verifies its own output by reading
the file back and comparing bytes.
"""

import os

LINE = "Every night my wife whispers my name in her sleep, and tonight she used my middle name, which she never knew."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text == text.strip(), "no surrounding whitespace"
    assert "\n" not in text, "single line only"
    assert text.isascii(), "plain ASCII only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file must hold exactly the line, byte for byte.
    # The gate counts characters (1-200, not only whitespace), so also assert
    # the decoded text matches, not just the raw bytes.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "read-back mismatch"
    assert written.decode("utf-8").strip() == text, "decoded text mismatch"
    print(f"wrote {len(written)} bytes ({len(text)} chars) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
