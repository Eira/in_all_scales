from index import transpose, get_scales_group, get_pattern, get_scale_formula
from models import ScaleGroup, Key, TransPattern, Pattern, ScaleFormula


def test_get_pattern():
    pattern_name = 'Pattern 1'

    res = get_pattern(pattern_name)

    assert res == Pattern(
        name='Pattern 1',
        pattern=[1, 2, 3],
    )


def test_get_scale_formula():
    scale_name = 'minor'

    res = get_scale_formula(scale_name)

    assert res == ScaleFormula(
        name='minor',
        formula=[2, 1, 2, 2, 1, 2, 2],
    )


def test_get_scales_group_happy_path():
    scale_formula = ScaleFormula(
        name='major',
        formula=[2, 2, 1, 2, 2, 2, 1],
    )
    res = get_scales_group(scale_formula)

    assert res == ScaleGroup(
        name='major',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
            ),
            Key(
                name='D',
                scale=['D', 'E', 'Gb', 'G', 'A', 'B', 'Db'],
            ),
            Key(
                name='Eb',
                scale=['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
            ),
            Key(
                name='E',
                scale=['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb'],
            ),
            Key(
                name='F',
                scale=['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
            ),
            Key(
                name='Gb',
                scale=['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F'],
            ),
            Key(
                name='G',
                scale=['G', 'A', 'B', 'C', 'D', 'E', 'Gb'],
            ),
            Key(
                name='Ab',
                scale=['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
            ),
            Key(
                name='A',
                scale=['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab'],
            ),
            Key(
                name='Bb',
                scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
            ),
            Key(
                name='B',
                scale=['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb'],
            ),
        ]
    )


def test_transpose_happy_path():
    pattern = Pattern(
        name='Pattern 1',
        pattern=[1, 3, 5],
    )
    scale_group = ScaleGroup(
        name='major test',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
            ),
        ]
    )

    res = transpose(pattern, scale_group)
    assert res == [
        TransPattern(
            key='C',
            notes=['C', 'E', 'G'],
        ),
        TransPattern(
            key='Db',
            notes=['Db', 'F', 'Ab']
        ),
    ]
