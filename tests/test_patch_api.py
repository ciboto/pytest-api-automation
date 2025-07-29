import requests

def test_patch_update_post_title(base_url):
    payload = {"title": "patched title"}
    response = requests.patch(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "patched title"
