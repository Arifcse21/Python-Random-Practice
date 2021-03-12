"""
Concerned with storing and retrieving data from a Database

"""
from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as conn:     # Context manager
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS BOOKS(NAME TEXT PRIMARY KEY, AUTHOR TEXT, READ INTEGER)")


def add_book(name, author):
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books VALUES (?, ?, 0)",  (name, author))


def get_all_books():
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books ORDER BY name")
        # books = cursor.fetchall()   # [(name, author, read), (name, author, read)]
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,))


def delete_book(name):
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books where name=?", (name,))













