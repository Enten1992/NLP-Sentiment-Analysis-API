from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format=\"%(asctime)s - %(levelname)s - %(message)s\")

app = FastAPI(
    title=\"Sentiment Analysis API\",
    description=\"A simple API for sentiment analysis using Hugging Face Transformers.\",
    version=\"1.0.0\"
)

# Load pre-trained sentiment analysis model
# Using a smaller, fine-tuned BERT model for efficiency
logging.info("Loading sentiment analysis model...")
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
logging.info("Sentiment analysis model loaded successfully.")

class TextInput(BaseModel:
    text: str

@app.post("/sentiment")
async def analyze_sentiment(text_input: TextInput):
    """
    Analyzes the sentiment of the provided text.
    """
    logging.info(f"Received sentiment analysis request for text: {text_input.text[:50]}...")
    result = sentiment_pipeline(text_input.text)[0]
    sentiment = result["label"]
    score = result["score"]
    logging.info(f"Sentiment analysis complete. Label: {sentiment}, Score: {score:.4f}")
    return {"text": text_input.text, "sentiment": sentiment, "score": score}

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API status.
    """
    return {"status": "ok", "model_loaded": True}
