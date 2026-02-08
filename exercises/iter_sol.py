# Concepts:
# Iterators
# An iterator object's .__iter__() method.
# An iterator object's .__next__() method.
# Python's built-in iter() function.
# Python's built-in next() function.

# ------------------------------------------------------------
# 1. Definition
# ------------------------------------------------------------
"""
An iterator is an object that returns values one at a time and
keeps track of its current position in a sequence.

To be an iterator, an object must implement:

1. __iter__()  -> returns the iterator object itself
2. __next__()  -> returns the next item and raises StopIteration
                  when no items remain.
"""

# ------------------------------------------------------------
# 2. Create iterators from different iterables
# ------------------------------------------------------------

print("Creating iterators from different iterables:\n")

lst = [10, 20, 30]
tpl = (1, 2, 3)
string = "ABC"
rng = range(3)
dct = {"a": 1, "b": 2, "c": 3}

list_iterator = iter(lst)
tuple_iterator = iter(tpl)
string_iterator = iter(string)
range_iterator = iter(rng)
dict_iterator = iter(dct)

print('next(list_iterator):', next(list_iterator))
print('next(tuple_iterator):', next(tuple_iterator))
print('next(string_iterator):', next(string_iterator))
print('next(range_iterator):', next(range_iterator))

# Iterates over keys
print('next(dict_iterator):', next(dict_iterator))


# ------------------------------------------------------------
# 3. Using iterator methods directly
# ------------------------------------------------------------

print("\nUsing iterator methods directly:")

nums = [100, 200, 300]
it = iter(nums)

# .__iter__() returns the iterator itself.
print('it.__iter__():', it.__iter__())

# Calling the .__next__() method manually.
print('it.__next__():', it.__next__())
print('it.__next__():', it.__next__())
print('it.__next__():', it.__next__())

try:
  print('it.__next__():', it.__next__())
except StopIteration:
  print("StopIteration raised: Iterator exhausted.")


# ------------------------------------------------------------
# 4. Using next() built-in function
# ------------------------------------------------------------

print("\nUsing next() built-in:")

values = iter([1, 2, 3])

while True:
  try:
    value = next(values)
    print('value:', value)
  except StopIteration:
    print("No more values.")
    break


# ------------------------------------------------------------
# 5. Demonstrating how for-loop uses iterators
# ------------------------------------------------------------

print("\nFor-loop iteration:")

numbers = [7, 8, 9]

for n in numbers:
  print(n)

print("\nEquivalent manual iteration:")

it = iter(numbers)

while True:
  try:
    n = next(it)
    print('n:', n)
  except StopIteration:
    break


# ------------------------------------------------------------
# 6. Custom iterator implementation
# ------------------------------------------------------------

print("\nCustom iterator example:")


class CountUpTo:
  def __init__(self, limit):
    self.limit = limit
    self.current = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.limit:
      raise StopIteration

    value = self.current
    self.current += 1

    return value


counter = CountUpTo(5)

for num in counter:
  print('num:', num)


'''
Learning Outcomes Demonstrated:

Difference between iterable and iterator shown
Creation of iterators using iter()
Retrieval using next()
StopIteration handling demonstrated
For-loop internal mechanics shown
Custom iterator implemented
'''