"""
Dunder (double underscore) methods and variables in Python
---------------------------------------------------------

Dunder methods and variables are special, predefined names that let your
objects define exactly what happens when they are used with Python's built-in
operations (like +, print(), ==, <, >) and constructs (like for-loops and len()).

Dunder Methods (behavior)
------------------------
These define how objects act with built-in operations:

Addition
- __add__(self, other)   -> a + b
- __radd__(self, other)  -> b + a (fallback if left operand doesn't handle it)
- __iadd__(self, other)  -> a += b (in-place, if supported)

Printing / String Representation
- __str__(self)  -> user-friendly output (used by print())
- __repr__(self) -> developer-focused, unambiguous output (used in REPL/debugging)
  Difference: __str__ is for readability, __repr__ is for precision

Comparisons
- __eq__(self, other) -> a == b
- __ne__(self, other) -> a != b
- __lt__(self, other) -> a < b
- __le__(self, other) -> a <= b
- __gt__(self, other) -> a > b
- __ge__(self, other) -> a >= b
  Each method corresponds to a specific comparison operator

Iteration
- __iter__(self) -> returns an iterator
- __next__(self) -> returns next value, raises StopIteration when done
  Difference: __iter__ sets up iteration, __next__ produces values


Dunder Variables (data / metadata)
---------------------------------
These store or expose information about objects:

Object identity & structure
- __dict__  -> dictionary of an object’s attributes
- __class__ -> the class the object belongs to

Class / definition info
- __name__   -> name of a class, function, or module
- __module__ -> module where the object was defined
- __bases__  -> base classes of a class

Documentation & metadata
- __doc__         -> docstring (documentation)
- __annotations__ -> type hints

Special execution context
- __name__ == "__main__" when a file is run directly:

    if __name__ == "__main__":
        ...

Summary
-------
- Dunder methods: define behavior (what an object does)
- Dunder variables: store metadata (what an object is / contains)
"""