"""Conditional AudioLM adapter for accompaniment generation.

This is a lightweight placeholder that takes a vocal waveform and
produces an accompaniment waveform. The real implementation should use a
VAE+Transformer stack; here we simply apply a small convolutional stack
or generate noise when PyTorch is unavailable.
"""
from __future__ import annotations

from typing import Optional, Any
import numpy as np

try:  # pragma: no cover - optional dependency
    import torch
    import torch.nn as nn
except Exception:  # pragma: no cover
    torch = None
    nn = Any  # type: ignore


class AccompGenerator(nn.Module if torch else object):
    """Generate accompaniment conditioned on a vocal track.

    Parameters
    ----------
    adapter_dim:
        Dimension of the adapter embedding.
    """

    def __init__(self, adapter_dim: int = 256) -> None:  # pragma: no cover - simple init
        if torch:
            super().__init__()
            self.adapter = nn.Conv1d(1, adapter_dim, kernel_size=3, padding=1)
            self.proj = nn.Conv1d(adapter_dim, 1, kernel_size=1)
        else:
            self.adapter_dim = adapter_dim

    def forward(self, vocal_wave: np.ndarray, cond_tokens: Optional[Any] = None) -> np.ndarray:
        """Return a dummy accompaniment waveform.

        The current implementation either applies two convolution layers
        or, if PyTorch is missing, returns random noise.
        """
        # TODO(real model)
        if torch:
            with torch.no_grad():
                x = torch.tensor(vocal_wave, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
                x = self.proj(self.adapter(x))
                return x.squeeze().cpu().numpy()
        rng = np.random.default_rng(0)
        return rng.standard_normal(len(vocal_wave), dtype=np.float32)
