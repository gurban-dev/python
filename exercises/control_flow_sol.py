items = ['apples', 'kefir', 'eggs']
prices = [0.95, 1.25, 2.99]

# Print out how many items there are.
print('len(items):', len(items))

# The input() function temporarily pauses the program
# and waits until the user inputs some data and clicks
# the "Enter" key on their keyboard.
choice = input('\nWhat would you like to buy? ').lower()

print('\nchoice:', choice)

# Reveal how many characters the user inputted.
print('\nlen(choice):', len(choice))

# The following is the equality operator:
# ==

# The equality operator tests if the operand on its left
# is equal to the one on its right.

# Python is case-sensitive when it comes to determining
# whether two strings are equal to each other.
print('\n"KEFIR" == "kefir":', "KEFIR" == "kefir")

print('\nchoice in items:', choice in items, '\n')

if choice in items:
	index = items.index(choice)

	# Capitalise the first letter of choice after
	# finding the index in "items" list.
	choice = choice.capitalize()

	price = prices[index]

	# Get the last letter in the item.
	if choice[-1] == 's':
		choice += " are"
	else:
		choice += " is"

	print(choice, "available.")
else:
	print("Sorry, we don't sell that item.")