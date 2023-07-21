import uvicorn
from fastapi import FastAPI, Request, Form
from endpoints.feature_engineering import *
from endpoints.dimensionality_reduction import *
import logging
import os


log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs', 'app.log'))

# For example, to read the log file:
with open(log_file_path, 'r') as log_file:

    # Logging Configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file_path,
        filemode="a"
    )


app = FastAPI()

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
