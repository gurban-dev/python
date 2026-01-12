fruits = ['persimmon', 'mango', 'pineapple']

# Syntax for writing a list comprehension:
# [<item> for <variable> in <iterable>]

# <item> is what you want to include in the new list, <variable> is
# the temporary name you give to each element as you loop, and
# <iterable> is the collection you're looping over.

lst = [fruit for fruit in fruits]

# for fruit in fruits iterates or loops over every single
# item inside 'fruits'.

# The first 'fruit' specifies what will be included in the new list.
# Here, we include each fruit itself.

print('lst:', lst)