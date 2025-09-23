'''
Exercise 2

Write a program that:

Creates a list of your top 5 favorite movies.

Converts the list into a tuple (so it cannot be changed).

Creates a dictionary where the key is the movie title
and the value is the release year.

Prints:

The first movie in the list

The last movie in the tuple

All the keys (movie titles) in the dictionary

💡 Hint: Use .keys() to get dictionary keys.
'''

def movie():
  user_input = input(
    "Enter a list of your top five favourite movies " \
    "with a comma between them:\n")

  user_list = user_input.split(",")

  user_tuple = tuple(user_list)

  movie_dates = input(
    "\nEnter the list of the release dates for the" \
    " corresponding\nmovies with a comma separating them:\n")
  dates_list = movie_dates.split(",")

  movie_dictionary = dict(zip(user_list, dates_list))

  print(f"\nFirst movie in list: {user_list[0]}")
  print(f"Last movie in the tuple: {user_tuple[4]}")

  print('\n', movie_dictionary.keys())

movie()