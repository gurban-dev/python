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
	print("It's a warm day.")
	print("Drink plenty of water.")

# if-elif-else statement
if is_cold:
	print("It is a cold day.")
	print("Wear warm clothes.")
elif is_rainy:
	print('It is a rainy day.')
	print('Wear a rain coat.')
else:
  print("It's a lovely day.")

# The "and" keyword makes sure that both
# conditions to the left and right of it
# evaluate to True before entering the block.
if is_cold and is_rainy:
  print('\nIt\'s cold and rainy.')

if is_hot and is_rainy:
  print('It\'s either hot or rainy.')

# The two subsequent float literals represent
# percentage values.
inflation_rate = 7.5
unemployment_rate = 8

# Write two separate if statements if there are two
# separate conditions that can both be true.
# In other words, these conditions are independent of
# each other.

# Floats and integers can be compared to each other with
# comparison operators.
if inflation_rate > 5:
  print("\nInflation is high! Prices are rising quickly.")

if unemployment_rate > 7.0:
  print("\nUnemployment is high! Many people are not\n" \
	"participating in the labour market.")

# The below print statement always executes regardless
# of any boolean value because it is not part of the
# above if-statement.
print("\nEnjoy your day.")