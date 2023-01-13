import pytest

from src.app import app


@pytest.fixture
def test_app():
    """Config app for testing"""
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture
def client(test_app):
    """Get app test client"""
    return test_app.test_client()
