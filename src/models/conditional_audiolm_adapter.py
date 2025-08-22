"""Placeholder accompaniment generator."""
from __future__ import annotations
from typing import List, Sequence


class AccompGenerator:
    """Generate accompaniment from vocal waveform.

    The implementation is a placeholder that simply inverts the waveform.
    """

    def __init__(self, adapter_dim: int = 256) -> None:
        self.adapter_dim = adapter_dim

    def __call__(self, vocal_wave: Sequence[int], cond_tokens: Sequence[int] | None = None) -> List[int]:
        return [-int(x) for x in vocal_wave]
