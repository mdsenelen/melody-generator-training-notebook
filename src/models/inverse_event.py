"""Inverse dynamics model for IDDM."""
from __future__ import annotations

from typing import Sequence
import numpy as np


class InverseEventModel:
    """Predict next action given state transitions."""

    def __init__(self, num_actions: int = 10) -> None:
        self.num_actions = num_actions
        self.w = np.zeros((num_actions,), dtype=np.float32)

    def train(self, states: Sequence[int], next_states: Sequence[int], actions: Sequence[int], lr: float = 0.1, epochs: int = 50) -> None:
        for _ in range(epochs):
            pred = self(states, next_states)
            grad = np.zeros_like(self.w)
            for p, a in zip(pred, actions):
                grad[a] += p[a] - 1
            self.w -= lr * grad

    def __call__(self, states: Sequence[int], next_states: Sequence[int]) -> np.ndarray:
        logits = np.tile(self.w, (len(states), 1))
        e = np.exp(logits - logits.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)
