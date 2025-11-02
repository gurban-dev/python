# "email" is the name of a variable.
# I know that "email" is a variable because the assignment
# operator (=) which looks like an equals sign in mathematics,
# comes right after it.
# email = input("Email Address: ")

# The input() function will prompt the user to enter
# their email address and will then assign the return
# value to the variable "email".

# Print the value assigned to the variable "email".
# print('email:', email)
# Indices:  0123456789
myString = ' him-him '

# The .replace() method finds all occurrences of the first
# substring and replaces them with the second substring.
print(myString.replace('him', 'her'))

print('len(myString):', len(myString))

# The .strip() method removes the leading and trailing
# whitespace characters from a string, but doesn't alter
# the original string.
print(myString.strip())

print('\nlen(myString):', len(myString))

# The len() function returns the length of a string.
# The length of a string is determined by the number
# of characters it contains.
print('\nlen("895"):', len("895"))

# The .count() method returns the number of occurrences
# of a substring in a string.
print('\n"100".count("100"):', "100".count("100"))

# The .capitalize() method returns a copy of the string with
# its first character capitalized and the rest lowercased.
print("\n'Good Morning'.capitalize():", 'Good Morning'.capitalize())

# The .title() method returns a copy of the string where
# the first character of each word is capitalized.
print("\n'string methods lesson 24'.title():",
      "string methods lesson 24".title())

print("\n'String Methods.txt'.replace('txt', 'py'):",
      "String Methods.txt".replace("txt", "py"))

'''
Syntax:
string[start:stop:step]

Assuming the step value is not negative:
start: The index where the slice begins (inclusive).
       If omitted, it defaults to the beginning of the sequence
       (index 0).

stop: The index where the slice ends (exclusive).
      If omitted, it defaults to one past the last index of the
      sequence.

step: The increment between elements. If omitted, it defaults to 1.

"!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2]

In the context of the above example:

Taking into account that the step value is negative:
The absence of a value before the first colon indicates that
the slice starts from one index past the end of the string
(len("!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI")).

The absence of a value before the second colon indicates that
the slice stops at one index before the beginning of the string.

The -2 is the step value, which means move backward by 2
characters each time. The negative makes the slicing occur
in reverse order.
'''
print('\n!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2]:\n',
      "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"[::-2], sep='')