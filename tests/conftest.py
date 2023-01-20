from typing import List

import pytest

from models import TransRowNotes, PatternInKey, PatternInScale, Pattern, RowNotes


@pytest.fixture()
def fixture_test_pattern() -> Pattern:
    pattern = Pattern(
        name='Pattern Triplets',
        scale_types=['major', 'minor'],
        pattern=[
            RowNotes(
                quants=['123', '234', '345', '456', '567', '678'],
            ),
            RowNotes(
                quants=['765', '654', '543', '432', '321'],
            ),
        ],
    )

    yield pattern


@pytest.fixture()
def fixture_trans_quant_notes() -> List[str]:
    """Group of notes, that should be shown together, like one bar."""
    trans_quant_notes = ['Ab', 'B', 'C']

    yield trans_quant_notes


@pytest.fixture()
def fixture_trans_row_notes(fixture_trans_quant_notes) -> TransRowNotes:
    """Groups of notes, gathered in a rows."""
    trans_row_notes = TransRowNotes(
        quants=[fixture_trans_quant_notes, fixture_trans_quant_notes, fixture_trans_quant_notes]
    )

    yield trans_row_notes


@pytest.fixture()
def fixture_pattern_in_key(fixture_trans_row_notes) -> PatternInKey:
    pattern_in_key = PatternInKey(
        key_name='C',
        pattern=[fixture_trans_row_notes, fixture_trans_row_notes]
    )
    yield pattern_in_key


@pytest.fixture()
def fixture_pattern_in_scale(fixture_pattern_in_key) -> PatternInScale:
    pattern_in_scale = PatternInScale(
        scale_type_name='test scale',
        pattern_name='test pattern',
        scales=[fixture_pattern_in_key, fixture_pattern_in_key]
    )

    yield pattern_in_scale
