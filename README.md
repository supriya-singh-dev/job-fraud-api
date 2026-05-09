# Job Fraud Detection API 🔍

REST API to detect fraudulent job postings using ML — Live on Render

## 🔗 Live Demo
https://job-fraud-api-fszq.onrender.com/docs

## Tech Stack
Python | FastAPI | Scikit-learn | Docker | Render

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API status |
| POST | /predict | Predict fraud |
| GET | /health | Health check |

## Sample Request
{
  "title": "Data Entry Work From Home",
  "description": "Earn 50000 per day, no experience needed..."
}

## Sample Response
{
  "is_fraud": true,
  "fraud_probability": 94.23,
  "result": "FRAUDULENT"
}

## Model Performance
- Accuracy: 98.07%
- Dataset: 18,000+ job postings
- Algorithm: Random Forest + TF-IDF NLP