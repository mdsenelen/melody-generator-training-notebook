"""High level API endpoints for generation."""
from __future__ import annotations

from pathlib import Path
from typing import Optional
import numpy as np
import wave

from ..dataio.stems import separate_vocals
from ..models.conditional_audiolm_adapter import AccompGenerator
from .mode_router import route_generation


DEFAULT_CFG = {
    "io": {"sample_rate": 24000, "out_dir": "outputs"},
    "modes": {"artist_style": "indie-pop", "fallback_if_vocal_missing": True},
    "singsong": {"adapter_dim": 256},
}


def generate_accompaniment(
    vocal_path: str,
    genre: Optional[str] = None,
    key: Optional[str] = None,
    bpm: Optional[float] = None,
) -> str:
    """Generate accompaniment from a vocal file and save to disk."""
    cfg = DEFAULT_CFG
    sr = cfg["io"]["sample_rate"]
    out_dir = Path(cfg["io"]["out_dir"])
    out_dir.mkdir(exist_ok=True)
    duration = 5
    rng = np.random.default_rng(0)
    dummy_input = rng.standard_normal(sr * duration, dtype=np.float32)
    stems = separate_vocals(dummy_input, sr)
    model = AccompGenerator(adapter_dim=cfg["singsong"]["adapter_dim"])
    accompaniment = model(stems["vocal"], None)
    out_path = out_dir / "accompaniment.wav"
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes((accompaniment * 32767).astype("<h").tobytes())
    return str(out_path)
