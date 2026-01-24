
'''
The variable 'famous_leader' stores a reference to the string
object whose value is "Alexander".

A reference is a way for a variable to point to an object
that exists in memory.

The variable 'famous_leader' and the reference it holds are stored on
the stack (or in the variable namespace).

The object itself is stored on the Python private heap, a section
of RAM where Python allocates objects at runtime.

Stack (variables / references)          Heap (actual objects)
+-----------------+                     +-------------------------+
| famous_leader   |  ---> Reference --> | "Alexander"             |
| (reference)     |                     | [unique ID / id()]      |
+-----------------+                     +-------------------------+

'''

famous_leader = 'Alexander'

# The id() function returns a unique identifier for
# an object, which is often its memory address in
# CPython (the standard Python implementation).
print('id(famous_leader):', id(famous_leader))