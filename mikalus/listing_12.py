mat = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]

# Integer/floor division, so only
# an integer is returned.
index1 = 2 // 4

index2 = 5 % 3

print('mat[index1]:', mat[index1])

'''
The second pair of square brackets, references
an element inside of the list referenced by
the first pair of square brackets.

mat[index1] returns [0, 1, 2]'''
print('\nmat[index1][index2]:', mat[index1][index2])

# The above line outputs the same as
# the ones below.
first_element = mat[index1]

print('first_element[index2]:', first_element[index2])