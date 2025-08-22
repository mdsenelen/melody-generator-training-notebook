from src.dataio.expert_split import tag_expert_background


def test_tag_expert_background():
    meta = [{'quality': 'high'}, {'quality': 'low'}]
    res = tag_expert_background(meta)
    assert res['expert_indices'] == [0]
    assert res['background_indices'] == [1]
