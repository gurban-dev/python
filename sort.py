'''
The sort() method sorts items in the list so that they
appear in ascending order (from the smallest value to
the largest value).

If the list contains alphabetical characters, the
sort() method sorts the characters in alphabetical
order.'''

letters = ['C', 'B', 'A']

letters.sort()

print('letters:', letters)

numbers = [3, 2, 1]

numbers.sort()

print(f'\nnumbers: {numbers}')

# Assigning True to the reverse parameter will sort the
# list in descending order (largest to smallest).
numbers.sort(reverse=True)

print(f'\nnumbers: {numbers}')