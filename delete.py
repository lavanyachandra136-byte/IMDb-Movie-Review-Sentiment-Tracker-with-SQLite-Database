import sqlite3

conn = sqlite3.connect("reviews.db")
cur = conn.cursor()

cur.execute("DELETE FROM reviews")  # All rows delete
conn.commit()
conn.close()

print("All data deleted!")