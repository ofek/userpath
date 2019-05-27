import pytest
import userpath

from .utils import ON_WINDOWS_CI, get_random_path

pytestmark = pytest.mark.skipif(not ON_WINDOWS_CI, reason='Tests only for throwaway Windows VMs on CI')


def test_prepend():
    location = get_random_path()
    assert not userpath.in_current_path(location)
    assert userpath.prepend(location)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_prepend_multiple():
    location1 = get_random_path()
    location2 = get_random_path()
    assert not userpath.in_current_path([location1, location2])
    assert userpath.prepend([location1, location2])
    assert userpath.in_new_path([location1, location2])
    assert userpath.need_shell_restart([location1, location2])


def test_append():
    location = get_random_path()
    assert not userpath.in_current_path(location)
    assert userpath.append(location)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_append_multiple():
    location1 = get_random_path()
    location2 = get_random_path()
    assert not userpath.in_current_path([location1, location2])
    assert userpath.append([location1, location2])
    assert userpath.in_new_path([location1, location2])
    assert userpath.need_shell_restart([location1, location2])
