# An integer variable.
house_price = 1000000

# A boolean variable.
has_good_credit = True

print('bool(has_good_credit):', bool(has_good_credit))

# The latest assigned value is exclusively the
# one looked at by the program.
# has_good_credit = False

# Assign True to has_good_credit was assigned True.
# Apply the "not" keyword to the has_good_credit
# variable.
print('\nnot has_good_credit:', not has_good_credit, '\n')

# not will negate a boolean value.
# If not is applied to True, True become False.
# The condition will evaluate to False and the program
# will flow to the else block.
if not has_good_credit:
	print('if block entered.')
	down_payment = 0.1 * house_price
else:
	print('else block entered.')
	down_payment = 0.2 * house_price

# A print statement with an f-string
# passed to it.
print(f"\nDown payment: ${down_payment}")