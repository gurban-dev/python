'''
Nested double quotes inside single quotes.
The double quotes are placed inside of the
string literal with single quotes.'''
course = 'Python for "Beginners"'

'''
Triple quotes allow you to create multi-line strings.

This means you can write text across multiple lines
without needing to concatenate strings or use
newline escape characters ('\n').'''
curriculum = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''

print('course:', course)

print(f'\ncurriculum: {curriculum}')