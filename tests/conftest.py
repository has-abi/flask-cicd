__doc__ = """
Pytest config module
"""


import pytest

from src.app import app


@pytest.fixture(name="testing_app")
def test_app():
    """Config app for testing"""
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(testing_app):
    """Get app test client"""
    return testing_app.test_client()
