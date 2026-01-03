'''
Python allows you to define functions with default
parameters, which are used when no argument is
passed for that parameter.

Remember:
Parameters with default arguments are optional and must
be placed after required parameters in the function
header.'''

# The subsequent two function headers are invalid:
# def greet(msg="Hello", name, punctuation="!"):
#   pass

# def greet(msg="Hello", punctuation="!", name):
#   pass

'''
Below is a valid function header because all non-default
parameters come before parameters with default values.

If a function does not explicitly return anything, Python
automatically returns None.'''
def greet(name, msg="Hello", punctuation="!"):
  # F-string
  print(f"{msg}, {name}{punctuation}")

# Invoking the greet() function by providing
# all arguments.
greet("Alice", "Hi", "?")

'''
Calling the greet() function with one default argument.

An argument was not provided for the "punctuation"
parameter. This means that in the greet() function
this parameter will be assigned "!".'''
greet("Bob", "Good day")

'''
The invocation of greet() with two default arguments
('Hello' and '!').

Since arguments were not provided for the parameters
"msg" and "punctuation", they will be assigned their
own default arguments.'''
greet("Charlie")