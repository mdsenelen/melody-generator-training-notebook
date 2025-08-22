"""Safe action utilities."""
from __future__ import annotations
from typing import List


def restrict_to_bc_topk(logits: List[float], k: int) -> List[float]:
    """Keep only the top-k logits, masking others with -inf."""
    if k >= len(logits):
        return logits
    sorted_indices = sorted(range(len(logits)), key=logits.__getitem__, reverse=True)
    threshold = logits[sorted_indices[k-1]]
    return [v if v >= threshold else float("-inf") for v in logits]
