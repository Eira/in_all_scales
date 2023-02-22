"""
This module contain descriptions of all scales.

As well as functions for scale processing.
"""

from app.models import Key, ScaleFormula, ScaleGroup


def _get_scale_formula(scale_name: str) -> ScaleFormula:
    """Take from the user scale name. Return object with name and scale formula sequence."""
    source = {
        'Major': [2, 2, 1, 2, 2, 2, 1],
        'Natural minor': [2, 1, 2, 2, 1, 2, 2],
        'Jazz melodic minor': [2, 1, 2, 2, 2, 2, 1],
        'Harmonic minor': [2, 1, 2, 2, 1, 3, 1],
        'Dorian': [2, 1, 2, 2, 2, 1, 2],
        'Phrygian Dominant': [1, 3, 1, 2, 1, 2, 2],
        'Blues major': [2, 1, 1, 3, 2, 3],
        'Blues minor': [3, 2, 1, 1, 3, 2],
        'Pentatonic major': [2, 2, 1, 2, 2, 2, 1],
        'Pentatonic minor': [2, 1, 2, 2, 1, 2, 2],
        'Whole-Tone': [2, 2, 2, 2, 2, 2],
        'Half-Whole': [2, 1, 2, 1, 2, 1, 2],
        'Whole-Half': [1, 2, 1, 2, 1, 2, 1],
        'Chromatic': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }.get(scale_name)
    if not source:
        raise RuntimeError

    return ScaleFormula(
        name=scale_name,
        formula=source,
    )


def get_scales_group(scale_formula: ScaleFormula) -> ScaleGroup:
    """Take scale formula. Returns group of scales."""
    base_scales = [
        Key(
            name='C',
            scale=['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C'],
        ),
        Key(
            name='Db',
            scale=['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
        ),
        Key(
            name='D',
            scale=['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D'],
        ),
        Key(
            name='Eb',
            scale=['Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb'],
        ),
        Key(
            name='E',
            scale=['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
        ),
        Key(
            name='F',
            scale=['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F'],
        ),
        Key(
            name='Gb',
            scale=['Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
        ),
        Key(
            name='G',
            scale=['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G'],
        ),
        Key(
            name='Ab',
            scale=['Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
        ),
        Key(
            name='A',
            scale=['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A'],
        ),
        Key(
            name='Bb',
            scale=['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb'],
        ),
        Key(
            name='B',
            scale=['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
        ),
    ]

    scales_list = []
    for key in base_scales:
        step = 0
        formuled_scale = [key.scale[0]]
        for num in scale_formula.formula:
            step += num
            formuled_scale.append(key.scale[step])

        formuled_key = Key(
            name=key.name,
            scale=formuled_scale,
        )
        scales_list.append(formuled_key)

    return ScaleGroup(
        name=scale_formula.name,
        scales=scales_list,
    )


def get_scale_group_from_name(scale_name: str) -> ScaleGroup:
    """Create scale object from the name."""
    formula = _get_scale_formula(scale_name)

    return get_scales_group(formula)
