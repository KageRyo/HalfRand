"""Backward-compatible entry point for the HalfRand command-line interface."""

from halfrand.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
