History
-------

master
^^^^^^

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

1.3.0 (2019-10-20)
^^^^^^^^^^^^^^^^^^

- Only require the dependency ``distro`` on Linux
- Ship tests with source distributions
- Expanded ``HISTORY.rst``

1.2.0 (2019-07-14)
^^^^^^^^^^^^^^^^^^

- Added support for shell auto-detection and selection

1.1.0 (2018-05-16)
^^^^^^^^^^^^^^^^^^

- First public stable release

1.0.0 (2018-05-16)
^^^^^^^^^^^^^^^^^^

- Renamed PyPI package from `adduserpath` to `userpath`.
  Installed package in site-packages remains named `userpath`
- Converted files to Unix end of lines

0.4.0 (2017-09-28)
^^^^^^^^^^^^^^^^^^

- Expand `~` and `~user` constructions if `$HOME` or `user` is known

0.3.0 (2017-09-26)
^^^^^^^^^^^^^^^^^^

- Renamed argument path to locations
- Support operations on multiple locations
- Improved image

0.2.0 (2017-09-21)
^^^^^^^^^^^^^^^^^^

- First release on PyPI, as package named `adduserpath`

0.1.5 (2017-09-20)
^^^^^^^^^^^^^^^^^^

- Improved setup.py

0.1.0 (2017-09-20)
^^^^^^^^^^^^^^^^^^

- First release on GitHub, `setup.py` package named `adduserpath`

0.0.1 (2017-09-20)
^^^^^^^^^^^^^^^^^^

- first commit, site-packages package named `userpath`
