'''
## Exercise

A small shop wants to store its products in a database.

1. Create a table called `products` with columns `id`, `name` (TEXT), and `price` (INTEGER).
2. Add at least 3 products (for example Tea, 10).
3. Read and print all products.
4. Bonus print only the products with a price greater than 20 (hint `WHERE price  `).

Tip you can reuse `shop.db` from above — a database can hold many tables.
'''
from databases_7_Exercise_products_dao import Products

products_ddl ="""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
"""

products_insert = "INSERT INTO products (name, price) VALUES (?, ?)"

products_details = [
    ("Tea", 15),
    ("Green Tea", 20),
    ("Lemon Tea", 15),
    ("COffee", 20),
    ("Biscuit", 5),
    ("Bun", 10),
    ("Idle", 40),
    ("Dosa", 60),
    ("Wada", 70),
]

products_select = "SELECT * FROM products"


print("Creating Connection")
connection = Products.get_connectio("shop.db")
print("Connection Created !!!")
print()


print("Creating Table")
Products.create_table(connection, products_ddl)
print("Table Created !!!")
print()


print("Inserting Records")
Products.insert_records(connection, products_insert, products_details)
print("Records Inserted !!!")
print()


print("Fetching All Records")
records = Products.select_all_records(connection, products_select)
print("Records Fetched !!!")
print()

print("Records Are:")
for rec in records:
    print(rec)
print()


print("Commit")
connection.commit()
print("Commited !!!")
print()


print("Closing Connection")
connection.close()
print("Connection Closed !!!")
print()
