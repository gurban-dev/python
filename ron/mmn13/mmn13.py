# Question 1

def complement(lst):
    """
    Returns the complement of a list of natural
    numbers.

    The complement list includes all natural
    numbers from 1 to the maximum number in
    "lst" that do not appear in "lst".

    If "lst" is empty, the function returns an
    empty list.

    Constraints:
    -----------
    - Avoids using the 'in' operator for
    membership checks.
    - Uses basic Python constructs only (no
    dictionaries, no sorting).
    - Assumes all elements in lst are distinct
    natural numbers.

    Parameters
    ----------
    lst : list of int
    A list of distinct natural numbers.

    Returns
    -------
    list of int
    The complement of lst from 1 to max(lst),
    inclusive.
    """

    # Return an empty list if input is empty.
    if not lst:
        return []

    # Find the maximum value in lst.
    # max_value = find_max(lst)

    max_value = max(lst)

    # Initialize an empty list to hold the result.
    result = []

    # Loop through the range from 1 to max_value.
    for num in range(1, max_value + 1):
        # Flag to check if num is in "lst".
        found = False

        '''
        Loop through "lst" to check if num is present.

        The inner for loop is needed because it
        checks whether the current number in the
        range exists in "lst".'''
        for value in lst:
            if value == num:
                found = True
                break

        # If num is not found in lst, add it to result.
        if not found:
            result.append(num)

    return result

# Question 2

# Part A
def shift_k_right(lst, k):
    """
    Returns a new list after performing a right
    circular shift of size "k" on the input list.

    A right circular shift moves each element in
    the list to the right by "k" positions, wrapping
    elements around to the front of the list as needed.

    Parameters
    ----------
    lst : list
        The list to be shifted.

    k : int
        The number of positions to shift elements
        to the right.

    Returns
    -------
    list
        A new list that is the result of a right
        circular shift by "k" positions.

    Raises
    ------
    ValueError
        If "k" is negative or greater than the
        length of the list.
    """
    length = len(lst)

    # Ensure "k" is within a valid range.
    if k < 0 or k > length:
        raise ValueError(
            "Shift value k must be between 0 "
            "and the length of the list.")

    # Perform right circular shift using slicing.

    '''
    Suppose k = 1.
    
    lst = [1, 2, 3, 4, 5]

    lst[-1:] extracts the last k element.
    
    lst[:-1] extracts all elements up until
    the last k elements.

    lst[-1:] + lst[:-1]
    
    [5] + [1, 2, 3, 4]

    [5, 1, 2, 3, 4]
    '''
    return lst[-k:] + lst[:-k]

# Part B
def shift_right_size(a, b):
    """
    Determines the right circular shift size "k" that
    makes list "a" equal to list "b" after a shift.

    The function checks all possible right circular shifts
    from 0 to the length of the list and returns the first
    valid shift size that results in "b".

    As instructed, this function utilises shift_k_right()
    from part A of question 2.

    Parameters
    ----------
    a : list
        The original list to be shifted.

    b : list
        The target list to match after shifting.

    Returns
    -------
    int or None
        The shift size "k" that makes list "a" equal to
        list "b" after a right circular shift.

        "k" must be in [0, length] (inclusive).

        Returns None if no valid shift is found or if
        the lists are not of equal length.
    """

    # Check if the lists have the same length.
    if len(a) != len(b):
        return None

    # Iterate over all possible shift values.
    
	# Suppose the following:
    # a = [4, -1, 9, 7, 11, 2]
    # b = [11, 2, 4, -1, 9, 7]
    
	# for k in range(6):
    for k in range(len(a)):
        # 1st iteration:
        # shifted = shift_k_right(a, 0)

        shifted = shift_k_right(a, k)

        # Check if the shifted list matches the target.
        if shifted == b:
            return k

    # Return None if no valid shift is found.
    return None

# Question 3

def is_perfect(lst):
    """
    Determines if the given list is a 'perfect list'.

    A 'perfect list' is defined by the following conditions:
    - Starting from index 0, each value in the list represents
      the next index to visit.
    - Every index is visited exactly once.
    - The scan reaches an element with value 0.
    - The scan terminates at the index where the value is 0.

    Parameters
    ----------
    lst : list of int
        The list to be evaluated.

    Returns
    -------
    bool
        True if lst is a perfect list, False otherwise.

    Raises
    ------
    IndexError
        If an index outside the list is accessed.
    TypeError
        If any element in the list is not an integer.
    """

    # Handle empty list: it is considered perfect.
    if not lst:
        return True

    # Get the length of the list and
	# initialize tracking variables.
    length = len(lst)
    
	# Track visited indices.
    visited = [False] * length
    
	# Start scanning from index 0.
    index = 0
    
	# Flag to check if zero is found.
    zero_found = False
    
	# Count the steps to avoid infinite loops.
    steps = 0

    while True:
        # Ensure index is within bounds.
        if index < 0 or index >= length:
            raise IndexError("Index out of bounds during scan.")

        # Check if the current element is an integer.
        if not isinstance(lst[index], int):
            raise TypeError("List contains a non-integer value.")

        # If index has already been visited, return False.
        if visited[index]:
            return False

        # Mark the current index as visited.
        visited[index] = True

        steps += 1

        # Check if the value is 0, indicating termination.
        if lst[index] == 0:
            zero_found = True

            # Terminate the scan when reaching 0.
            break

        # Move to the next index as dictated by the current
		# value.
        index = lst[index]

    # Ensure all indices are visited and 0 was found.
    return all(visited) and zero_found

# Question 4

