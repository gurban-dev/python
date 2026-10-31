# Syntax for variable declaration:
# <variable_name> = <value_being_assigned_to_the_variable>

# The variable name is always on the left side of the
# assignment operator (=).

# The input() function temporarily pauses the program and
# waits until the user clicks the Enter button on their
# keyboard. After this, the data inputted by the user is
# returned by the input() function as a string.

# The user input returned by the input() function is
# then assigned to the variable named 'given_name'.
given_name = input('Please input your given name: ')

# Two arguments being passed to the print() function:
# First argument: '\ngiven_name:'
# Second argument: given_name

# The following is a newline escape sequence: \n
# It adds a newline depending on where it is put.
print('\ngiven_name:', given_name)

num1 = input('\nPlease input an integer: ')

num2 = input('\nPlease input another integer: ')

# String concatenation.
sum = num1 + num2

print('\nHave a look at the data types for num1 and num2:')

# Output the data types of num1 and num2 with
# Python's built-in type() function.
print('type(num1):', type(num1))

print('type(num2):', type(num2))

# Why is "sum" a variable?
# Answer:
# It is to the left of an assignment operator.

# String concatenation
# The two strings num1 and num2 are being put
# together side by side.
print('\nnum1 + num2:', num1 + num2)

print('\nsum:', sum)

# The string that is returned by the input() function
# is converted to an integer data type.
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
Notice how calling functions in Python requires that
you include open and closed parentheses after their
names:
print()
type()
input()
range()
'''