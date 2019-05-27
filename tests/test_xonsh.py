import pytest
import userpath

from .utils import ON_WINDOWS_CI, get_random_path

SHELL_NAME = 'xonsh'

pytestmark = pytest.mark.skipif(ON_WINDOWS_CI, reason='Tests not run on Windows CI')


@pytest.mark.usefixtures('shell_test')
class TestDebian(object):
    DOCKERFILE = 'debian'

    def test_prepend(self, request, shell_test):
        if shell_test is None:
            location = get_random_path()
            assert not userpath.in_current_path(location)
            assert userpath.prepend(location)
            assert userpath.in_new_path(location)
            assert userpath.need_shell_restart(location)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')

    def test_prepend_multiple(self, request, shell_test):
        if shell_test is None:
            location1 = get_random_path()
            location2 = get_random_path()
            assert not userpath.in_current_path([location1, location2])
            assert userpath.prepend([location1, location2])
            assert userpath.in_new_path([location1, location2])
            assert userpath.need_shell_restart([location1, location2])
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')


    def test_append(self, request, shell_test):
        if shell_test is None:
            location = get_random_path()
            assert not userpath.in_current_path(location)
            assert userpath.append(location)
            assert userpath.in_new_path(location)
            assert userpath.need_shell_restart(location)
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')


    def test_append_multiple(self, request, shell_test):
        if shell_test is None:
            location1 = get_random_path()
            location2 = get_random_path()
            assert not userpath.in_current_path([location1, location2])
            assert userpath.append([location1, location2])
            assert userpath.in_new_path([location1, location2])
            assert userpath.need_shell_restart([location1, location2])
        else:
            process = shell_test(request.node.name)
            stdout, stderr = process.communicate()

            assert process.returncode == 0, (stdout + stderr).decode('utf-8')
