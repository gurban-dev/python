'''
In Python, a method is a function that
"belongs to" an object.

Functions are different because they are
standalone blocks of code that are not
tied to any object.

Python documentation:
https://docs.python.org/3/tutorial/classes.html#instance-objects

An effective way to distinguish a function from a
method in Python is to look at how it's called in
the source code.

Functions are called as: function(argument)

Methods are called as: object.method()
'''

# Declare a list data structure.
list_of_strs = list([1])

# Declare a set data structure.
set_of_strs = set([1])

'''
Because the list() and set() classes expect
iterables rather than single elements, 1 was
wrapped in square brackets so that a list
would be passed as an argument.'''

print(f'list_of_strs: {list_of_strs}\n'
      f'set_of_strs: {set_of_strs}')

# Insert an element/item to "list_of_strs".
list_of_strs.add(2)

'''
The print() function has the ability to output
the data stored in both "list_of_strs" and
"set_of_strs".

If the append() method can be used to insert
additional elements/items into the list named
"list_of_strs", can this method be used for
the same purpose on the set named "set_of_strs"?
If not, why?'''

# Insert an element/item to "set_of_strs".
set_of_strs.add(2)

'''
The append() method cannot be used to insert
elements into the set named "set_of_strs"
because it is defined in the Python list class
and is only available to list objects that were
instantiated from that class, not to set objects.'''

# set_of_strs.append(2)