import hashlib
import json
import logging
import os
import pathlib

import click

logger = logging.Logger("main")


def load_files(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            yield pathlib.Path(root, name)


def hash_file(file_path, hash_type):
    assert hash_type in hashlib.algorithms_available

    with open(file_path, "rb") as f:
        return getattr(hashlib, hash_type)(f.read()).hexdigest()


@click.group()
@click.option("--verbose", "-v", count=True)
def cli(verbose):
    level = {0: "INFO", 1: "WARN", 2: "INFO", 3: "DEBUG"}.get(verbose, "INFO")

    logger.setLevel(level)


@cli.command()
@click.argument("base", default=".", type=click.Path(exists=True))
@click.option(
    "--store", "-s",
    default="store.json",
    type=click.Path(), help="will store result hashed in a given file"
)
@click.option("--override", is_flag=True)
@click.option("--hash-type", default="sha256", type=click.Choice(["sha256"]))
def init(base, store, override, hash_type):
    if pathlib.Path(store).exists() and not override:
        logger.error("Will not override file. Exiting early")
        exit(1)

    results = {str(f): hash_file(f, hash_type) for f in load_files(base)}

    output_json = json.dumps(results)

    if store is None:
        logger.info(output_json)
    else:
        with open(store, "w") as out:
            out.write(output_json)
            logger.debug("Written to file {}".format(store))


if __name__ == '__main__':
    cli()
