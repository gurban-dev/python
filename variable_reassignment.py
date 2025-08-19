'''
This program demonstrates variable re-assignment.
Assign a value to the dollars variable.

2.75 is a floating-point number which means
that the variable "dollars" will be of the
float data type.'''
dollars = 2.75

'''
The comma in a print statement automatically
appends or adds a whitespace character before
the end or the beginning of a string literal.'''
print('I have', dollars, 'in my account.')

# With f-string
# print(f'I have {dollars} in my account.')

'''
Reassign dollars so it references a different
value.

The original value of 2.75 was overwritten with
99.95 because of re-assigning a value to an
existing variable. This process is called
variable re-assignment.'''
dollars = 99.95
print('But now I have', dollars, 'in my account!')

print(f"\nBefore type(dollars): {type(dollars)}")

'''
"dollars" was initially a float, but because
it was assigned the string literal "nothing",
its data type became a string.

Unline other programming languages, in Python
this is legal.'''
dollars = "nothing"

print(f"After type(dollars): {type(dollars)}")

print(f'\nUnfortunately, now I have {dollars} in my account!')