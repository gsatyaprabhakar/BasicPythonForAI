import sqlite3

# connect() opens the database file. If the file does not exist yet,
# SQLite creates it for us. So this one line makes a new database.
conn = sqlite3.connect("shop.db")

# The cursor is the tool we use to send commands to the database.
cursor = conn.cursor()

print("Database is ready!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        text TEXT,
        label TEXT,
        score INTEGER
    )
""")

print("Table created!")


conn.close()
print("Database closed.")
