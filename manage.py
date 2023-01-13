from coverage import coverage

app_cov = coverage(include="src/*", omit=["tests/*"])
app_cov.start()

import pytest
from flask.cli import FlaskGroup

from src.app import app

cli = FlaskGroup(app)  # type: ignore


@cli.command()
def test():
    """Run tests with pytest"""
    pytest.main(["--rootdir", "./tests"])


@cli.command()
def cov():
    """Run tests with coverage"""
    pytest_result = pytest.main(["-x", "./tests"])
    if pytest_result == 0:
        app_cov.stop()
        app_cov.save()
        app_cov.report()
        app_cov.html_report()
        app_cov.erase()
        return 0
    return 1


if __name__ == "__main__":
    cli()
