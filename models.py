import joblib
import os

# Model path
MODEL_PATH = os.path.join("Saved_models", "email_classifier.pkl")

def load_model():
    """Load the trained pipeline"""
    return joblib.load(MODEL_PATH)

def predict_category(pipeline, email_text: str):
    """Predict the category of an email"""
    return pipeline.predict([email_text])[0]

