from typing import List

from models import ScaleGroup, Key, TransPattern

test_pattern = [1, 3, 5]
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

# todo считывание матрицы из файла
# todo считывание паттерна из файла


def transpose(pattern: List, scale_group: ScaleGroup) -> List[TransPattern]:
    """ Transpose pattern to one scale. Return the dict with patterns for all keys of the scale."""
    # todo test

    transposed_pattern = []

    for elem in scale_group.scales:  # todo как тут быть с именованием
        temp_pattern = []
        for note in pattern:
            temp_pattern.append(elem.scale[note - 1])

        key_pattern = TransPattern(
            key=elem.name,
            pattern=temp_pattern,  # todo как тут аппендить?
        )

        transposed_pattern.append(key_pattern)

    return transposed_pattern
    #return scale.name todo еще вернуть название группы


def transpose_output(transposed_pattern):
    """Return HTML with transposed pattern."""
    # todo test
    # подготовить к выводу блоки с патерном
    ...
