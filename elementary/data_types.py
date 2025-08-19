# In Python, text that is surrounded by quotes,
# are called string literals. They could be
# surrounded by either "double quotes" or 'single
# quotes'.

# "Emilka" is not only a string, but also a string
# literal because it is enclosed by quotes.

# Assigning a string literal to a variable means
# that the data type of that variable will be a
# string.

# cat_name refers to the string object that was
# created in memory.
cat_name = "Emilka"

# A whole number without quotes, is an integer.
# The data type of the variable "no_of_houses"
# is an integer.
no_of_houses = 2

# This is how old the cat is. It's a number with
# a decimal, like 0.5.

# Numbers with decimals are called floating-point numbers.
# Assigning a floating-point number to a variable means
# that variable will be of the float data type.
kitten_age = 0.5

# cat_age is also a float.
cat_age = 2.0

print('type(cat_age):', type(cat_age))

# This is a True or False fact. This cat likes
# milk, so we write True (with a capital T).
likes_milk = True

# Now we want to say something about the cat!
# The print() function lets us show a message on
# the screen.

# The print() function is given eight pieces of data
# (these pieces of data are called arguments):
# 1. The variable that stores the cat's name (cat_name)
# 2. The string literal 'is'
# 3. The variable that stores the cat's age (cat_age)
# 4. The string literal 'years old.'
# 5. cat_name
# 6. The string literal 'has'
# 7. The variable storing the number of houses (no_of_houses)
# 8. The string literal 'houses.'

# Each piece is separated by a comma. When you use
# commas in print(), Python adds a space between
# each part automatically.
print(cat_name, 'is', cat_age, 'years old.',
      cat_name, 'has', no_of_houses, 'houses.')