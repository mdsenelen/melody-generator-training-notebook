from types import SimpleNamespace
from src.utils.mode_router import route_generation


def test_route_generation():
    cfg = SimpleNamespace(modes=SimpleNamespace(fallback_if_vocal_missing=True, artist_style='rock'))
    mode, kwargs = route_generation(False, cfg=cfg)
    assert mode == 'full_song'
    assert kwargs['style'] == 'rock'
    mode2, _ = route_generation(True, cfg=cfg)
    assert mode2 == 'accompaniment'
