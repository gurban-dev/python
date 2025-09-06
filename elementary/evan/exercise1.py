'''
Directions:

1. Create a variable called given_name and assign it
   your name as a string.

2. Create a variable called age and assign it your age
   as an integer.

3. Create a variable called likes_cat_drawings and assign
   it the value True (because you like cat drawings!).

4. Use the print() function to print a sentence that says:

Hello, my name is [given_name], I am [age] years old, and
it is [likes_cat_drawings] that I like cat drawings!

Replace the brackets with the values of your variables
by using the variable names.

5. Now, ask the end user to type their favourite colour
   using the input() function and store it in a variable
   called favourite_colour.

6. Print a sentence that says:
   Your favourite colour is [favourite_colour]!
'''

# given_name is the name of the variable.

# The equals sign (=) in mathematics is called the
# assignment operator in programming.

# 'Sofiia' is the value assigned to given_name.

# What you see on the left side of the assignment
# operator is the variable.
# given_name in this case.
given_name = 'Sofiia'

# Remember:
# What you see on the right side of the assignment
# operator is the value being assigned to the variable.
# 9 in this case.
age = 9

# Boolean data type.
likes_cat_drawings = True

# F-string must begin with a lowercase f that comes
# before the pair of quotes.

# To include variables in an f-string, you must
# surround them with curly braces.
print(f'Hello, my name is {given_name}, I am {age} years old, and '
      f'it is {likes_cat_drawings} that I like cat drawings!')

# What you see on the left side of the assignment
# operator (=) is the variable.
favourite_colour = input('\nInput your favourite colour: ')

print(f'\nYour favourite colour is {favourite_colour}!')