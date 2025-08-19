'''
A string literal is the text enclosed
in quotes in a program's source code.

It is hard-coded into the program.
"Hello" is a string literal.'''
print(f'This is a string literal:\n\"Hello\"')

'''
A string object is the instance of the built-in
Python string class that gets created in memory
when a string literal is assigned to a variable.

"greeting" is not only a variable, but refers
to a string object.'''
greeting = "Hello"

# String variable called "greeting".
print("\ngreeting:", greeting)

# type() reveals the kind of object
# the variable "greeting" is holding.
print("\ntype(\"World\"):", type("World"))

print("\ntype(greeting):", type(greeting))

'''
User input is always a string object in memory,
but not a string literal because it is not a
hard-coded string written in the source code
enclosed with quotes.'''
user_input = input("\nType something: ")

print("\nYou typed (as a string object):", user_input)