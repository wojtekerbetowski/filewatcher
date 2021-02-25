from pathlib import Path

from . import snapshot_repository as repo

def test_store_and_load(tmpdir):
    snapshot_file = Path(tmpdir, "snapshot_file")

    data = {
        "key": "value",
    }

    repo.store(snapshot_file, data)
    loaded = repo.load(snapshot_file)

    assert snapshot_file.exists()
    assert loaded == data
    
