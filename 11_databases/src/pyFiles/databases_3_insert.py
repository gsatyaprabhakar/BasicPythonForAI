import sqlite3

# connect() opens the database file. If the file does not exist yet,
# SQLite creates it for us. So this one line makes a new database.
conn = sqlite3.connect("shop.db")

# The cursor is the tool we use to send commands to the database.
cursor = conn.cursor()

print("Database is ready!")

cursor.execute(
    "INSERT INTO reviews (text, label, score) VALUES (?, ?, ?)",
    ("The biryani was amazing!", "positive", 5)
)

# commit() actually saves the change to the file. Without it, nothing is saved.
conn.commit()

print("One review saved.")


conn.close()
print("Database closed.")
