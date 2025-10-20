# Syntax for variable declaration:
# <variable_name> = <value_being_assigned>

# The variable name is ALWAYS on the left side
# of the assignment operator.
given_name = input('Please input your given name: ')

# What data on the next line is being stored?
# Answer: The value that is assigned to the variable
#         is the data being stored.
given_name = 'William Shakespeare'

# The assignment operator (=) is in
# between the left and right sides.
# left_side = right_side

print('\ngiven_name:', given_name)

# Python's built-in input() functon will
# ask the user to input a particular piece
# of information.
num1 = input('\nPlease input an integer: ')

num2 = input('\nPlease input another integer: ')

# Concatenate the two inputted integers.
sum = num1 + num2

print('\nHave a look at the data types for num1 and num2:')

# Output the data types of num1 and num2 with
# Python's built-in type() function.
print('type(num1):', type(num1))

print('type(num2):', type(num2))

# Why is sum a variable?
# Answer:
# It is to the left of the assignment operator.

# String concatenation
# The two strings num1 and num2 are being put
# together side by side.
print('\nnum1 + num2:', num1 + num2)

print('\nsum:', sum)

num1 = int(input('\nPlease input an integer: '))

num2 = int(input('\nPlease input another integer: '))

# Why is it that num1 and num2 are all of a sudden
# integers rather than strings?
# Answer:
# Python's built-in int() function will cast or convert
# the return value of input() to an integer.

print('\nHave a look at the data types for num1 and num2:')

print('type(num1):', type(num1))

print('type(num2):', type(num2))

# Arithmetic operation: Addition
# The sum of two integers num1 and num2 is being
# calculated.
print('\nnum1 + num2:', num1 + num2)

sum = num1 + num2

print('\nsum:', sum)

'''
Notice how functions in Python have parentheses
after their names:
print()
type()
input()
int()
'''