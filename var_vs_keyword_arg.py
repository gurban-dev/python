'''
The PEP 8 style guide says:
Always put one space around the = operator when
assigning a value to a variable because it
improves readability.
'''
name = "Thomas"

'''
The PEP 8 style guide also says not to put spaces around
the assignment operator (=) in keyword arguments (end="")
because, in function calls, the assignment operator (=)
does not perform a variable assignment. Instead, it assigns
the value "" to the parameter end inside the print() function.

"Hello" is a positional argument because it's passed
without explicitly naming the parameter.

end="", on the other hand, is a keyword argument
because the parameter name is explicitly specified.

end → the parameter name inside the function.

"" → the value being assigned to the parameter.
'''
print("Hello", end="")