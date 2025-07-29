import requests

def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    # JSONPlaceholder sempre retorna 200 para delete, embora nada seja realmente removido
    assert response.status_code == 200
