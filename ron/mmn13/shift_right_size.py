def shift_k_right(lst, k):
    """
    Returns a new list which is the result of a
    right circular shift of size "k" on the input
    list "lst".

    A right circular shift moves each element in
    the list to the right by "k" positions, wrapping
    elements around to the front as needed.

    Parameters
    ----------
    lst : list
        A list of elements to be shifted.

    k : int
        The number of positions to shift elements
        to the right.

    Returns
    -------
    list
        A new list that is the result of a right
        circular shift of "lst" by "k" positions.

    Raises
    ------
    ValueError
        If "k" is negative or greater than the
        length of the list.
    """
    length = len(lst)

    # Validate input: "k" must be within range.
    if k < 0 or k > length:
        raise ValueError(
            "Shift value k must be between 0 "
            "and the length of the list.")

    # Perform the shift using slicing.
    return lst[-k:] + lst[:-k]

def shift_right_size(a, b):
    """
    Determines the right circular shift size "k" such
    that shifting list a by "k" positions results in
    list "b".

    Uses the shift_k_right() function to attempt each
    valid shift size from 0 up to the length of the
    list.

    Parameters
    ----------
    a : list
        The original list to be shifted.

    b : list
        The target list to match after shifting.

    Returns
    -------
    int or None
        The shift size "k" that makes a equal to "b"
        after a right circular shift.

        Returns None if no such shift exists or if the
        lists are not the same length.
    """
    # Check if lists are of the same length.
    if len(a) != len(b):
        return None

    # Try each possible shift value from 0 to len(a).
    for k in range(len(a) + 1):
        shifted = shift_k_right(a, k)

        if shifted == b:
            return k

    # No shift results in list a matching list b.
    return None

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print('shift_right_size(a, b):', shift_right_size(a, b))

c = [1, 2, 3, 4, 5]
d = [4, 5, 1, 2, 3]
print('\nshift_right_size(c, d):', shift_right_size(c, d))

lst = [1, 2, 3, 4, 5]
k = 3

print('\nshift_k_right(lst, k):', shift_k_right(lst, k))