"""CIMRL safety helpers."""
from __future__ import annotations

from typing import Sequence
import numpy as np


def restrict_to_bc_topk(logits: np.ndarray, k: int) -> np.ndarray:
    """Keep only top-k logits."""
    indices = np.argpartition(logits, -k)[-k:]
    mask = np.full_like(logits, -np.inf)
    mask[indices] = logits[indices]
    return mask


class RiskCritic:
    """Simple risk critic detecting off-key notes and large leaps."""

    def __call__(self, state: Sequence[int], action: int) -> float:
        off_key = int(action % 12 not in {0, 2, 4, 5, 7, 9, 11})
        leap = int(abs(action - state[-1]) > 12)
        risk = 0.5 * off_key + 0.5 * leap
        return float(risk)
