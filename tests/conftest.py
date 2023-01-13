__doc__ = """
Pytest config module
"""


import pytest

from src.app import app


@pytest.fixture
def test_app():
    """Config app for testing"""
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(client_app):
    """Get app test client"""
    return client_app.test_client()
