import pytest

from tuxinator_api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_status(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert json_data['status'] == 'ok'
