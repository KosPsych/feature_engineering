import uvicorn
from fastapi import FastAPI, Request
from endpoints.feature_engineering import *
app = FastAPI()

# curl -X POST http://127.0.0.1:8000/feature_engineering -H "Content-Type: application/json" -d @cvas_data.json

@app.post("/feature_engineering")
async def create_features(request: Request):
    return feature_engineering (await request.json())
