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
    if not pattern:
        logging.warning('There no such a pattern or lick in program.')
        # Todo предложить создать
        # todo test
        return 0
    if user_scale_group not in pattern.scale_types:
        # todo тут какая то ерудна
        logging.warning('This scale is not applicable for this pattern or lick.')
        # Todo предложить выбрать из возможных
        # todo test

    # создать списки паттернов
    transposed_pattern_list = transpose(pattern, user_scale_group)
    # генерируем файлы
    cnt = transpose_output(transposed_pattern_list)

    return cnt


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', {'test_scale_name'})
