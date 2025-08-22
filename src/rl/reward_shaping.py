"""Reward shaping utilities."""
from __future__ import annotations
from typing import List


def apply_vfo_reward(rewards: List[float], values: List[float], lam: float) -> List[float]:
    """Add value-based shaping term to rewards."""
    return [r + lam * v for r, v in zip(rewards, values)]
