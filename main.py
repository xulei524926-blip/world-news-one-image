#!/usr/bin/env python3
"""Sum up 20 November 2026's world news in one image.

The entry image is a broadsheet front page composed for this bounty and
committed beside this program as entry.png. Running the program writes
that image, byte for byte, to /output/entry.png. It uses only the
Python standard library, touches no network, and produces identical
output on every run.
"""
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    dst = Path("/output/entry.png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
