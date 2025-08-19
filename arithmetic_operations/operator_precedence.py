"""
Operator precedence or order of operations:
1. Parentheses ()

2. Exponentiation **

These operators have the same precedence level:
3. Multiplication *,
   Float division /,
   Integer or floor division //,
   and remainder (modulo) %

4. Addition and subtraction: + -

The multiplication ( * ), floating-point division ( / ),
integer division ( // ), and remainder ( % ) operators
have the same precedence.

The addition ( + ) and subtraction ( - ) operators
likewise have the same precedence.

When two operators with the same precedence level
share an operand, the operators execute from left
to right.

The multiplication and float division operators
share the operand 5 in the below example.

E.g.
2 * 5 / 5

What is the use case for arithmetic operations?
"""

"""
Removing the parentheses in the below expression
doesn't alter the outcome because multiplication ( * )
has a higher precedence level than addition ( + )."""
weekly_earnings = 10 + (20 * 30)

print(f'weekly_earnings: {weekly_earnings}')

"""
Are the values of the expressions 4 / (3 * (2 - 1))
and 4 / 3 * (2 - 1) the same?

4 / (3 * (2 - 1)) -> 4 / (3 * (1)) -> 4 / 3

4 / 3 * (2 - 1) -> 4 / 3 * (1) -> 4 / 3

The answer is yes because division and multiplication
have the same precedence level and removing the
parentheses around 3 * (2 - 1) doesn't change the
order of operations.

Removing the parentheses from (2 - 1) would indeed
change the calculation because rather than subtracting
1 from 2 first, 4 / 3 would be multiplied by 2.
"""
num1 = 4 / (3 * (2 - 1))

print(f'\nnum1: {num1}')

num2 = 4 / 3 * (2 - 1)

print(f'\nnum2: {num2}')

# / is called floating-point or
# float division.
num3 = 4 / (3 * 2 - 1)

print(f'\nnum3: {num3}')

# // is integer or floor division.
# This means that only an integer can be
# returned from a computation.
num4 = 4 // (3 * 2 - 1)

print(f'\nnum4: {num4}')

# Five fits into four zero times.
# Thus, zero is returned.
num5 = 4 // 5

print(f'\nnum5: {num5}')

# Python has a built-in method called
# type() for revealing the data type
# of variables.
print(f'\ntype(10.0): {type(10.0)}')

'''
6 % 5 (six modulo five) is equal to 1.

5 can fully fit into 6 one time.
However, there is still a remainder of 1
because 5 * 1 = 5 and 6 - 5 = 1.

There is still a remainder of 1 after
the number 5 has been fully fit into 6
the most number of times it can be.

6 is congruent to 1 mod 5.

6 - 1 = 5 and 5 can be divided evenly by 5.

When 6 is divided by 5, there is a remainder of
1 because 6 cannot be evenly divided by 5.'''
num6 = 6 % 5

print(f'\nnum6: {num6}')

# 3 % 5 = 3
num7 = 3 % 5

'''
3 is congruent to 3 mod 5.
3 - 3 = 0 and 0 can be
divided evenly by five.

Zero divided by anything will
not have any remainder.

When the number of the right side of the
remainder operator (%) is larger than the
number on the left side, the expression
will evaluate to the value of the number
on the left side.'''

'''
99 is congruent to 99 mod 100.

99 - 99 = 0 and 0 can be divided evenly
by 100 or anything.

Therefore, subtracting 99 from 99
will allow the result to be divided
evenly by 100.'''
num8 = 99 % 100

print(f'\nnum8: {num8}')

'''
61 is congruent to 1 mod 10.

61 - 1 = 60 and 60 can be
evenly divided by 10.'''
num9 = 61 % 10

print(f'\nnum9: {num9}')