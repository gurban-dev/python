# : bool is called a type hint/annotation.
# It's purpose is to inform whoever is reading this program,
# to expect that the it_is_rainy variable will be assigned
# a boolean value.
it_is_rainy: bool = True

print('it_is_rainy:', it_is_rainy)

# The bool() function will reveal whether an argument
# evaluates to True or False.
print('\nbool(it_is_rainy):', bool(it_is_rainy))

# The if it_is_rainy clause, causes the flow of the Python
# program to enter its block when the variable "it_is_rainy"
# evaluates to True.

# When the variable "it_is_rainy" does not evaluate to True,
# the flow of the Python program enters the else block.
if it_is_rainy:
  print('\nBring an umbrella.')
else:
  # The following line is executed when the conidition in
  # the if statement (it_is_rainy), evaluates to False.
  print('\nDon\'t bring an umbrella.')