# Original string.
course1 = "Python Programming"

'''
How can the substring "Programming" be outputted
with quotes around it?

Double quotes can be nested or put inside a pair
of single quotes, this way they appear in the
output of a program.'''

course1 = 'Python "Programming"'

course1 = "Python 'Programming'"

# The \" double quote escape sequence may also be
# utilised to achieve the same outcome.
course1 = "Python \"Programming"

'''
Ignore the SyntaxWarning generated as a consequence of the
baskslash (\).

The backslash by itself is called the escape character (\).

\" is called the double quote escape sequence because it
makes the program escape the second double quote that
would normally follow the first one.'''
print(f'course1: {course1}')

# A single quote escape sequences likewise exists in Python.
# Perhaps as expected, it includes a single quote into the
# string output.
course2 = "Python \'Programming"

print('course2:', course2)

# A double backslash escape sequence exists and its purpose
# is to include a backslash.
course3 = "Python \\Programming"

print('course3:', course3)

# Newline escape sequence:
course4 = "Python \nProgramming"

print(f'course4: {course4}')

# The tab escape sequence positions the content in the
# string at the 8th position or index 9 if the content
# is made up of less than 8 characters.
print("\n1234567\\t1234567:\n1234567\t1234567")

# The tab escape sequence inserts 8 whitespace characters
# between strings that are made up of 8 characters and more.
print("\n12345678\\t12345678:\n12345678\t12345678")

'''
Some of the more common escape sequences in Python:
\" Double quote escape sequence
\' Single quote escape sequence
\\ Backslash escape sequence
\n Newline escape sequence
\t Tab escape sequence
'''