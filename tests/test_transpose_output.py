from app.transpose_output import transpose_output


def test_transpose_output_smoke(fixture_pattern_in_scale):
    source = [fixture_pattern_in_scale, fixture_pattern_in_scale]

    res = transpose_output(source)

    assert res == 2
