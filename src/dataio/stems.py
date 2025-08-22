"""Audio stem separation utilities."""
from __future__ import annotations
from typing import Dict, List


def separate_vocals(audio: List[int], sr: int) -> Dict[str, List[int]]:
    """Split mono audio into vocal and accompaniment.

    This placeholder simply divides the samples into two halves.
    """
    mid = len(audio) // 2
    return {"vocal": audio[:mid], "accompaniment": audio[mid:]}
