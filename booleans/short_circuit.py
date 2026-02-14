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
print(False and check())

# In the below example, the Python interpreter realises that the
# first subexpression evaluates to True, and since the 'or' operator
# requires only one of the subexpressions to be True, it already knows
# that the entire expression will evaluate to True.

# "Checked!" is never printed.
print(True or check())

watermelon_on_sale = True
it_is_sunny = False

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