import pytest
import userpath

from .utils import ON_WINDOWS_CI, get_random_path

pytestmark = pytest.mark.skipif(not ON_WINDOWS_CI, reason='Tests only for throwaway Windows VMs on CI')


def test_prepend():
    location = get_random_path()
    assert not userpath.in_current_path(location)
    assert userpath.prepend(location, check=True)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_prepend_multiple():
    locations = [get_random_path(), get_random_path()]
    assert not userpath.in_current_path(locations)
    assert userpath.prepend(locations, check=True)
    assert userpath.in_new_path(locations)
    assert userpath.need_shell_restart(locations)


def test_append():
    location = get_random_path()
    assert not userpath.in_current_path(location)
    assert userpath.append(location, check=True)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_append_multiple():
    locations = [get_random_path(), get_random_path()]
    assert not userpath.in_current_path(locations)
    assert userpath.append(locations, check=True)
    assert userpath.in_new_path(locations)
    assert userpath.need_shell_restart(locations)
