# The built-in set data structure can be declared
# with the set() function so long as a list is passed
# to it as an argument.
# items = set([1, 1, 'Venice', 'Venice'])

# items = set(list([1, 1, 'Venice', 'Venice']))

# If a program attempts to include duplicate values
# inside of a set data structure, the set will
# internally or implicitly exclude those duplicate
# items.
items = {1, 1, 'Venice', 'Venice'}

# Also, remember that sets do not supporting indexing.
# Unlike a list, you cannot access the first element
# in a set by doing the following:
# print('items[0]:', items[0])

# If you need to access elements via indexing, stick
# with lists.

print('items:', items)

# Sets are mutable. They can be modified after
# they are initialised.

# The .add() method will add items in a random
# order to the set.
items.add('Istanbul')

print('items:', items)