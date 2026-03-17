'''
Python's zip() function is a built-in function that takes
iterables (like lists, tuples, or strings), pairs elements
from each iterable based on their positions into a tuple,
and returns it.

The zip() function stops when the shortest input iterable
is exhausted.

The number of items in the list will be equal to the number
of items in the smallest iterable being passed to the zip()
function.

The number of items in each tuple in the list, will be equal
to the number of iterables being passed to the zip() function.
'''

x = ['zero', 'one']
y = [10, 11, 12]
z = [20, 21, 22, 23]

# When passing x, y and z to zip(), only the first two elements
# from each list are paired, because 'x' has only two elements.
# The remaining elements of y (12) and z (22, 23) are ignored.

'''
The zip() function returns a zip object which is an iterator.

If outputted, the identity of the iterator would be seen. Therefore,
the zip object must be converted to a list data structure, so that
the paired tuples can be seen.'''
print('list(zip(x, y):', list(zip(x, y)), '\n')

# Since 'y' was passed as the first argument to the zip() function,
# the items from 'y' will be positioned first in each of the tuples.
print('list(zip(y, x):', list(zip(y, x)), '\n')

# Only two tuples will be returned because list 'z' contains only
# two elements.
print('list(zip(x, y, z):', list(zip(x, y, z)))

# list(zip(x, y, z)) returns [(1, 11, 'one'), (2, 12, 'two')]