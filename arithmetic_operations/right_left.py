"""
Most operators in Python have left-to-right
associativity.

This entails evaluating expressions from left-to-right.

There is an exception to the left-to-right rule.
When two ** (pairs of asterisk operators) share
an operand, the operators execute right-to-left.

For example, the expression
2**3**4 is evaluated as 2**(3**4)."""
num = 2**3**4

"""
num = 2**3**4

3 ** 4 = 81

num = 2**81

2**81 = 2417851639229258349412352

num = 2417851639229258349412352
"""

print(f'num: {num}')