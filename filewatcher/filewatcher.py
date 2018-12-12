import asyncio
import hashlib
import json
import logging
import os
import pathlib

import click
import click_completion

logger = logging.Logger("main")


async def load_files(dir_path):
    await asyncio.sleep(0)

    return (
        pathlib.Path(root, name)
        for root, dirs, files in os.walk(dir_path, topdown=False)
        for name in files
    )


async def hash_file(file_path, hash_type):
    await asyncio.sleep(0)

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
    asyncio.run(ainit(base, store, override, hash_type))


async def ainit(base, store, override, hash_type):
    if pathlib.Path(store).exists() and not override:
        logger.error("Will not override file. Exiting early")
        exit(1)

    files = await load_files(base)

    results = {}
    for f in files:
        results[str(f)] = await hash_file(f, hash_type)

    output_json = json.dumps(results)

    if store is None:
        logger.info(output_json)
    else:
        with open(store, "w") as out:
            out.write(output_json)
            logger.debug("Written to file {}".format(store))


@cli.command()
@click.argument("base", default=".", type=click.Path(exists=True))
@click.option(
    "--store",
    "-s",
    type=click.Path(exists=True),
    help="will store result hashed in a given file",
)
@click.option("--hash-type", default="sha256", type=click.Choice(["sha256"]))
def verify(base, store, hash_type):
    asyncio.run(averify(base, store, hash_type))


async def averify(base, store, hash_type):
    files = await load_files(base)

    results = {}
    for f in files:
        results[str(f)] = await hash_file(f, hash_type)
    with open(store) as store_file:
        output_json = json.load(store_file)

    diff = [key for key, value in results.items() if value != output_json.get(key)]

    if diff:
        print(f"Files changed: {diff}")
        exit(len(diff))


@cli.command()
@click.option(
    "--append/--overwrite", help="Append the completion code to the file", default=None
)
@click.option(
    "-i", "--case-insensitive/--no-case-insensitive", help="Case insensitive completion"
)
@click.argument(
    "shell",
    required=False,
    type=click_completion.DocumentedChoice(click_completion.core.shells),
)
@click.argument("path", required=False)
def completion(append, case_insensitive, shell, path):
    """Install the click-completion-command completion"""
    extra_env = (
        {"_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE": "ON"}
        if case_insensitive
        else {}
    )
    shell, path = click_completion.core.install(
        shell=shell, path=path, append=append, extra_env=extra_env
    )
    click.echo("%s completion installed in %s" % (shell, path))


if __name__ == '__main__':
    cli()
