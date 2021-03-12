"""
Concerned with storing and retrieving data from a Database

"""
import sqlite3


def create_book_table():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS BOOKS(NAME TEXT PRIMARY KEY, AUTHOR TEXT, READ INTEGER)")
    conn.commit()
    conn.close()


def add_book(name, author):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books VALUES (?, ?, 0)",  (name, author))
    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY name")

    # books = cursor.fetchall()   # [(name, author, read), (name, author, read)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    conn.close()

    return books


def mark_book_as_read(name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET read=1 WHERE name=?",(name,))
    conn.commit()
    conn.close()


def delete_book(name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books where name=?", (name,))
    conn.commit()
    conn.close()













