
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os

# Initialize FastAPI app
app = FastAPI(title="NLP Sentiment Analysis API",
              description="A simple API for performing sentiment analysis on text.",
              version="1.0.0")

# Load sentiment analysis pipeline
# You can specify a different model if needed, e.g., "distilbert-base-uncased-finetuned-sst-2-english"
# Ensure the model is downloaded or available offline for production deployment
model_name = os.getenv("SENTIMENT_MODEL", "distilbert-base-uncased-finetuned-sst-2-english")
print(f"Loading sentiment analysis model: {model_name}...")
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
print("Sentiment analysis model loaded successfully.")

class TextInput(BaseModel):
    text: str

@app.get("/", summary="Root endpoint", tags=["Health Check"])
async def read_root():
    return {"message": "Welcome to the NLP Sentiment Analysis API! Visit /docs for API documentation.",
            "status": "healthy"}

@app.post("/analyze_sentiment", summary="Analyze sentiment of text", tags=["Sentiment Analysis"])
async def analyze_sentiment(input: TextInput):
    """
    Analyzes the sentiment of the provided text.

    - **text**: The input text string to analyze.
    """
    try:
        result = sentiment_pipeline(input.text)
        return {"input_text": input.text, "sentiment_result": result[0]}
    except Exception as e:
        return {"error": str(e), "message": "Failed to analyze sentiment."}

if __name__ == "__main__":
    import uvicorn
    # To run this application:
    # uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    # Or directly via Python script (for development/testing):
    print("Starting Uvicorn server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
