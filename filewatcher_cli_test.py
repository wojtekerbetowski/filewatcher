import functools
import json

from click.testing import CliRunner

import filewatcher_cli

runner = CliRunner()


def isolated_filesystem(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        with runner.isolated_filesystem():
            return fun(*args, **kwargs)

    return wrapper


@isolated_filesystem
def test_happy_path():
    with open("a.txt", "w") as file:
        file.write("hello")

    res = runner.invoke(filewatcher_cli.main, ["store", "."])

    assert res.exit_code == 0

    with open("store.json") as store:
        data = json.load(store)

    assert data["a.txt"] == "5d41402abc4b2a76b9719d911017c592"


@isolated_filesystem
def test_not_overriding():
    with open("store.json", "w") as file:
        file.write("{}")

    res = runner.invoke(filewatcher_cli.main, ["store", "."])

    assert res.exit_code != 0

    assert "Store already exists" in str(res.exception)


@isolated_filesystem
def test_verify_no_changes():
    with open("a.txt", "w") as file:
        file.write("hello")

    res = runner.invoke(filewatcher_cli.main, ["store", "."])

    assert res.exit_code == 0

    res = runner.invoke(filewatcher_cli.main, ["verify", "."])

    assert res.exit_code == 0


@isolated_filesystem
def test_verify_fail_on_changes():
    with open("a.txt", "w") as file:
        file.write("hello")

    res = runner.invoke(filewatcher_cli.main, ["store", "."])

    assert res.exit_code == 0

    with open("a.txt", "w") as file:
        file.write("other")

    res = runner.invoke(filewatcher_cli.main, ["verify", "."])

    assert res.exit_code != 0
