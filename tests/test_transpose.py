from app.models.models_pattern import PatternInKey, PatternInScale, RowNotes, TransRowNotes
from app.models.models_scale import Key, ScaleGroup
from app.transpose import _create_trans_key_list, _create_trans_quant, _create_trans_row, _create_trans_row_list, transpose


def test_create_trans_quant_happy_path():
    quant = '234'
    key_scale = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'B', 'C']

    res = _create_trans_quant(quant, key_scale)

    assert res == 'Db Eb Fb'


def test_create_trans_row_happy_path():
    row = ['123', '234', '345', '456', '567', '678']
    key_scale = ['Cb', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = _create_trans_row(row, key_scale)

    assert isinstance(res, TransRowNotes)
    assert res.quants == ['Cb D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']


def test_create_trans_row_list_happy_path():
    pattern_rows = [RowNotes(quants=['123', '234', '345', '456', '567', '678']), RowNotes(quants=['765', '654', '543', '432', '321'])]
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = _create_trans_row_list(pattern_rows, key_scale)

    assert isinstance(res, list)
    assert isinstance(res[0], TransRowNotes)
    assert len(res) == 2
    assert res[0].quants == ['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']


def test_create_trans_key_list_happy_path(fixture_test_pattern):
    scale_group = ScaleGroup(
        name='Major',
        scales=[Key(name='C', scale=['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']), Key(name='Db', scale=['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db']), Key(name='D', scale=['D', 'E', 'Gb', 'G', 'A', 'B', 'Db', 'D']), Key(name='Eb', scale=['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb']), Key(name='E', scale=['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb', 'E']), Key(name='F', scale=['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F']), Key(name='Gb', scale=['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F', 'Gb']), Key(name='G', scale=['G', 'A', 'B', 'C', 'D', 'E', 'Gb', 'G']), Key(name='Ab', scale=['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab']), Key(name='A', scale=['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab', 'A']), Key(name='Bb', scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb']), Key(name='B', scale=['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb', 'B'])]
    )
    res = _create_trans_key_list(scale_group, fixture_test_pattern)

    assert isinstance(res, list)
    assert isinstance(res[0], PatternInKey)
    assert len(res) == 12
    assert res[0].key_name == 'C'
    assert res[0].pattern[0].quants == ['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']


def test_transpose_happy_path(fixture_test_pattern):
    res = transpose(fixture_test_pattern)

    assert isinstance(res, list)
    assert isinstance(res[0], PatternInScale)
    assert len(res) == 2
    assert res[0].scale_type_name in {'Major', 'Natural minor'}
    assert res[0].pattern_name == 'Triplets'
    assert isinstance(res[0].scales, list)
    assert isinstance(res[0].scales[0], PatternInKey)


def test_transpose_user_scales_happy_path(fixture_test_pattern):
    scale_group_list = ['Natural minor', 'Major']

    res = transpose(fixture_test_pattern, scale_group_list)

    assert isinstance(res, list)
    assert isinstance(res[0], PatternInScale)
    assert res[0].scale_type_name == 'Natural minor'
    assert res[1].scale_type_name == 'Major'
    assert res[0].pattern_name == 'Triplets'
    assert isinstance(res[1].scales[0], PatternInKey)
