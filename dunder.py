"""
Dunder methods and variables in Python

The term "dunder" is short for "double underscore".
---------------------------------------------------------

Dunder methods and variables are predefined names that let your
objects define exactly what happens when they are used with
Python's built-in operations (like +, print(), ==, <, >) and
constructs (like for-loops and len()).

Dunder Methods (behaviour)
--------------------------
These define how objects act with built-in operations:

Addition
- __add__(self, other)   -> a + b

Printing / String Representation
- __str__(self)  -> determines what gets shown when you print or format
					an object.

"Country: {}".format(luxembourg1)

- __repr__(self) -> __repr__ is used when Python needs a representation
  					of the object inside another structure or when no
					__str__ is available.

Comparisons
- __eq__(self, other) -> a == b

  This method corresponds to a specific comparison operator.

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

Special execution context
- __name__ == "__main__" when a file is run directly:

    if __name__ == "__main__":
        ...

Summary
-------
- Dunder methods: define behaviour (what an object does with Python's
  built-in operations)

- Dunder variables: store metadata (what an object is / contains)
"""


class Country:
	def __init__(self, country_name):
		self.country_name = country_name

	def __str__(self):
		# return f"\n{self.country_name}"
		return "\n" + self.country_name

	# Determines the way a list of Country objects would be
	# displayed when printing the list.
	def __repr__(self):
		return self.country_name
	
	# Determines how two different Country objects are compared.
	# Think about what attributes should be compared for this class
	# when deciding if two different Country objects are equal.
	def __eq__(self, other_obj):
		# Check if the other object is not an instance of this class.

		# Evaluates to True if 'other_obj' references an object that is
		# not an instance of the Country class.
		if not isinstance(other_obj, Country):
			return False

		# Send True back to where this method was invoked if the names of
		# the countries are the same.
		return self.country_name == other_obj.country_name
    
luxembourg1 = Country("Luxembourg")
luxembourg2 = Country("Luxembourg")

countries = [luxembourg1, luxembourg2]

print(f'luxembourg1: {luxembourg1}')

# The text that is displayed when printing out the content of a list
# of objects is controlled by the .__repr__() dunder method.
print(f'\ncountries: {countries}')

# The below comparison with the equality operator is equivalent to:
# luxembourg1.__eq__(luxembourg2)

# In the .__eq__() dunder method:
# self references 'luxembourg1'.
# other_obj references 'luxembourg2'.
print(f'\nluxembourg1 == luxembourg2: {luxembourg1 == luxembourg2}')

# The __class__ dunder variable reveals the name of the class
# that the object is an instance of.
print('\nluxembourg1.__class__:', luxembourg1.__class__)

# The __dict__ dunder variable reveals the attributes an object
# contains.
print('luxembourg1.__dict__:', luxembourg1.__dict__)