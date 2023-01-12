import logging
from typing import List

from models import ScaleGroup, Key, TransPattern, Pattern

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
def get_scales_group(file_path: str) -> ScaleGroup:
    """Get scales group from the file. Returns it like the model."""

    file = open(file_path)
    source = file.readlines()
    name = source[0].strip()
    source_scales = source[1:]
    file.close()

    scales = []
    for line in source_scales:
        key = Key(
            name=line.partition(':')[0],
            scale=line.strip().partition(':')[2].split(),

        )
        scales.append(key)
    scale_group = ScaleGroup(
        name=name,
        scales=scales
    )

    return scale_group


def get_pattern(file_path: str) -> Pattern:
    """Get pattern from the file. Returns it like the list."""
    file = open(file_path)
    source = file.readlines()
    file.close()

    for note in source[1:]:
        pattern_source = list(map(int, note.split()))

    pattern = Pattern(
        name=source[0].strip(),
        pattern=pattern_source
    )

    return pattern


def transpose(pattern: Pattern, scale_group: ScaleGroup) -> List[TransPattern]:
    """ Transpose pattern to one scale. Return the dict with patterns for all keys of the scale."""
    # todo test

    transposed_pattern = []

    for elem in scale_group.scales:  # todo как тут быть с именованием
        temp_pattern = []
        for note in pattern.pattern:
            temp_pattern.append(elem.scale[note - 1])

        key_pattern = TransPattern(
            name=pattern.name,
            key=elem.name,
            pattern=temp_pattern,  # todo как тут аппендить?
        )

        transposed_pattern.append(key_pattern)

    return transposed_pattern
    #return scale.name todo еще вернуть название группы и название паттерна


def transpose_output(transposed_pattern):
    """Return HTML with transposed pattern."""
    # todo test
    # подготовить к выводу блоки с патерном
    ...


def main(pattern_file_path: str, scales_file_path: str) -> None:
    """
    Do the main runner of "To all scales" project.

    Transpose selected by user pattern to selected scale.
    Return HTML with the result.
    """
    scale_group = get_scales_group(scales_file_path)
    transpose(pattern_file_path, scale_group)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if app_settings.debug else logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main()
