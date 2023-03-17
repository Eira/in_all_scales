from app.models.models_pattern import Pattern, RowNotes
from app.pattern import get_pattern


def test_get_pattern(fixture_test_pattern_in_pattern_source):
    pattern_name = 'test scale'

    res = get_pattern(pattern_name)

    assert isinstance(res, Pattern)
    assert res.name == 'test scale'
    assert res.scale_types == {'scale 1', 'scale 2'}
    assert res.pattern == [
        RowNotes(
            quants=['123', '24', '5'],
        ),
        RowNotes(
            quants=['5', '42', '321'],
        ),
    ]
