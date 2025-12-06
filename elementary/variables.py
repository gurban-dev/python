# 'Alexander' is a string literal because
# it is surrounded by quotation marks.
student_name = 'Alexander'

# The id() function returns a unique identifier for
# an object, which is often its memory address in
# CPython (the standard Python implementation).
print('id(student_name):', id(student_name))

# Assigning a string literal to a variable creates a
# variable that has a reference to a string object.

# The variable student_name on line 3 is a variable
# that has a reference to a string object because it
# was assigned a string literal.

tutor_name = "Dennis"

# Python's built-in type() function reveals the data
# type of variables.

# Arguments in functions are separated by commas (,), and
# by default, are outputted with spaces between them.
print('type(student_name):', type(student_name))

# Literals can also be passed to the type() function
# as arguments.
print('\ntype(\"Dennis\"):', type("Dennis"))

'''
= (called the equals sign in mathematics) is
called the assignment operator in programming.

The assignment operator (=) does not check equality.

It is used for assigning data to a variable:'''
flavour = 'vanilla'

"""
'vanilla' is the data being assigned. 'vanilla'
is a string literal because it is surrounded by
quotation marks on its left and right sides.

When you see data surrounded by quotes (single or
double quotes), you immediately know that you are
working with a string data type.

Since flavour is assigned the string literal
'vanilla' it is a string variable.
"""