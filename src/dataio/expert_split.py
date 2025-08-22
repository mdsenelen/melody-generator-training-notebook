"""Expert/background tagging utilities."""
from __future__ import annotations

from typing import Iterable, Dict, List, Tuple


def tag_expert_background(meta: Iterable[Dict[str, int]]) -> Tuple[List[int], List[int]]:
    """Tag indices of expert and background samples.

    Parameters
    ----------
    meta:
        Iterable of metadata dictionaries each containing an ``expert`` key
        with value 1 for expert data and 0 otherwise.
    """
    expert_idx, background_idx = [], []
    for i, m in enumerate(meta):
        if m.get("expert", 0) == 1:
            expert_idx.append(i)
        else:
            background_idx.append(i)
    return expert_idx, background_idx
