from typing import List

from app.create_html import create_transposed_pattern_html
from app.models import PatternInScale


def transpose_output(transposed_pattern_list: List[PatternInScale]) -> int:
    """Create group of HTML files with transposed pattern."""
    # todo test
    cnt = 0
    for pattern_in_scale in transposed_pattern_list:
        scale_type_name = pattern_in_scale.scale_type_name
        pattern_name = pattern_in_scale.pattern_name

        transposed_pattern_html = create_transposed_pattern_html(pattern_in_scale)

        title = f'{scale_type_name}, {pattern_name}'
        plain_css = """html {
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

.pattern_name {
    font-size: 28px;
    margin-bottom: 5px;
}

.scale_group_name {
    margin-top: 5px;
    margin-bottom: 38px;
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
            <h2 class="pattern_name">{pattern}</h2>
            <h2 class="scale_group_name">{scale_group}</h2>
        </header>
        <div class="content">
            {data}
        </div>
        <footer>©"Into all scales" created by Irina Eiduk, 2023</footer>
    </body>
</html>
""".format(pattern=pattern_name, scale_group=scale_type_name, title=title, styles=plain_css, data=transposed_pattern_html)

        file_name = f"results/{scale_type_name.replace(' ', '_').lower()}_{pattern_name.replace(' ', '_').lower()}"
        html_file = open(f"{file_name}.html", 'w+')
        html_file.write(html_code)
        html_file.close()

        cnt += 1

    return cnt
