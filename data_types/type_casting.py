# Explicit type casting is done manually by the programmer using
# built-in functions like int(), float() or str().

# A common use case of type casting is converting user input which
# is always returned as a string by the input() function, to a numeric
# type to perform computations.

int_numeral = int(input('Enter a numeral with a decimal point: '))

# Notice how inputting 1.5 when prompted by the input() function and
# then explicitly casting it as an integer with the int() function
# raises an exception.

# The downside of explicit type converson from a float to an int is
# that accuracy is reduced:
# 1.5 -> 1

print('type(int_numeral):', type(int_numeral), '\n')

float_numeral = float(input('Enter a numeral with a decimal point: '))

print('type(float_numeral):', type(float_numeral))

# Implicit type casting is performed automatically by Python when combining
# different data types in an expression:
sum = 0 + .0

# Before .0 is added to 0, Python internally converts 0 to .0.

# When an int and a float are used in the same arithmetic expression, the
# int is converted to a float.