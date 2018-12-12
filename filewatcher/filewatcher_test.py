import os

import pytest
from click.testing import CliRunner

from . import filewatcher


@pytest.fixture
def runner() -> CliRunner:
    runner = CliRunner()

    with runner.isolated_filesystem():
        yield runner


def test_integration(runner: CliRunner):
    os.mkdir("workdir")

    runner.invoke(
        filewatcher.cli,
        ["init", "-s", "log.json", "workdir"]
    )

    result = runner.invoke(
        filewatcher.cli,
        ["verify", "-s", "log.json", "workdir"]
    )

    assert result.output == ""
    assert result.exit_code == 0
