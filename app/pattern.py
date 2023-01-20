from app.models import Pattern, RowNotes

_pattern_source = {
    'test scale': Pattern(
        name='test scale',
        scale_types=['scale 1', 'scale 2'],
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ],
    ),
    'Pattern Up and down': Pattern(
        name='Pattern Up and down',
        scale_types=['major', 'minor'],
        pattern=[
            RowNotes(
                quants=['123', '456', '787', '654', '321'],
            ),
        ],
    ),
    'Pattern Triplets': Pattern(
        name='Pattern Triplets',
        scale_types=['major', 'minor'],
        pattern=[
            RowNotes(
                quants=['123', '234', '345', '456', '567', '678'],
            ),
            RowNotes(
                quants=['765', '654', '543', '432', '321'],
            ),
        ],
    ),
    'Pattern In thirds': Pattern(
        name='Pattern In thirds',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['13', '24', '35', '46', '57', '68', '72'],
            ),
            RowNotes(
                quants=['86', '75', '64', '53', '42', '31', '27', '1'],
            ),
        ],
    ),
    'Pattern Skip a step': Pattern(
        name='Pattern Skip a step',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1342', '3564', '5786', '7238'],
            ),
            RowNotes(
                quants=['8657', '6435', '4213', '2761'],
            ),
        ],
    ),
    'Pattern Minor Pentatonic Skip a step': Pattern(
        name='Pattern Minor Pentatonic Skip a step',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1453', '4785', '3574', '7348'],
            ),
            RowNotes(
                quants=['8547', '5314', '3751'],
            ),
        ],
    ),
    'Pattern Slow Minor Pentatonic Build up': Pattern(
        name='Pattern Slow Minor Pentatonic Build up',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1713', '4314', '3134', '5435'],
            ),
            RowNotes(
                quants=['4345', '7547', '5457', '8758'],
            ),
        ],
    ),
    'pentatonic scale': [1, 3, 4, 5, 7, 8, 7, 5, 4, 3, 1],
    'blues scale': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
}


# todo вероятно пригодится
def create_pattern(pattern_name: str, scale_types: str, pattern: str) -> Pattern:
    """Create pattern object from users data."""
    scale_types_list = scale_types.strip().split(',')
    source_row_list = pattern.strip().split(' ')
    row_list = []
    for source_row in source_row_list:
        row = RowNotes(
            quants=source_row.split(',')
        )
        row_list.append(row)

    return Pattern(
        name=pattern_name,
        scale_types=scale_types_list,
        pattern=row_list,
    )


def get_pattern(pattern_name: str) -> Pattern:
    """Take from the user pattern name. Return object with name and pattern sequence."""
    pattern = _pattern_source.get(pattern_name)

    return pattern
