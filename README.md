# NLP-Sentiment-Analysis-API

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.x-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Hugging Face Transformers](https://img.shields.io/badge/Transformers-4.x-orange?style=flat-square&logo=huggingface)](https://huggingface.co/docs/transformers/)
[![Docker](https://img.shields.io/badge/Docker-latest-blue?style=flat-square&logo=docker)](https://www.docker.com/)

A RESTful API for real-time sentiment analysis using advanced Natural Language Processing (NLP) techniques. This project leverages pre-trained transformer models (e.g., BERT, RoBERTa) from the Hugging Face Transformers library to provide endpoints for text classification, entity recognition, and sentiment scoring. It includes a simple web interface for demonstration and is designed for easy deployment with Docker.

## 🌟 Features

- **Real-time Sentiment Analysis:** Analyze text sentiment (positive, negative, neutral) with high accuracy.
- **Transformer Models:** Utilizes state-of-the-art pre-trained models like `distilbert-base-uncased-finetuned-sst-2-english` for efficient inference.
- **FastAPI Backend:** A high-performance, easy-to-use web framework for building robust APIs.
- **Docker Support:** Containerized application for consistent deployment across different environments.
- **Interactive API Documentation:** Automatic interactive API documentation (Swagger UI/ReDoc) provided by FastAPI.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Docker (optional, for containerized deployment)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Enten1992/NLP-Sentiment-Analysis-API.git
    cd NLP-Sentiment-Analysis-API
    ```
2.  Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 📂 Project Structure

```
NLP-Sentiment-Analysis-API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── Dockerfile
├── requirements.txt
├── README.md
```

## 📈 Usage

### 1. Run the API Locally

```bash
cd app
uvicorn main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`. You can view the interactive documentation at `http://127.0.0.1:8000/docs`.

### 2. API Endpoints

- **`/sentiment` (POST):** Analyze the sentiment of a given text.

    **Request Body Example:**
    ```json
    {
      "text": "This is an amazing product! I love it."
    }
    ```

    **Response Example:**
    ```json
    {
      "text": "This is an amazing product! I love it.",
      "sentiment": "POSITIVE",
      "score": 0.999
    }
    ```

### 3. Build and Run with Docker

```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Ethan Reed - ethan.reed.ai@example.com

Project Link: [https://github.com/Enten1992/NLP-Sentiment-Analysis-API](https://github.com/Enten1992/NLP-Sentiment-Analysis-API)
