import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

# Dataset load karo (tumhara existing dataset use karo)
df = pd.read_csv("fake_job_postings.csv")
df["text"] = df["title"].fillna("") + " " + df["description"].fillna("")
df = df[["text", "fraudulent"]].dropna()

X = df["text"]
y = df["fraudulent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline banao
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)
print(f"Accuracy: {pipeline.score(X_test, y_test):.4f}")

# Model save karo
joblib.dump(pipeline, "model/fraud_model.pkl")
print("Model saved!")