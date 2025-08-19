'''
Function: identity_matrix
This function checks whether a given 2D list
is an identity matrix.

An identity matrix must be square and contain
only integers.

All diagonal elements must be 1, and all
off-diagonal elements must be 0.

Raises a TypeError if any element is not an
integer.

Raises an IndexError if the matrix is not
square.'''

def identity_matrix(mat):
	# Get number of rows in matrix.
	num_rows = len(mat)

	# Check that matrix is square: each row
	# must have the same length as num_rows.
	for row in mat:
		if len(row) != num_rows:
			raise IndexError("Matrix is not square")

	# Check every element in the matrix.
	for i in range(num_rows):
		for j in range(len(mat[i])):
			# Check if element is an integer.
			if not isinstance(mat[i][j], int):
				raise TypeError("Matrix contains a non-integer element")

		# Check identity matrix conditions.
		if i == j:
			# Diagonal elements must be 1.
			if mat[i][j] != 1:
				return False
		else:
			# Off-diagonal elements must be 0.
			if mat[i][j] != 0:
				return False

	# At this point in the program, all conditions
	# are satisfied, so return True.
	return True