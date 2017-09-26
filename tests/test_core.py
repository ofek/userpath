from base64 import urlsafe_b64encode
from os import urandom

import userpath


def test_prepend():
    location = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path(location)
    assert userpath.prepend(location)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_prepend_multiple():
    location1 = urlsafe_b64encode(urandom(5)).decode()
    location2 = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path([location1, location2])
    assert userpath.prepend([location1, location2])
    assert userpath.in_new_path([location1, location2])
    assert userpath.need_shell_restart([location1, location2])


def test_append():
    location = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path(location)
    assert userpath.append(location)
    assert userpath.in_new_path(location)
    assert userpath.need_shell_restart(location)


def test_append_multiple():
    location1 = urlsafe_b64encode(urandom(5)).decode()
    location2 = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path([location1, location2])
    assert userpath.append([location1, location2])
    assert userpath.in_new_path([location1, location2])
    assert userpath.need_shell_restart([location1, location2])
