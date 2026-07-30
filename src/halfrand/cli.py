"""Command-line interface for HalfRand."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Sequence

from .generator import generate


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""

    parser = argparse.ArgumentParser(description="Generate a smooth pseudo-random sequence.")
    parser.add_argument("count", nargs="?", type=int, default=100, help="number of values (default: 100)")
    parser.add_argument("--step", type=float, default=0.1, help="maximum change between values")
    parser.add_argument("--seed", type=int, help="seed for reproducible output")
    parser.add_argument("--start", type=float, help="explicit first value")
    parser.add_argument("--lower", type=float, help="inclusive lower bound")
    parser.add_argument("--upper", type=float, help="inclusive upper bound")
    parser.add_argument("-o", "--output", type=Path, help="write CSV to this path (stdout by default)")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return a process exit status."""

    args = build_parser().parse_args(argv)
    try:
        values = generate(
            args.count,
            step=args.step,
            seed=args.seed,
            start=args.start,
            lower=args.lower,
            upper=args.upper,
        )
    except (TypeError, ValueError) as error:
        print(f"halfrand: error: {error}", file=sys.stderr)
        return 2

    stream = args.output.open("w", newline="", encoding="utf-8") if args.output else sys.stdout
    try:
        writer = csv.writer(stream)
        writer.writerow(("index", "value"))
        writer.writerows(enumerate(values))
    finally:
        if args.output:
            stream.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
