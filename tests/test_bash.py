import pytest
import userpath

from .utils import ON_WINDOWS_CI, get_random_path, testing_shell

SHELL_NAME = 'bash'

pytestmark = [
    pytest.mark.skipif(ON_WINDOWS_CI, reason='Tests not run on Windows CI'),
    pytest.mark.skipif(not testing_shell(SHELL_NAME), reason='Not testing shell '.format(SHELL_NAME)),
]


@pytest.mark.usefixtures('shell')
class TestDebian(object):
    DOCKERFILE = 'debian'

    def test_prepend(self):
        location = get_random_path()
        assert not userpath.in_current_path(location)
        assert userpath.prepend(location)
        assert userpath.in_new_path(location)
        assert userpath.need_shell_restart(location)


    def test_prepend_multiple(self):
        location1 = get_random_path()
        location2 = get_random_path()
        assert not userpath.in_current_path([location1, location2])
        assert userpath.prepend([location1, location2])
        assert userpath.in_new_path([location1, location2])
        assert userpath.need_shell_restart([location1, location2])


    def test_append(self):
        location = get_random_path()
        assert not userpath.in_current_path(location)
        assert userpath.append(location)
        assert userpath.in_new_path(location)
        assert userpath.need_shell_restart(location)


    def test_append_multiple(self):
        location1 = get_random_path()
        location2 = get_random_path()
        assert not userpath.in_current_path([location1, location2])
        assert userpath.append([location1, location2])
        assert userpath.in_new_path([location1, location2])
        assert userpath.need_shell_restart([location1, location2])
