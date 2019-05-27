import os
from base64 import urlsafe_b64encode

ON_WINDOWS_CI = 'APPVEYOR' in os.environ


def get_random_path():
    return urlsafe_b64encode(os.urandom(5)).decode()
