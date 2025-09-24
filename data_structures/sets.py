# The built-in set data structure is declared
# with open and closed parentheses.
# items = set([1, 1, 'Venice', 'Venice'])

# If a program attempts to include duplicate values
# inside of a set data structure, the set will
# automatically exclude those duplicate items.
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
items.add('Istanbul')

print('items:', items)