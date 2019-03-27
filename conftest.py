import os
import tempfile

import pytest


@pytest.fixture(autouse=True)
def isolated_filesystem():
    tempdir = tempfile.mkdtemp()
    last = os.getcwd()
    os.chdir(tempdir)
    yield
    os.chdir(last)
