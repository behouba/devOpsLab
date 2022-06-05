"""pytest is testing framework."""
import pytest

from main import create_app, get_ru_time

@pytest.fixture()
def app():
    """Create new app instance for testing."""
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    """Returns new client instance."""
    return app.test_client()


def test_index(client):
    """Test index (/) endpoint."""
    response = client.get("/")
    time = get_ru_time()
    html = f'Moscow time: {time} (UTC+3)'
    assert response.status_code == 200
    assert html in str(response.data)