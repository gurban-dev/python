# Floating-point number (data type: float).
total = 100.156

# print() inserts a space between arguments when multiple arguments
# are separated by commas.
print('total:', total)

'''
{total:.2f} -> placeholder used in an f-string to format a value.

total -> the variable whose value will be formatted.

: -> begins the format specification.

.2 -> precision (two digits after the decimal).

f -> display the number in decimal form with a fixed number of digits
     after the decimal.

.2f -> round and display exactly two digits after the decimal.
'''
print(f'\ntotal with string formatting: {total:.2f}')

# Note how the value referenced by the variable 'total' has not changed.

# Formatting only affects how the value is displayed. It does not modify
# the value stored in the variable.

print(f"\n{{2.155:.2f}}: {2.155:.2f}")

# 2.155 rounds to 2.15 because the float stored by Python is actually
# slightly smaller than 2.155 due to binary floating-point approximation.

# The value printed below reveals the decimal representation of the
# closest binary floating-point number stored for 2.155.

# This can be verified by executing the following:
print("\nformat(2.155, \".17f\"):", format(2.155, ".17f"))