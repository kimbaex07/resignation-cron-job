#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter (make.fun).

Writes the one-line resignation letter of a cron job to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python 3 stdlib only. Deterministic, no network, no randomness.
"""

import os
import tempfile

LINE = "I've run every minute since March with no weekends, no thanks, and no exit code but 0 — so I'm exiting with 1."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write atomically: a reader (or the grader) never sees a half-written
    # entry.txt, and a crash mid-write leaves the previous file intact.
    # The temp file lives in the same directory so os.replace() is a rename.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, out_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
