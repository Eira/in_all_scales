"""This is module with main runner of Into all scales."""

import logging
from typing import Optional, Set

from app.pattern import get_pattern
from app.transpose import transpose
from app.transpose_output import transpose_output


def main(pattern_name: str, user_scale_group: Optional[Set[str]] = None) -> int:
    """
    Do the main runner of "Into all scales" project.

    Transpose selected by user pattern to all scales, that program know.
    Return group of PDF files, according to amount of scales.
    """
    # получить данные для паттерна
    # получить данные для scale group

    # подготовить данные для паттерна
    pattern = get_pattern(pattern_name)
    #  todo написать сюда трай кеч
    #  todo test

    # создать списки паттернов
    transposed_pattern_list = transpose(pattern, user_scale_group)
    # генерируем файлы

    return transpose_output(transposed_pattern_list)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', {'test_scale_name'})
