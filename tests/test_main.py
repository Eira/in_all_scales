import pytest

from app.main import main


def test_main_happy_path():
    pattern_name = 'Up and down'

    res = main(pattern_name)

    assert res == 9


def test_main_wrong_pattern():
    pattern_name = 'wrong pattern'

    with pytest.raises(RuntimeError, match='There no such a pattern or lick in program.'):
        main(pattern_name)
