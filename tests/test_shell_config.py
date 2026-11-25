import os
import shutil
import subprocess

import pytest

from userpath.shells import Bash, Sh, Zsh


@pytest.mark.skipif(os.name == 'nt', reason='Requires POSIX shells and PATH syntax')
@pytest.mark.parametrize('shell_name,shell_class', [('sh', Sh), ('bash', Bash), ('zsh', Zsh)])
@pytest.mark.parametrize('front', [True, False])
@pytest.mark.parametrize('location', [
    '/opt/plain/bin',
    '/opt/with spaces/bin',
    '/opt/$HOME/bin',
    '/opt/$(printf expanded)/bin',
    '/opt/`printf expanded`/bin',
    '/opt/double"quote/bin',
    "/opt/single'quote/bin",
    r'/opt/back\slash/bin',
    '/opt/trailing\\',
    '/opt/first$dir:/opt/second"dir',
])
def test_config_preserves_literal_locations(tmp_path, shell_name, shell_class, front, location):
    executable = shutil.which(shell_name)
    if executable is None:
        pytest.skip('{} is not installed'.format(shell_name))

    original_path = '/usr/bin:/bin'
    expected = ':'.join((location, original_path) if front else (original_path, location))
    configs = shell_class(home=str(tmp_path)).config(location, front=front)
    for contents in configs.values():
        result = subprocess.check_output(
            [executable, '-c', contents + '\nprintf "%s" "$PATH"'],
            env={'HOME': str(tmp_path), 'PATH': original_path},
            universal_newlines=True,
        )
        assert result == expected
