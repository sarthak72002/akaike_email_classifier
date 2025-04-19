---
title: Akaike Email Classifier 🚀
emoji: ✉️
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "3.50.2"
app_file: app.py
pinned: false
---

# Akaike Email Classification API 🚀

This project implements an **Email Classification System** that:
- 🔒 Masks Personally Identifiable Information (PII) from incoming support emails.
- 🧠 Classifies emails into predefined categories like Billing Issues, Technical Support, Account Management, etc.
- 🚀 Deploys the full pipeline as an interactive API using Gradio.

---

## 📋 Features

- **Regex + SpaCy NER** based PII masking (without using heavy LLMs)
- **TF-IDF + Logistic Regression** based email classification
- **Gradio Interface** for quick testing and deployment
- Clean structured JSON output showing masked email and detected PII entities

---

## 🛠 Technologies Used

- Python 3.12.9
- Scikit-learn (Model Training & Evaluation)
- SpaCy (Named Entity Recognition)
- Gradio (User Interface Deployment on Hugging Face)
- FastAPI Architecture Principles
- Pandas (Data Handling)

---

## 🚀 Setup Instructions

```bash
# Clone or download the repository

# Optional: Create a virtual environment
python -m venv env
source env/bin/activate  # Linux/macOS
# OR
env\Scripts\activate     # Windows

# Install project dependencies
pip install -r requirements.txt

# Download SpaCy English model
python -m spacy download en_core_web_sm

# (Optional) Re-train the model if needed
python train_models.py

# Launch the Gradio App
python app.py
```
---

## 📤 API Usage

**Input:**
- Email text via Gradio textbox.

**Output:**
- Masked Email
- Predicted Category
- List of Detected Entities (position, type, original text)

---

## 🧠 Author
- Sarthak | Akaike Assignment | 2025
