from app.main import main


def test_main_happy_path():
    pattern_name = 'Whole step up and down'

    res = main(pattern_name)

    assert res == 1
