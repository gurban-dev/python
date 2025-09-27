# In Python, an f-string (short for formatted string
# literal) lets you put variables directly inside a
# string literal using {} (curly braces). This makes
# your code shorter and easier to read.

name = "Herodotus"
century = 5

# Using an f-string.
print(f"The father of history is {name}.\n"
      f"He lived during the {century}th century BC.")

'''
Practice Exercise

Create three variables:
fruit → your favorite fruit (string)

color → the color of that fruit (string)

times_per_week → how many times you eat it in a week (integer)


Use an f-string to print a sentence about your fruit:
E.g.
My favourite fruit is banana. It is yellow, and I eat it
3 times per week.
'''
fruit = 'apple'

color = 'green'

times_per_week = 5

print(f'\nMy favourite fruit is {fruit}. It is '
      f'{color}, and\nI eat it {times_per_week} '
      f'times per week.')