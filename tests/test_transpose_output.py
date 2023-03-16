from app.models.models_pattern import PatternInKey, PatternInScale, TransRowNotes
from app.transpose_output import _create_file_name, _get_html_pattern, transpose_output


def test_get_html_pattern_happy_path(fixture_test_pattern_in_pattern_source):
    pattern_in_scale = PatternInScale(scale_type_name='test scale', pattern_name='test pattern', scales=[PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])]), PatternInKey(key_name='C', pattern=[TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C']), TransRowNotes(quants=['Ab B C', 'Ab B C', 'Ab B C'])])])

    res = _get_html_pattern(pattern_in_scale)

    print(res)
    assert res.startswith('<!DOCTYPE html>')
    assert res.endswith('</html>')
    assert '<style>' in res
    assert '<p class="pattern">' in res
    assert '<span class="scale_quant">Ab B C</span>' in res
    assert '<section>' in res


def test_create_file_name():
    scale_type_name = 'test_scale'
    pattern_name = 'test_pattern'

    res = _create_file_name(scale_type_name, pattern_name)

    assert res.endswith('test_scale_test_pattern')


def test_transpose_output_smoke(fixture_pattern_in_scale):
    source = [fixture_pattern_in_scale, fixture_pattern_in_scale]

    res = transpose_output(source)

    assert res == 2
