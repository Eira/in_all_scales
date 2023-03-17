# Into all scales

[![linters](https://github.com/Eira/into_all_scales/actions/workflows/linters.yml/badge.svg?branch=main)](https://github.com/Eira/into_all_scales/actions/workflows/linters.yml)
[![tests](https://github.com/Eira/into_all_scales/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Eira/into_all_scales/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/Eira/into_all_scales/branch/main/graph/badge.svg?token=2TDKVAFWKR)](https://codecov.io/gh/Eira/into_all_scales)

An instrument to transform musical patterns to all scales.

### Local setup
```shell
$ git clone git@github.com:Eira/into_all_scales.git
$ cd into_all_scales
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry
$ poetry install
```

### Local run tests
```shell
$ python -m pytest
```

### Local run linters
```
poetry run flake8 app/

poetry run mypy app/
```
