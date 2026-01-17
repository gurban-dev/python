# The built-in set data structure can be declared with
# the set() function so long as a list is passed to it
# as an argument.
items = set([1, 1, 'Venice', 'Venice'])

items = set(list([1, 1, 'Venice', 'Venice']))

# If a program attempts to include duplicate values
# inside of a set data structure, the set will
# internally or implicitly exclude those duplicate
# values.
items = {1.0, 1.0, 1, 1, 'Venice', "Venice"}

# In the case of 1.0 and 1, the set considers these to be
# duplicates because they are equal to each other:
# 1 == 1.0 returns True

# Since 1.0 is encountered first when the set is constructed, it is
# added to the set.

# When 1 is later encountered, Python sees that it has the same hash
# as 1.0. A hash is an integer value produced by the hash() function
# and is used by hash-based collections (like sets and dictionary keys)
# to quickly group and look up values.

# Since 1 and 1.0 produce the same hash and the equality check
# (1 == 1.0) evaluates to True, Python treats 1 as a duplicate
# of 1.0 and discards it.

# Also, remember that sets do not supporting indexing.
# Unlike a list, you cannot access the first element
# in a set by doing the following:
# print('items[0]:', items[0])

# It is not possible to obtain the first element from a set because
# sets are unordered and have no defined iteration order.

# If you need to access elements via indexing, stick
# with lists.

print('items:', items)

# Sets are mutable. They can be modified after
# they are initialised.

# The .add() method will add items in a random
# order to the set.
items.add('Istanbul')

# Attempt to add a duplicate to this set.
items.add("Venice")

# Notice that if you run this program multiple times
# you will eventually see that the items in the set
# are not outputted in the same order.

# This is because unlike lists, sets are unordered.
print('items:', items)

# The set difference operator.

courses = [
  "Data Structures & Algorithms",
  "Object-oriented Programming",
  "Database Design"
]

courses_completed = [
  "Database Design"
]

# To find the difference between two lists, convert them to sets
# using set(), then apply the set difference operator (-).
print("set(courses) - set(courses_completed):",
      set(courses) - set(courses_completed))