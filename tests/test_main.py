from app.main import main


def test_main_happy_path():
    pattern_name = 'Pattern Up and down'

    res = main(pattern_name)

    assert res == 9
