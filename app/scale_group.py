"""
This module contain descriptions of all scales.

As well as functions for scale processing.
"""
from typing import List

from app.models.models_scale import Key, ScaleFormula, ScaleGroup

_scales_formulas_source = {
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
    }


_base_scales_source = [
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


def _get_scale_formula(scale_name: str) -> ScaleFormula:
    """Take from the user scale name. Return object with name and scale formula sequence."""
    formula = _scales_formulas_source.get(scale_name)
    if not formula:
        raise RuntimeError

    return ScaleFormula(
        name=scale_name,
        formula=formula,
    )


def _get_formuled_scale(key: Key, scale_formula: ScaleFormula) -> List[str]:
    """Apply scale formula to the chromatic scale. Returns selected scale notes list."""
    step = 0
    formuled_scale = [key.scale[0]]
    for num in scale_formula.formula:
        step += num
        formuled_scale.append(key.scale[step])

    return formuled_scale


def _get_scales_group(scale_formula: ScaleFormula) -> ScaleGroup:
    """Take scale formula. Returns group of scales."""


    scales_list = [
        Key(
            name=key.name,
            scale=_get_formuled_scale(key, scale_formula),
        )
        for key in _base_scales_source
    ]

    return ScaleGroup(
        name=scale_formula.name,
        scales=scales_list,
    )


def get_scale_group_from_name(scale_name: str) -> ScaleGroup:
    """Create scale object from the name."""
    formula = _get_scale_formula(scale_name)

    return _get_scales_group(formula)
