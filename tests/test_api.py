__doc__ = """
Test api module
"""


from urllib.parse import urlencode


def call_get_with_params(client, path, params):
    """Request a GET endpoint with params"""
    url = f"{path}?{urlencode(params)}"
    response = client.get(url)
    return response


def test_process(client):
    """Test api process endpoint"""
    params = {"text": "test   text"}
    response = call_get_with_params(client, "/process", params)
    assert response.status_code == 200
    assert response.json["originalText"] == "test   text"
    assert response.json["processed"] == "test text"
