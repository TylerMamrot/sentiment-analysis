"""
Main server that serves model predictions and trains classifier
"""

from fastapi import FastAPI
import joblib

from routers import predict

app = FastAPI()


app.include_router(predict)


@app.get("/")
def root():
    return {"message": "hey this works"}
