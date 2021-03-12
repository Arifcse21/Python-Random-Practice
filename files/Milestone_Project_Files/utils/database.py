"""
Concerned with storing and retrieving data from a file

Format of the json  file:
[
    {
        'name': 'Book Name',
        'author' : 'Author name',
        'read' : True
    },
    {
        name': 'Book Name',
        'author' : 'Author name',
        'read' : True
    },

]
"""
import json

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    with open(books_file, 'a') as file:
        books = get_all_books()
        books.append({'name': name, 'author': author, 'read': False})
        _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)














