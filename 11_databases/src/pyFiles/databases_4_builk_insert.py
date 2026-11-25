import sqlite3

# connect() opens the database file. If the file does not exist yet,
# SQLite creates it for us. So this one line makes a new database.
conn = sqlite3.connect("shop.db")

# The cursor is the tool we use to send commands to the database.
cursor = conn.cursor()

more_reviews = [
    ("Delivery was very late and food was cold.", "negative", 1),
    ("Good taste, fair price.", "positive", 4),
    ("It was okay, nothing special.", "neutral", 3),
    ("App kept crashing during payment.", "negative", 2),
]

cursor.executemany(
    "INSERT INTO reviews (text, label, score) VALUES (?, ?, ?)",
    more_reviews
)
conn.commit()

print("Added", len(more_reviews), "more reviews.")


conn.close()
print("Database closed.")
