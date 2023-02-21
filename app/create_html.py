"""This module create HTML code with transposed patterns of licks."""

from app.models import PatternInKey, PatternInScale, TransRowNotes


def _create_quant_html(quotes_list: str) -> str:
    """Create html with one quant of the row in transposed pattern."""
    return f"""
        <span class="scale_quant">{quotes_list}</span>
    """


def _create_row_html(pattern_row: TransRowNotes) -> str:
    """Create html with one row of the transposed pattern."""
    quants_list_html = ''
    for quotes_list in pattern_row.quants:
        quants_list_html += _create_quant_html(quotes_list)

    return f"""<p class="pattern">
        {quants_list_html}
    </p>
    """


def _create_key_html(pattern_in_key: PatternInKey) -> str:
    """Create html with transposed pattern in one key."""
    pattern_row_list_html = ''
    for pattern_row in pattern_in_key.pattern:
        pattern_row_list_html += _create_row_html(pattern_row)

    return f"""<section>
        <h3>{pattern_in_key.key_name}</h3>
        {pattern_row_list_html}
    </section>
    """


def create_transposed_pattern_html(pattern_in_scale: PatternInScale) -> str:
    """Create html with list of transposed pattern in every key."""
    transposed_pattern_html = ''
    for pattern_in_key in pattern_in_scale.scales:
        key_html = _create_key_html(pattern_in_key)
        transposed_pattern_html += key_html

    return transposed_pattern_html
