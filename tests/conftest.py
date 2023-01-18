from typing import List

import pytest

from models import TransRowNotes, PatternInKey, PatternInScale


@pytest.fixture()
def fixture_trans_quant_notes() -> List[str]:
    """Group of notes, that should be shown together, like one bar."""
    trans_quant_notes = ['A', 'B', 'C']

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
