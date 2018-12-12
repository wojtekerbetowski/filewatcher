import click


@click.group()
def cli():
    pass


@cli.command()
def hello():
    print("Hello world")


if __name__ == '__main__':
    cli()
