from app.models.models_pattern import PatternInScale, PatternInKey, TransRowNotes
from app.transpose_output import transpose_output, _get_html_pattern, _create_file_name


def test_get_html_pattern_smoke():
    pattern_in_scale = PatternInScale(scale_type_name='test scale', pattern_name='test pattern', scales=[PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])]), PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])])])

    res = _get_html_pattern(pattern_in_scale)

    assert res is not None


def test_create_file_name():
    pattern_in_scale = PatternInScale(scale_type_name='test scale', pattern_name='test pattern', scales=[PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])]), PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])])])

    res = _create_file_name(pattern_in_scale)

    assert res == 'results/test_scale_test_pattern'


def test_transpose_output_smoke(fixture_pattern_in_scale):
    source = [fixture_pattern_in_scale, fixture_pattern_in_scale]

    res = transpose_output(source)

    assert res == 2
