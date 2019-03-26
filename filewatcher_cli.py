import json
import os
from pathlib import Path

import click

from filewatcher import hashing, file_loader


@click.group()
def main():
    pass


@main.command()
@click.argument("directory")
@click.option("--store", type=click.Path(), required=False, default="store.json")
@click.option("--override", is_flag=True)
def store(directory, store, override):
    store_path = Path(store)
    if store_path.exists() and not override:
        raise Exception("Store already exists. Use --override flag to force.")

    hashes = hash_tree(directory)

    with store_path.open("w") as store:
        json.dump(hashes, store)


@main.command()
@click.argument("directory")
@click.option("--store", type=click.Path(), required=False, default="store.json")
def verify(directory, store):
    store_path = Path(store)
    with store_path.open() as store_file:
        data = json.load(store_file)

    hashes = hash_tree(directory, store_path=store_path)

    assert data == hashes


def hash_tree(directory, store_path=None):
    paths = [
        Path(root, name)
        for root, dirs, files in os.walk(directory)
        for name in files
    ]

    return {
        str(path): hashing.hash_str(file_loader.load_file(path))
        for path in paths
        if path.is_file() and not path == store_path
    }


if __name__ == "__main__":
    main()
