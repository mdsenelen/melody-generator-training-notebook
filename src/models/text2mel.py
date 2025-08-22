"""Text to melody placeholder."""
from __future__ import annotations
import random
from typing import List


def text_to_melody(lyrics: str, mood: str, key: str, tempo: int) -> List[int]:
    """Convert text into a dummy melody token sequence."""
    random.seed(len(lyrics) + tempo)
    return [random.randint(0, 127) for _ in range(16)]
