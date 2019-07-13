import os
import subprocess
from itertools import chain

import pytest

from userpath.shells import SHELLS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def pytest_configure(config):
    # pytest will emit warnings if these aren't registered ahead of time
    for shell in sorted(SHELLS):
        config.addinivalue_line('markers', '{shell}: marker to only run tests for {shell}'.format(shell=shell))


@pytest.fixture(scope='class')
def shell_test(request):
    if 'SHELL' in os.environ:
        yield
    else:
        compose_file = os.path.join(HERE, 'docker', 'docker-compose.yaml')
        shell_name = request.module.SHELL_NAME
        dockerfile = getattr(request.cls, 'DOCKERFILE', 'debian')
        container = '{}-{}'.format(shell_name, dockerfile)

        tox_env = os.environ['TOX_ENV_NAME']
        python_version = '.'.join(tox_env.replace('py', ''))

        try:
            os.environ['SHELL'] = shell_name
            os.environ['DOCKERFILE'] = dockerfile
            os.environ['PYTHON_VERSION'] = python_version
            subprocess.check_call(['docker-compose', '-f', compose_file, 'up', '-d', '--build'])

            # Python gets really upset when compiled files from different paths and/or platforms are encountered
            clean_package()

            yield lambda test_name: subprocess.Popen(
                [
                    'docker',
                    'exec',
                    '-w',
                    '/home/userpath',
                    container,
                    'coverage',
                    'run',
                    '-m',
                    'pytest',
                    'tests/{}::{}::{}'.format(os.path.basename(request.module.__file__), request.node.name, test_name),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        finally:
            # Clean up for the next tox invocation
            clean_package()

            # Tear down without checking for errors
            subprocess.call(['docker-compose', '-f', compose_file, 'down'])
            del os.environ['SHELL']
            del os.environ['DOCKERFILE']
            del os.environ['PYTHON_VERSION']


def clean_package():
    to_delete = []
    walker = os.walk(ROOT)

    top = next(walker)
    top[1].remove('.tox')

    for root, dirs, files in chain((top,), walker):
        for f in files:
            if f.endswith('.pyc'):
                to_delete.append(os.path.join(root, f))

    for f in to_delete:
        os.remove(f)
