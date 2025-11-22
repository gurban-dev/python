# The data type of "is_hot" and "is_cold" are
# boolean variables.

# A boolean variable is one that has been assigned
# a value of True or False.
is_hot = False

is_cold = True

is_rainy = True

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

# if statement
if is_hot:
	print("It's a hot day.")
	print("Drink plenty of water.")

# if-elif-else statement
# If "is_cold" evalutes to True, Python will not check
# the condition on line 51. It'll move on to the next
# part of the program.
if is_cold:
	print("It is a cold day.")
	print("Wear warm clothes.")
elif is_rainy:
	print('It is a rainy day.')
	print('Wear a rain coat.')
else:
  print("It's a lovely day.")

# The "and" keyword makes sure that both
# conditions to its left and to its  right
# evaluate to True before entering the block.
if is_cold and is_rainy:
  print('\nIt\'s cold and rainy.')

# Short-circuit evaluation:
# If the condition to the left of the "and" operator
# evaluates to False, Python will not even bother checking
# condition on the right side of the "and" operator because
# both conditions must evaluate to True for the compound
# expression to return to True.
if is_hot and is_rainy:
  print('It\'s either hot or rainy.')

# When should two if statements be written separately?
# Answer:
# Two separate if statements are used when the conditions 
# are independent of each other, meaning both can be true 
# at the same time. Each condition is evaluated separately.

developed_country = True
lacks_crude_oil = False

if developed_country:
  print("\nInflation is high! Prices are rising quickly.")

if lacks_crude_oil:
  print("\nDoes not have crude oil.")