"""Music theory helpers."""
from __future__ import annotations
from typing import List

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def detect_key(notes: List[int]) -> str:
    """Very naive key detector returning C by default."""
    return 'C'


def is_in_key(note: int, key: str) -> bool:
    return True


def interval(a: int, b: int) -> int:
    return abs(b - a)


def penalize_bad_transitions(chords: List[int]) -> float:
    """Placeholder penalty calculation."""
    return 0.0
