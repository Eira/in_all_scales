from typing import List

from app.transpose import create_trans_quant, create_trans_row, create_trans_row_list, transpose
from app.models import RowNotes, PatternInScale, Key, ScaleGroup, PatternInKey, TransRowNotes


def test_create_trans_quant_smoke():
    quant = '234'
    key_scale = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'B', 'C']

    res = create_trans_quant(quant, key_scale)

    assert res is not None


def test_create_trans_row_smoke():
    row = ['123', '234', '345', '456', '567', '678']
    key_scale = ['Cb', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row(row, key_scale)

    assert res is not None


def test_create_trans_row_list_smoke():
    pattern_rows = [RowNotes(quants=['123', '234', '345', '456', '567', '678']), RowNotes(quants=['765', '654', '543', '432', '321'])]
    key_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

    res = create_trans_row_list(pattern_rows, key_scale)

    assert res is not None


def test_transpose_happy_path(fixture_test_pattern):
    res = transpose(fixture_test_pattern)

    assert isinstance(res, List)
    assert isinstance(res[0], PatternInScale)
    assert res[0].scale_type_name == 'Natural major'
    assert res[1].scale_type_name == 'Natural minor'
    assert res[0].pattern_name == 'Pattern Triplets'
    assert res[0].scales == [PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']), TransRowNotes(quants=['B A G', 'A G F', 'G F E', 'F E D', 'E D C'])]), PatternInKey(key_name='Db', pattern=[TransRowNotes(quants=['Db Eb F', 'Eb F Gb', 'F Gb Ab', 'Gb Ab Bb', 'Ab Bb C', 'Bb C Db']), TransRowNotes(quants=['C Bb Ab', 'Bb Ab Gb', 'Ab Gb F', 'Gb F Eb', 'F Eb Db'])]), PatternInKey(key_name='D', pattern=[TransRowNotes(quants=['D E Gb', 'E Gb G', 'Gb G A', 'G A B', 'A B Db', 'B Db D']), TransRowNotes(quants=['Db B A', 'B A G', 'A G Gb', 'G Gb E', 'Gb E D'])]), PatternInKey(key_name='Eb', pattern=[TransRowNotes(quants=['Eb F G', 'F G Ab', 'G Ab Bb', 'Ab Bb C', 'Bb C D', 'C D Eb']), TransRowNotes(quants=['D C Bb', 'C Bb Ab', 'Bb Ab G', 'Ab G F', 'G F Eb'])]), PatternInKey(key_name='E', pattern=[TransRowNotes(quants=['E Gb Ab', 'Gb Ab A', 'Ab A B', 'A B Db', 'B Db Eb', 'Db Eb E']), TransRowNotes(quants=['Eb Db B', 'Db B A', 'B A Ab', 'A Ab Gb', 'Ab Gb E'])]), PatternInKey(key_name='F', pattern=[TransRowNotes(quants=['F G A', 'G A Bb', 'A Bb C', 'Bb C D', 'C D E', 'D E F']), TransRowNotes(quants=['E D C', 'D C Bb', 'C Bb A', 'Bb A G', 'A G F'])]), PatternInKey(key_name='Gb', pattern=[TransRowNotes(quants=['Gb Ab Bb', 'Ab Bb B', 'Bb B Db', 'B Db Eb', 'Db Eb F', 'Eb F Gb']), TransRowNotes(quants=['F Eb Db', 'Eb Db B', 'Db B Bb', 'B Bb Ab', 'Bb Ab Gb'])]), PatternInKey(key_name='G', pattern=[TransRowNotes(quants=['G A B', 'A B C', 'B C D', 'C D E', 'D E Gb', 'E Gb G']), TransRowNotes(quants=['Gb E D', 'E D C', 'D C B', 'C B A', 'B A G'])]), PatternInKey(key_name='Ab', pattern=[TransRowNotes(quants=['Ab Bb C', 'Bb C Db', 'C Db Eb', 'Db Eb F', 'Eb F G', 'F G Ab']), TransRowNotes(quants=['G F Eb', 'F Eb Db', 'Eb Db C', 'Db C Bb', 'C Bb Ab'])]), PatternInKey(key_name='A', pattern=[TransRowNotes(quants=['A B Db', 'B Db D', 'Db D E', 'D E Gb', 'E Gb Ab', 'Gb Ab A']), TransRowNotes(quants=['Ab Gb E', 'Gb E D', 'E D Db', 'D Db B', 'Db B A'])]), PatternInKey(key_name='Bb', pattern=[TransRowNotes(quants=['Bb C D', 'C D Eb', 'D Eb F', 'Eb F G', 'F G A', 'G A Bb']), TransRowNotes(quants=['A G F', 'G F Eb', 'F Eb D', 'Eb D C', 'D C Bb'])]), PatternInKey(key_name='B', pattern=[TransRowNotes(quants=['B Db Eb', 'Db Eb E', 'Eb E Gb', 'E Gb Ab', 'Gb Ab Bb', 'Ab Bb B']), TransRowNotes(quants=['Bb Ab Gb', 'Ab Gb E', 'Gb E Eb', 'E Eb Db', 'Eb Db B'])])]


def test_transpose_user_scales_happy_path(fixture_test_pattern):
    scale_group_list = ['Natural minor', 'Natural major']

    res = transpose(fixture_test_pattern, scale_group_list)

    assert isinstance(res, List)
    assert isinstance(res[0], PatternInScale)
    assert res[0].scale_type_name == 'Natural minor'
    assert res[1].scale_type_name == 'Natural major'
    assert res[0].pattern_name == 'Pattern Triplets'
    assert res[1].scales == [PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['C D E', 'D E F', 'E F G', 'F G A', 'G A B', 'A B C']), TransRowNotes(quants=['B A G', 'A G F', 'G F E', 'F E D', 'E D C'])]), PatternInKey(key_name='Db', pattern=[TransRowNotes(quants=['Db Eb F', 'Eb F Gb', 'F Gb Ab', 'Gb Ab Bb', 'Ab Bb C', 'Bb C Db']), TransRowNotes(quants=['C Bb Ab', 'Bb Ab Gb', 'Ab Gb F', 'Gb F Eb', 'F Eb Db'])]), PatternInKey(key_name='D', pattern=[TransRowNotes(quants=['D E Gb', 'E Gb G', 'Gb G A', 'G A B', 'A B Db', 'B Db D']), TransRowNotes(quants=['Db B A', 'B A G', 'A G Gb', 'G Gb E', 'Gb E D'])]), PatternInKey(key_name='Eb', pattern=[TransRowNotes(quants=['Eb F G', 'F G Ab', 'G Ab Bb', 'Ab Bb C', 'Bb C D', 'C D Eb']), TransRowNotes(quants=['D C Bb', 'C Bb Ab', 'Bb Ab G', 'Ab G F', 'G F Eb'])]), PatternInKey(key_name='E', pattern=[TransRowNotes(quants=['E Gb Ab', 'Gb Ab A', 'Ab A B', 'A B Db', 'B Db Eb', 'Db Eb E']), TransRowNotes(quants=['Eb Db B', 'Db B A', 'B A Ab', 'A Ab Gb', 'Ab Gb E'])]), PatternInKey(key_name='F', pattern=[TransRowNotes(quants=['F G A', 'G A Bb', 'A Bb C', 'Bb C D', 'C D E', 'D E F']), TransRowNotes(quants=['E D C', 'D C Bb', 'C Bb A', 'Bb A G', 'A G F'])]), PatternInKey(key_name='Gb', pattern=[TransRowNotes(quants=['Gb Ab Bb', 'Ab Bb B', 'Bb B Db', 'B Db Eb', 'Db Eb F', 'Eb F Gb']), TransRowNotes(quants=['F Eb Db', 'Eb Db B', 'Db B Bb', 'B Bb Ab', 'Bb Ab Gb'])]), PatternInKey(key_name='G', pattern=[TransRowNotes(quants=['G A B', 'A B C', 'B C D', 'C D E', 'D E Gb', 'E Gb G']), TransRowNotes(quants=['Gb E D', 'E D C', 'D C B', 'C B A', 'B A G'])]), PatternInKey(key_name='Ab', pattern=[TransRowNotes(quants=['Ab Bb C', 'Bb C Db', 'C Db Eb', 'Db Eb F', 'Eb F G', 'F G Ab']), TransRowNotes(quants=['G F Eb', 'F Eb Db', 'Eb Db C', 'Db C Bb', 'C Bb Ab'])]), PatternInKey(key_name='A', pattern=[TransRowNotes(quants=['A B Db', 'B Db D', 'Db D E', 'D E Gb', 'E Gb Ab', 'Gb Ab A']), TransRowNotes(quants=['Ab Gb E', 'Gb E D', 'E D Db', 'D Db B', 'Db B A'])]), PatternInKey(key_name='Bb', pattern=[TransRowNotes(quants=['Bb C D', 'C D Eb', 'D Eb F', 'Eb F G', 'F G A', 'G A Bb']), TransRowNotes(quants=['A G F', 'G F Eb', 'F Eb D', 'Eb D C', 'D C Bb'])]), PatternInKey(key_name='B', pattern=[TransRowNotes(quants=['B Db Eb', 'Db Eb E', 'Eb E Gb', 'E Gb Ab', 'Gb Ab Bb', 'Ab Bb B']), TransRowNotes(quants=['Bb Ab Gb', 'Ab Gb E', 'Gb E Eb', 'E Eb Db', 'Eb Db B'])])]
