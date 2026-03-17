"""
In Python, there is a backslash (\) is
called a line continuation character.

It is used for breaking a long statement
into multiple lines.

Type the backslash character at the point you want
to break the statement, then press the Enter key
on the keyboard.
"""

result1 = 2 * 2 + 3 * 3 + 4 * 4 + 5 * 5

print(f'result1: {result1}')

# The line continuation character at the end of the
# first line tells the interpreter that the statement
# is continued onto the next line.
result2 = 2 * 2 + 3 * 3 + \
          4 * 4 + 5 * 5

print(f'\nresult2: {result2}')

"""
Including the line continuation character (\) in a print()
statement will include the whitespace characters in the
output.

If I removed the newline character on the second line,
whitespace characters would be seen in the output.
"""
print('\nToday it will be sunny with occasional showers. \
       \nThe temperature will reach seventy degrees.')

monday = 'food and beverages'

tuesday = 'appliances'

wednesday = 'home\nmaintenance equipment'

"""
A statement that is enclosed in parentheses
into multiple lines without using the line
continuation character.
"""
print("\nMonday's sales are ", monday,
      " and Tuesday's\nsales are ", tuesday,
      " and Wednesday's sales are ", wednesday, ".", sep='')

# With f-string.
print(f"\nMonday's sales are {monday} "
      f"and Tuesday's\nsales are {tuesday} "
      f"and Wednesday's sales are {wednesday}.")

# Also qualifies as valid source code.
total = (1 + 2 + 3 +
         4 + 5 + 6 +
         7 + 8 + 9)