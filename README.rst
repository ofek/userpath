userpath
========

.. image:: https://img.shields.io/travis/ofek/userpath/master.svg?logo=travis&label=Travis%20CI
    :target: https://travis-ci.org/ofek/userpath
    :alt: CI - Travis

.. image:: https://img.shields.io/appveyor/ci/ofek/userpath/master.svg?logo=appveyor&label=AppVeyor
    :target: https://ci.appveyor.com/project/ofek/userpath
    :alt: CI - AppVeyor

.. image:: https://img.shields.io/codecov/c/github/ofek/userpath/master.svg?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CgogPGc+CiAgPHRpdGxlPmJhY2tncm91bmQ8L3RpdGxlPgogIDxyZWN0IGZpbGw9Im5vbmUiIGlkPSJjYW52YXNfYmFja2dyb3VuZCIgaGVpZ2h0PSI0MDIiIHdpZHRoPSI1ODIiIHk9Ii0xIiB4PSItMSIvPgogPC9nPgogPGc+CiAgPHRpdGxlPkxheWVyIDE8L3RpdGxlPgogIDxwYXRoIGlkPSJzdmdfMSIgZmlsbC1ydWxlPSJldmVub2RkIiBmaWxsPSIjZmZmZmZmIiBkPSJtMjUuMDE0LDBjLTEzLjc4NCwwLjAxIC0yNS4wMDQsMTEuMTQ5IC0yNS4wMTQsMjQuODMybDAsMC4wNjJsNC4yNTQsMi40ODJsMC4wNTgsLTAuMDM5YTEyLjIzOCwxMi4yMzggMCAwIDEgOS4wNzgsLTEuOTI4YTExLjg0NCwxMS44NDQgMCAwIDEgNS45OCwyLjk3NWwwLjczLDAuNjhsMC40MTMsLTAuOTA0YzAuNCwtMC44NzQgMC44NjIsLTEuNjk2IDEuMzc0LC0yLjQ0M2MwLjIwNiwtMC4zIDAuNDMzLC0wLjYwNCAwLjY5MiwtMC45MjlsMC40MjcsLTAuNTM1bC0wLjUyNiwtMC40NGExNy40NSwxNy40NSAwIDAgMCAtOC4xLC0zLjc4MWExNy44NTMsMTcuODUzIDAgMCAwIC04LjM3NSwwLjQ5YzIuMDIzLC04Ljg2OCA5LjgyLC0xNS4wNSAxOS4wMjcsLTE1LjA1N2M1LjE5NSwwIDEwLjA3OCwyLjAwNyAxMy43NTIsNS42NTJjMi42MTksMi41OTggNC40MjIsNS44MzUgNS4yMjQsOS4zNzJhMTcuOTA4LDE3LjkwOCAwIDAgMCAtNS4yMDgsLTAuNzlsLTAuMzE4LC0wLjAwMWExOC4wOTYsMTguMDk2IDAgMCAwIC0yLjA2NywwLjE1M2wtMC4wODcsMC4wMTJjLTAuMzAzLDAuMDQgLTAuNTcsMC4wODEgLTAuODEzLDAuMTI2Yy0wLjExOSwwLjAyIC0wLjIzNywwLjA0NSAtMC4zNTUsMC4wNjhjLTAuMjgsMC4wNTcgLTAuNTU0LDAuMTE5IC0wLjgxNiwwLjE4NWwtMC4yODgsMC4wNzNjLTAuMzM2LDAuMDkgLTAuNjc1LDAuMTkxIC0xLjAwNiwwLjNsLTAuMDYxLDAuMDJjLTAuNzQsMC4yNTEgLTEuNDc4LDAuNTU4IC0yLjE5LDAuOTE0bC0wLjA1NywwLjAyOWMtMC4zMTYsMC4xNTggLTAuNjM2LDAuMzMzIC0wLjk3OCwwLjUzNGwtMC4wNzUsMC4wNDVhMTYuOTcsMTYuOTcgMCAwIDAgLTQuNDE0LDMuNzhsLTAuMTU3LDAuMTkxYy0wLjMxNywwLjM5NCAtMC41NjcsMC43MjcgLTAuNzg3LDEuMDQ4Yy0wLjE4NCwwLjI3IC0wLjM2OSwwLjU2IC0wLjYsMC45NDJsLTAuMTI2LDAuMjE3Yy0wLjE4NCwwLjMxOCAtMC4zNDgsMC42MjIgLTAuNDg3LDAuOWwtMC4wMzMsMC4wNjFjLTAuMzU0LDAuNzExIC0wLjY2MSwxLjQ1NSAtMC45MTcsMi4yMTRsLTAuMDM2LDAuMTExYTE3LjEzLDE3LjEzIDAgMCAwIC0wLjg1NSw1LjY0NGwwLjAwMywwLjIzNGEyMy41NjUsMjMuNTY1IDAgMCAwIDAuMDQzLDAuODIyYzAuMDEsMC4xMyAwLjAyMywwLjI1OSAwLjAzNiwwLjM4OGMwLjAxNSwwLjE1OCAwLjAzNCwwLjMxNiAwLjA1MywwLjQ3MWwwLjAxMSwwLjA4OGwwLjAyOCwwLjIxNGMwLjAzNywwLjI2NCAwLjA4LDAuNTI1IDAuMTMsMC43ODdjMC41MDMsMi42MzcgMS43Niw1LjI3NCAzLjYzNSw3LjYyNWwwLjA4NSwwLjEwNmwwLjA4NywtMC4xMDRjMC43NDgsLTAuODg0IDIuNjAzLC0zLjY4NyAyLjc2LC01LjM2OWwwLjAwMywtMC4wMzFsLTAuMDE1LC0wLjAyOGExMS43MzYsMTEuNzM2IDAgMCAxIC0xLjMzMywtNS40MDdjMCwtNi4yODQgNC45NCwtMTEuNTAyIDExLjI0MywtMTEuODhsMC40MTQsLTAuMDE1YzIuNTYxLC0wLjA1OCA1LjA2NCwwLjY3MyA3LjIzLDIuMTM2bDAuMDU4LDAuMDM5bDQuMTk3LC0yLjQ0bDAuMDU1LC0wLjAzM2wwLC0wLjA2MmMwLjAwNiwtNi42MzIgLTIuNTkyLC0xMi44NjUgLTcuMzE0LC0xNy41NTFjLTQuNzE2LC00LjY3OSAtMTAuOTkxLC03LjI1NSAtMTcuNjcyLC03LjI1NSIvPgogPC9nPgo8L3N2Zz4=&label=Codecov
    :target: https://codecov.io/github/ofek/userpath?branch=master
    :alt: Codecov

