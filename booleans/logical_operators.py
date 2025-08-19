x = 3
y = 5

'''
The "and" operator connects two Boolean expressions
into one compound expression. Both subexpressions
must be true for the compound expression to be true.'''

'''
x is odd if x % 2 != 0
3 % 2 returns 1. != is called the not equal
operator.

1 != 0 evalutes to True.
5 % 2 returns 1. == returns True if the two values
being compared are equal to each other.
1 == 0 evalutes to False.
y is even if y % 2 == 0
'''
print('x % 2 != 0 and y % 2 == 0:', x % 2 != 0 and y % 2 == 0)

'''
The expression y >= x becomes 5 >= 3, which
evaluates to True.

The expression x > x becomes 3 > 3, which
evaluates to False.

Therefore: True and False yields False.'''
print('\ny >= x and x > x:', y >= x and x > x)

print('\nTrue and False:', True and False)

'''
The "or" operator connects two Boolean expressions
into one compound expression. One or both
subexpressions must be true for the compound
expression to be true. It is only necessary for
one of the subexpressions to be true, and it does
not matter which.'''

'''
x = 3
y = 5

The expression y < x becomes 5 < 3, which
evaluates to False.

The expression x < y becomes 3 < 5, which
evaluates to True.

Therefore: False or True yields True.'''
print('\ny < x or x < y):', y < x or x < y)

'''
The expression y < x becomes 5 < 3, which
evaluates to False.

The expression y < y becomes 5 < 5, which
evaluates to False.

Therefore: False or False yields False.'''
print('\ny < x or y < y:', y < x or y < y)

print('\nTrue or False:', True or False)

'''
The "not" operator is a unary operator, meaning it
works with only one operand. The operand must be
a Boolean expression. The not operator reverses
the truth of its operand. If it is applied to an
expression that is true, the operator returns false.

If it is applied to an expression that is false,
the operator returns true.'''

'''
x = 3
y = 5

The expression x >= y becomes 3 >= 5, which
evaluates to False.

Applying negation: not (3 >= 5) evaluates to
True.

Applying a second negation: not (not (3 >= 5))
evaluates to False.'''
print('\nnot (not x >= y):', not (not x >= y))

print('\nnot True:', not True)

print('\nnot False:', not False)

'''
x = 3
y = 5

(x % 2 != 0 and (y % 2 == 0 or (x == 3 and not y < 6)))
or (x > y and not y == 5) is False:
x % 2 != 0 is True

(y % 2 == 0 or (x == 3 and not y < 6))
is False:
y % 2 == 0 is False

(x == 3 and not y < 6) is False:
x == 3 is True
not y < 6 is False

(x > y and not y == 5) is False:
x > y is False
'''

# x = 3
# y = 5

# x % 2 != 0 -> True
# y % 2 == 0 -> False
# x == 3 -> True
# not y < 6 -> False
# (x == 3 and not y < 6) -> False

# x > y -> False
# not y == 5 -> False

# print(
#   (
#     True and
#     False
#   ) or
#   False
# )
print('\n(x % 2 != 0 and (y % 2 == 0 or (x == 3 and\nnot '
      'y < 6))) or (x > y and not y == 5):', (x % 2 != 0
       and (y % 2 == 0 or (x == 3 and not y < 6))) or \
       (x > y and not y == 5))

'''
Both the "and" and "or" operators perform short-circuit
evaluation. Here's how it works with the "and" operator:
If the expression on the left side of the "and" operator
is false, the expression on the right side will not be
checked. Because the compound expression will be false
if only one of the subexpressions is false, it would
waste CPU time to check the remaining expression. So,
when the "and" operator finds that the expression on its
left is false, it short-circuits and does not evaluate
the expression on its right.'''
print('False and True', False and True)

'''
Here's how short-circuit evaluation works with the "or"
operator: If the expression on the left side of the
"or" operator is true, the expression on the right side
will not be checked. Because it is only necessary for
one of the expressions to be true, it would waste CPU
time to check the remaining expression.'''
print('True or False:', True or False)