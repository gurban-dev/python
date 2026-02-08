# A variable is a name that holds a reference to an object
# that exists in memory throughout the runtime of a Python
# program.

# The variable 'famous_leader' holds a reference to the
# string object 'Alexander the Great'.

# 'Alexander the Great' is a string literal because it is
# surrounded by quotation marks.
famous_leader = 'Alexander the Great'

print('famous_leader:', famous_leader)

# Assigning a string literal to a variable creates a
# variable that has a reference to a string object.

# The variable 'famous_leader' on line 6 is a variable
# that has a reference to a string object because it
# was assigned a string literal.

# Python's built-in type() function reveals the data type
# of data that is passed to it as an argument.

# Arguments in functions are separated by commas (,), and
# by default, are outputted with spaces between them.
print("\ntype('Alexander the Great'):", type('Alexander the Great'))

# Literals can also be passed to the type() function
# as arguments.
print('\ntype(famous_leader):', type(famous_leader))

'''
= (called the equals sign in mathematics) is called
the assignment operator in programming.

The assignment operator (=) does not check equality.
'''

# It is used for assigning data to a variable:
flavour = 'vanilla'

"""
'vanilla' is the data being assigned. 'vanilla'
is a string literal because it is surrounded by
quotation marks on its left and right sides.

When you see content surrounded by quotes (single or
double quotes), you immediately know that you are
working with a string data type.

Since the variable 'flavour' is assigned the string
literal 'vanilla' it is a string variable.
"""