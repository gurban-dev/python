class Book:
	# Class variable.
	total_books = 0

	def __init__(self, title, author):
		# Instance variables.
		self.title = title
		self.author = author

		# Increment total_books whenever a new book is created.
		Book.total_books += 1

	@classmethod
	def get_total_books(cls):
		return cls.total_books

	@staticmethod
	def is_long_book(pages):
		return pages >= 500

	def __str__(self):
		return f"Title: {self.title}, Author: {self.author}"
	
	def __repr__(self):
		return f"Title: {self.title}, Author: {self.author}"

# ---- Creating book instances ----

book1 = Book("War and Peace", "Leo Tolstoy")
book2 = Book("Crime and Punishment", "Fyodor Dostoevsky")

# ---- Printing book details ----

print(book1)
print(book2)

# ---- Printing total number of books ----

print("Total books:", Book.get_total_books())

# ---- Checking if a book is long ----

print("book1.is_long_book(399):", book1.is_long_book(399))

books = [book1, book2]

# Question:
# Why does adding a __repr__() method reveal the details of
# each object in a list?

# Answer:
# Printing a list invokes the list's built-in __repr__() method.
# This method calls repr() on each element in the list, which in
# turn invokes each element's __repr__() method.

# By defining a __repr__() method in the Book class, that method
# overrides the default __repr__() method for Book objects.