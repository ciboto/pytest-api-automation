import requests

def test_post_create_post(base_url):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"
    assert "id" in data
