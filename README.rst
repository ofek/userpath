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

Only 2!

pybin
^^^^^

.. code-block:: bash

    $ pybin -h
    Usage: pybin [OPTIONS] COMMAND [ARGS]...

      Shows the location of the bin directory and whether or not it is in the
      user PATH.

    Options:
      -p, --pypath TEXT  An absolute path to a Python executable.
      --version          Show the version and exit.
      -h, --help         Show this message and exit.

    Commands:
      put  Updates the user PATH

pybin put
^^^^^^^^^

.. code-block:: bash

    $ pybin put -h
    Usage: pybin put [OPTIONS]

      Updates the user PATH. The shell must be restarted for the update to take
      effect.

    Options:
      -p, --pypath TEXT  An absolute path to a Python executable.
      -f, --force        Update PATH even if it appears to be correct.
      -h, --help         Show this message and exit.

API
---

.. code-block:: python

    >>> from pybin import in_path, locate, put_in_path
    >>> in_path()
    False
    >>> locate()
    'C:\\Users\\Ofek\\AppData\\Roaming\\Python\\Python36\\Scripts'
    >>> success = put_in_path()

Manual modification
-------------------

Use the location pybin shows in concert with this very comprehensive document
Java provides: `<https://www.java.com/en/download/help/path.xml>`_

License
-------

userpath is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_
- `Apache License, Version 2.0 <https://choosealicense.com/licenses/apache-2.0>`_

at your option.
