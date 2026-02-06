'''
Python's zip() function is a built-in function that takes iterables (like
lists, tuples, or strings), aggregates or combines their elements into
a tuple, and returns it.

The zip() function stops when the shortest input iterable is exhausted.

The number of items in the list will be equal to the number of items
in the smallest iterable being passed to the zip() function.

The number of items in each tuple in the list, will be equal to the
number of iterables being passed to the zip() function.
'''

x = [1, 2, 3, 4]
y = [11, 12, 13, 14, 15]
z = ['one', 'two']

# 15 will be excluded as it doesn't have another element to be paired up with.

'''
The zip() function returns a zip object which is an iterator.

If outputted, the identity of the iterator would be seen. Therefore, the zip object
must be converted to a list data structure, so that the paired tuples can be seen.'''
print('list(zip(x, y):', list(zip(x, y)))
      
print('list(zip(y, x):', list(zip(y, x)))

# Only two tuples will be returned because list 'z' contains only two elements.
print('list(zip(x, y, z):', list(zip(x, y, z)))

# list(zip(x, y, z)) returns [(1, 11, 'one'), (2, 12, 'two')]