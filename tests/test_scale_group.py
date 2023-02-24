from app.models import Key, ScaleFormula, ScaleGroup
from app.scale_group import (_get_scale_formula, get_scale_group_from_name,
                             _get_scales_group, _get_formuled_scale)


def test_get_scale_formula():
    scale_name = 'Natural minor'

    res = _get_scale_formula(scale_name)

    assert res == ScaleFormula(
        name='Natural minor',
        formula=[2, 1, 2, 2, 1, 2, 2],
    )


def test_get_formuled_scale():
    key = Key(
        name='C',
        scale=['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C'],
    )
    scale_formula = ScaleFormula(
        name='Major',
        formula=[2, 2, 1, 2, 2, 2, 1],
    )

    res = _get_formuled_scale(key, scale_formula)

    assert res == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']


def test_get_scales_group_happy_path():
    scale_formula = ScaleFormula(
        name='Major',
        formula=[2, 2, 1, 2, 2, 2, 1],
    )
    res = _get_scales_group(scale_formula)

    assert res == ScaleGroup(
        name='Major',
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


def test_get_scale_group_from_name_smoke():
    scale_name = 'Natural minor'
    res = get_scale_group_from_name(scale_name)

    assert res is not None
