"""
The concept or abstract idea of a dictionary:

A dictionary is a collection of data where the
structure of the data is key-value pairs.

Each element in a dictionary has two parts:
a key and a value.

You use a key to locate a specific value.

Key-value pairs are often referred to as mappings
because each key is mapped to a value or corresponds
to a value.

You can create a dictionary by enclosing key-value
pair elements inside a set of curly braces ( {} ).
dict_name = {
  <key>: <value>,
  <key>: <value>
}

An element consists of a key, followed by a colon,
followed by a whitespace character followed by a
value:
'John': 41

The keys of a dictionary do not have to be string
literals like 'John', but remember that they must
be immutable or unchangeable.
"""
integers = {
  1: 'One',
  2: 'Two',
  3: 'Three'
}

"""
To retrieve a value from a dictionary, write
an expression in the following format:
dictionary_name[key]

dictionary_name is the variable that references the
dictionary, and key is the key for one of the key-value
pairs.

If the key exists in the dictionary, the expression
returns the value that is associated with the key.

If the key does not exist, a KeyError exception is
raised.
"""
# print('integers[0]:', integers[0])

print(f'integers[1]: {integers[1]}')

'''
The keys in a dictionary can be of different data
types as long as they are immutable or unchangeable.

The values can also be of different data types.
'''

# 'abc' is a string.
# 999 is an integer.
# (3, 6, 9) is a tuple.
mixed_up = { 'abc': 1, 999: 'yada yada', (3, 6, 9): [3, 6, 9] }

print(f'\nmixed_up: {mixed_up}\n')

# In some programs, an empty dictionary is
# initialised for the purpose of inserting
# elements or key-value pairs later on.
employees = {}

# Python's built-in dict() method is another
# option to pick from when declaring empty
# dictionaries.
managers = dict()