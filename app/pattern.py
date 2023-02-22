"""
This module contain descriptions of all patterns and licks.

And also functions for creating and getting patterns.
"""

from app.models import Lick, Pattern, PatternType, RowNotes

_pattern_source: dict[str, PatternType] = {
    'test scale': Pattern(
        name='test scale',
        scale_types={'scale 1', 'scale 2'},
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ],
    ),
    'Up and down': Pattern(
        name='Up and down',
        scale_types={
            'Major',

            'Natural minor',
            'Jazz melodic minor',
            'Harmonic minor',

            'Dorian',
            'Phrygian Dominant',

            'Whole-Tone',

            'Half-Whole',
            'Whole-Half',
        },
        pattern=[
            RowNotes(
                quants=['123', '456', '717', '654', '321'],
            ),
        ],
    ),
    'Minor Pentatonic Up and down': Pattern(
        name='Minor Pentatonic Up and down',
        scale_types={
            'Natural minor',
        },
        pattern=[
            RowNotes(
                quants=['134578'],
            ),
            RowNotes(
                quants=['875431'],
            ),
        ],
    ),
    'Major Pentatonic Up and Down': Pattern(
        name='Major Pentatonic Up and Down',
        scale_types={
            'Major',
        },
        pattern=[
            RowNotes(
                quants=['123568'],
            ),
            RowNotes(
                quants=['865321'],
            ),
        ],
    ),
    'Triplets': Pattern(
        name='Triplets',
        scale_types={
            'Major',

            'Natural minor',
            'Jazz melodic minor',
            'Harmonic minor',

            'Dorian',
            'Phrygian Dominant',
        },
        pattern=[
            RowNotes(
                quants=['123', '234', '345', '456', '567', '678'],
            ),
            RowNotes(
                quants=['765', '654', '543', '432', '321'],
            ),
        ],
    ),
    'Run': Pattern(
        name='Run',
        scale_types={
            'Major',

            'Natural minor',
            'Jazz melodic minor',
            'Harmonic minor',

            'Dorian',
            'Phrygian Dominant',
        },
        pattern=[
            RowNotes(
                quants=['1232', '3454', '5676', '7121'],
            ),
            RowNotes(
                quants=['1767', '6545', '4323', '2171'],
            ),
        ],
    ),
    'In thirds': Pattern(
        name='In thirds',
        scale_types={
            'Major',

            'Natural minor',
            'Jazz melodic minor',
            'Harmonic minor',

            'Dorian',
            'Phrygian Dominant',

            'Half-Whole',
            'Whole-Half',
        },
        pattern=[
            RowNotes(
                quants=['13', '24', '35', '46', '57', '68', '72'],
            ),
            RowNotes(
                quants=['86', '75', '64', '53', '42', '31', '27', '1'],
            ),
        ],
    ),
    'Skip a step': Pattern(
        name='Skip a step',
        scale_types={
            'Major',

            'Natural minor',
            'Jazz melodic minor',
            'Harmonic minor',

            'Dorian',
            'Phrygian Dominant',
        },
        pattern=[
            RowNotes(
                quants=['1342', '3564', '5786', '7238'],
            ),
            RowNotes(
                quants=['8657', '6435', '4213', '2761'],
            ),
        ],
    ),
    'Minor Pentatonic Skip a step': Pattern(
        name='Minor Pentatonic Skip a step',
        scale_types={'Pentatonic minor'},
        pattern=[
            RowNotes(
                quants=['1453', '4785', '3574', '7348'],
            ),
            RowNotes(
                quants=['8547', '5314', '3751'],
            ),
        ],
    ),
    'Slow Minor Pentatonic Build up': Pattern(
        name='Slow Minor Pentatonic Build up',
        scale_types={'Pentatonic minor'},
        pattern=[
            RowNotes(
                quants=['1713', '4314', '3134', '5435'],
            ),
            RowNotes(
                quants=['4345', '7547', '5457', '8758'],
            ),
        ],
    ),
    'Whole tone up and down': Pattern(
        name='Whole tone up and down',
        scale_types={'Whole-Tone'},
        pattern=[
            RowNotes(
                quants=['1234567654321'],
            ),
        ],
    ),
    'Chromatic Run': Pattern(
        name='Chromatic Run',
        scale_types={
            'Chromatic',
        },
        pattern=[
            RowNotes(
                quants=['1232', '3454', '5676', '7898', '9,10,11,10', '11,12,13,12'],
            ),
        ],
    ),
    'The Lick': Lick(
        name='The Lick',
        scale_types={
            'Dorian',
        },
        pattern=[
            RowNotes(
                quants=['56786', '45'],
            ),
        ],
    ),
    'Harmonic Minor lick': Lick(
        name='The Lick',
        scale_types={
            'Harmonic minor',
        },
        pattern=[
            RowNotes(
                quants=['71', '23', '45', '24', '37', '21', '54', '3', '1'],
            ),
        ],
    ),
    #  'blues scale': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
}


# todo вероятно пригодится переписать еще для lick
def create_pattern(pattern_name: str, scale_types: str, pattern: str) -> Pattern:
    """Create pattern object from users data."""
    scale_types_list = set(scale_types.strip().split(','))
    source_row_list = pattern.strip().split(' ')
    row_list = []
    for source_row in source_row_list:
        row = RowNotes(
            quants=source_row.split(','),
        )
        row_list.append(row)

    return Pattern(
        name=pattern_name,
        scale_types=scale_types_list,
        pattern=row_list,
    )


def get_pattern(pattern_name: str) -> PatternType:
    """Take from the user pattern name. Return object with name and pattern sequence."""
    pattern = _pattern_source.get(pattern_name)
    if not pattern:
        raise RuntimeError

    return pattern
