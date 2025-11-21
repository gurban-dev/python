print("### Numeric Types ###")

'''
The data type of the variable "int_var" is
an integer because it is assigned 10 which
is a number without a decimal point and not
enclosed by quotation marks.'''
int_var = 10

# The data type is a float because the number contains
# a decimal point and is not enclosed in quotation
# marks.
float_var = 10.

# Utilise the built-in type() function to output
# the data type of variables and literals likewise.

# <class 'int'> is returned by type(int_var).
print(f"int_var: {int_var}, type(int_var): {type(int_var)}")

print(f"float_var: {float_var}, type(float_var): {type(float_var)}")

print("\n### Text Sequence Types ###")

'''
String variables are declared usually by
assigning string literals which can be
identified by "" (double quotes) or ''
(single quotes).'''
str_var = "Hello, World!"

# The data type is still a string.
str_var = '100'

print(f"str_var: {str_var}, type(str_var): {type(str_var)}")

print("\n### Boolean Types ###")

# A boolean variable stores a boolean value.
# A boolean value is either True or False.
# Be sure to assign True and not true.
lives_in_vaduz = False
does_not_live_in_vaduz = True

print(f"lives_in_vaduz: {lives_in_vaduz}, type(lives_in_vaduz): {type(lives_in_vaduz)}")
print(f"does_not_live_in_vaduz: {does_not_live_in_vaduz}, "
      f"type(does_not_live_in_vaduz): {type(does_not_live_in_vaduz)}")

print("\n### The Null Object ###")

# "None" holds the equivalent of null or the absence of a value.
# This object is returned by functions that don't explicitly return a value.
none_type = None

print(f"none_type: {none_type}, type(none_type): {type(none_type)}\n")

# What does the print() functon return?
return_value = print('Hello!')

print('return_value:', return_value, '\n')

# In Python, variables are not fixed to one data type.
# You can change the type by assigning a new value.
return_value = True

print('return_value:', return_value)