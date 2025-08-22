"""High level API endpoints for generation."""
from __future__ import annotations

from pathlib import Path
from typing import Optional
import wave

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
    # Local imports keep optional heavy dependencies from affecting
    # environments that only use melody generation.
    import numpy as np  # type: ignore
    from ..dataio.stems import separate_vocals  # type: ignore
    from ..models.conditional_audiolm_adapter import AccompGenerator  # type: ignore

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


def generate_melody_in_key(
    key: str,
    model_path: str = "web_model.pt",
    out_dir: Optional[str] = None,
) -> str:
    """Generate a placeholder melody file for the requested key.

    Parameters
    ----------
    key:
        Musical key in which the melody should be generated.
    model_path:
        Path to a pretrained model used for styling. The current
        implementation does not load the model but keeps the interface so
        that future work can hook into it.
    out_dir:
        Optional output directory. If not provided, ``DEFAULT_CFG``'s
        ``io.out_dir`` is used.
    """

    cfg = DEFAULT_CFG
    sr = cfg["io"]["sample_rate"]
    if out_dir is None:
        out_dir = Path(cfg["io"]["out_dir"])
    else:
        out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    # This dummy implementation writes silence to a WAV file. In a real
    # system ``model_path`` would be used to condition generation on style
    # and ``key``.
    duration = 5
    num_samples = sr * duration

    out_path = out_dir / f"melody_{key}.wav"
    silence = b"\x00\x00" * num_samples
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(silence)
    return str(out_path)
