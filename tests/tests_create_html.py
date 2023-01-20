from index import create_quant_html, create_row_html, create_key_html, create_transposed_pattern_html, transpose_output


def test_create_quant_html_smoke(fixture_trans_quant_notes):
    res = create_quant_html(fixture_trans_quant_notes)

    assert res


def test_create_row_html_smoke(fixture_trans_row_notes):
    res = create_row_html(fixture_trans_row_notes)

    assert res


def test_create_key_html_smoke(fixture_pattern_in_key):
    res = create_key_html(fixture_pattern_in_key)

    assert res


def test_create_transposed_pattern_html_smoke(fixture_pattern_in_scale):
    res = create_transposed_pattern_html(fixture_pattern_in_scale)

    assert res


def test_transpose_output_smoke(fixture_pattern_in_scale):
    source = [fixture_pattern_in_scale, fixture_pattern_in_scale]

    res = transpose_output(source)

    assert res == 2
