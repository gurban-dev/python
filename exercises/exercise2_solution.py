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