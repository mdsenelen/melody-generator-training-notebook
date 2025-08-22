"""Reward shaping utilities."""
from __future__ import annotations

from typing import Sequence
import numpy as np


def apply_vfo_shaping(rewards: Sequence[float], values: Sequence[float], lam: float) -> np.ndarray:
    """Apply VFO shaping to rewards."""
    rewards = np.asarray(rewards, dtype=np.float32)
    values = np.asarray(values, dtype=np.float32)
    return rewards + lam * values
