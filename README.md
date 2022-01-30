# userpath

| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/ofek/userpath/actions/workflows/test.yml/badge.svg)](https://github.com/ofek/userpath/actions/workflows/test.yml) [![CD - Build](https://github.com/ofek/userpath/actions/workflows/build.yml/badge.svg)](https://github.com/ofek/userpath/actions/workflows/build.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/userpath.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/userpath/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/userpath.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/userpath/) |
| Meta | [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/ofek?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/ofek) |

-----

This is a tool for modifying a user's `PATH`.

**Table of Contents**

- [Installation](#installation)
- [CLI](#cli)
- [API](#api)
- [License](#license)

## Installation

```console
pip install userpath
```

## CLI

```console
$ userpath -h
Usage: userpath [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  append   Appends to the user PATH
  prepend  Prepends to the user PATH
  verify   Checks if locations are in the user PATH
```

## API

```pycon
>>> import userpath
>>> location = r'C:\Users\Ofek\Desktop\test'
>>>
>>> userpath.in_current_path(location)
False
>>> userpath.in_new_path(location)
False
>>> userpath.append(location)
True
>>> userpath.in_new_path(location)
True
>>> userpath.need_shell_restart(location)
True
```

## License

`userpath` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
