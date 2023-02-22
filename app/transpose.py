"""This module create the list of scales with pattern with transposed notes."""

from typing import List, Optional, Set

from app.models import PatternInKey, PatternInScale, PatternType, RowNotes, TransRowNotes
from app.scale_group import get_scale_group_from_name


def _create_trans_quant(quant: str, key_scale: List[str]) -> str:
    """Transpose the quant in scale row to letters notes."""
    trans_note_list = ''
    for note in quant:
        trans_note_list.join(f'{key_scale[int(note) - 1]} ')
    return trans_note_list.strip()


def _create_trans_row(row: List[str], key_scale: List[str]) -> TransRowNotes:
    """Gather transposed quants to the row."""
    trans_quant_list = []

    for quant in row:
        trans_note_list = _create_trans_quant(quant, key_scale)

        trans_quant_list.append(trans_note_list)

    return TransRowNotes(
        quants=trans_quant_list,
    )


def _create_trans_row_list(pattern_rows: List[RowNotes], key_scale: List[str]) -> List[TransRowNotes]:
    """Gather transposed rows to lists."""
    trans_row_list = []

    for row in pattern_rows:
        trans_row = _create_trans_row(row.quants, key_scale)
        trans_row_list.append(trans_row)

    return trans_row_list


def transpose(pattern: PatternType, user_scale_group: Optional[Set[str]] = None) -> List[PatternInScale]:
    """
    Transpose pattern all possible scales or to selected one.

    Return list of objects with patterns for all keys of the scale.
    """
    transposed_pattern_list = []
    scale_type_list: Set[str] = set()

    if user_scale_group is None:
        scale_type_list = pattern.scale_types
    elif user_scale_group:
        scale_type_list = user_scale_group

    if not scale_type_list:
        raise RuntimeError

    for scale_type in scale_type_list:
        scale_group = get_scale_group_from_name(scale_type)

        patterned_key_list = []
        for key_scale in scale_group.scales:
            trans_row_list = _create_trans_row_list(pattern.pattern, key_scale.scale)

            patterned_key = PatternInKey(
                key_name=key_scale.name,
                pattern=trans_row_list,
            )
            patterned_key_list.append(patterned_key)

        transposed_pattern = PatternInScale(
            scale_type_name=scale_group.name,
            pattern_name=pattern.name,
            scales=patterned_key_list,
        )

        transposed_pattern_list.append(transposed_pattern)
    return transposed_pattern_list
