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

    hashes = {}

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = Path(root, name)
            if path.is_file():
                hashes[str(path)] = hashing.hash_str(file_loader.load_file(path))

    with store_path.open("w") as store:
        json.dump(hashes, store)


if __name__ == "__main__":
    main()
