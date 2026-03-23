# An iterator is an object that produces a value one at a time
# while keeping track of its current position in a sequence.

# Instead of producing all values at once, an iterator yields
# the next value in a sequence only when requested.

# An object is considered an iterator if it implements the following
# two methods:
# 1. .__iter__() -> returns the iterator object itself
# 2. .__next__() -> returns the next value, raises StopIteration when
#                   there aren't any items left in the sequence to yield

nums = [1, 2, 3]

# The iter() function returns an iterator object for the iterable you
# pass to it.

# Create a list iterator object from the list 'nums'.
# This iterator keeps track of its position in the list.
it = iter(nums)

# Invoking the .__iter__() method on the iterator returns the iterator
# object itself.

# The "address-looking" part in the printed output comes from the
# iterator's default .__repr__() method, not the __iter__() method
# itself.
print('it.__iter__():', it.__iter__())

# Return the unique identifier/identity of the iterator object
# as an integer.

# In the CPython implementation of Python, this is typically the
# memory address of the object.
print('\nid(it):', id(it), '\n')

# Return the next value in the sequence.
# print('it.__next__():', it.__next__())

# Calling .__iter__() on an iterator returns the iterator object itself.

# This remains true even after advancing the iterator with .__next__().

# The returned object is the same iterator, not a new one.
print('it.__iter__():', it.__iter__(), '\n')

# print('it.__next__():', it.__next__())

# A for loop implicitly creates an iterator from the iterable and
# repeatedly calls next() on it to yield items one by one.

# Here, the iterator is being manually advanced using Python's built-in
# next() function inside the body of the for loop.
for i in range(len(nums)):
	print(f'Iteration {i+1}:\nnext(it): {next(it)}\n')