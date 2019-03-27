import json
import os
import pathlib
import typing

from . import hashing, file_loader

DEFAULT_STORE_FILE = "store.json"


Hashes = typing.Dict[str, str]


def hash_tree(directory: str, store_path: pathlib.Path = None) -> Hashes:
    """Walks the given directory and returns a filename to hash dict"""

    paths = [
        pathlib.Path(root, name)
        for root, dirs, files in os.walk(directory)
        for name in files
    ]

    return {
        str(path): hashing.hash_str(file_loader.load_file(path))
        for path in paths
        if path.is_file() and not path == store_path
    }


def store_hashes(store_path: pathlib.Path, hashes: Hashes, override: bool) -> None:
    """Saves hashes into a given JSON file"""

    if store_path.exists() and not override:
        raise Exception("Store already exists. Use --override flag to force.")

    with store_path.open("w") as store:
        json.dump(hashes, store)


def load_hashes(store_path: pathlib.Path) -> Hashes:
    """Load `Hashes` from a given JSON file"""

    with store_path.open() as store_file:
        return json.load(store_file)
