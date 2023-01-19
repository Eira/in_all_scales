from index import create_trans_row_list, create_trans_row, create_trans_quant
from models import RowNotes


def test_create_trans_quant_smoke():
    quant = '234'
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_quant(quant, key_scale)

    assert res is not None



def test_create_trans_row():
    row = ['123', '234', '345', '456', '567', '678']
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row(row, key_scale)

    assert res is not None


def test_create_trans_row_list_smoke():
    pattern_rows = [RowNotes(quants=['123', '234', '345', '456', '567', '678']), RowNotes(quants=['765', '654', '543', '432', '321'])]
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row_list(pattern_rows, key_scale)

    assert res is not None
