userpath
========

.. image:: https://img.shields.io/pypi/v/userpath.svg?style=flat-square
    :target: https://pypi.org/project/userpath
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/ofek/userpath/master.svg?style=flat-square
    :target: https://travis-ci.org/ofek/userpath
    :alt: Travis CI

.. image:: https://img.shields.io/codecov/c/github/ofek/userpath/master.svg?style=flat-square
    :target: https://codecov.io/gh/ofek/userpath
    :alt: Codecov

.. image:: https://img.shields.io/pypi/pyversions/userpath.svg?style=flat-square
    :target: https://pypi.org/project/userpath
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/l/userpath.svg?style=flat-square
    :target: https://choosealicense.com/licenses
    :alt: License

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
Python 2.6-2.7/3.3+ and PyPy.

.. code-block:: bash

    $ pip install adduserpath

Commands
--------

Only 3!

.. code-block:: bash

    $ userpath -h
    Usage: userpath [OPTIONS] COMMAND [ARGS]...

    Options:
      --version   Show the version and exit.
      -h, --help  Show this message and exit.

    Commands:
      append   Appends to the user PATH
      prepend  Prepends to the user PATH
      verify   Checks if a location is in the user PATH

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
