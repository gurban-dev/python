'''
Function: create_sub_matrix
This function returns a square submatrix of
the given matrix 'mat'.

The submatrix is of size 'size' x 'size'
and is centered in the original matrix.

It assumes 'size' is an odd positive integer
not larger than the number of rows in 'mat'.

Raises IndexError if not all rows in the matrix
have the same length (i.e., not truly square).'''
def create_sub_matrix(mat, size):
	# Get the number of rows in the matrix.
	num_rows = len(mat)

	# Ensure that all rows are the same length
	# to confirm the matrix is square.
	for row in mat:
		if len(row) != num_rows:
			raise IndexError("Matrix is not square")

	# Calculate the center index of the matrix.
	center_index = num_rows // 2

	# Calculate the half size of the submatrix.
	half_size = size // 2

	# Determine the starting and ending indices
	# for rows and columns.
	start_row = center_index - half_size
	end_row = center_index + half_size + 1

	start_col = center_index - half_size
	end_col = center_index + half_size + 1

	# Create and return the submatrix by slicing
	# the original matrix.
	sub_matrix = []

	for i in range(start_row, end_row):
		# Append a slice of each row to the submatrix
		sub_matrix.append(mat[i][start_col:end_col])

	return sub_matrix