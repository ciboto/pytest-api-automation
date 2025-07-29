import pytest
import os

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
