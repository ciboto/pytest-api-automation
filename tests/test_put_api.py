import requests

def test_put_update_post(base_url):
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    response = requests.put(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"
