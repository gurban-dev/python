# Indices:    0              1
# cities = ['minecraft', 'roblox']

# Indexes:
#          0 or -3    1 or -2       2 or -1
cities = ['Greece', 'Ukraine', 'Switzerland']

# Inclusive index range: -3 to 2

# Accesses the first item in the list 'cities'.
print('cities[0]:', cities[0])

greece = cities[0]

# 'Greece' is an iterable.

# An iterable is a sequence of values.
print('\ngreece:', greece)

# Indexes:
#  012345
# 'Greece'

# How can the first character from 'greece' be extracted?
character_of_greece = 'greece'[0]

print('\ncharacter_of_greece:', character_of_greece)

print('\nitems[0] == \'roblox\':', cities[0] == 'roblox')

# len() returns the number of cities inside a list.
print('\nlen(cities):', len(cities))

# Equality operator (==) checks whether cities[0]
# is equal to 'minecraft'.
if cities[0] == 'minecraft':
  print('The first item is \'minecraft\'.')