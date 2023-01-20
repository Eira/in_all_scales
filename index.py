import logging
from typing import List, Optional

from models import ScaleGroup, Key, Pattern, ScaleFormula, PatternInScale, TransRowNotes, PatternInKey, RowNotes

_pattern_source = {
    'test scale': Pattern(
        name='test scale',
        scale_types=['scale 1', 'scale 2'],
        pattern=[
            RowNotes(
                quants=['123', '24', '5'],
            ),
            RowNotes(
                quants=['5', '42', '321'],
            ),
        ],
    ),
    'Pattern Up and down': Pattern(
        name='Pattern Up and down',
        scale_types=['major', 'minor'],
        pattern=[
            RowNotes(
                quants=['123', '456', '787', '654', '321'],
            ),
        ],
    ),
    'Pattern Triplets': Pattern(
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
    ),
    'Pattern In thirds': Pattern(
        name='Pattern In thirds',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['13', '24', '35', '46', '57', '68', '72'],
            ),
            RowNotes(
                quants=['86', '75', '64', '53', '42', '31', '27', '1'],
            ),
        ],
    ),
    'Pattern Skip a step': Pattern(
        name='Pattern Skip a step',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1342', '3564', '5786', '7238'],
            ),
            RowNotes(
                quants=['8657', '6435', '4213', '2761'],
            ),
        ],
    ),
    'Pattern Minor Pentatonic Skip a step': Pattern(
        name='Pattern Minor Pentatonic Skip a step',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1453', '4785', '3574', '7348'],
            ),
            RowNotes(
                quants=['8547', '5314', '3751'],
            ),
        ],
    ),
    'Pattern Slow Minor Pentatonic Build up': Pattern(
        name='Pattern Slow Minor Pentatonic Build up',
        scale_types=['minor'],
        pattern=[
            RowNotes(
                quants=['1713', '4314', '3134', '5435'],
            ),
            RowNotes(
                quants=['4345', '7547', '5457', '8758'],
            ),
        ],
    ),
    'pentatonic scale': [1, 3, 4, 5, 7, 8, 7, 5, 4, 3, 1],
    'blues scale': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1],
}


# todo вероятно пригодится
def create_pattern(pattern_name: str, scale_types: str, pattern: str) -> Pattern:
    """Create pattern object from users data."""
    scale_types_list = scale_types.strip().split(',')
    source_row_list = pattern.strip().split(' ')
    row_list = []
    for source_row in source_row_list:
        row = RowNotes(
            quants=source_row.split(',')
        )
        row_list.append(row)

    return Pattern(
        name=pattern_name,
        scale_types=scale_types_list,
        pattern=row_list,
    )


def get_pattern(pattern_name: str) -> Pattern:
    """Take from the user pattern name. Return object with name and pattern sequence."""
    pattern = _pattern_source.get(pattern_name)

    return pattern


def get_scale_formula(scale_name: str) -> ScaleFormula:
    """Take from the user scale name. Return object with name and scale formula sequence."""
    source = {
        'major': [2, 2, 1, 2, 2, 2, 1],
        'pentatonic major': [2, 2, 1, 2, 2, 2, 1],
        'blues major': [2, 1, 1, 3, 2, 3],
        'jazz melodic minor': [2, 1, 2, 2, 2, 2, 1],
        'harmonic minor': [2, 1, 2, 2, 1, 3, 1],
        'minor': [2, 1, 2, 2, 1, 2, 2],
        'pentatonic minor': [2, 1, 2, 2, 1, 2, 2],
        'blues minor': [3, 2, 1, 1, 3, 2],
    }.get(scale_name)

    scale_formula = ScaleFormula(
        name=scale_name,
        formula=source,
    )
    return scale_formula


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

    scale_group = ScaleGroup(
        name=scale_formula.name,
        scales=scales_list,
    )
    return scale_group


def get_scale_group_from_name(scale_name: str) -> ScaleGroup:
    """Create scale object from the name."""
    #todo test
    formula = get_scale_formula(scale_name)
    scale_group = get_scales_group(formula)

    return scale_group