# Part A
def identity_matrix(mat):
    """
    Checks if the given 2D list is an identity matrix.

    An identity matrix is a square matrix with 1s on the main
    diagonal and 0s elsewhere. This function ensures that the 
    matrix is square and contains only integers. 

    Parameters:
    mat (list of list of int): A 2D list representing the
    						   matrix to be checked.

    Returns:
    bool: True if the matrix is an identity matrix, False
          otherwise.

    Raises:
    TypeError: If any element in the matrix is not an
     		   integer.
    IndexError: If the matrix is not square.
    """
    
    # Get the number of rows in the matrix.
    num_rows = len(mat)

    # Check if the matrix is square, i.e., all rows
    # should have the same length as num_rows.
    for row in mat:
        if len(row) != num_rows:
            raise IndexError("Matrix is not square")

    # Iterate through each element of the matrix.
    for i in range(num_rows):
        for j in range(len(mat[i])):
            # Ensure that every element is an integer.
            if not isinstance(mat[i][j], int):
                raise TypeError(
                    "Matrix contains a non-integer element")

            # Check identity matrix conditions.
            if i == j:
                # Diagonal elements must be 1.
                if mat[i][j] != 1:
                    return False
            else:
                # Off-diagonal elements must be 0.
                if mat[i][j] != 0:
                    return False

    # If all checks pass, the matrix is an
	# identity matrix.
    return True

# Part B
def create_sub_matrix(mat, size):
    """
    Returns a centered square submatrix of the given matrix.

    The submatrix has dimensions of size x size, where size
    is an odd positive integer, and is centered in the
    original matrix. It assumes that the given size is not
    larger than the number of rows in the matrix.

    Parameters:
    mat (list of list of int): A 2D list representing the
      						   square matrix.
    size (int): The size of the submatrix to extract, an
     			odd positive integer.

    Returns:
    list of list of int: A submatrix of the original
     					 matrix, with  dimensions size
                         x size, centered.

    Raises:
    IndexError: If not all rows in the matrix have
    			the same length.
    """
    
    # Get the number of rows in the matrix.
    num_rows = len(mat)

    # Ensure all rows have the same length to confirm
	# square matrix.
    for row in mat:
        if len(row) != num_rows:
            raise IndexError("Matrix is not square")

    # Calculate the center index of the matrix.
    center_index = num_rows // 2

    # Calculate half the size of the submatrix.
    half_size = size // 2

    # Determine the start and end indices for rows
	# and columns.
    start_row = center_index - half_size
    end_row = center_index + half_size + 1

    start_col = center_index - half_size
    end_col = center_index + half_size + 1

    # Create and return the submatrix by slicing the
	# original matrix.
    sub_matrix = []
    for i in range(start_row, end_row):
        sub_matrix.append(mat[i][start_col:end_col])

    return sub_matrix

# Part C
def max_identity_matrix(mat):
    """
    This function searches for the largest centered
    square submatrix within 'mat' that is an identity
    matrix.

    It checks progressively smaller odd-sized submatrices,
    starting from the largest possible size.

    An identity matrix has 1s along the main diagonal
    and 0s elsewhere. The function will return the size
    of the largest identity matrix found, or 0 if none
    is found.

    Parameters:
    mat (list of list of int): A 2D square matrix
    						   represented as a list
                               of lists. Each list
    						   corresponds to a row.
    
    Returns:
    int: The size of the largest identity matrix found
    	 within the matrix. If no identity matrix is
         found, returns 0.

    Raises:
    IndexError: If the matrix is not square (i.e., the
    			rows have different lengths).

    TypeError: If any element in the matrix is not an
    		   integer.
    """
    
    # Get the number of rows in the matrix. For
	# a square matrix, the number of rows equals
	# the number of columns.
    num_rows = len(mat)

    # Ensure that all rows in the matrix have the
	# same length, i.e., the matrix is square.
    for row in mat:
        if len(row) != num_rows:
            raise IndexError("Matrix is not square")

    # Check if all elements in the matrix are integers.
	# If any element is not an integer, raise a TypeError.
    for i in range(num_rows):
        for j in range(num_rows):
            if not isinstance(mat[i][j], int):
                print("TypeError raised in max_identity_matrix() function.")
                raise TypeError("Matrix contains non-integer elements")

    # Start with the largest possible odd-sized
	# submatrix and check down to size 1.
    for size in range(num_rows, 0, -1):
        # Ensure that the submatrix size is odd.
        if size % 2 == 1:
            # Calculate the center index and half the size
			# of the submatrix to extract a centered square
			# submatrix.
            
			# Middle index of the matrix.
            center_index = num_rows // 2
            
			# Half of the size of the submatrix.
            half_size = size // 2
            
			# Starting row index for the submatrix.
            start_row = center_index - half_size
            
			# Ending row index for the submatrix (inclusive).
            end_row = center_index + half_size + 1

            # Starting column index for the submatrix.
            start_col = center_index - half_size

            # Ending column index for the submatrix (inclusive).
            end_col = center_index + half_size + 1

            # Extract the submatrix of the current size.
            sub_matrix = []
            for i in range(start_row, end_row):
                sub_matrix.append(mat[i][start_col:end_col])

            # Check if the submatrix is an identity matrix.
            is_identity = True
            for i in range(size):
                for j in range(size):
                    if i == j:
                        # Check the diagonal elements.
                        if sub_matrix[i][j] != 1:
                            is_identity = False
                            break
                    else:
                        # Check the non-diagonal elements.
                        if sub_matrix[i][j] != 0:
                            is_identity = False
                            break
                if not is_identity:
                    break

            # If an identity matrix is found, return its size.
            if is_identity:
                return size

    # If no identity matrix is found, return 0.
    return 0