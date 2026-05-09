from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# App create karo
app = FastAPI(
    title="Job Fraud Detection API",
    description="Detects fraudulent job postings using ML",
    version="1.0.0"
)

# Model load karo
model = joblib.load("model/fraud_model.pkl")

# Input format define karo
class JobPosting(BaseModel):
    title: str
    description: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "Job Fraud Detection API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict(job: JobPosting):
    text = job.title + " " + job.description
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0]

    return {
        "title": job.title,
        "is_fraud": bool(prediction),
        "fraud_probability": round(float(probability[1]) * 100, 2),
        "result": "FRAUDULENT" if prediction == 1 else "LEGITIMATE"
    }

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}