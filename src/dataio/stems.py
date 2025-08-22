"""Audio stem separation utilities.

This module currently provides a placeholder vocal/accompaniment
separation using either torchaudio's HPSS or a naive split. The API is
kept stable so that it can be swapped with a proper UVR/MDX model later.
"""
from __future__ import annotations

from typing import Dict
import numpy as np

try:  # pragma: no cover - optional dependency
    import torch
    import torchaudio
except Exception:  # pragma: no cover - fallback for environments without torch
    torch = None
    torchaudio = None


def separate_vocals(audio: np.ndarray, sr: int) -> Dict[str, np.ndarray]:
    """Separate a mono waveform into vocal and accompaniment components.

    Parameters
    ----------
    audio:
        Waveform as a 1-D numpy array.
    sr:
        Sample rate in Hz.

    Returns
    -------
    dict
        Dictionary with keys ``vocal`` and ``accompaniment``.
    """
    if torch and torchaudio:
        waveform = torch.tensor(audio).unsqueeze(0)
        hpss = torchaudio.transforms.HPSS()
        harm, percuss = hpss(waveform)
        vocal = percuss.squeeze(0).numpy()
        accompaniment = harm.squeeze(0).numpy()
        return {"vocal": vocal, "accompaniment": accompaniment}
    # Fallback: simple even split
    half = len(audio) // 2
    return {"vocal": audio[:half], "accompaniment": audio[half:]}
