import logging
from typing import List

from models import ScaleGroup, Key, TransPattern, Pattern, ScaleFormula

test_major_scale = ScaleGroup(
    name='test',
    scales=[
        Key(
            name='A',
            scale=['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
        ),
        Key(
            name='Bb',
            scale=['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
        ),
    ]
)


def get_pattern(pattern_name: str) -> Pattern:
    """Take from the user pattern name. Return object with name and pattern sequence."""
    source = {
        'Pattern 1': [1, 2, 3],
        'Pattern 2': [1, 2, 3, 2, 3, 4],
    }.get(pattern_name)

    pattern = Pattern(
        name=pattern_name,
        pattern=source,
    )
    return pattern


def get_scale_formula(scale_name: str) -> ScaleFormula:
    """Take from the user scale name. Return object with name and scale formula sequence."""
    source = {
        'major': [2, 2, 1, 2, 2, 2, 1],
        'minor': [2, 1, 2, 2, 1, 2, 2],
    }.get(scale_name)

    scale_formula = ScaleFormula(
        name=scale_name,
        formula=source,
    )
    return scale_formula


def get_scales_group(scale_formula: ScaleFormula) -> ScaleGroup:
    """Take scale formula. Returns group of scales."""
    base_scales = [
        Key(
            name='C',
            scale=['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
        ),
        Key(
            name='Db',
            scale=['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C'],
        ),
        Key(
            name='D',
            scale=['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
        ),
        Key(
            name='Eb',
            scale=['Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D'],
        ),
        Key(
            name='E',
            scale=['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb'],
        ),
        Key(
            name='F',
            scale=['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
        ),
        Key(
            name='Gb',
            scale=['Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F'],
        ),
        Key(
            name='G',
            scale=['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
        ),
        Key(
            name='Ab',
            scale=['Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G'],
        ),
        Key(
            name='A',
            scale=['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
        ),
        Key(
            name='Bb',
            scale=['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A'],
        ),
        Key(
            name='B',
            scale=['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb'],
        ),
    ]

    scales_list = []
    for key in base_scales:
        step = 0
        formuled_scale = []
        for num in scale_formula.formula:
            formuled_scale.append(key.scale[step])
            step += num

        formuled_key = Key(
            name=key.name,
            scale=formuled_scale,
        )
        scales_list.append(formuled_key)

    scale_group = ScaleGroup(
        name=scale_formula.name,
        scales=scales_list,
    )

    return scale_group


def transpose(pattern: Pattern, scale_group: ScaleGroup) -> List[TransPattern]:
    """
     Transpose pattern to one scale.
     Return the dict with patterns for all keys of the scale.
     """
    # todo test

    transposed_pattern = []

    for elem in scale_group.scales:  # todo как тут быть с именованием
        temp_pattern = []
        for note in pattern.pattern:
            temp_pattern.append(elem.scale[note - 1])

        key_pattern = TransPattern(
            key=elem.name,
            pattern=temp_pattern,  # todo как тут аппендить?
        )

        transposed_pattern.append(key_pattern)

    return transposed_pattern


def transpose_output(transposed_pattern):
    """Return HTML with transposed pattern."""
    # todo test
    # подготовить к выводу блоки с патерном
    ...


def main(pattern_name: str, scale_name: str) -> None:
    """
    Do the main runner of "To all scales" project.

    Transpose selected by user pattern to selected scale.
    Return HTML with the result.
    """
    # todo test
    # ? Получить от пользователя паттерн и тональность
    pattern = get_pattern(pattern_name)
    scale_formula = get_scale_formula(scale_name)

    # Сгенерировать группу тональностей по заданной формуле
    scale_group = get_scales_group(scale_formula)

    # Транспонировать паттерн в выбранную группу тональностей
    transposed_pattern = transpose(pattern, scale_group)

    # Вывести в HTML паттерн в 12 тональностях
    transpose_output(transposed_pattern)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', 'test_scale_name')
