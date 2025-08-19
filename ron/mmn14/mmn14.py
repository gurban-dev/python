# Question 1
def find_max(lst):
    """
    Finds the maximum value in a K-shift rotated list.

    A K-shift rotation moves each element K positions to
    the right, wrapping around the list. This function
    assumes that such a rotation has already occurred and
    the list is rotated in ascending order. It uses a
    modified binary search to find the maximum efficiently
    without altering the list or using extra space.

    Parameters:
        lst (list): A list of unique numerical values.

    Returns:
        int or float: The maximum value in the list.
                      Returns None if the list is empty.
    """

    # If the list is empty.
    if not lst:
        return None
 
    low = 0

    high = len(lst) - 1

    while low <= high:
        # The // operator represents integer division.
        mid = (low + high) // 2

        # The next two lines of source code ensure
        # that edge cases are handled safely.

        # Find the index before "mid".
        prev = (mid - 1 + len(lst)) % len(lst)

        # Find the index after "mid".
        next = (mid + 1) % len(lst)

        '''
        Finding the indexes before and after "mid"
        are necessary because then the program can
        check the elements located in those indexes
        to determine if the element at "mid" is the
        largest in the list.'''

        # Check if mid is the maximum.
        if lst[mid] > lst[next] and lst[mid] > lst[prev]:
            return lst[mid]

        # Decide which half to continue searching.
        if lst[mid] >= lst[low]:
            low = mid + 1
        else:
            high = mid - 1

    # If the array is fully sorted and not rotated.
    return lst[-1]

# Question 2
def find_pairs(lst, K):
    """
    Counts the number of unique pairs in a sorted list 
    where the difference between elements equals K.

    Parameters:
    lst (list of int): A list of sorted integers.
    K (int): The target difference between elements.

    Returns:
    int: The number of unique pairs with difference K.
    """
    count = 0

    i = 0
    j = 1

    n = len(lst)

    while j < n:
        diff = lst[j] - lst[i]

        if diff == K:
            count += 1
            i += 1
            j += 1
        elif diff < K:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1

    return count

# Question 3 Part A
def update_list(lst, value, index=0, removed=False):
    """
    Removes the first occurrence of a specified value
    from a list using recursion.

    Parameters:
    lst (list): The list from which to remove the value.

    value: The value to remove from the list.

    index (int, optional): The current index in recursion.
                           The default is 0.

    removed (bool, optional): Tracks if value has been
                              removed. Default is False.

    Returns:
    list: A new list with the first occurrence of the
          value removed.
    """

    # Base case: reached the end of the list
    if index == len(lst):
        return []

    # If the value has been found, but hasn't been
    # removed it yet, skip it once.
    if lst[index] == value and not removed:
        return update_list(lst, value, index + 1, True)

    # Otherwise, keep the current element and continue.
    return [lst[index]] + update_list(lst, value, index + 1, removed)

# Question 3 Part B
# Has a worst-case time complexity of O(n^2).
# def equal_lists(lst1, lst2):
#     """
#     Recursively checks if two lists contain the same elements 
#     with the same frequency, in any order.

#     Parameters:
#         lst1 (list): The first list of numerical values.
#         lst2 (list): The second list of numerical values.

#     Returns:
#         bool: True if both lists contain the same elements with 
#               identical frequencies; False otherwise.
#     """

#     # Checks if both lists are empty.
#     if not lst1 and not lst2:
#         return True

#     # If one list is empty, but the other is not.
#     if not lst1 or not lst2:
#         return False

#     def update_list(lst, value):
#         """
#         Recursively removes the first occurrence of a value 
#         from the list if it exists.

#         Parameters:
#             lst (list): List to be updated.
#             value (int or float): Value to remove.

#         Returns:
#             list: Updated list after removing value.
#         """
#         def helper(index):
#             # Reached end of list
#             if index == len(lst):
#                 return lst

#             # Value found, remove it
#             if lst[index] == value:
#                 lst[:] = lst[:index] + lst[index+1:]
#                 return lst

#             # Continue checking next element
#             return helper(index + 1)

#         return helper(0)

#     # Try removing lst1[0] from lst2 copy
#     # If update_list() is utilised, the worst-case
#     # time complexity would be O(n^2).
#     updated_lst2 = update_list(lst2[:], lst1[0])

#     # If nothing was removed, value not found
#     if len(updated_lst2) == len(lst2):
#         return False

#     # Continue checking with the rest of lst1
#     return equal_lists(lst1[1:], updated_lst2)

# Remove the above function named equal_lists
# if you decide to move forward with the below
# approach since it has a time complexity of
# O(n log n) during the worst-case:
def equal_lists(lst1, lst2):
    """
    Determines whether two lists contain the same elements,
    regardless of order, using recursive comparison.

    Parameters:
    lst1 (list): The first list to compare.
    lst2 (list): The second list to compare.

    Returns:
    bool: True if both lists contain the same elements,
          False otherwise.
    """

    # If the lists aren't the same length, they can't be equal.
    if len(lst1) != len(lst2):
        return False

    # Sort both lists so we can do an element-wise comparison.
    sorted_lst1 = sorted(lst1)
    sorted_lst2 = sorted(lst2)

    # Compare each element recursively
    def compare_recursive(i):
        if i == len(sorted_lst1):
            return True  # Reached the end, everything matched
        if sorted_lst1[i] != sorted_lst2[i]:
            return False  # Found a mismatch
        return compare_recursive(i + 1)

    return compare_recursive(0)

# Question 4
def is_palindrome(lst):
    """
    Checks whether a list is a palindrome using 
    recursive comparison.

    The time complexity is O(n), where "n" represents
    the length of the list.

    Parameters:
    lst (list): The list to check for palindrome 
        properties.

    Returns:
    bool: True if the list is a palindrome, 
        False otherwise.
    """
    def check(start, end):
        if start >= end:
            return True
        if lst[start] != lst[end]:
            return False
        return check(start + 1, end - 1)

    return check(0, len(lst) - 1)