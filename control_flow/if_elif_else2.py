# "bool" is a data type in Python.
# Simply put, assigning True or False makes a variable
# a boolean variable.
condition1: bool = False
condition2: bool = True
condition3: bool = True

# If condition1 evaluates to True, line 11 will be executed,
# and no other conditions will be checked.
if condition1:
	print(f'condition1 evaluated to {condition1}.')
elif condition2:
	print(f'condition2 evaluated to {condition2}.')
elif condition3:
	print(f'condition3 evaluated to {condition3}.')
else:
	print('None of the conditions evaluated to True.')

# The following two if statements are necessary if you
# still wanted conidtion2 and condition3 evaluated after
# condition1 evaluates to True.

# This is done when two conditions are indepenent of each other.
if condition2:
	print(f'condition2 evaluated to {condition2}.')

if condition3:
	print(f'condition3 evaluated to {condition3}.')