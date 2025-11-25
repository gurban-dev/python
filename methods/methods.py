'''
In Python, a method is a function that "belongs to" an
object.

Functions are different because they are standalone
blocks of code that are not tied to any object, meaning
they can be invoked independently without needing to
be called on an object.

An effective way to distinguish a function from a
method in Python is to look at how it's called in
the source code.

Functions are called as: function(argument)

E.g.
print("Hello World!")

Methods are always called on an object using the dot notation:
object.method()

Do not confuse np.array() with being a method.

array() is a function that is defined inside the numpy module.

import numpy as np
np.array()

E.g.
"Alexander".upper()
'''

# Declare a list data structure.
list_of_ints = list([1])

# Declare a set data structure.
set_of_ints = set([1])

'''
Because the list() and set() classes expect iterables
rather than single elements, 1 was wrapped in square
brackets so that a list would be passed as an argument.'''

print(f'list_of_ints: {list_of_ints}\n'
      f'set_of_ints: {set_of_ints}')

# Insert an element/item to "list_of_ints".
list_of_ints.append(2)

'''
The print() function has the ability to output
the data stored in both "list_of_ints" and
"set_of_ints".

Question:
If the append() method can be used to insert
additional elements/items into the list named
"list_of_ints", can this method be used for
the same purpose on the set named "set_of_ints"?
If not, why?

Answer:
The append() method cannot be used to insert
elements into the set named "set_of_ints"
because it is defined in the Python list class
and is only available to list objects that were
instantiated from that class, not to set objects.
'''

# Insert an element/item to "set_of_ints".
set_of_ints.add(2)

# Generates an AttributeError because 'set' objects
# do not have a method named "append".
# set_of_ints.append(2)