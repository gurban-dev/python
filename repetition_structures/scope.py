# Indexes/indices
#                 0           1         2         3          4
countries = ['Australia', 'Canada', 'Germany', 'Japan', 'Australia']

# When you use a for loop or a while loop, it means
# that you are looping over an iterable.

# In this case, enumerate(countries) must return an
# iterable.

# 'indexes_for_australia' is globally scoped, meaning that it is
# a variable that can be accessed anywhere in this program.
indexes_for_australia = []

def get_indexes_for_australia(countries):
  # indexes_for_australia is locally scoped because it is
  # defined inside a function.

  # This particular 'indexes_for_australia' is not accessible
  # outside of this function.

  '''
  Upon encountering a variable name, Python looks it up in the following
  order:
  1. Local (inside the current function)
  2. Outer function if nested
  3. Global
  4. Built-in (len, print, etc.)
  '''
  indexes_for_australia = []

  # enumerate() will return both the index and the value
  # of the item in the current iteration.
  for index, value in enumerate(countries):
    print(f"index: {index}, value: {value}")

    if value == 'Australia':
      indexes_for_australia.append(index)
  return indexes_for_australia

print(f'\nget_indexes_for_australia(countries): '
      f'{get_indexes_for_australia(countries)}\n')

for index, value in enumerate(countries):
  # Initialising the empty list inside the for loop
  # would be a mistake, because it resets the list
  # on every iteration.

  # As a result, you would only keep the last match for
  # 'Australia', or none at all.

  # Instead, initialise the list one time before the loop so
  # it can accumulate results properly.

  # Note: Python loops do not have their own scope.
  # Variables declared inside a loop are still accessible
  # after the loop ends.

  # indexes_for_australia = []

  print(f"index: {index}, value: {value}")

  if value == 'Australia':
    indexes_for_australia.append(index)

# In spite of being outside of the for loop, the
# indexes_for_australia variable is still accessible
# because for loops do not have their own scope.
print('\nindexes_for_australia:', indexes_for_australia)

# Scoped globally.
# Will output the last index and value of the final iteration.
print('\nindex:', index)
print('value:', value)