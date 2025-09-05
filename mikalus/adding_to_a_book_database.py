"""
EXERCISE - ADDING TO A BOOK DATABASE

You are given a dictionary with the names of authors as keys
and dictionaries as corresponding values. In the subdictionary,
each value is the title of a book published by the author, and
each key is the year in which that specific book was published.

You are also given the name of another author, which is stored
in a variable, and the titles of some books he / she wrote. For 
every book, you are also given the year in which it was published.

The exercise is to include the data that is not yet included in
the dictionary stored in variable 'books' in the same way as the
other data is stored in the dictionary.
"""
books = {
    "J.K. Rowling": {1997: "Harry Potter and the Philosopher's Stone",
                     1998: "Harry Potter and the Chamber of Secrets", 
                     1999: "Harry Potter and the Prisoner of Azkaban",
                     2000: "Harry Potter and the Goblet of Fire"},
    "George Orwell": {1933: "Down and Out in Paris and London",
                      1934: "Burmese Days", 1935: "A Clergyman's Daughter"},
    "Gabriel Garcia Marquez": {1967: "One Hundred Years of Solitude",
                               1975: "The Autumn of the Patriarch", 
                               1985: "Love in the Time of Cholera"}
}

Author = "Stephen King"
book1_by_author = "Knightriders, 1981"
books_by_author = ["Creepshow, 1982", "Cat's Eye, 1985", "Silver Bullet, 1985"]

print(books)

# Append book1_by_author.

books_by_author.append(book1_by_author)

print(f'books_by_author: {books_by_author}')

stephen_king_dict = {}

# Separate the year and the title.
for book_by_author in books_by_author:
	# Finding the index of the comma in each string.
	index = book_by_author.find(",")

	# Slicing the string up to the index
	book_name = book_by_author[:index]

	year_published_as_int = int(book_by_author[-4:])

	print('book_name:', book_name)

	print('year_published_as_int:', year_published_as_int, '\n')

	print('type(year_published_as_int):', type(year_published_as_int), '\n')
     
	if year_published_as_int not in stephen_king_dict:
		stephen_king_dict[year_published_as_int] = book_name
	else:
		stephen_king_dict[year_published_as_int] += ", " + book_name

sorted_stephen_king_dict = dict(sorted(stephen_king_dict.items()))

print(f'sorted_dict: {sorted_stephen_king_dict}')

books[Author] = sorted_stephen_king_dict

print('\nbooks dictionary:')
for key, value in books.items():
  print(key, value)