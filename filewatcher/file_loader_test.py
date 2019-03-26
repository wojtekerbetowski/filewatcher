import tempfile

from filewatcher import file_loader


def test_loading_file_content(tmpdir):
    file = tmpdir.join("hello.txt")
    file.write("my content")

    content = file_loader.load_file(file)

    assert content == "my content"


def test_loading_missing_file():
    try:
        file_loader.load_file("/sure/theres/no/such/file")
    except Exception as e:
        assert "Missing file" in str(e)
