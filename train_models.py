import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# 1. Load Dataset
df = pd.read_csv("Masked_Email_Classification_Dataset.csv")

# 2. Check columns
print("Dataset Columns:", df.columns.tolist())
# Expected columns: ['masked_email', 'type']

# 3. Use correct columns
X = df['masked_email']    # Input features (masked emails)
y = df['type']            # Target labels (Billing Issues, Technical Support, etc.)

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Build the Pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),          # Text to TF-IDF features
    ('clf', LogisticRegression(max_iter=200))  # Classifier
])

# 6. Train the Model
pipeline.fit(X_train, y_train)
print("✅ Model training completed!")

# 7. Save the Trained Model
# Create Saved_models folder if not exists
os.makedirs("Saved_models", exist_ok=True)

model_path = os.path.join("Saved_models", "email_classifier.pkl")
joblib.dump(pipeline, model_path)
print(f"✅ Model saved at: {model_path}")


