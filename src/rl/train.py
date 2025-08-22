"""Training utilities (placeholders)."""
from __future__ import annotations
import random
from typing import Dict, List, Tuple

from src.models.critics import VFOValue
from src.models.inverse_event import predict_action
from src.rl.reward_shaping import apply_vfo_reward
from src.rl.safe_actions import restrict_to_bc_topk


def train_bc() -> float:
    """Return dummy BC loss."""
    return 0.0


def train_vfo_value() -> Tuple[float, float]:
    """Train value model on synthetic data and return expert/background medians."""
    model = VFOValue()
    expert_scores = [model([1, 1, 1, 1]) for _ in range(5)]
    background_scores = [model([0, 0, 0, 0]) for _ in range(5)]
    return (sum(expert_scores)/len(expert_scores), sum(background_scores)/len(background_scores))


def train_inverse() -> float:
    """Train inverse model on synthetic data and report top-1 accuracy."""
    s = [random.randint(0, 10) for _ in range(4)]
    a = [random.randint(0, 10) for _ in range(4)]
    s_next = [s[i] + a[i] for i in range(4)]
    pred = predict_action(s, s_next)
    correct = sum(int(p == a[i]) for i, p in enumerate(pred))
    return correct / len(a)


def train_ppo() -> Dict[str, float]:
    """Return dummy PPO stats."""
    rewards = [0.1, 0.2, 0.3]
    values = [0.5, 0.6, 0.7]
    shaped = apply_vfo_reward(rewards, values, lam=0.3)
    logits = [0.1, 0.4, 0.2]
    restricted = restrict_to_bc_topk(logits, k=2)
    mean_reward = sum(shaped) / len(shaped)
    return {"mean_reward": mean_reward, "restricted_logits": restricted}
