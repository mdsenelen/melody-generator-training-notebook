"""Simple CLI/API for generation."""
from __future__ import annotations

import argparse
from typing import Optional, List

from ..utils.endpoints import (
    generate_accompaniment,
    generate_melody_in_key,
)
from ..utils.theory import get_available_chords


def list_chords() -> List[str]:
    """Expose chord names that can be displayed to the user."""
    return get_available_chords()


def prepare_chord_button(chord: str) -> str:
    """Return the label for the UI button that triggers melody generation."""
    return f"Create melody in {chord} key"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run demo generation")
    parser.add_argument(
        "--list-chords", action="store_true", help="Display available chords"
    )
    parser.add_argument("--select", type=str, help="Select a chord by name")
    parser.add_argument(
        "--generate", action="store_true", help="Generate melody after selecting"
    )

    args = parser.parse_args()

    if args.demo:
        path = generate_accompaniment("dummy.wav")
        print(f"Generated: {path}")

    if args.list_chords:
        print("Available chords: " + ", ".join(list_chords()))

    if args.select:
        button = prepare_chord_button(args.select)
        print(f"Button: {button}")
        if args.generate:
            out = generate_melody_in_key(args.select)
            print(f"Generated: {out}")


if __name__ == "__main__":  # pragma: no cover
    main()
