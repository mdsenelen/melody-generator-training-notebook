"""Training loops for various models."""
from __future__ import annotations

from typing import Dict, Any
import numpy as np

from ..models.critics import VFOValue
from ..models.inverse_event import InverseEventModel
from .reward_shaping import apply_vfo_shaping
from .safe_actions import RiskCritic


def train_vfo_value(states: np.ndarray, labels: np.ndarray) -> VFOValue:
    model = VFOValue()
    model.train(states, labels)
    return model


def train_inverse(dataset: Dict[str, np.ndarray]) -> InverseEventModel:
    model = InverseEventModel(num_actions=dataset["num_actions"])
    model.train(dataset["s"], dataset["s_next"], dataset["a"])
    return model


def train_bc() -> None:  # pragma: no cover - placeholder
    pass


def train_ppo() -> None:  # pragma: no cover - placeholder
    pass
