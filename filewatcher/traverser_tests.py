from pathlib import Path

from . import traverser


def test_empty_dir(tmpdir):
    assert traverser.list_files(Path(tmpdir)) == []

def test_regular_files(tmpdir):
    Path(tmpdir, "first_file").touch()
    Path(tmpdir, "second_file").touch()

    result = traverser.list_files(Path(tmpdir))

    assert len(result) == 2
    assert Path(tmpdir, "first_file") in result
    assert Path(tmpdir, "second_file") in result

def test_nested_file(tmpdir):
    directory = Path(tmpdir, "dir")
    directory.mkdir()
    Path(directory, "first_file").touch()

    result = traverser.list_files(Path(tmpdir))

    assert len(result) == 1
    assert Path(tmpdir, "dir", "first_file") in result
