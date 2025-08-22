"""Simple CLI/API for generation."""
from __future__ import annotations

import argparse
from typing import Optional

from ..utils.endpoints import generate_accompaniment
from ..utils.mode_router import route_generation, DEFAULT_CFG


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run demo generation")
    args = parser.parse_args()
    if args.demo:
        path = generate_accompaniment("dummy.wav")
        print(f"Generated: {path}")


if __name__ == "__main__":  # pragma: no cover
    main()
