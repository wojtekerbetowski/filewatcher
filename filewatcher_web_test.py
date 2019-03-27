import os
import tempfile

import flask
import pytest

import filewatcher_web


@pytest.fixture(autouse=True)
def isolated_filesystem():
    tempdir = tempfile.mkdtemp()
    last = os.getcwd()
    os.chdir(tempdir)
    yield
    os.chdir(last)


client = filewatcher_web.app.test_client()


def test_hashing():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.get("/web/hash?directory=.")

    assert res.status_code == 200, res.data

    assert b"a.txt" in res.data
