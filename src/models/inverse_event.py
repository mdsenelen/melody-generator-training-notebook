"""Inverse dynamics model placeholder."""
from __future__ import annotations
from typing import List


def predict_action(s_t: List[int], s_tp1: List[int]) -> List[int]:
    """Return difference between states as action."""
    length = min(len(s_t), len(s_tp1))
    return [s_tp1[i] - s_t[i] for i in range(length)]
