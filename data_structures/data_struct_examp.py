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
Inside of an f-string, make sure the opposite type of quotation
marks are used than the one that declared the f-string (e.g., use
double quotes outside if you use single quotes inside).

However, within the f-string's curly braces, it's legal to use
the same quotation mark type.
"""
print(f"phonebook['Chris']: {phonebook["Chris"]}")

name = 'Thomas'
age = 30

print(f'Hello, my name is {name}. I am {age} years old.')

# Remember that string comparisons are case sensitive.
# The expression phonebook['chris'] will fail to map to
# a value because the key 'Chris' exists in the dictionary
# as opposed to 'chris'.
# print(f'phonebook[\"chris\"]: {phonebook["chris"]}')

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

# The subsequent line demonstrates how a new key-value
# pair can be added to the 'phonebook' dictionary.
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
print(f'\nNumber of contacts in the phonebook: {len(phonebook)}\n')

for given_name in phonebook:
	print(f'key: {given_name}, phonebook[\'{given_name}\']: {phonebook[given_name]}')

# Delete all of the elements in a dictionary by
# calling the .clear() method on the dictionary.
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

# Create a list for the employee names.
# Then create another list for the employee phone numbers.

employee_names = ['Chris', 'Katie', 'Joanne']

phone_numbers = ['555-1111', '555-2222', '555-3333']

'''
How could we combine these two lists into a list of tuples where
each tuple contains an employee name and the corresponding phone
number?
'''

# The built-in zip() function can be used to pair up the elements
# from two or more iterables (e.g., lists, tuples, etc.) into
# tuples.

# Each tuple will contain one element from each iterable.
names_and_numbers = zip(employee_names, phone_numbers)

# The zip() function returns an iterator that points to the zip
# object. To obtain the first tuple in the zip object, pass the
# iterator as an argument to the next() function.
print('next(names_and_numbers):', next(names_and_numbers))

# Repeat to see the next tuple.
print('\nnext(names_and_numbers):', next(names_and_numbers))

# Another way to view all of the tuples in the zip object
# is to convert the zip object to a list.
names_and_numbers = list(names_and_numbers)

print('\nnames_and_numbers:', names_and_numbers)

# Add a duplicate tuple.
names_and_numbers.append(('Chris', '555-1111'))

# Use the set() function to remove the duplicate.
names_and_numbers = set(names_and_numbers)

print('\nnames_and_numbers:', names_and_numbers)