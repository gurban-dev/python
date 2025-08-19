def is_perfect(lst):
    """
    Determines whether the given list is a 'perfect list'
    based on a value-based scan.

    A list is considered perfect if:
    - Starting at index 0, each value is used as the
      next index to visit.
    - The scan visits all indices in the list exactly once.
    - The scan reaches a value of 0 at some point.
    - The scan terminates at the index with value 0.
    
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
        If the scan attempts to access an index
        outside the list.
    TypeError
        If the list contains any non-integer elements.
    """
    # Handle empty list: considered perfect
    if not lst:
        return True

    length = len(lst)
    visited = [False] * length
    index = 0
    zero_found = False

    # Number of steps performed (avoid infinite loops).
    steps = 0

    while True:
        # Raise error if index is out of bounds.
        if index < 0 or index >= length:
            raise IndexError("Index out of bounds during scan.")

        # Check element type
        if not isinstance(lst[index], int):
            raise TypeError("List contains a non-integer value.")

        # If already visited, a loop is
        # detected; not a perfect list.
        if visited[index]:
            return False

        # Mark current index as visited.
        visited[index] = True
        steps += 1

        # Check if we reached a 0 value
        # (termination condition).
        if lst[index] == 0:
            zero_found = True
            break  # Terminate scan

        # Move to the next index as dictated
        # by the value at the current index.
        index = lst[index]

    # Perfect list if all indices are
    # visited and a zero was found.
    return all(visited) and zero_found

# False (cycle, no 0 reached)
print('is_perfect([2, 3, 2, 3, 0]):',
      is_perfect([2, 3, 2, 3, 0]))

# True (perfect)
print('\nis_perfect([2, 3, 4, 0, 1]):',
      is_perfect([2, 3, 4, 0, 1]))

# True (empty is perfect)
print('\nis_perfect([]):', is_perfect([]))

# Raises IndexError
print('\nis_perfect([1, 2, 3]):',
      is_perfect([1, 2, 3]))

# Raises TypeError
print('\nis_perfect([1, \'a\', 3]):',
      is_perfect([1, 'a', 3]))