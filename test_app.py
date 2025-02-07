import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=5&b=10')
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}

def test_invalid_input(client):
    response = client.get('/add?a=abc&b=10')
    assert response.status_code == 400

def test_divide_by_zero(client):
    response = client.get('/divide?a=10&b=0')
    assert response.status_code == 400
