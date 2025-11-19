import sqlite3

# Database open chestunnam
conn = sqlite3.connect("reviews.db")
cur = conn.cursor()

# Table nundi anni rows tiskuntunnam
cur.execute("SELECT * FROM reviews")

data = cur.fetchall()

# Data print
for row in data:
    print(row)
cur.execute("DELETE FROM reviews")   

conn.close()
