'''
When the + (add) operator is used with two
strings, it performs string concatenation.

This means that it appends one string to another.'''

# One argument being passed to print().
print('This is ' + 'one string.')

# Two arguments are being passed to print().
print('This is', 'one string.\n')

'''
String concatenation can be useful for breaking up
a string literal, so that a lengthy call to the
print() function can span multiple lines.

Having a string literal span multiple lines is
necessary sometimes because it makes a program
more readable.'''

print('This is a very long string that needs to be broken into multiple lines. It spans several lines and retains its original formatting.')

print('\nThis is a very long string that needs to be ' +
      'broken\ninto multiple lines. It spans several ' +
      'lines and\nretains its original formatting.')