"""This module create a PDF file with transposed pattern of lick in one scale."""

import os
from typing import List

from pyhtml2pdf import converter  # type: ignore

from app.create_html import create_transposed_pattern_html
from app.models.models_pattern import PatternInScale
from app.settings import CSS_PATH, HTML_TEMPLATE_PATH, RESULTS_PATH


def _get_html_pattern(pattern_in_scale: PatternInScale) -> str:
    """Get html pattern from the file. Return html with exact pattern in scale."""
    with open(CSS_PATH) as css_file:
        css = css_file.read()

    with open(HTML_TEMPLATE_PATH) as html_template:
        html_code = html_template.read().format(
            pattern=pattern_in_scale.scale_type_name,
            scale_group=pattern_in_scale.pattern_name,
            title='{0}, {1}'.format(
                pattern_in_scale.scale_type_name,
                pattern_in_scale.pattern_name,
            ),
            data=create_transposed_pattern_html(pattern_in_scale),
            style=css,
        )

    return html_code


def _create_file_name(scale_type_name: str, pattern_name: str) -> str:
    """Generate file name for transposed pattern file."""
    scale_type_name_norm = scale_type_name.replace(' ', '_').lower()
    pattern_name_norm = pattern_name.replace(' ', '_').lower()

    return f'{RESULTS_PATH}/{scale_type_name_norm}_{pattern_name_norm}'


def transpose_output(transposed_pattern_list: List[PatternInScale]) -> int:
    """Create group of PDF files with transposed pattern."""
    # todo test
    cnt = 0
    for pattern_in_scale in transposed_pattern_list:
        file_name = _create_file_name(pattern_in_scale.scale_type_name, pattern_in_scale.pattern_name)

        with open(f'{file_name}.html', 'w+') as html_file:
            html_file.write(_get_html_pattern(pattern_in_scale))

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
