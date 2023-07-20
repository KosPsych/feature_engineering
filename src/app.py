import uvicorn
from fastapi import FastAPI, Request
from endpoints.feature_engineering import *
from endpoints.dimensionality_reduction import *


app = FastAPI()

# curl -X POST http://127.0.0.1:8000/feature_engineering -H "Content-Type: application/json" -d @cvas_data.json

# curl -X POST http://127.0.0.1:8000/dimensionality_reduction -H "Content-Type: application/json" -d @new.json


# Feature engineering
@app.post("/feature_engineering")
async def create_features(request: Request):
    return feature_engineering (await request.json())


# Dimensionality_reduction
@app.post("/dimensionality_reduction")
async def reduce_dimensions(request: Request):
    return dimensionality_reduction (await request.json())



# simple healthcheck Endpoint
@app.get("/healthcheck")
def healthcheck():
    return {'status': 'UP'}
