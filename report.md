# 📄 Akaike Email Classification Report

---

## 1. Introduction to the Problem Statement

The aim of this project is to build a production-ready **Email Classification System** for a support team. The system must:
- **Mask Personal Identifiable Information (PII)** such as email addresses, phone numbers, and Aadhar numbers before processing.
- **Classify** the masked email into predefined categories like "Billing Issues", "Technical Support", or "Account Management".
- **Expose the solution** as a Gradio-powered API suitable for deployment on Hugging Face Spaces.

The system must ensure data privacy compliance, accuracy in classification, and scalability.

---

## 2. Approach Taken for PII Masking and Classification

### PII Masking
- **Regex-Based Matching**: Designed regex patterns for structured PII fields like emails, phone numbers, Aadhar, credit/debit numbers.
- **spaCy NER**: Used SpaCy's en_core_web_sm model to detect names (PERSON entities).
- **Masking Logic**: Each detected PII instance is replaced by a placeholder like `[email]`, `[full_name]`, `[phone_number]`, preserving text positions.

### Email Classification
- **Feature Extraction**: Applied TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert email text into numeric features.
- **Model Selection**: Chose Logistic Regression for its interpretability, speed, and robust multi-class classification performance.
- **Training Dataset**: Utilized a masked email dataset with labels provided in "Masked_Email_Classification_Dataset.csv".

---

## 3. Model Selection and Training Details

- **Model Type**: Logistic Regression (One-vs-Rest classifier internally).
- **Vectorizer**: TfidfVectorizer (default parameters).
- **Train/Test Split**: 80% Training, 20% Testing.
- **Evaluation Metrics**:
  - Accuracy
  - Precision, Recall, F1-Score

- **Saved Model**: Persisted trained pipeline (vectorizer + classifier) as `Saved_models/email_classifier.pkl` using joblib.
- **API Format**: Gradio interface accepting input text, masking PII, classifying, and returning JSON output.

---

## 4. Challenges Faced and Solutions Implemented

### Challenges:
- **Multiple overlapping PII matches** could cause masking position conflicts.
- **Dataset not having masked emails** initially caused key errors.
- **Dependency conflicts** during setup (e.g., numpy, spacy, langchain versions).
- **Deployment Adjustments**: Hugging Face Spaces needed Gradio-specific app structure.

### Solutions:
- **Masked first, then classified**: Ensured text position indexes were consistent after masking.
- **Adjusted code to work with available columns**: Used "email" or "masked_email" dynamically.
- **Created a Clean Virtual Environment**: Installed only minimal necessary libraries.
- **Simplified API Design**: Used standalone Gradio app instead of full FastAPI server to match Hugging Face deployment best practices.

---

# ✅ Final System
- Real-time Email Masking
- Category Prediction
- JSON Structured Output
- Deployable on Hugging Face Spaces 🚀

---

# 🧠 Prepared by
- Sarthak | Akaike Assignment 2025

