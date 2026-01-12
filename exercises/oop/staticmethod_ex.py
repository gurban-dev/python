'''
Objective:
Practice using @staticmethod and @classmethod in a
real-world scenario.


Scenario:
You are building a mini system to track books in a library.


Requirements

Create a class Book with:

Instance variables:
title (string)

author (string)

Class variable:

total_books (integer, initially 0)


Methods:
__init__(self, title, author)

Initialises title and author

Increments Book.total_books whenever a new book is created

@classmethod get_total_books(cls)

Returns the total number of books

@staticmethod is_long_book(pages)

Returns True if the number of pages is 500 or more, otherwise False

__str__(self)

Returns a string in the format: "Title: <title>, Author: <author>"


Tasks
Create 3 book instances with different titles and authors.

Print each book to see its details using print(book).

Use Book.get_total_books() to print the total number of
books created.

Use Book.is_long_book(pages) to check if a book with 600
pages is considered long.
'''