# Sentiment Analysis API

A RESTful Web API for English text sentiment analysis, developed using **FastAPI** and a pre-trained **DistilBERT** model from Hugging Face.

This project was developed as part of the **Computational Thinking – Application Programming Interface (API) Lab** at the University of Science, Vietnam National University Ho Chi Minh City.

## 1. Student Information

- **Full Name:** Bùi Thảo Duyên
- **Student ID:** 25127316  
- **University:** University of Science – VNU-HCM
- **Faculty:** Information Technology
- **Course:** Computational Thinking

## 2. Project Overview

This project provides a Web API that analyzes the sentiment of English text and classifies it into one of two categories:

- **POSITIVE:** The text expresses positive sentiment.
- **NEGATIVE:** The text expresses negative sentiment.

The API also returns a confidence score indicating the model's confidence in its prediction.

The system uses FastAPI to handle HTTP requests and Hugging Face Transformers to perform sentiment classification.

## 3. Hugging Face Model

- **Model Name:** DistilBERT Base Uncased Fine-tuned SST-2
- **Model ID:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- **Model URL:** https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- **Task:** Text Classification / Sentiment Analysis
- **Language:** English

DistilBERT is a lightweight version of BERT designed to perform natural language processing tasks efficiently.

The selected model has been fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset for binary sentiment classification.

## 4. Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Hugging Face Transformers
- PyTorch
- Pydantic
- Requests

## 5. Project Structure

```text
sentiment-analysis-api/
├── main.py
├── test_model.py
├── test_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

**File Descriptions:**

- `main.py`: Implements the FastAPI application, loads the model, and defines the API endpoints.
- `test_model.py`: Tests the Hugging Face model independently.
- `test_api.py`: Tests API endpoints using the Python requests library.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: Provides project documentation and usage instructions.
- `.gitignore`: Excludes unnecessary local files from version control.

## 6. Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/thaoduyensld/sentiment-analysis-api.git
cd sentiment-analysis-api
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

On Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

An internet connection is required to download the Hugging Face model during the first execution.

## 7. Running the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The application will be available at:

http://127.0.0.1:8000

Interactive Swagger API documentation:

http://127.0.0.1:8000/docs

## 8. API Endpoints

### 8.1. GET /

Returns basic information about the API and the selected model.

**Example Response:**

```json
{
  "message": "Welcome to Sentiment Analysis API",
  "model": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
  "description": "Analyze positive and negative sentiment"
}
```

### 8.2. GET /health

Checks whether the application is running and the model has been initialized.

**Example Response:**

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 8.3. POST /predict

Accepts English text in JSON format and returns the predicted sentiment and confidence score.

**Request URL:**

```text
http://127.0.0.1:8000/predict
```

**Example Request – Positive Sentiment:**

```json
{
  "text": "I love learning Python!"
}
```

**Example Response:**

```json
{
  "input": "I love learning Python!",
  "label": "POSITIVE",
  "score": 0.9998
}
```

**Example Request – Negative Sentiment:**

```json
{
  "text": "This movie is terrible!"
}
```

**Example Response:**

```json
{
  "input": "This movie is terrible!",
  "label": "NEGATIVE",
  "score": 0.9997
}
```

*Note: Confidence scores are illustrative and may vary depending on the model output.*

## 9. Input Validation and Error Handling

The API validates input data using Pydantic.

The input must:

- Be provided as JSON.
- Contain a required `text` field.
- Contain a string between 1 and 1,000 characters.
- Not consist entirely of whitespace.

**Example Invalid Request:**

```json
{
  "text": ""
}
```

**Expected HTTP Status:** `422 Unprocessable Entity`

The API also handles model inference failures and returns an HTTP `500 Internal Server Error` response when prediction fails.

## 10. API Testing

The API is tested using the Python `requests` library.

Ensure that the FastAPI server is running before executing the tests.

Run:

```bash
python test_api.py
```

The test script includes:

| Test Case | Expected Status |
|---|---|
| GET / | 200 |
| GET /health | 200 |
| POST /predict – Positive input | 200 |
| POST /predict – Negative input | 200 |
| POST /predict – Empty text | 422 |
| POST /predict – Missing text | 422 |

The model can also be tested independently:

```bash
python test_model.py
```

## 11. Demonstration Video

The demonstration video introduces the selected Hugging Face model, explains the source code, demonstrates how to run the application, and tests the API using different inputs.

**Video Link:** https://drive.google.com/file/d/1EFSsp5_Gbj1b8u5M_6x8V6v42eUaUzGJ/view?usp=sharing

## 12. Conclusion

This project demonstrates how to integrate a pre-trained Hugging Face machine learning model into a RESTful Web API using FastAPI.

Through this project, the following concepts were practiced:

- Using pre-trained machine learning models.
- Developing RESTful APIs with FastAPI.
- Handling GET and POST HTTP requests.
- Validating input data with Pydantic.
- Returning structured JSON responses.
- Implementing error handling.
- Testing APIs using Python requests.
- Organizing and documenting a Python project.