watermelon_on_sale = True
it_is_sunny = False

# Output:
# it_is_sunny and watermelon_on_sale: False
print('it_is_sunny and watermelon_on_sale:',
      it_is_sunny and watermelon_on_sale)

'''
Python performs short-circuit evaluation on the above
boolean expression because it realises that the first
condition is False and both conditions must be True in
order for the compound expression to evaluate to True.

For the subsequent compound expression, only one of the
conditions must evaluate to True for the compound expression
to be True because of the "or" operator.
'''

# Output:
# watermelon_on_sale or it_is_sunny: True
print('\nwatermelon_on_sale or it_is_sunny:',
      watermelon_on_sale or it_is_sunny)