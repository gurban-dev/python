'''
Concepts:
Floats (decimal numbers like 49.99)
Booleans (True or False)
The type() function (to check data types)
String concatenation (joining text with +)
'''

# Task 1:
# Create a variable called pet_name and set it to your pet's name (a string).

# Imagine someone hands you a label on a envelope named "pet_name".
# You open the letter and find a address.

# You go to the address and find the value "Fluffy".

# Example:
pet_name = "Fluffy"

# Assigning a different data type to a variable is
# legal because Python is a dyanmically-typed programming
# language.
# pet_name = 10

# Print out the memory address that "pet_name" points to.
# This memory disappears when the runtime of this Python
# program if finished. 
print('hex(id(pet_name)):', hex(id(pet_name)))

# Create a variable called pet_price and set it to a
# decimal number (float).
# Example:
pet_price = 49.99

# Create a variable called is_friendly and set it to
# True or False (boolean).
# Example:
is_friendly = True

# Task 2:
# Use print() and type() to see what type pet_name is.
# Example:
# Output: <class 'str'>
print('\ntype(pet_name):', type(pet_name))

# Use print() and type() to see what type pet_price is.
# Output: <class 'float'>
print('\ntype(pet_price):', type(pet_price))

# Use print() and type() to see what type is_friendly is.
# Output: <class 'bool'>
print('\ntype(is_friendly):', type(is_friendly))

# Task 3:
# Create a variable called pet_weight with a decimal
# number (how many kilograms?)
pet_weight = 5.5

# Create a variable called needs_grooming with True or False.
needs_grooming = False

# Task 4:
# Create a welcome message using + to join strings
# Example: message = "Welcome! Meet " + pet_name + "!"
# Then print your message
print('\nWelcome ' + pet_name + ".")

# Create a price message that says how much your pet costs
# Hint: You need to convert pet_price to a string using str()
# Example: "This pet costs $" + str(pet_price)

'''
pet_price = 49.99

The effect of str(pet_price):
49.99 -> "49.99"
'''

print("\nThis pet costs " + str(pet_price) + ".")

# Task 5:
# Print a sentence that tells if your pet is friendly.

'''
is_friendly = True

The effect of str(is_friendly):
True -> "True"
'''
print("\n" + pet_name + " is friendly: " + str(is_friendly) + ".")