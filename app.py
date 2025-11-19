from flask import Flask, request, render_template
import sqlite3
import pickle
import matplotlib.pyplot as plt
import io
import base64

# Load model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__ )

# Function to insert review + prediction into DB
def save_to_database(movie, review, sentiment):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO reviews (movie_name, review, sentiment) VALUES (?, ?, ?)",
                (movie, review, sentiment))
    conn.commit()
    conn.close()

# Function to get all sentiments for a movie
def get_movie_sentiments(movie):
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("SELECT sentiment FROM reviews WHERE LOWER(movie_name) LIKE LOWER(?)", ('%'+movie+'%',))
    rows = cur.fetchall()
    conn.close()

    sentiments = [row[0] for row in rows]
    return sentiments

@app.route("/", methods=["GET", "POST"])
def index():
    chart_url = None
    prediction = None

    if request.method == "POST":
        movie_name = request.form["movie"]
        review_text = request.form["review"]

        # Convert text → vector
        review_vec = vectorizer.transform([review_text])

        # Predict
        pred = model.predict(review_vec)[0]
        prediction = "Positive" if pred == 1 else "Negative"

        # Save to DB
        save_to_database(movie_name, review_text, prediction)

        # Generate graph
        sentiments = get_movie_sentiments(movie_name)
        pos = sentiments.count("Positive")
        neg = sentiments.count("Negative")

        plt.figure(figsize=(5, 4))
        plt.bar(["Positive", "Negative"], [pos, neg])
        plt.title(f"Sentiment Analysis for {movie_name}")

        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        chart_url = base64.b64encode(img.getvalue()).decode()

    return render_template("index.html", prediction=prediction, chart_url=chart_url)

if __name__ == "__main__":
    app.run(debug=True)