'''
Python's zip() function is a built-in function
that takes iterables (like lists, tuples, or
strings), aggregates or combines their elements
into a tuple, and return it.

The zip() function stops when the shortest
input iterable is exhausted.
'''

x = [1, 3, 5, 7]
y = [2, 4, 6, 8, 9]
z = ['one', 'two']

# 9 will be excluded as it doesn't have
# another element to be paired up with.

'''
zip(x, y) returns a zip object which is an
iterator. If outputted, the memory address
of the iterator would be seen. Therefore,
the zip object must be converted to a list
data structure, so that the paired tuples
can be seen.'''
print('list(zip(x, y):', list(zip(x, y)))
      
print('list(zip(y, x):', list(zip(y, x)))

# Only two tuples will be returned because
# list z contains only two elements.
print('list(zip(x, y, z):', list(zip(x, y, z)))