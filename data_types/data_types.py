print("### Numeric Types ###")

'''
The data type of the variable "int_var" is
an integer because it is assigned 10 which
is a whole number. 10 doesn't have a
fractional part.'''
int_var = 10

'''
The data type is a float or a floating-point
number because it contains a decimal point
which indicates that the numeric value has a
fractional part.'''
float_var = 10.0

# Utilise the built-in type() function to
# output the data type of the variable.

# <class 'int'> is returned by type(int_var).
print(f"Integer: {int_var}, Type: {type(int_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")

# Sequence Types
print("\n### Sequence Types ###")

'''
String variables are declared usually by
assigning string literals which can be
identified by "" (double quotes) or ''
(single quotes).'''
str_var = "Hello, World!"

# The data type is still a string.
str_var = '100'

print(f"str_var: {str_var}, Type: {type(str_var)}")

# Boolean Types
print("\n### Boolean Types ###")

# A boolean variable stores a boolean value.
# A boolean value is either True or False.
# Be sure to assign True and not true.
boolean_true = True
boolean_false = False

print(f"Boolean True: {boolean_true}, Type: {type(boolean_true)}")
print(f"Boolean False: {boolean_false}, Type: {type(boolean_false)}")

print("\n### None Type ###")

# "none_type" holds the equivalent of
# null or the absence of a value.
none_type = None
print(f"None: {none_type}, Type: {type(none_type)}")