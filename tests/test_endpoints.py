import os
import wave
import struct
from src.utils.endpoints import generate_accompaniment


def _make_wav(path: str) -> None:
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(8000)
        w.writeframes(struct.pack('<' + 'h'*8000, *([0]*8000)))


def test_generate_accompaniment(tmp_path):
    vocal = tmp_path / 'vocal.wav'
    _make_wav(str(vocal))
    out = generate_accompaniment(str(vocal))
    assert os.path.exists(out)
