# Explicit type casting is done manually by the programmer using
# built-in functions like int(), float() or str().

# A common use case of type casting is converting user input which
# is always returned as a string by the input() function, to a numeric
# type to perform computations.

# Initialise 'int_number' with None as opposed to 0 because there
# should not be the false impression that the end user inputted 0.
int_number = None

try:
    # int() can only convert strings that represent whole numbers (no decimal
    # point).

    # If the user enters a value like "1.5", Python raises a ValueError because
    # "1.5" is not a valid base-10 integer literal.

    # A base-10 integer literal is a number composed of only digits 0-9 with
    # no decimal point.
    int_number = int(input('Enter a number with a decimal point (e.g., 1.5): '))
except ValueError as err:
    print(f"Invalid input: {err}")

# Uncomment the ensuing line to see what happens to the program
# when the exception is not caught.
# int_number = int(input('Enter a number with a decimal point (e.g., 1.5): '))

# Notice how inputting 1.5 when prompted by the input() function and
# then explicitly casting it as an integer with the int() function
# raises an exception.

# The downside of explicit type converson from a float to an int is
# that accuracy is reduced due to the loss of the fractional part
# of the number:
# 1.5 -> 1

print('\ntype(int_number):', type(int_number), '\n')

float_number = float(input('Enter a number with a decimal point: '))

print('type(float_number):', type(float_number))

# Implicit type casting is performed automatically by Python when
# combining different data types in an expression:
sum = 0 + .0

# Because one operand is a float, Python converts the integer 0 to 0.0
# and performs floating-point addition.

# When an int and a float are used in the same arithmetic expression,
# the int is converted to a float.