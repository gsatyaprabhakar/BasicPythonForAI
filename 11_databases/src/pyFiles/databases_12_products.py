import sqlite3


with sqlite3.connect("shop.db") as conn:
    cursor = conn.cursor()
    
    # Delete the rows
    cursor.execute("DELETE FROM products")
    
    print(f"Rows deleted: {cursor.rowcount}")

conn.commit()
conn.close()
print("Database closed.")
