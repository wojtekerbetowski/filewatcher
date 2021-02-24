from pathlib import Path

from . import hasher


def test_hasher(tmpdir):
    f = Path(tmpdir, "file")
    with f.open("w"):
        f.write_text("some content")
    
    result = hasher.hash_content(f)

    assert result == "94e66df8cd09d410c62d9e0dc59d3a884e458e05"
