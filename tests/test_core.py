from base64 import urlsafe_b64encode
from os import urandom

import userpath


def test_prepend():
    location = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path(location)
    assert userpath.prepend(location)
    assert userpath.in_new_path(location)


def test_append():
    location = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path(location)
    assert userpath.append(location)
    assert userpath.in_new_path(location)