|

.. image:: https://img.shields.io/pypi/pyversions/userpath.svg?logo=python&label=Python&logoColor=gold
    :target: https://pypi.org/project/userpath
    :alt: PyPI - Supported Python versions

.. image:: https://img.shields.io/pypi/v/userpath.svg?logo=python&label=PyPI&logoColor=gold
    :target: https://pypi.org/project/userpath
    :alt: PyPI - Version

.. image:: https://img.shields.io/pypi/dm/userpath.svg?color=blue&label=Downloads&logo=python&logoColor=gold
    :target: https://pypi.org/project/userpath
    :alt: PyPI - Downloads

|

.. image:: https://img.shields.io/badge/License-MIT%2FApache--2.0-9400d3.svg
    :target: https://choosealicense.com/licenses
    :alt: License: MIT/Apache-2.0

.. image:: https://img.shields.io/badge/say-thanks-ff69b4.svg
    :target: https://saythanks.io/to/ofek
    :alt: Say Thanks

-----

Ever wanted to release a cool new app but found it difficult to add its
location to PATH for users? Me too! This tool does that for you on all
major operating systems and does not require elevated privileges!

    **Fear not, this only modifies the user PATH; the system PATH is never
    touched nor even looked at!**

.. contents:: **Table of Contents**
    :backlinks: none

Installation
------------

userpath is distributed on `PyPI <https://pypi.org>`_ as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 2.7/3.6+ and PyPy.
::

    $ pip install userpath

Commands
--------

Only 3!
::

    $ userpath -h
    Usage: userpath [OPTIONS] COMMAND [ARGS]...

    Options:
      --version   Show the version and exit.
      -h, --help  Show this message and exit.

    Commands:
      append   Appends to the user PATH
      prepend  Prepends to the user PATH
      verify   Checks if locations are in the user PATH

.. image:: https://raw.githubusercontent.com/ofek/visuals/master/userpath/lt.PNG
    :alt: Example run

API
---

.. code-block:: python

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

License
-------

userpath is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.

History
-------

Important changes are emphasized.

1.4.2
^^^^^

- Fix fallback mechanism for detecting the name of the parent process

1.4.1
^^^^^

- Fix PATH registry key type on Windows

1.4.0
^^^^^

- Fix duplicating system paths on Windows
- Prevent adding paths multiple times on macOS/Linux
- Send CLI errors to stderr instead of stdout

1.3.0
^^^^^

- Only require the dependency ``distro`` on Linux
- Ship tests with source distributions

1.2.0
^^^^^

- Added support for shell auto-detection and selection

1.1.0
^^^^^

- First public stable release

View `all history <https://github.com/ofek/userpath/blob/master/HISTORY.rst>`_
