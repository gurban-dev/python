'''
Concepts:
Instance variables
Class variables

Exercise: Tracking Library Books

You are building a library management system for a small community library.

Each time a book is created in the system, the library wants to keep track
of the total number of books registered.

Requirements

Create a class called Book.

The class should have:

A class-level variable called total_books that tracks how many books have
been created.

Each book instance should store:
title

author


Every time a new Book object is created:

The total_books count should automatically increase by 1.

Create a function called print_total_books that prints the total number
of books currently registered.

Call print_total_books after creating several Book objects to verify
that the count updates correctly.


Example Usage (Expected Behavior)
b1 = Book("1984", "George Orwell")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("Dune", "Frank Herbert")

print_total_books()
'''