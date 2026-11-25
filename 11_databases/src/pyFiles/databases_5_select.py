import sqlite3

# connect() opens the database file. If the file does not exist yet,
# SQLite creates it for us. So this one line makes a new database.
conn = sqlite3.connect("shop.db")

# The cursor is the tool we use to send commands to the database.
cursor = conn.cursor()

cursor.execute("SELECT * FROM reviews")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()
print("Database closed.")
