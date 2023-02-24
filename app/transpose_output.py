"""This module create a PDF file with transposed pattern of lick in one scale."""

import os
from typing import List

from pyhtml2pdf import converter  # type: ignore

from app.create_html import create_transposed_pattern_html
from app.models.models_pattern import PatternInScale


def transpose_output(transposed_pattern_list: List[PatternInScale]) -> int:
    """Create group of HTML files with transposed pattern."""
    # todo test
    cnt = 0
    for pattern_in_scale in transposed_pattern_list:
        scale_type_name = pattern_in_scale.scale_type_name
        pattern_name = pattern_in_scale.pattern_name

        transposed_pattern_html = create_transposed_pattern_html(pattern_in_scale)

        title = f'{scale_type_name}, {pattern_name}'
        with open('../assets/page_template.html') as html_template:
            html_code = html_template.read().format(
                pattern=pattern_name,
                scale_group=scale_type_name,
                title=title,
                data=transposed_pattern_html,
            )

        file_name = f"results/{scale_type_name.replace(' ', '_').lower()}_{pattern_name.replace(' ', '_').lower()}"

        with open(f'{file_name}.html', 'w+') as html_file:
            html_file.write(html_code)

        path = os.path.abspath(f'{file_name}.html')
        converter.convert(
            f'file:///{path}',
            f'{file_name}.pdf',
            print_options={
                'marginTop': 0,
                'marginRight': 0,
                'marginBottom': 0,
                'marginLeft': 0,
                'landscape': True,
                'paperWidth': 15,
                'paperHeight': 17,
            },
        )

        cnt += 1

    return cnt
