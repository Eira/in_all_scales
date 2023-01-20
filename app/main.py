import logging

from app.pattern import get_pattern
from app.transpose import transpose
from app.transpose_output import transpose_output


def main(pattern_name: str) -> None:
    """
    Do the main runner of "Into all scales" project.

    Transpose selected by user pattern to all scales, that program know.
    Return group of HTML files, according to amount of scales.
    """
    # todo test
    #получить данные для паттерна
    # подготовить данные для паттерна и формулы?
    pattern = get_pattern(pattern_name)
    #scale_formula = get_scale_formula(scale_name)

    # сгенерировать лад
    #scale_group = get_scales_group(scale_formula)

    # создать списки паттернов по ладам
    transposed_pattern_list = transpose(pattern)
    # генерируем файлы
    transpose_output(transposed_pattern_list)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', 'test_scale_name')
