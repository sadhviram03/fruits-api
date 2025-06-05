from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_fruits():
    response = client.get("/fruits")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_and_read_fruit():
    new_fruit = {"fruit": "banana", "color": "yellow"}
    post_response = client.post("/fruits", json=new_fruit)
    assert post_response.status_code == 200
    fruit_id = post_response.json()["id"]

    get_response = client.get(f"/fruits/{fruit_id}")
    assert get_response.status_code == 200
    assert get_response.json()["fruit"] == "banana"