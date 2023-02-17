from app.models import Pattern, RowNotes
from app.pattern import create_pattern, get_pattern


def test_create_pattern_happy_path():
    pattern_name = 'test pattern'
    scale_types = 'scale 1,scale 2'  # todo решить проблему с пробелами
    pattern = '123,24,5 5,42,321'

    res = create_pattern(pattern_name, scale_types, pattern)

    assert res == Pattern(
        name='test pattern',
        scale_types={'scale 1', 'scale 2'},
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ],
    )


def test_get_pattern():
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
