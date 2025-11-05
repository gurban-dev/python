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