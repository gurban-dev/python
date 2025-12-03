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

# Notice that lists always use square brackets [].
# In other programming languages they're called "arrays",
# but in Python they're called "lists".

for colour in colours:
  print('colour:', colour)
print()

for letter in 'wordwoll':
  print(letter)

# The following Python list has indexes.
# The first index begins at 0.
# The first element has an index of 0.

# Indexes:
#          0        1       2
pets = ['Kitten', 'Cat', 'Parrot']

# Access the element stored at index 0.
print('\npets[0]:', pets[0])

print('\npets[2]:', pets[2])

# Keep in mind that the largest index in the list is
# 2. Notice how the largest index is one less than
# the size or the number of elements inside the list.
# print('\npets[3]:', pets[3])

if pets[1] == 'Cat':
  print('\nThe item at index 1 is \'Cat\'.')

if pets[-1] == 'Parrot':
  print('\nThe item at index -1 is \'Parrot\'.')