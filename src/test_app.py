from fastapi.testclient import TestClient
from app import app
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = TestClient(app)

# testing feature_engineering
def test_feature_engineering():
    # URL of the API endpoint where you want to send the POST request
    path = os.environ.get('original_path')
    # Load the JSON data from the file and convert it to a dictionary

    with open(path, "r") as file:
        json_data = json.load(file)

    response = client.post("/feature_engineering", json=json_data)
    assert response.status_code == 200

# testing healthcheck
def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {'status': 'UP'}

# testing dimensionality_reduction
def test_dimensionality_reduction():

    # URL of the API endpoint where you want to send the POST request
    path = os.environ.get('fe_path')
    # Load the JSON data from the file and convert it to a dictionary

    with open(path, "r") as file:
        json_data = json.load(file)

    response = client.post("/dimensionality_reduction?target=amount", json=json_data)
    assert response.status_code == 200
