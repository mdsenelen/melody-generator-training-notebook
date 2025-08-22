"""Text to melody token generator (placeholder)."""
from __future__ import annotations

from typing import List


def text_to_melody(lyrics: str, mood: str, key: str, tempo: int) -> List[int]:
    """Convert text description to a dummy list of melody tokens."""
    tokens = [len(lyrics.split()), len(mood), len(key), tempo % 12]
    return tokens
