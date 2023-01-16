from index import transpose, get_scales_group, get_pattern, get_scale_formula, transpose_output, main
from models import ScaleGroup, Key, Pattern, ScaleFormula, PatternInScale, TransRowNotes, PatternInKey, QuantNotes, TransQuantNotes


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
        formula=[2, 1, 2, 2, 1, 2, 2, 1],
    )


def test_get_scales_group_happy_path():
    scale_formula = ScaleFormula(
        name='major',
        formula=[2, 2, 1, 2, 2, 2, 1, 1],
    )
    res = get_scales_group(scale_formula)

    assert res == ScaleGroup(
        name='major',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'],
            ),
            Key(
                name='D',
                scale=['D', 'E', 'Gb', 'G', 'A', 'B', 'Db', 'D'],
            ),
            Key(
                name='Eb',
                scale=['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
            ),
            Key(
                name='E',
                scale=['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb', 'E'],
            ),
            Key(
                name='F',
                scale=['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'],
            ),
            Key(
                name='Gb',
                scale=['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F', 'Gb'],
            ),
            Key(
                name='G',
                scale=['G', 'A', 'B', 'C', 'D', 'E', 'Gb', 'G'],
            ),
            Key(
                name='Ab',
                scale=['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],
            ),
            Key(
                name='A',
                scale=['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab', 'A'],
            ),
            Key(
                name='Bb',
                scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
            ),
            Key(
                name='B',
                scale=['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'B'],
            ),
        ]
    )


def test_transpose_happy_path():
    pattern = Pattern(
        name='Pattern 1',
        pattern=[1, 2, 3, 4, 5, 6, 7, 8],
    )
    scale_group = ScaleGroup(
        name='major test',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'],
            ),
        ]
    )

    res = transpose(pattern, scale_group)
    assert res == PatternInScale(
        scale_type_name='major test',
        pattern_name='Pattern 1',
        scales=[
            Key(
                name='C',
                scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            ),
            Key(
                name='Db',
                scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db']
            ),
        ]
    )


def test_transpose_output_smoke(fixture_pattern_in_scale):
    source = [fixture_pattern_in_scale, fixture_pattern_in_scale]

    res = transpose_output(source)

    assert res == 2


def test_main_smoke():
    pattern_name = 'scale'
    scale_name = 'minor'
    main(pattern_name, scale_name)
