"""Expert/background dataset tagging."""
from __future__ import annotations
from typing import Dict, Iterable, List


def tag_expert_background(meta: Iterable[Dict]) -> Dict[str, List[int]]:
    """Return indices for expert and background samples based on metadata."""
    expert, background = [], []
    for idx, m in enumerate(meta):
        (expert if m.get("quality") == "high" else background).append(idx)
    return {"expert_indices": expert, "background_indices": background}
