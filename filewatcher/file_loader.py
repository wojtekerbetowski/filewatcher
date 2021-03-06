import pathlib

import string


def load_file(filename: str) -> str:
    """Loads the content of a file"""

    if not pathlib.Path(filename).exists():
        raise Exception("Missing file")

    with open(filename) as f:
        return f.read()
