import logging
from typing import List

from models import ScaleGroup, Key, Pattern, ScaleFormula, TransposedPattern


def get_pattern(pattern_name: str) -> Pattern:
    """Take from the user pattern name. Return object with name and pattern sequence."""
    source = {
        'Pattern 1': [1, 2, 3],
        'Pattern 2': [1, 2, 3, 2, 3, 4, 3, 4, 5],
    }.get(pattern_name)

    pattern = Pattern(
        name=pattern_name,
        pattern=source,
    )
    return pattern


def get_scale_formula(scale_name: str) -> ScaleFormula:
    """Take from the user scale name. Return object with name and scale formula sequence."""
    source = {
        'major': [2, 2, 1, 2, 2, 2, 1],
        'minor': [2, 1, 2, 2, 1, 2, 2],
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
            scale=['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'],
        ),
        Key(
            name='Db',
            scale=['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C'],
        ),
        Key(
            name='D',
            scale=['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db'],
        ),
        Key(
            name='Eb',
            scale=['Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D'],
        ),
        Key(
            name='E',
            scale=['E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb'],
        ),
        Key(
            name='F',
            scale=['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E'],
        ),
        Key(
            name='Gb',
            scale=['Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F'],
        ),
        Key(
            name='G',
            scale=['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
        ),
        Key(
            name='Ab',
            scale=['Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G'],
        ),
        Key(
            name='A',
            scale=['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
        ),
        Key(
            name='Bb',
            scale=['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A'],
        ),
        Key(
            name='B',
            scale=['B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb'],
        ),
    ]

    scales_list = []
    for key in base_scales:
        step = 0
        formuled_scale = []
        for num in scale_formula.formula:
            formuled_scale.append(key.scale[step])
            step += num

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


def transpose(pattern: Pattern, scale_group: ScaleGroup) -> TransposedPattern:
    """
     Transpose pattern to one scale.
     Return the dict with patterns for all keys of the scale.
     """
    # todo test
    patterned_key_list = []
    for scale in scale_group.scales:

        note_list = []
        for note in pattern.pattern:
            note_list.append(scale.scale[note-1])

        patterned_key = Key(
            name=scale.name,
            scale=note_list,
        )
        patterned_key_list.append(patterned_key)

    transposed_pattern = TransposedPattern(
        scale_name=scale_group.name,
        pattern_name=pattern.name,
        scales=patterned_key_list,
    )
    return transposed_pattern


def transpose_output(transposed_pattern: TransposedPattern):
    """Create HTML with transposed pattern."""
    # todo test
    scale_name = transposed_pattern.scale_name
    pattern_name = transposed_pattern.pattern_name
    transposed_pattern_html = ''

    for key in transposed_pattern.scales:

        key_html = f'''
            <section>
                <h3>{key.name}</h3>
                <p class="pattern">{' '.join(key.scale)}</p>
            </section>
        '''
        transposed_pattern_html += key_html

    title = f'{scale_name}, {pattern_name}'
    plain_css = """
html {
    position: relative;
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
    width: 500px;
    text-align: center;
}
.content {
    margin: auto;
    width: 500px;
    text-align: center;
}

.pattern {
    font-size: 25px;
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

    html_file = open(f"{scale_name.replace(' ', '_').lower()}.html", 'w+')
    html_file.write(html_code)
    html_file.close()


def main(pattern_name: str, scale_name: str) -> None:
    """
    Do the main runner of "To all scales" project.

    Transpose selected by user pattern to selected scale.
    Return HTML with the result.
    """
    # todo test
    pattern = get_pattern(pattern_name)
    scale_formula = get_scale_formula(scale_name)

    scale_group = get_scales_group(scale_formula)

    transposed_pattern = transpose(pattern, scale_group)

    transpose_output(transposed_pattern)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',  # noqa: WPS323
    )

    main('test_pattern_name', 'test_scale_name')
