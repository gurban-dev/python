# In Python, short-circuit evaluation means:
# Python stops checking the rest of a logical expression as soon as the
# result is known.

# - For 'and', if the first condition is False, the second is not evaluated.
# - For 'or', if the first condition is True, the second is not evaluated.

# This can save time and prevent unnecessary computations.

def check():
    print("Checked!")

    return True

# Since the first subexpression evaluates to False, the Python
# interpreter won't check the second subexpression to determine
# the final outcome of this compound expression because it already
# knows that the entire expression will return False since the
# 'and' operator requires that both subexpressions evaluate to True.

# "Checked!" is never printed.
print('False and check():', False and check(), '\n')

# check() is evaluated since the interpreter doesn't yet know what
# the compound expression evaluates to by simply looking at the first
# subexpression (False). This is because the or logical operator
# requires that only one subexpression must evaluate to True in order
# for the entire expression to also evaluate to True.
print('False or check():', False or check())

# In the below example, the interpreter realises that the first
# subexpression evaluates to True, and since the 'or' operator
# requires only one of the subexpressions to be True, it already
# knows that the entire expression will evaluate to True.

# "Checked!" is never printed.
print('\nTrue or check():', True or check())

it_is_sunny = False
watermelon_on_sale = True

# Output:
# it_is_sunny and watermelon_on_sale: False
print('\nit_is_sunny and watermelon_on_sale:',
      it_is_sunny and watermelon_on_sale)

'''
Python stops evaluating as soon as the outcome is known:
- For 'and', if the first is False, the second is not checked.
- For 'or', if the first is True, the second is not checked.
'''

# Output:
# watermelon_on_sale or it_is_sunny: True
print('\nwatermelon_on_sale or it_is_sunny:',
      watermelon_on_sale or it_is_sunny)