'''
A string literal is the quotation marks and text
enclosed inside of them in a program's source code.

It is hard-coded into the program.
"Hello" is a string literal.

\n is a newline escape sequence.
\" is a double quote escape sequence.
'''
print(f'This is a string literal:\n\"Hello\"')

'''
A string object is the instance of the built-in
Python string class that gets created in memory
when a string literal is assigned to a variable.

greeting is not only a variable, but refers
to a string object.'''
greeting = "Hello"

# String variable called "greeting".
print("\ngreeting:", greeting)

# The type() function reveals the data type
# of the argument that is passed to it.
print("\ntype(\"World\"):", type("World"))

# The type() function will return the data type
# of the variable greeting.
# Then the print() function will print that data
# type to the screen.
print("\ntype(greeting):", type(greeting))

'''
User input is always a string object in memory,
but not a string literal because it is not a
hard-coded string written into the source code
enclosed with quotes.'''
user_input = input("\nType something: ")

print("\nYou typed (as a string object):", user_input)

# In the Python interactive shell, show how you would
# print the following sentence to the screen, but with
# outer double quotes:
# The term to meet is "rendez-vous".
print('\nThe term to meet is "rendez-vous".')

# Preceding a double quotation mark with a
# backslash makes it a double quote escape
# sequence.
print("\nThe term to meet is \"rendez-vous\".")