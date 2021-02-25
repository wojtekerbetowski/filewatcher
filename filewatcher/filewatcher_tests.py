from pathlib import Path

from . import filewatcher

def test_filewatcher_no_change(tmpdir):
    dir = Path(tmpdir, "dir")
    dir.mkdir()

    with Path(dir, "file").open("w") as f:
        f.write("some content")

    snapshot = Path(tmpdir, "snapshot.json")

    filewatcher.save(dir, snapshot)

    result = filewatcher.verify(dir, snapshot)

    assert result == filewatcher.Changes()


def test_filewatcher_new_file(tmpdir):
    dir = Path(tmpdir, "dir")
    dir.mkdir()

    with Path(dir, "file").open("w") as f:
        f.write("some content")

    snapshot = Path(tmpdir, "snapshot.json")

    filewatcher.save(dir, snapshot)

    Path(dir, "new file").touch()

    result = filewatcher.verify(dir, snapshot)

    assert "new file" in result.new


def test_filewatcher_deleted(tmpdir):
    dir = Path(tmpdir, "dir")
    dir.mkdir()

    with Path(dir, "file").open("w") as f:
        f.write("some content")

    snapshot = Path(tmpdir, "snapshot.json")

    filewatcher.save(dir, snapshot)

    Path(dir, "file").unlink()

    result = filewatcher.verify(dir, snapshot)

    assert "file" not in result.changed
    assert "file" in result.removed


def test_filewatcher_changed(tmpdir):
    dir = Path(tmpdir, "dir")
    dir.mkdir()

    with Path(dir, "file").open("w") as f:
        f.write("some content")

    snapshot = Path(tmpdir, "snapshot.json")

    filewatcher.save(dir, snapshot)

    with Path(dir, "file").open("w") as f:
        f.write("different content")

    result = filewatcher.verify(dir, snapshot)

    assert "file" in result.changed
