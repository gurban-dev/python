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

strings = ['one', 'two']
integers = [1, 2, 3]
floats = [1.0, 2.0, 3.0, 4.0]

# When passing strings, integers and floats to zip(), only the first two
# elements from each list are paired, because 'strings' has only two elements.
# The remaining elements of integers (12) and floats (22, 23) are ignored.

'''
The zip() function returns a zip object which is an iterator.

If outputted, the identity of the iterator would be seen. Therefore,
the zip object must be converted to a list data structure, so that
the paired tuples can be seen.'''
print('list(zip(strings, integers):', list(zip(strings, integers)), '\n')

# Since 'integers' was passed as the first argument to the zip() function,
# the items from 'integers' will be positioned first in each of the tuples.
print('list(zip(integers, strings):', list(zip(integers, strings)), '\n')

# Only two tuples will be returned because list 'floats' contains only
# two elements.
print('list(zip(strings, integers, floats):', list(zip(strings, integers, floats)))

# list(zip(strings, integers, floats)) returns [(1, 11, 'one'), (2, 12, 'two')]