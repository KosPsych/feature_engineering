import uvicorn
from fastapi import FastAPI, Request
from endpoints.feature_engineering import *
from endpoints.healthcheck import *
app = FastAPI()

# curl -X POST http://127.0.0.1:8000/feature_engineering -H "Content-Type: application/json" -d @cvas_data.json


# Feature engineering
@app.post("/feature_engineering")
async def create_features(request: Request):
    return feature_engineering (await request.json())

# simple healthcheck Endpoint
@app.get("/healthcheck")
def healthcheck():
    return {'status': 'UP'}
