# In Python, an f-string (short for formatted string
# literal) lets you put variables directly inside a
# string literal using {} (curly braces). This makes
# your code shorter and easier to read.

name = "Herodotus"

century = 5

# Using an f-string requires preceding the quotation marks
# with a lowercase f.

# The f before the string tells Python to evaluate expressions
# inside the curly braces {} and insert the result into the
# string before printing.
print(f"The father of history is {name}.\n"
      f"He lived during the {century}th century BC.\n")

# An advantage of using f-strings is that variables that reference
# integers, are automatically converted to strings.

# Without an f-string:
print("The father of history is " + name + ".\n"
      "He lived during the " + str(century) + "th century BC.\n")

'''
Practice Exercise

Create three variables:
fruit -> your favorite fruit (string)

colour -> the colour of that fruit (string)

times_per_week -> how many times you eat it in a week (integer)


Use an f-string to print a sentence about your fruit:
E.g.
My favourite fruit is banana. It is yellow, and I eat it
3 times per week.
'''
fruit = 'apple'

colour = 'green'

times_per_week = 5

print(f'My favourite fruit is {fruit}. It is '
      f'{colour}, and\nI eat it {times_per_week} '
      f'times per week.')