from src.app import app


def test_config():
    assert app.config["TESTING"] == True
