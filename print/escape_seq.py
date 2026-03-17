# In Python, a backslash (\) is called an escape character,
# and its purpose is to introduce escape sequences.

# It signals Python to treat the following character
# as part of an escape sequence (e.g., \n for newline,
# \t for tab, \\ for a backslash).

# A control character is a non-printable character that
# directs the program or terminal to perform a specific
# action (e.g., moving to a new line or inserting a tab)
# instead of displaying a literal symbol.

# \n is the newline escape sequence. When printed, it
# doesn't appear as "\n"; instead, it moves the output 
# position to the beginning of the next line in the
# terminal or console.

print('One\nTwo\nThree')

"""
The tab escape sequence (\t) advances the
output to the next horizontal tab position.

A tab position normally appears after every
eighth character.

This means that the first character after a tab
escape sequence will begin on the next eighth
position.
"""
print('\n0123456789012345678')
print('Mon\tTues\tWed')

first_half_of_week = 'Mon\tTues\tWed'

# Each \t (tab) escape sequence will increase the
# length or size of the string by one character.
print(f'\nlen(first_half_of_week): {len(first_half_of_week)}')

print(f'\nfirst_half_of_week[0]: {first_half_of_week[0]}'
      f'\nfirst_half_of_week[4]: {first_half_of_week[4]}'
      f'\nfirst_half_of_week[9]: {first_half_of_week[9]}')

"""
You can use the single quote (\') and double quote (\")
escape sequences to display quotation marks.
"""
print('\nYour assignment is to read "Hamlet" by tomorrow.')

print("\nYour assignment is to read \"Hamlet\" by tomorrow.")

print('\nI\'m ready to begin.')

# The \\ escape character can be made use of to
# display a backslash.

# Use two backslashes (\\) to represent a single
# backslash (\) in the output.
print('\nThe path is C:\\temp\\data.')