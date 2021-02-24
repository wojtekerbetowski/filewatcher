import pathlib


def list_files(directory: pathlib.Path) -> list[pathlib.Path]:
    return [x for x in directory.glob('**/*') if x.is_file()]
