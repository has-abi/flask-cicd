__doc__ = """
Test config module
"""


from src.app import app


def test_config():
    """Test config"""
    assert app.config["TESTING"] is True
