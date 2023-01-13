from index import transpose, get_scales_group, get_pattern, create_scale_group
from models import ScaleGroup, Key, TransPattern, Pattern

def test_create_scale_group():
    major_formula = [2, 2, 1, 2, 2, 2, 1]
    res = create_scale_group('E', major_formula)

    assert res == []


def test_get_scales_group_happy_path():
    res = get_scales_group('scales/test.txt')

    assert res == ScaleGroup(
        name='Test scales',
        scales=[
            Key(
                name='Am',
                scale=['A', 'B', 'C'],
            ),
            Key(
                name='Bbm',
                scale=['Bb', 'C', 'Db'],
            ),
        ]
    )


def test_get_pattern_happy_path():
    res = get_pattern('patterns/test.txt')
    assert res == Pattern(
        name='Test pattern',
        pattern=[1, 2, 3]
    )


def test_transpose_happy_path():
    test_pattern = Pattern(
        name='Test pattern',
        pattern=[1, 3, 5]
    )
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
            name='Test pattern',
            key='A',
            pattern=['A', 'C#', 'E'],
        ),
        TransPattern(
            name='Test pattern',
            key='Bb',
            pattern=['Bb', 'D', 'F']
        ),
    ]
