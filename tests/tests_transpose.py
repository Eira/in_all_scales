from index import create_trans_row_list, create_trans_row, create_trans_quant, transpose
from models import RowNotes, PatternInScale, Key, ScaleGroup


def test_create_trans_quant_smoke():
    quant = '234'
    key_scale = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'B', 'C']

    res = create_trans_quant(quant, key_scale)

    assert res is not None


def test_create_trans_row():
    row = ['123', '234', '345', '456', '567', '678']
    key_scale = ['Cb', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row(row, key_scale)

    assert res is not None


def test_create_trans_row_list_smoke():
    pattern_rows = [RowNotes(quants=['123', '234', '345', '456', '567', '678']), RowNotes(quants=['765', '654', '543', '432', '321'])]
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row_list(pattern_rows, key_scale)

    assert res is not None


# todo переписать
def test_transpose_happy_path(fixture_test_pattern):
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

    res = transpose(fixture_test_pattern)
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
