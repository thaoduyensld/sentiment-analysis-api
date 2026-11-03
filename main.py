
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from transformers import pipeline
import logging


MODEL_NAME = (
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sentiment Analysis API",
    description="Analyze English text using Hugging Face DistilBERT",
    version="1.0.0"
)



classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    device=-1
)


class TextInput(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=1000,
        description="English text to analyze"
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Text must not be empty")

        return value


@app.get("/")
def home():
    return {
        "message": "Welcome to Sentiment Analysis API",
        "model": MODEL_NAME,
        "description": "Analyze positive and negative sentiment"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": classifier is not None
    }


@app.post("/predict")
def predict(data: TextInput):
    try:
        result = classifier(data.text)[0]

        return {
            "input": data.text,
            "label": result["label"],
            "score": round(float(result["score"]), 4)
        }

    except Exception:
        logger.exception("Model prediction failed")

        raise HTTPException(
            status_code=500,
            detail="Model prediction failed"
        )
