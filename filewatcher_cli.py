from pathlib import Path

import click

import filewatcher


@click.group()
def main():
    pass


@main.command()
@click.argument("directory")
@click.option(
    "--store", type=click.Path(), required=False, default=filewatcher.DEFAULT_STORE_FILE
)
@click.option("--override", is_flag=True)
def store(directory: str, store: str, override: bool):
    store_path = Path(store)

    hashes = filewatcher.hash_tree(directory)

    filewatcher.store_hashes(store_path, hashes, override)


@main.command()
@click.argument("directory")
@click.option("--store", type=click.Path(), required=False, default="store.json")
def verify(directory, store):
    store_path = Path(store)

    data = filewatcher.load_hashes(store_path)

    hashes = filewatcher.hash_tree(directory, store_path=store_path)

    assert data == hashes


if __name__ == "__main__":
    main()
