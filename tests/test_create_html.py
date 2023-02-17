from app.create_html import create_quant_html, create_row_html, create_key_html, create_transposed_pattern_html


def test_create_quant_html_happy_path(fixture_trans_quant_notes):
    res = create_quant_html(fixture_trans_quant_notes)

    assert res == '\n        <span class="scale_quant">Ab B C</span>\n    '


def test_create_row_html_happy_path(fixture_trans_row_notes):
    res = create_row_html(fixture_trans_row_notes)

    assert res == ('<p class="pattern">\n'
 '        \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '    </p>\n'
 '    ') != ('<p class="pattern">\n'
 '        \n'
 '        <span class="scale_quant">[\'Ab\', \'B\', \'C\']</span>\n'
 '    \n'
 '        <span class="scale_quant">[\'Ab\', \'B\', \'C\']</span>\n'
 '    \n'
 '        <span class="scale_quant">[\'Ab\', \'B\', \'C\']</span>\n'
 '    \n'
 '    </p>\n'
 '    ')


def test_create_key_html_smoke(fixture_pattern_in_key):
    res = create_key_html(fixture_pattern_in_key)

    assert res == ('<section>\n'
 '        <h3>C</h3>\n'
 '        <p class="pattern">\n'
 '        \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '    </p>\n'
 '    <p class="pattern">\n'
 '        \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '        <span class="scale_quant">Ab B C</span>\n'
 '    \n'
 '    </p>\n'
 '    \n'
 '    </section>\n'
 '    ')


def test_create_transposed_pattern_html_smoke(fixture_pattern_in_scale):
    res = create_transposed_pattern_html(fixture_pattern_in_scale)

    assert res
    assert isinstance(res, str)



