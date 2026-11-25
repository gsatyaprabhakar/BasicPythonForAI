'''
## Exercise

A small shop wants to store its products in a database.

1. Create a table called `products` with columns `id`, `name` (TEXT), and `price` (INTEGER).
2. Add at least 3 products (for example Tea, 10).
3. Read and print all products.
4. Bonus print only the products with a price greater than 20 (hint `WHERE price  `).

Tip you can reuse `shop.db` from above — a database can hold many tables.
'''
import sqlite3
from sqlite3 import Connection, Cursor

class Products:

    def get_connectio(db_name:str) -> Connection :

        return sqlite3.connect(db_name)

    
    def create_table(connection:Connection, table_ddl:str) -> Cursor:
        cursor = connection.cursor()
        
        return cursor.execute(table_ddl)

    
    def insert_records(connection:Connection, insert_query:str, values_list:list) -> Cursor:
        cursor = connection.cursor()
        cursor.executemany(
            insert_query,
            values_list
        )

        return connection.commit()

    
    def select_all_records(connection:Connection, select_query:str) -> list:
        cursor = connection.cursor()
        cursor.execute(select_query)

        return cursor.fetchall()

    
    def select_records(connection:Connection, select_query:str, value:int) -> list:
        cursor = connection.cursor()
        cursor.execute(select_query, (value,))

        return cursor.fetchall()
