# print() is a built-in Python function.
# Functions are stand alone. Functions can be
# invoked on their own without objects.
print("Hello World 🐱")

# The print() function accepts and argument and
# prints it to the screen.

"""
The asterisk surrounded by double quotes ("*")
is a string literal because it is enclosed by
a pair of quotes.

This string literal ("*") is being multiplied
ten times which means that it will be outputted
ten times."""
print("*" * 10)

# greeting is the string variable.
# 'Good morning!' is the string literal
# that is assigned to the greeting variable.
greeting: str = 'Good morning!'

print('type(greeting):', type(greeting), '\n')

print('type(1):', type(1), end='\n\n')

# The print() function in Python automatically appends
# a newline escape sequence (\n) by default at the end
# of the outputted string.
print('One', end='\n')
print('Two')
print('Three')

"""
If you do not want the print() function to start a
new line of output when it finishes displaying its
output, you can pass the following keyword argument:
end='':
"""
print('One', end='')

# Print a whitespace character rather
# than merely an empty string literal.
print('Two', end=' ')

print('Three', end='-')

"""
When multiple arguments are passed to the print()
function, they are automatically separated by a
space when outputted in the terminal.

Passing multiple arguments to a function, requires
separating them with a comma.

No_of_arguments = no_of_commas + 1
"""
print('One', 'Two', 'Three')

# Only one argument is passed to the print()
# function is because there aren't any commas,
# which would indicate that more than one
# argument is being passed.
print('One' + 'Two' + 'Three')

"""
The "sep" parameter in the print() function
specifies the string that should be printed
between the items. By default, "sep" is set
to a whitespace character (' '), but if you
pass an empty string ('') as an argument to
"sep", no space will be printed between the
items.

Remember that keyword arguments like "end"
and "sep" must be passed after positional
arguments like 'Three'.
"""
print('One', 'Two', 'Three', sep='')

# Specifies that the printed items should
# be separated with the 🐱 character.
print('One', 'Two',  'Three', sep='🐱')