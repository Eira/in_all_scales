from app.main import main


def test_main_happy_path():
    pattern_name = 'Whole tone up and down'

    res = main(pattern_name)

    assert res == 1


def test_main_wrong_pattern():
    pattern_name = 'random pattern'

    res = main(pattern_name)

    assert res == 0
    # todo надо как то нормально написать про вывод ошибки
