from base64 import urlsafe_b64encode
from os import urandom

import userpath


def test_prepend():
    path = urlsafe_b64encode(urandom(5)).decode()
    assert not userpath.in_current_path(path)
    userpath.prepend(path)
    print(userpath.get_new_path())
    assert userpath.in_new_path(path)
