"""
An escape character is a special character
that is preceded with a backslash ( \ ).

\n is the newline escape character. When the \n
escape character is printed, it isn't displayed
on the screen. Instead, it causes output to
advance to the next line.
"""
print('One\nTwo\nThree')

"""
The tab escape character (\t) advances the
output to the next horizontal tab position.

A tab position normally appears after every
eighth character.

This means that the first character after a
tab escape character will begin on the eighth
position.
"""
print('\n0123456789012345678')
print('Mon\tTues\tWed')

first_half_of_week = 'Mon\tTues\tWed'

# Each \t (tab) escape character will increase the
# length or size of the string by one character.
print(f'\nlen(first_half_of_week): {len(first_half_of_week)}')

print(f'\nfirst_half_of_week[0]: {first_half_of_week[0]}'
      f'\nfirst_half_of_week[5]: {first_half_of_week[5]}'
      f'\nfirst_half_of_week[9]: {first_half_of_week[9]}')

"""
You can use the \' and \" escape characters
to display quotation marks.
"""
print('\nYour assignment is to read "Hamlet" by tomorrow.')

print("\nYour assignment is to read \"Hamlet\" by tomorrow.")

print('I\'m ready to begin.')

# The \\ escape character can be made
# use of to display a backslash.
# Two backslashes will output to be
# a single backslash.
print('\nThe path is C:\\temp\\data.')