import json
import os
import pathlib
import typing

from . import hashing, file_loader

DEFAULT_STORE_FILE = "store.json"


def hash_tree(directory, store_path=None):
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


def store_hashes(
    store_path: pathlib.Path, hashes: typing.Dict[str, str], override: bool
):
    if store_path.exists() and not override:
        raise Exception("Store already exists. Use --override flag to force.")

    with store_path.open("w") as store:
        json.dump(hashes, store)


def load_hashes(store_path: pathlib.Path):
    with store_path.open() as store_file:
        return json.load(store_file)
