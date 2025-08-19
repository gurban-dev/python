def max_identity_matrix(mat):
    # Get the number of rows in the matrix.
    num_rows = len(mat)

    # Ensure all rows have the same length
	# (i.e., the matrix is square).
    for row in mat:
        if len(row) != num_rows:
            raise IndexError("Matrix is not square")

    # Check if all elements are integers.
    for i in range(num_rows):
        for j in range(num_rows):
            if not isinstance(mat[i][j], int):
                raise TypeError("Matrix contains non-integer elements")

    # Start with the largest possible odd-sized
	# submatrix and check down to 1.
    for size in range(num_rows, 0, -1):
        # Ensure the submatrix is odd-sized.
        if size % 2 == 1:
            # Get the centered submatrix of the current size.
            center_index = num_rows // 2
            half_size = size // 2
            start_row = center_index - half_size
            end_row = center_index + half_size + 1
            start_col = center_index - half_size
            end_col = center_index + half_size + 1

            # Create the submatrix.
            sub_matrix = []

            for i in range(start_row, end_row):
                sub_matrix.append(mat[i][start_col:end_col])

            # Check if the submatrix is an identity matrix.
            is_identity = True

            for i in range(size):
                for j in range(size):
                    if i == j:
                        if sub_matrix[i][j] != 1:
                            is_identity = False
                            break
                    else:
                        if sub_matrix[i][j] != 0:
                            is_identity = False
                            break
                if not is_identity:
                    break

            # If identity matrix is found, return its size.
            if is_identity:
                return size

    # If no identity matrix is found, return 0.
    return 0