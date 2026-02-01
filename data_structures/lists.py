'''
Lists are dynamic data structures, meaning that items
may be added or removed from them during the runtime
of a Python program.

This means that the size of a list can change throughout
the runtime of a Python program.

You can use indexing, slicing and various methods to
to work with lists in a program.

Below is a statement that creates a list of integer
literals.

The items that are enclosed in brackets and separated
by commas are the list elements. 2 is the first element
for instance, its index is 0 (zero).'''

# Indices:      0  1  2  3   4
even_numbers = [2, 2, 6, 8, 10]

# Remember that a list can store duplicate values.

# A list can hold items of different data types:
info = ['Alicia', 27, 1550.87, True, []]

# The print() function can be used display an entire list.
print('info:', info)

# Index the first item.
print('\ninfo[0]:', info[0])

# Index the last item.
print('\ninfo[-1]:', info[-1])

# Index the second to last item.
print('\ninfo[-2]:', info[-2])

'''
Python also has a built-in list() function that can
convert certain types of objects to lists.

Recall that the range() function returns an iterable,
which is an object that holds a series of values that
can be iterated over.

In the following context, range() returns an iterable or
a collection of items containing the values 0, 1, 2, 3,
and 4.
'''
zero_to_four = list(range(5))

print(f'\nzero_to_four: {zero_to_four}')

'''
When passing three arguments to the range() function,
the first argument is the start value, the second
argument is the stop value (exclusive), and the third
argument is the step value.

range(start_value, stop_value (exclusive), step_value)

range(1, 10, 2) returns an iterable containing [1, 3, 5, 7, 9]
which will then be assigned to the variable "numbers".

The list() function casts the range to a list.'''
numbers = list(range(1, 10, 2))

print('\nnumbers:', numbers)

# Lists are mutable, meaning that their elements
# can be changed after the list is created.

# Assign "Nine" to the last index in the "numbers" list.
numbers[4] = "Nine"

# The following line produces the same outcome as the one above
# because the last item in a list is always at index -1:
# numbers[-1] = "Nine"

print('\nnumbers:', numbers)