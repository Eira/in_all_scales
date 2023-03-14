from app.models.models_pattern import Pattern, RowNotes
from app.pattern import get_pattern


def test_get_pattern(fixture_text_pattern_in_pattern_source):
    pattern_name = 'test scale'

    res = get_pattern(pattern_name)

    assert res == Pattern(
        name='test scale',
        scale_types={'scale 1', 'scale 2'},
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ]
    )
