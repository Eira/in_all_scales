from index import transpose, get_scales_group
from models import ScaleGroup, Key, TransPattern


def test_get_scales_group_happy_path():
    res = get_scales_group('scales/test.txt')

    assert res == ScaleGroup(
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


def test_transpose_happy_path():
    test_pattern = [1, 3, 5]
    test_major_scale = ScaleGroup(
        name='Test scales',
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

    res = transpose(test_pattern, test_major_scale)
    assert res == [
        TransPattern(
            key='A',
            pattern=['A', 'C#', 'E'],
        ),
        TransPattern(
            key='Bb',
            pattern=['Bb', 'D', 'F']
        ),
    ]
