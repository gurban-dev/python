countries = ['Australia', 'Canada', 'Germany', 'Japan', 'Australia']

# When you use a for loop or a while loop, it means
# that you are looping over an iterable.

# In this case, enumerate(countries) must return an
# iterable.

# Global scope, meaning that indexes_for_australia
# is a variable that can be accessed anywhere in
# this program.
# indexes_for_australia = []

def get_indexes_for_australia(countries):
  indexes_for_australia = []

  # enumerate() will return both the index and the value
  # of the item in the current iteration.
  for index, value in enumerate(countries):
    # Intialise an empty list.
    # Local scope, meaning that indexes_for_australia
    # can only be accessed within this function.
    indexes_for_australia = []

    print(f"index: {index}, value: {value}")

    if value == 'Australia':
      indexes_for_australia.append(index)
  return indexes_for_australia

print(f'get_indexes_for_australia(countries):'
      f'{get_indexes_for_australia(countries)}')

for index, value in enumerate(countries):
  # Initialising the empty list inside the for loop
  # would be a mistake, because it resets the list
  # on every iteration.
  # As a result, you would only keep the last match for
  # 'Australia', or none at all.

  # Instead, initialise the list once before the loop so
  # it can accumulate results properly.

  # Note: Python loops do not have their own scope.
  # Variables declared inside a loop are still accessible
  # after the loop ends.

  indexes_for_australia = []

  print(f"index: {index}, value: {value}")

  if value == 'Australia':
    indexes_for_australia.append(index)

print('indexes_for_australia:', indexes_for_australia)