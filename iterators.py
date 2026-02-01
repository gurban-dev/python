# An iterator is an object that produces a value one at a
# time while keeping track of where it is in a sequence.

# Instead of producing all values at once, an iterator
# yields the next value when requested.

# An object is an iterator if it implemenets two methods:
# .__iter__()
# .__next__()

nums = [1, 2, 3]

# Instruct Python to create a list iterator object.
it = iter(nums)

# -Return the identity of the object.
print('it.__iter__():', it.__iter__())

# Return the next value in the sequence.
print('it.__next__():', it.__next__())

# for i in range(len(nums)):
#   print(f'Iteration {i+1}:\nnext(it): {next(it)}\n')