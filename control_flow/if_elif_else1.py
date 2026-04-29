# The data type of "is_hot" and "is_cold" are
# boolean variables.

# A boolean variable is one that has been assigned
# a value of True or False.
is_hot = False

is_cold = True

"""
In if statements, conditions are evaluated.

In the following example, the "is_hot" variable is
being evaluated. If "is_hot" has a value of True,
the program will execute the block of indented
statements following the if clause.

The "elif" keyword is used when more than one condition
needs to be verified.

Even if two separate conditions for two different if
clauses are True, only the block of indented statements
following the clause that is evaluated first, will be
executed.

Even if "is_hot" and "is_cold" are both True, only the
block of indented statements following the if clause
containing "is_hot" will be executed because it is written
before the if clause containing "is_cold".

In an if-else or if-elif-else statement, only one block
of indented statements is executed.
"""

print('bool(is_hot):', bool(is_hot), '\n')

# if-elif-else statement
# Notice how only one of these conditions can be True at
# the same time which is why if "is_hot" evalutes to True,
# Python will not check the condition on line 45. It'll
# move on to the next part of the program.
if is_hot:
	print("It's a hot day.")
	print("Drink plenty of water.")
elif is_cold:
	print("It is a cold day.")
	print("Wear warm clothes.")
else:
  	print("It is neither cold nor hot.")

is_rainy = True

# The "and" keyword makes sure that both
# conditions to its left and to its right
# evaluate to True before entering the block.
if is_hot and is_rainy:
	print('\nIt\'s cold and rainy.')

# Short-circuit evaluation:
# If the condition to the left of the "and" operator
# evaluates to False, Python will not even bother checking
# condition on the right side of the "and" operator because
# both conditions must evaluate to True for the compound
# expression to return to True.
if is_rainy or is_hot:
	print('It\'s either hot or cold.')

# When should two if statements be written separately?
# Answer:
# Two separate if statements are used when the conditions 
# are independent of each other, meaning both can be true 
# at the same time. Each condition is therefore evaluated
# separately.

developed_country = False
has_crude_oil = True

if developed_country:
  	print("\nThe country ranks highly on the human development "
		  "index report.")
else:
  	print("\nThe country is still developing.")

if has_crude_oil:
  	print("\nThe country has crude oil.")
else:
  	print("\nThe country does not have crude oil.")