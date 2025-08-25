# This is a single-line comment.
# Comments are notes written in a program.
# Comments are not only for the programmer to remember
# what their code did, but for others working with them
# on a team to understand the program.

# The computer ignores comments, but they help anyone
# reading your code comprehend what the code is doing.

# There are two integer variables declared on lines 17
# and 19.

# The assignment operator (=) tells us that two
# variables are being declared and initialised.

# The variable salami_pizza_pies is initialised with 10.
salami_pizza_pies = 10

bufalina_pizza_pies = 10

# Computing the sum of the two different pizza pies.

# The variable total_pizza_pies is assigned 20 because
# 20 is what is returned by the subsequent computation:
# salami_pizza_pies + bufalina_pizza_pies
total_pizza_pies = salami_pizza_pies + bufalina_pizza_pies

print("total_pizza_pies:", total_pizza_pies)

# Python's built-in input() function will prompt the user
# to enter something, and will return what they entered.

# The value returned by the input() function will be assigned
# to the pies_ordered variable as a string data type.
pies_ordered = input('\nHow many pizza pies would you like to order? ')

# Python's built-in type() function.

# type(pies_ordered) will return <class 'str'> because
# the string returned by the input() function on line 35
# was assigned to pies_ordered.

# The print() function will take what is returned
# by type(pies_ordered) and print it to the screen.
print('\ntype(pies_ordered):', type(pies_ordered))

print('\npies_ordered:', pies_ordered)

# Is 2 written without quotes surrounding it?
# Is 2 written without a decimal point?
# If the two above conditions were met, then the data
# type of 2 is an integer.
white_cat_drawings = 2
brown_cat_drawings = 2

# type(white_cat_drawings) returns the data type of the
# variable white_cat_drawings.
# In this case, because white_cat_drawings was assigned a
# number without quotes around it and without a decimal
# point, its data type is an integer.
print('type(white_cat_drawings):', type(white_cat_drawings))

total_cat_drawings = white_cat_drawings + brown_cat_drawings

print('\nwhite_cat_drawings:', white_cat_drawings)
print('brown_cat_drawings:', brown_cat_drawings)
print('total_cat_drawings:', total_cat_drawings)