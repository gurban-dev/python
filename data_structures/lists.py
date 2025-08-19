'''
Lists are dynamic data structures, meaning that
items may be added to them or removed from them.
You can use indexing, slicing, and various methods
to work with lists in a program.

Each item that is stored in a list is called an
element.

Below is a statement that creates a list of integers.

The items that are enclosed in brackets and separated
by commas are the list elements. 2 the first element
for example.'''
even_numbers = [2, 4, 6, 8, 10]

# List of strings.
names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adriana']

# A list can hold items of different types:
info = ['Alicia', 27, 1550.87]

# The print() function can be used display an
# entire list.
print('info:', info)

'''
Python also has a built-in list() function that can
convert certain types of objects to lists.

Recall that the range() function returns an iterable,
which is an object that holds a series of values that
can be iterated over.

In the following context, range() returns an iterable
containing the values 0, 1, 2, 3, and 4.
'''
zero_to_five = list(range(5))
print(f'\nzero_to_five: {zero_to_five}')

'''
When passing three arguments to the range() function,
the first argument is the starting value, the second
argument is the ending limit, and the third argument
is the step value.

range(start, stop_and_exclude, step)

range(1, 10, 2) returns an iterable containing
[1, 3, 5, 7, 9] which will then be assigned to
the variable "numbers".'''
numbers = list(range(1, 10, 2))
print('\nnumbers:', numbers)