import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("reviews.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT,
    review TEXT,
    sentiment TEXT
)
""")

print("Database and table created successfully!")

conn.commit()
conn.close()
