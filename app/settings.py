"""Application settings."""

import os

path_root = os.path.dirname(__file__)

RESULTS_PATH = os.path.abspath(
    os.path.join(path_root, '..', 'results'),
)

HTML_TEMPLATE_PATH = os.path.abspath(
    os.path.join(path_root, '..', 'assets', 'page_template.html'),
)

CSS_PATH = os.path.abspath(
    os.path.join(path_root, '..', 'assets', 'style.css'),
)
