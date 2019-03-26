import pathlib


def load_file(filename):
    if not pathlib.Path(filename).exists():
        raise Exception("Missing file")

    with open(filename) as f:
        return f.read()
