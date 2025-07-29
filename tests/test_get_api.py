import requests

def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