def create_trans_quant(quant: str, key_scale: List[Key]) -> str:
    """Transpose the quant in scale row to letters notes."""
    trans_note_list = ''
    for note in quant:
        trans_note_list += f'{key_scale[int(note) - 1]} '
    return trans_note_list.strip()


def create_trans_row(row: List[str], key_scale: List[Key]) -> TransRowNotes:
    """Gather transposed quants to the row."""
    trans_quant_list = []

    for quant in row:
        trans_note_list = create_trans_quant(quant, key_scale)

        trans_quant_list.append(trans_note_list)

    trans_row = TransRowNotes(
        quants=trans_quant_list
    )

    return trans_row


def create_trans_row_list(pattern_rows: List[RowNotes], key_scale: List[Key]) -> List[TransRowNotes]:
    """Gather transposed rows to lists."""
    trans_row_list = []

    for row in pattern_rows:
        trans_row = create_trans_row(row.quants, key_scale)
        trans_row_list.append(trans_row)

    return trans_row_list


# todo разобрать на функции
def transpose(pattern: Pattern, scale_group_list: Optional[List[ScaleGroup]] = None) -> List[PatternInScale]:
    """
     Transpose pattern all possible scales or to selected one.
     Return list of objects with patterns for all keys of the scale.
     """
    # todo test
    transposed_pattern_list = []

    if scale_group_list is None:
        for scale_type in pattern.scale_types:
            scale_group = get_scale_group_from_name(scale_type)

            patterned_key_list = []
            for key_scale in scale_group.scales:
                trans_row_list = create_trans_row_list(pattern.pattern, key_scale.scale)

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


def transpose_output(transposed_pattern_list: List[PatternInScale]) -> int:
    """Create group of HTML files with transposed pattern."""
    # todo test
    cnt = 0
    for pattern_in_scale in transposed_pattern_list:
        scale_type_name = pattern_in_scale.scale_type_name
        pattern_name = pattern_in_scale.pattern_name

        transposed_pattern_html = create_transposed_pattern_html(pattern_in_scale)

        title = f'{scale_type_name}, {pattern_name}'
        plain_css = """
        html {
            position: relative;
            min_height: 100%;
        }
        h1 {
            position: absolute;
            top: 10px;
            right: 15px;

            font-size: 16px;
            font-weight: bold;
            color: lightgrey;
        }

        footer {
            position: absolute;
            right: 15px;
            bottom: 10px;

            color: grey;
        }

        .header {
            margin: auto;
            width: 800px;
            text-align: center;
        }
        .content {
            margin: auto;
            width: 800px;
            text-align: center;
        }

        .pattern {
            font-size: 25px;
        }
        
        .scale_quant {
            margin: 5px;
        }
        """
        html_code = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style type="text/css">
            {styles}
        </style>
    </head>
    <body>
        <header class="header">
            <h1>into all scales</h1>
            <h2>{title}</h2>
        </header>
        <div class="content">
            {data}
        </div>
        <footer>©"Into all scales" created by Irina Eiduk, 2023</footer>
    </body>
</html>
""".format(title=title, styles=plain_css, data=transposed_pattern_html)

        file_name = f"results/{scale_type_name.replace(' ', '_').lower()}_{pattern_name.replace(' ', '_').lower()}"
        html_file = open(f"{file_name}.html", 'w+')
        html_file.write(html_code)
        html_file.close()

        cnt += 1

    return cnt


def main(pattern_name: str) -> None:
    """
    Do the main runner of "Into all scales" project.

    Transpose selected by user pattern to all scales, that program know.
    Return group of HTML files, according to amount of scales.
    """
    # todo test
    #получить данные для паттерна
    # подготовить данные для паттерна и формулы?
    pattern = get_pattern(pattern_name)
    #scale_formula = get_scale_formula(scale_name)

    # сгенерировать лад
    #scale_group = get_scales_group(scale_formula)

    # создать списки паттернов по ладам
    transposed_pattern_list = transpose(pattern)
    # генерируем файлы
    transpose_output(transposed_pattern_list)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', 'test_scale_name')
