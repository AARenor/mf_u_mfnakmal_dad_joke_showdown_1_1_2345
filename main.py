"""Write one short dad joke for make.fun's bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5."""

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"


def output_dir() -> Path:
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
