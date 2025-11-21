# print() is a built-in Python function that displays data to the
# screen.
print("Hello World 🐱!")

# You can pass values (called arguments) to print().
# The value "*" is a string literal because it is written inside quotes.
# Multiplying a string causes it to repeat.
print("*" * 10)

# Variables store data. Here, the variable greeting stores a string literal.
greeting: str = "Good morning!"

# type() shows the data type of a value or variable.
print('type(greeting):', type(greeting))
print('type(1):', type(1), '\n')

# By default, print() includes a newline escape sequence ("\n")
# at the end of its output.
print('One')
print('Two')
print('Three')

# You can remove the newline escape sequence by using the
# "end" keyword argument.
print('One', end='')
print('Two', end=' ')
print('Three', end='-')

# Each comma separates arguments, and the print() function places
# a space between them in the output.
print('\nOne', 'Two', 'Three')

# Using the + operator concatenates strings without adding spaces
# in between.
print('One' + 'Two' + 'Three')

# The "sep" parameter controls what appears between items in the
# output.
print('One', 'Two', 'Three', sep='')
print('One', 'Two', 'Three', sep='🐱')