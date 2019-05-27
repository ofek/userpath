import os
from base64 import urlsafe_b64encode

import pytest

ON_WINDOWS_CI = 'APPVEYOR' in os.environ
SKIP_WINDOWS_CI = pytest.mark.skipif(ON_WINDOWS_CI, reason='Tests not run on Windows CI')


def get_random_path():
    return urlsafe_b64encode(os.urandom(5)).decode()
