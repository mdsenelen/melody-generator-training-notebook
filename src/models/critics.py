"""Critic models including Value-from-Observations."""
from __future__ import annotations

from typing import Sequence
import numpy as np


class VFOValue:
    """Simple value function approximator."""

    def __init__(self) -> None:
        self.w = 0.0

    def train(self, states: Sequence[float], labels: Sequence[float], lr: float = 0.1, epochs: int = 100) -> None:
        for _ in range(epochs):
            pred = self(states)
            grad = np.mean((pred - labels) * states)
            self.w -= lr * grad

    def __call__(self, states: Sequence[float]) -> np.ndarray:
        arr = np.asarray(states, dtype=np.float32)
        return arr * self.w
