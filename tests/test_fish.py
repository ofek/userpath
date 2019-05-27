import pytest
import userpath

from .utils import SKIP_WINDOWS_CI, get_random_path

SHELL_NAME = 'fish'

pytestmark = [SKIP_WINDOWS_CI, pytest.mark.fish]


@pytest.mark.usefixtures('shell_test')
class TestDebian(object):
    DOCKERFILE = 'debian'

    def test_prepend(self, request, shell_test):
        if shell_test is None:
            location = get_random_path()
            assert not userpath.in_current_path(location)
            assert userpath.prepend(location, check=True)
            assert userpath.in_new_path(location)
            assert userpath.need_shell_restart(location)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')

    def test_prepend_multiple(self, request, shell_test):
        if shell_test is None:
            locations = [get_random_path(), get_random_path()]
            assert not userpath.in_current_path(locations)
            assert userpath.prepend(locations, check=True)
            assert userpath.in_new_path(locations)
            assert userpath.need_shell_restart(locations)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')

    def test_append(self, request, shell_test):
        if shell_test is None:
            location = get_random_path()
            assert not userpath.in_current_path(location)
            assert userpath.append(location, check=True)
            assert userpath.in_new_path(location)
            assert userpath.need_shell_restart(location)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')

    def test_append_multiple(self, request, shell_test):
        if shell_test is None:
            locations = [get_random_path(), get_random_path()]
            assert not userpath.in_current_path(locations)
            assert userpath.append(locations, check=True)
            assert userpath.in_new_path(locations)
            assert userpath.need_shell_restart(locations)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')
