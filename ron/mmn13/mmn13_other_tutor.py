#Question 1:Complement Function
def complement(lst):
    """
    Returns a list of natural numbers not present in lst,
    starting from 1 up to the maximum value in lst.

    Parameters:
    lst (list): A list of unique natural numbers (positive integers).

    Returns:
    list: A list of missing natural numbers from 1 to max(lst).

    Notes:
    - Does not sort lst.
    - Does not use 'in' outside of for loops.
    - Returns [] if lst is empty.
    """
    if lst == []:
        return []

    max_val = max(lst)
    missing = []

    for num in range(1, max_val + 1):
        found = False
        for item in lst:
            if item == num:
                found = True
                break
        if not found:
            missing.append(num)

    return missing


#Question 2A: shift_k_right Function
def shift_k_right(lst, k):
    """
    This function performs a rightward circular shift on the input list by k positions.
    
    Parameters:
    lst (list): A list of elements to be shifted
    k (int): The number of positions to shift to the right
    
    Returns:
    list: A new list after performing the right circular shift
    
    Raises:
    ValueError: If k is negative or greater than the length of lst
    """

    # Handle the case when the list is empty
    if len(lst) == 0:
        return lst

    # Check for invalid shift amount
    if k < 0 or k > len(lst):
        raise ValueError("Shift amount must be non-negative and not greater than the list length.")

    # If shift is 0, return the original list
    if k == 0:
        return lst[:]

    # Perform the circular right shift
    # Last k elements come first, then the remaining elements
    return lst[-k:] + lst[:-k]

#Question 2B: shift_right_size function
def shift_k_right(lst, k):
    # Helper function from 2A (must be present for 2B to work)
    if len(lst) == 0:
        return lst

    if k < 0 or k > len(lst):
        raise ValueError("Shift amount must be non-negative and not greater than the list length.")

    if k == 0:
        return lst[:]

    return lst[-k:] + lst[:-k]

def shift_right_size(a, b):
    """
    Returns the smallest shift k such that shifting list a to the right by k gives list b.
    Returns None if not possible.
    """
    if len(a) != len(b):
        return None

    for k in range(len(a)):
        if shift_k_right(a, k) == b:
            return k

    return None

#Question 3: Index Based Scanning for perfect 
def is_perfect(lst):
    """
    Checks if a list is 'perfect' by following a value-guided scan.

    A list is perfect if:
    1. All elements are visited exactly once starting at index 0.
    2. The scan ends when the value at the current index is 0.

    Parameters:
    lst (list): A list of integers.

    Returns:
    bool: True if the list is perfect, False otherwise.

    Raises:
    IndexError: If a jump goes out of list bounds.
    TypeError: If any list element is not an integer.
    """

    if lst == []:
        return True  # Empty list is considered perfect

    n = len(lst)
    visited = [False] * n
    current = 0
    count = 0

    while True:
        # Check for out-of-bounds index
        if current < 0 or current >= n:
            raise IndexError("Index out of bounds during scan.")

        # Retrieve the value (raises TypeError if it's not an integer)
        val = lst[current]

        # Check if we've already visited this index
        if visited[current]:
            return False  # Not perfect due to repeat

        visited[current] = True
        count += 1

        if val == 0:
            return count == n  # Must end on 0 after visiting all once

        current = val  # Jump to the next index

#Question 4: identity matrices and submatrix operations
#Question 4A:function named identity_matrix
def identity_matrix(mat):
    """
    Checks whether a given 2D list is an identity matrix.

    Returns:
    - True if it is an identity matrix.
    - False otherwise.

    Raises:
    - TypeError: if any value in mat is not an int.
    - IndexError: if mat is not square.
    """
    num_rows = len(mat)

    for row in mat:
        if len(row) != num_rows:
            raise IndexError("Matrix is not square.")

    for i in range(num_rows):
        for j in range(num_rows):
            val = mat[i][j]
            if not isinstance(val, int):
                raise TypeError("Matrix contains non-integer value.")
            if i == j:
                if val != 1:
                    return False
            else:
                if val != 0:
                    return False

    return True

#Question 4B:function named create_sub_matrix
def create_sub_matrix(mat, size):
    """
    Returns a square submatrix of given odd size centered in mat.

    Parameters:
    - mat: square 2D list
    - size: odd integer not larger than number of rows

    Raises:
    - IndexError: if any row has a different length
    """
    n = len(mat)

    for row in mat:
        if len(row) != n:
            raise IndexError("Matrix rows are not all the same length.")

    center = n // 2
    offset = size // 2

    submatrix = []
    for i in range(center - offset, center + offset + 1):
        submatrix.append(mat[i][center - offset:center + offset + 1])

    return submatrix
#Question 4C:function named max_identity_matrix
def max_identity_matrix(mat):
    """
    Finds the largest centered identity matrix in mat.

    Returns:
    - size (odd integer) of the largest identity matrix found
    - 0 if none found

    Raises:
    - IndexError: if any row has a different length
    - TypeError: if any value is not an integer
    """
    n = len(mat)

    for row in mat:
        if len(row) != n:
            raise IndexError("Matrix rows are not all the same length.")

    for size in range(n if n % 2 == 1 else n - 1, 0, -2):
        try:
            sub = create_sub_matrix(mat, size)
            if identity_matrix(sub):
                return size
        except TypeError:
            print("Not all values are int")
            return 0

    return 0
