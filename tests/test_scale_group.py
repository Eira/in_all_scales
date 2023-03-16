from app.models.models_scale import Key, ScaleFormula, ScaleGroup
from app.scale_group import _get_formuled_scale, _get_scale_formula, _get_scales_group, get_scale_group_from_name


def test_get_scale_formula():
    scale_name = 'Natural minor'

    res = _get_scale_formula(scale_name)

    assert isinstance(res, ScaleFormula)
    assert res.name == 'Natural minor'
    assert res.formula == [2, 1, 2, 2, 1, 2, 2]


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

    assert isinstance(res, ScaleGroup)
    assert res.name == 'Major'
    assert len(res.scales) == 12
    assert res.scales[0].name == 'C'
    assert res.scales[0].scale == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']


def test_get_scale_group_from_name_smoke():
    scale_name = 'Natural minor'
    res = get_scale_group_from_name(scale_name)

    assert res is not None
