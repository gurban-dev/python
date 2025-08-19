'''
Python allows you to define functions with default
parameters, which are used when no argument is
passed for that parameter.

Remember:
Parameters with default values are optional and must
be placed after required parameters in the function
header.'''

# The subsequent two function headers are invalid:
# def greet(msg="Hello", name, punctuation="!"):
# def greet(msg="Hello", punctuation="!", name):

'''
Valid function header because the default parameter
is declared before the non-default ones.

greet() is a void function because it doesn't
return anything back to where it was invoked.'''
def greet(name, msg="Hello", punctuation="!"):
  # F-string
  print(f"{msg}, {name}{punctuation}")

# Invoking the greet() function with providing
# all arguments.
greet("Alice", "Hi", "?")
# Output: Hi, Alice?

'''
Calling the greet() function with one default argument.
An argument was not provided for the "punctuation"
parameter. This means that in the greet() function
this parameter will be assigned "!".'''
greet("Bob", "Good day")
# Output: Good day, Bob!

'''
The invocation of greet() with two default arguments
('Hello' and '!').

Since arguments were not provided for the parameters
"msg" and "punctuation", they will be assigned their
own default arguments.'''
greet("Charlie")
# Output: Hello, Charlie!