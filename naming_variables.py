'''
In Python, there a quite a few built-in keywords.
These keywords mustn't be used as variable names.

The following generates a syntax error because
"for" is one of the keywords in Python:'''
# for = 2

'''
Think of a variable as a jar with an attached label
that stores a value.

"minimum_wage" is the label attached to the jar
and the value 15 is being stored inside of it.'''

'''
"minimum_wage" is the name of the variable.

Both 15 and 15.0 represent whole numbers because neither
has a fractional part (no digits after the decimal other
than zero).

However, because 15 is written without a decimal point,
Python treats it as an integer (int). Even though 15.0
represents the same number mathematically, it is a
floating-point number (float) because it includes a
decimal point.'''
minimum_wage_int = 15

# Float data type.
minimum_wage_float = 15.0

# A Python variable name cannot contain spaces.
# human development index = 0.9

# Illegal because variable names cannot begin
# with a digit.
# 3dGraph = 1

# Special characters like # should be avoided.
# Mixture#3 = 'Green and blue'

# Digits can be included in variable names so
# long as they are not the first character.

# The string literal 'Green and red' is being
# assigned to the variable named "mixture1".
mixture1 = 'Green and red'

# Variable names may begin with underscores.
_human_development_index = 0.8

noofpaidvacationdays = 35

'''
The two variations of "noOfPaidVacationDays"
written below should be used instead because
they are more readable than the above one.

In a program, only one variable containing this
name would be declared rather than three.'''

# Written with the snake case naming convention:
no_of_paid_vacation_days = 35

'''
The following is the camel case naming convention.

The first word starts with a lowercase letter.
Each subsequent word starts with an uppercase letter.'''
noOfPaidVacationDays = 35