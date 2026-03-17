class Book:

    # Class variable (shared by all Book objects).
    total_books = 0

    def __init__(self, title, author):
        # Instance variables (specific to each book).
        self.title = title
        self.author = author

        # Increase the class variable each time a Book is created.
        Book.total_books += 1


# Function to print the total number of books.
def print_total_books():
    print("Total books registered:", Book.total_books)


b1 = Book("1984", "George Orwell")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("Dune", "Frank Herbert")

print_total_books()