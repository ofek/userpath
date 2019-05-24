import os
import subprocess

import pytest


@pytest.fixture(scope='class')
def shell(request):
    shell_name = request.module.shell_name
    dockerfile = getattr(request.cls, 'dockerfile', 'debian')
