'''
Python's zip() function is a built-in function that takes iterables
(like lists, tuples, or strings), pairs elements from each iterable
by position into tuples and returns an iterator.

The zip() function stops when the shortest input iterable is exhausted.

The number of tuples produced will be equal to the number of items
in the smallest iterable being passed to the zip() function.

The number of items in each tuple in the list, will be equal to the
number of iterables being passed to the zip() function.
'''

text = ['one', 'two']
ints = [1, 2, 3]
floats = [1.0, 2.0, 3.0, 4.0]

# When passing 'text', 'ints' and 'floats' to zip(), only the first two
# elements from each list are paired, because 'text' has only two
# elements.

# The remaining elements of 'ints' (3) and 'floats' (3.0, 4.0) are ignored.

'''
The zip() function returns a zip object which is an iterator.

If printed directly, the zip object itself is shown (not its contents).

Therefore, the zip object must be converted to a list data structure,
so that the paired tuples can be seen.'''
print('list(zip(text, ints):', list(zip(text, ints)), '\n')

# Since 'ints' was passed as the first argument to the zip() function,
# the items from ''ints'' will be positioned first in each of the tuples.
print('list(zip(ints, text):', list(zip(ints, text)), '\n')

# Only two tuples will be returned because 'text' is the shortest list
# and it has two items.
print('list(zip(text, ints, floats):', list(zip(text, ints, floats)))

# list(zip(text, ints, floats)) returns [('one', 1, 1.0), ('two', 2, 2.0)].