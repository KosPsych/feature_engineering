import uvicorn
from fastapi import FastAPI, Request, Form
from endpoints.feature_engineering import *
from endpoints.dimensionality_reduction import *
import logging



# Logging Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="../logs/app.log",
    filemode="a"
)


app = FastAPI()

# curl -X POST http://127.0.0.1:8000/feature_engineering -H "Content-Type: application/json" -d @cvas_data.json -o f_e_result.json

# curl -X POST http://127.0.0.1:8000/dimensionality_reduction?target=amount -H "Content-Type: application/json" -d @f_e_result.json -o reduced.json

# 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

# Feature engineering
@app.post("/feature_engineering")
async def create_features(request: Request):
    logging.info("feature_engineering endpoint accessed.")
    return feature_engineering (await request.json())


# Dimensionality_reduction
@app.post("/dimensionality_reduction")
async def reduce_dimensions(request: Request, target: str):
    logging.info("dimensionality_reduction endpoint accessed.")
    return dimensionality_reduction (await request.json(), target)


# simple healthcheck Endpoint
@app.get("/healthcheck")
def healthcheck():
    logging.info("healthcheck endpoint accessed.")
    return {'status': 'UP'}
