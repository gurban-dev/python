"""
The concept or abstract idea of a dictionary:

A dictionary is a collection of data where
the structure of the data is key-value pairs.
Each element in a dictionary has two parts:
a key and a value. You use a key to locate a
specific value.

Key-value pairs are often referred to as mappings
because each key is mapped to a value.

You can create a dictionary by enclosing the
elements inside a set of curly braces ( {} ).

An element consists of a key, followed by a
colon, followed by a value:
'John': 41

The keys of a dictionary do not have to be
string literals, but remember that they must
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
dictionary, and key is the key for the element.

If the key exists in the dictionary, the expression
returns the value that is associated with the key.

If the key does not exist, a KeyError exception is
raised.
"""
# print('integers[0]: ', integers[0])

print(f'integers[1]: {integers[1]}')

"""
Suppose you had employees with the following given
names: Chris, Katie, and Joanne.

How could we create a dictionary where the keys
are the names of the employees and the values are
their respective phone numbers?

"""
phonebook = {
  'Chris': '555-1111',
  'Katie': '555-2222',
  'Joanne': '555-3333'
}

"""
When accessing a string literal dictionary key,
in an f-string, the quotation type wrapped around
the f-string cannot be the same as the quotation
type used for access the string literal dictionary
key.
"""
print(f"\nphonebook[\'Chris\']: {phonebook['Chris']}")

# Remember that string comparisons are case sensitive.
# The expression phonebook['chris'] will not locate the
# key 'Chris' in the dictionary.
# print(f'phonebook[\"chris\"]: {phonebook["chris"]}')

# print(f'phonebook[Chris]: {phonebook[Chris]}')

# There is no such key as '555-3333' in the phonebook
# dictionary, so a KeyError exception is raised.
# print(f"phonebook[\'555-3333\']: {phonebook['555-3333']}")

"""
To prevent such an exception, you can use the in
operator to determine whether a key exists in a
dictionary before trying to use it to retrieve a value.
"""
if '555-3333' in phonebook:
  print(f"phonebook[\'555-3333\']: {phonebook['555-3333']}")

# Generates a NameError because Chris is not defined.
# if Chris in phonebook:
#   print(f'phonebook[Chris]: {phonebook[Chris]}')

# The not in operator determines whether
# a key does not exist in a dictionary.
if '555-3333' not in phonebook:
  print('\nKey \'555-3333\' was not found.')

'''
Dictionaries are mutable objects. You can add new
key-value pairs to a dictionary with an assignment
statement in the following general format:

dictionary_name[key] = value
'''
print(f'\nphonebook: {phonebook}')

# Adding a new key-value pair or element
# to the phonebook dictionary.
phonebook['Joe'] = '555-0123'

print(f'\nphonebook: {phonebook}')

"""
You cannot have duplicate keys in a dictionary.
When you assign a value to an existing key, the
new value replaces the existing value as shown
below:
"""
phonebook['Chris'] = '555-4444'

print(f'\nphonebook: {phonebook}')

'''
You can delete an existing key-value pair from a
dictionary with the del statement. Here is the
general format:
del dictionary_name[key]
'''

del phonebook['Chris']

print(f'\nphonebook: {phonebook}')

# Verify that a key 'Chris' exists in the
# phonebook dictionary before attempting to
# delete its pair.
if 'Chris' in phonebook:
  del phonebook['Chris']
else:
  print('\nKey \'Chris\' not found in phonebook.')

# Use the len() function to obtain the number
# of elements inside of a dictionary:
print(f'\nNumber of elements in phonebook: {len(phonebook)}')

'''
The keys in a dictionary can be of different data
types as long as they are immutable or unchangeable.
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

for given_name in phonebook:
  print(f'key: {given_name}, phonebook[\'{given_name}\']: {phonebook[given_name]}')

# Delete all of the elements in a dictionary by
# calling the clear() method on the dictionary.
phonebook.clear()

print(f'\nphonebook: {phonebook}')

'''
The dictionary's get() method obtains the value
associated with a specified key. If the key is
not found, the method does not raise an exception.

The get() method is an alternative to the [] operator,
and instead, it returns a default value.

Format:
dictionary_name.get(key, default)

"dictionary_name" is the name of the dictionary.

"key" is the key to search for in the dictionary.

"default" is the default value to return if "key"
is not found.
'''
print('\nphonebook.get(\'Joe\', \'Entry not found\'):',
  phonebook.get('Joe', 'Entry not found'))