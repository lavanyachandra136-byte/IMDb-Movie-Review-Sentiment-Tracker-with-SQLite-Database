# IMDb-Movie-Review-Sentiment-Tracker-with-SQLite-Database
🎬 IMDb Movie Review Sentiment Tracker with SQLite Database

A Machine Learning + Flask Web Application that predicts whether a movie review is Positive or Negative using the IMDb dataset.
The system stores user-submitted movie names and their predicted sentiments in an SQLite database and displays results in a clean dashboard.


🚀 Project Overview

This project takes movie reviews, processes them using TF-IDF vectorization, and classifies them using Logistic Regression.
Users can enter any movie name and review through a web interface, and the app shows:

✔ Predicted sentiment

✔ Movie review stored in SQLite

✔ Dashboard showing sentiment statistics (Positive vs Negative)


🧠 Features

✔ Machine Learning model trained on IMDb dataset

✔ Flask web application

✔ SQLite database integration

✔ Dashboard with sentiment graph


🗂 Project Structure

imdb_sentiment_tracker/
│── app.py
│── train_model.py
│── imdb.db
│── IMDb Dataset.csv
│── templates/
│     ├── index.html
│── mode model.pkl
├── vectorizer.pkl

⚙ Technologies Used

Technology	Purpose

Python	Backend & ML
Flask	Web Framework
SQLite	Database
Sklearn	ML model + TF-IDF
HTML/CSS	Frontend

🧪 Model Training

The Machine Learning model is trained in train_model.py:

Loads IMDb Dataset

Cleans and preprocesses text

Converts text → TF-IDF vectors

Trains Logistic Regression classifier

Saves the model and vectorizer using pickle


To train the model:

python train_model.py

▶ How to Run the Application

1️⃣ Install dependencies

pip install flask sklearn pandas numpy

2️⃣ Run the Flask server

python app.py

3️⃣ Open in browser

http://127.0.0.1:5000/


📊 Dashboard

The application shows:

Total movie reviews

Positive reviews count

Negative reviews count

A sentiment bar chart


All data is fetched from SQLite database.
✔ Easy to run locally

✔ Fully open-source
