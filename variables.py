
'''
The variable given_name stores a reference to the string
object whose value is "Alexander".

A reference is a way for a variable to point to an object
that exists in memory.

The variable given_name and the reference it holds are stored on
the stack (or in the variable namespace).

The object itself is stored on the Python private heap, a section
of RAM where Python allocates objects at runtime.

Stack (variables / references)          Heap (actual objects)
+-----------------+                     +-------------------------+
| given_name       |  ---> Reference --> | "Alexander"            |
| (reference)      |                     | [unique ID / id()]     |
+-----------------+                     +-------------------------+

'''

given_name = 'Alexander'

print('id(given_name)):', id(given_name))