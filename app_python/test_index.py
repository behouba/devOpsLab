"""Index test."""
import pytest

from main import create_app, get_ru_time

@pytest.fixture
def client():
    """App fixture."""
    with create_app().test_client() as clt:
        yield clt


def test_index(client):
    """Test index (/) endpoint."""
    response = client.get("/")
    time = get_ru_time()
    html = f'Moscow time: {time} (UTC+3)'
    assert response.status_code == 200
    assert html in str(response.data)
