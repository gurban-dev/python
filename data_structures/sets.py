# A set is a mutable, unordered collection of unique elements
# that does not support indexing.

# If you need to initialise an empty set, you must use the built-in
# set() function because then Python will think that you are declaring
# a dictionary.

# Empty set:
# items = set()

# Empty dictionary:
# items = {}

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

# Sets keep only unique elements.
# Two values are considered the same if:
#   - their hashes are equal, and
#   - they compare equal with ==

# Since 1 == 1.0 evaluates to True and hash(1) == hash(1.0) evaluates
# to True, the set treats them as duplicates and keeps only the first
# -one that is included in the set.

# Strings with the same content are also equal,
# so 'Venice' and "Venice" collapse into one element.

# Also, remember that since sets do not supporting indexing,
# you cannot access the first element in a set by doing the
# following:
# print('items[0]:', items[0])

# It is not possible to obtain the first element from a set because
# sets are unordered and have no defined iteration order.

# If you need to access elements via indexing, stick with lists.

print('items:', items)

# Sets are mutable. They can be modified after
# they are initialised.

# The .add() method will add items in a random order to the set.
items.add('Istanbul')

# Attempt to add a duplicate to this set.
items.add("Venice")

# Notice that if you run this program multiple times
# you will eventually see that the items in the set
# are not outputted in the same order.

# This is because unlike lists, sets are unordered.
print('items:', items, '\n')

# However, in the Python interactive shell the items in the same set
# will always be printed in the same order because the same hash table
# is being reprinted, but in a file that hash table is rebuilt on each
# run, so the display order can change.

# A hash table is how Python stores set items so they can be found quickly,
# which is why sets do not keep items in a predictable order.

items.remove("Venice")

print("items after removing \"Venice\":\n", items, sep="")

# A KeyError exception is raised if an item that does not
# exist in a set is attempted to be removed from it.
# items.remove("Athens")

# Membership operator: checks if a value exists in a collection.
print("\n1.0 in items:", 1.0 in items, '\n')

# Insertion, deletion, and lookup are O(1) on average because sets are
# implemented using a hash table. A hash function maps each element to
# a specific index (slot) in an underlying array, allowing direct access
# without scanning the entire collection.

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
print("set(courses) - set(courses_completed):\n",
      set(courses) - set(courses_completed), sep="")