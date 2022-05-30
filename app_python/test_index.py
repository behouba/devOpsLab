import pytest
from datetime import datetime
from main import create_app, get_ru_time

@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index(client):
    response = client.get("/")
    time = get_ru_time()
    html = 'Moscow time: {} (UTC+3)'.format(time)
    assert response.status_code == 200
    assert html in str(response.data)