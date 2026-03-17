import math

square_root = math.sqrt(144)

# Syntax:
# {variable:format_specifier}

# .2f indicates that the value stored in the variable
# square_root should be rounded to two decimal places.

# f indicates that the variable square_root is storing
# a floating-point number.

# 8 = width, < = left-align
print(f"Square Root: {square_root:<8.2f}")

# > = right-align
print(f"Square Root: {square_root:>8.2f}")

# ^ = center-align
print(f"Square Root: {square_root:^8.2f}")