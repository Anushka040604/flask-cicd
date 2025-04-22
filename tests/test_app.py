import pytest
from app.app import app  # Assuming 'app.py' is in the 'app' folder

@pytest.fixture
def client():
    """Fixture to provide a test client for the Flask app"""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_health(client):
    """Test the health route"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()  # Parse JSON response
    assert json_data['status'] == "OK"
