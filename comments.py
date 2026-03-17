'''
Comments are explanatory notes that document
specific lines or sections of a program.

They are intended for people who may be reading
the source code.

If a programmer views the same program they wrote
one year ago, comments will make it easier to grasp
the purpose and logic of the source code.'''

# This is a single line comment.

# Comments are ignored by the Python interpreter.
# For that reason, they are not seen in the
# terminal output.

# An end-line comment is a comment that
# appears at the end of a line of code:
print('Kate Austen') # Display the name.

print('123 Full Circle Drive') # Display the address.

print('Asheville, NC 28899') # Display the city, state, and ZIP.

# I do not write end-line comments because I feel
# that they visually clutter the code and make a
# program less readable.

'''
This is a multi-line comment.

Multi-line comments are more convenient for
writing longer comments because a number sign
(#) does not have to be typed on every new line.'''

def get_dictionary():
  # Avoid writing multi-line comments inside
  # dictionaries because they will be included
  # in the returned dictionary.
  return {
    # This is a single line comment inside the
    # dictionary.

    '''
    This is a multi-line comment inside the dictionary.'''
  }

print('get_dictionary():', get_dictionary())