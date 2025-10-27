watermelon_on_sale = False
it_is_sunny = True

# Output:
# watermelon_on_sale and it_is_sunny: False
print('watermelon_on_sale and it_is_sunny:',
      watermelon_on_sale and it_is_sunny)

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