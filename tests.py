from index import transpose


def test_transpose():
    test_pattern = [1, 3, 5]
    test_major_scale = {
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
        'Bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
    }

    res = transpose(test_pattern, test_major_scale)
    assert res == {'A': ['A', 'C#', 'E'], 'Bb': ['Bb', 'D', 'F']}
