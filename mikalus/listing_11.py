'''
The "not" keyword in Python is a logical operator
used to invert the logical value of a boolean
expression. In other words, it negates or reverses
a boolean value, so the inverse of that value is
returned.

It is a unary operator, meaning it operates on
a single operand.'''
ex1 = not (bool(0) or bool(True))

'''
Keep in mind that bool(0) evaluates to False
because 0 is considered falsy in Python.

Similarly, as seen below, bool("") evaluates to
False because an empty string is also considered
falsy.

bool(True) is merely True because the "True"
keyword is explicitly passed to the bool()
function.'''
print('bool(0):', bool(0))

print('bool(True):', bool(True))

print(f'ex1: {ex1}')

'''
not bool("") evaluates to True because the
empty string ("") is falsy, so it evalutes
to False, and then the "not" operator
negates this value.

3.14 is considered truthy because it is not
equal to zero. Truthy values evaluate to
True.'''
ex2 = not bool("") and bool(3.14)

print('\nbool(""):', bool(""))

'''
An empty string is considered falsy, meaning
that it evalutes to False in a boolean context.

Negating this False value with the "not" keyword
inverts it, so it becomes True.'''
print('not bool(""):', not bool(""))

'''
bool(3.14) evaluates to True because any number
that is not equal to zero is considered truthy
in Python.'''
print('bool(3.14):', bool(3.14))

print(f'ex2: {ex2}')