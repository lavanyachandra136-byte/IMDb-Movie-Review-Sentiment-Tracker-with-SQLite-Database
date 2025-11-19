import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load IMDb dataset
df = pd.read_csv("IMDB Dataset.csv")

# Convert sentiment to numerical (pos = 1, neg = 0)
df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['sentiment'], test_size=0.2, random_state=42
)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)

# Fit transform
X_train_vec = vectorizer.fit_transform(X_train)

# Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train_vec, y_train)

print("Training complete!")

# Save model + vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model saved as model.pkl")
print("Vectorizer saved as vectorizer.pkl")
