'''
1. Describe in your own words each of the following logical operators:

not
The "not" operator reverses (negates) a Boolean value.
If the value is True, "not" makes it False.
If the value is False, "not" makes it True.

and
The "and" operator returns True only if both operands are True.
If at least one operand is False, the result is False.

or
The "or" operator returns True if at least one operand is True.
It only returns False when both operands are False.


2. Write down the expected output of each instruction.

a = True
b = False

print('not(a):', not(a))
print('\nnot(b):', not(b))

Step-by-step evaluation:

not(a)
a = True
not(True) -> False

not(b)
b = False
not(False) -> True

Expected output:

not(a): False

not(b): True


3. Write down the expected output of each instruction.

a = False
b = False

x = not(a)
y = not(b)

Evaluate x and y first:

x = not(False) -> True
y = not(False) -> True

Now evaluate each print statement:

print('\na or b:', a or b)
False or False -> False

print('\nx and a:', x and a)
True and False -> False

print('\ny or b:', y or b)
True or False -> True

print('\nb and y:', b and y)
False and True -> False


Expected output:

a or b: False

x and a: False

y or b: True

b and y: False
'''