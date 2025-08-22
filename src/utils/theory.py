"""Basic music theory helpers."""
from __future__ import annotations

from typing import Sequence

KEYS = {
    "C": {0, 2, 4, 5, 7, 9, 11},
    "Am": {0, 2, 3, 5, 7, 8, 10},
}


def detect_key(notes: Sequence[int]) -> str:
    for name, scale in KEYS.items():
        if all(n % 12 in scale for n in notes):
            return name
    return "C"


def is_in_key(note: int, key: str) -> bool:
    return note % 12 in KEYS.get(key, KEYS["C"])


def interval(a: int, b: int) -> int:
    return abs(a - b)


def penalize_bad_transitions(chords: Sequence[int]) -> float:
    bad = sum(interval(a, b) > 7 for a, b in zip(chords, chords[1:]))
    return float(bad)
