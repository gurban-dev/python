# : bool a type hint/annotation.
it_is_rainy: bool = False

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
  print('\nDon\'t bring an umbrella.')