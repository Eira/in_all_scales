from app.models import TransRowNotes, PatternInKey, PatternInScale


def create_quant_html(quotes_list: str) -> str:
    """Create html with one quant of the row in transposed pattern."""
    pattern_row_html = f'''
        <span class="scale_quant">{quotes_list}</span>
    '''
    return pattern_row_html


def create_row_html(pattern_row: TransRowNotes) -> str:
    """Create html with one row of the transposed pattern."""
    quants_list_html = ''
    for quotes_list in pattern_row.quants:
        quants_list_html += create_quant_html(quotes_list)

    pattern_row_html = f'''<p class="pattern">
        {quants_list_html}
    </p>
    '''

    return pattern_row_html


def create_key_html(pattern_in_key: PatternInKey) -> str:
    """Create html with transposed pattern in one key."""
    pattern_row_list_html = ''
    for pattern_row in pattern_in_key.pattern:
        pattern_row_list_html += create_row_html(pattern_row)

    key_html = f'''<section>
        <h3>{pattern_in_key.key_name}</h3>
        {pattern_row_list_html}
    </section>
    '''

    return key_html


def create_transposed_pattern_html(pattern_in_scale: PatternInScale) -> str:
    """Create html with list of transposed pattern in every key."""
    transposed_pattern_html = ''
    for pattern_in_key in pattern_in_scale.scales:
        key_html = create_key_html(pattern_in_key)
        transposed_pattern_html += key_html

    return transposed_pattern_html
