test_pattern = [1,3,5]
test_major_scale = {
    'A': ['A','B','C#','D','E','F#','G#','A'],
    'Bb': ['Bb','C','D','Eb','F','G','A','Bb'],
}
# todo считывание матрицы из файла
# todo считывание паттерна из файла

def transpose(pattern, scale):
    """ Transpose pattern to one scale. Return the dict with patterns for all keys of the scale."""
    # todo test

    transposed_pattern = {}

    for key in scale:
        key_pattern = []
        for note in pattern:
            key_pattern.append(scale[key][note-1])

        transposed_pattern[key] = key_pattern

    return transposed_pattern


def transpose_output(transposed_pattern):
    """Return HTML with transposed pattern."""
    # todo test
    # подготовить к выводу блоки с патерном
    ...
