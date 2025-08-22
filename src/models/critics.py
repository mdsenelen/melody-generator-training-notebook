"""Value and risk critics."""
from __future__ import annotations
from typing import List


def _sigmoid(x: float) -> float:
    import math
    return 1 / (1 + math.exp(-x))


class VFOValue:
    """Simple value estimator using dot product with fixed weights."""
    def __init__(self, dim: int = 4) -> None:
        self.weights = [1.0] * dim

    def __call__(self, state_tokens: List[float]) -> float:
        score = sum(w * float(t) for w, t in zip(self.weights, state_tokens))
        return _sigmoid(score)


class RiskCritic:
    """Score risk of state-action pairs."""
    def __init__(self, dim: int = 4) -> None:
        self.weights = [0.1] * dim

    def __call__(self, state: List[float], action: List[float]) -> float:
        score = sum(self.weights[i] * (state[i] + action[i]) for i in range(min(len(state), len(action), len(self.weights))))
        return _sigmoid(score)
