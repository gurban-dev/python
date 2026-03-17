# The open and closed square brackets indicate that
# the following is a list.

# In other programming languages, a list is often
# called an "array".

# A list a data structure that is made up of ordered
# elements/items separated by commas.
list_data_structure = [
  'First element',
  'Second element',
  'Third element'
]

print('list_data_structure:', list_data_structure, '\n')

# The below list data structure stores four elements:
# 'lilac'
# 'turquoise'
# 'magenta'
# 'black'
colours = ['lilac', 'turquoise', 'magenta', 'black']

print(f'type(colours): {type(colours)}\n')

# What is the data type of each of these elements?
# Hint: Notice how they all have quotation marks around them.

# Notice that lists always have square brackets [].
# In other programming languages they're called "arrays",
# but in Python they're called "lists".

# For loop.
for letter in ['a', 'b', 'c']:
  print('letter:', letter)
print()

for letter in 'abc':
  print('letter:', letter)

# The following Python list has indexes.
# The first index begins at 0.
# The first element has an index of 0.

# Indexes:
#           0        1       2
animals = ['Giraffe', 'Panda', 'Hedgehog']

# Access the element stored at index 0.
print('\nanimals[0]:', animals[0])

print('\nanimals[2]:', animals[2])

# Keep in mind that the largest index in the list is
# 2. Notice how the largest index is one less than
# the size or the number of elements inside the list.
# print('\nanimals[3]:', animals[3])

if animals[1] == 'Cat':
  print('\nThe item at index 1 is \'Panda\'.')

# Check if the last item is equal to 'Parrot'.
if animals[-1] == 'Hedgehog':
  print('\nThe item at index -1 is \'Hedgehog\'.')
elif animals[-1] == 'Giraffe':
  print('\nThe item at index -1 is \'Giraffe\'.')
else:
  print('The last element is neither a \'Hedgehog\' nor \'Giraffe\'.')