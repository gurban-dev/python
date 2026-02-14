from collections import defaultdict

movies = [
  "The Matrix",
  "Gladiator",
  "Inception",
  "The Dark Knight",
  "Interstellar"
]

movies_tuple = tuple(movies)

movies_dict = {
  "The Matrix": 1999,
  "Gladiator": 2000,
  "Inception": 2010,
  "The Dark Knight": 2008,
  "Interstellar": 2014
}

print("First movie in the list:", movies[0])

print("\nLast movie in the tuple:", movies_tuple[-1])

print("\nAll movie titles in the dictionary:\n", movies_dict.keys())

# Reverse the list named movies.
# sequence[start:stop:step]
# movies is the sequence.

# Start from the end.
# Stop at the beginning.
# Step is -1
movies = movies[::-1]

# Start from the beginning.
# Stop at the end.
# Step is 1.
movies = movies[::1]

print('\nmovies:', movies)

print('\nLoop through movies')
for movie in movies:
  print(movie, end=", ")
  # print('movie:', movie)
print('\n')

# dict_movies = {}

# A defaultdict() automatically provides a default value
# whenever a nonexistent key is accessed, preventing a
# KeyError and ensuring the program continues smoothly.

# In this case, an empty str is the default value.
dict_movies = defaultdict(str)

print('\ntype(dict_movies):', type(dict_movies))

for index, movie in enumerate(movies):
  print(f'index: {index}, movie: {movie}')
  # print('movie:', movie)

  # On each iteration, add a key-value pair to dict_movies:
  dict_movies[index] = movie

print('\ndict_movies:\n', dict_movies, sep='', end='\n')

# -1 does not exist as a key in the dictionary dict_movies.
# Raises a KeyError.
print('\ndict_movies[-1]:', dict_movies[-1])

print('\nmovies:\n', movies, sep='')