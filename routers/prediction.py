from fastapi import APIRouter
from pydantic import BaseModel
from config import get_config
import joblib


config = get_config()
predict = APIRouter()

def get_model():
    return joblib.load(config.model_file)

class Inference(BaseModel):
    text: str

class Prediction(BaseModel):
    prediction: str


@predict.post("/predict/")
async def classify(inference: Inference) -> Prediction:
    model = get_model()
    p = model.predict([inference.text])
    prediction = "positive" if p == 1 else "negative"
    return Prediction(prediction=prediction)
