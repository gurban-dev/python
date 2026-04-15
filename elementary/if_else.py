# Syntax for variable declaration:
# <variable_name> = <value_being_assigned_to_the_variable>

# Variable name: age
# Value being assigned to the variable: 10
age = 10

# In Python, you can change the value that a variable
# references by assigning a new value to it.
age = 18

# A float can also be compared to the integer value 18 because
# despite being two different data types, they are part of the
# same type category (numeric).
# age = 18.1

# age >= 18 will return True or False depending on
# the value assigned to the variable named "age".
print(f'{age} >= 18: {age >= 18}\n')

# Line number 23 can be read as what follows:
# If age is greater than or equal (>=) to 18.
if age >= 18:
	# The following line is executed so long as age
	# is greater than or equal (>=) to 18.
	print('You are legally an adult.')
else:
	# The following line is executed if age is not greater
	# than or equal to 18.
	print('You are legally a minor.')