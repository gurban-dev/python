'''
if-else statement structure:

if condition:
 	instruction
else:
  	instruction
'''

likes_vanilla = True

vanilla_orders = 0

if likes_vanilla:
  	vanilla_orders += 1
else:
	# pass acts as a placeholder.

	# It's used when you syntactically need to write an
	# instruction/statement, but don't need to execute
	# an action.
	pass

print('vanilla_orders:', vanilla_orders)