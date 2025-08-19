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

    # Suppose lst is equal to [17, 40, 42, 2, 6, 11].
 
    low = 0

    # high = 5
    high = len(lst) - 1

    while low <= high:
        # The // operator represents integer division.
        # mid = 5 // 2 -> 2
        mid = (low + high) // 2

        # Handle edges safely.

        # Find the index before "mid".
        # prev = (2 - 1 + 6) % 6 -> (7) % 6 -> 1
        prev = (mid - 1 + len(lst)) % len(lst)

        '''
        Suppose lst = [2, 6]:

        low = 0
        high = len(lst) - 1

        # mid = (0 + 1) // 2 -> 0
        mid = (low + high) // 2

        # prev = mid - 1 -> 0 - 1 -> -1
        prev = mid - 1
        next = mid + 1 -> 0 + 1 -> 1

        Would return the last element in the list
        which would be inaccurate.
        lst[prev]

        Suppose lst = [3, 10]:
        low = 0
        high = 1
        mid = (0 + 1) // 2 = 0

        # 3 >= 3 -> True
        if lst[mid] >= lst[low]:
            # low = 1
            low = mid + 1

        Next iteration:
        low = 1
        high = 1
        mid = (1 + 1) // 2 -> 1

        next = mid + 1 -> 1 + 1 -> 2

        IndexError: list index out of range
        lst[next]
        '''

        # Find the index after "mid".
        # next = (2 + 1) % 6 -> (3) % 6 -> 3
        next = (mid + 1) % len(lst)

        '''
        Finding the indexes before and after "mid"
        are necessary because then the program can
        check the elements located in those indexes
        to determine if the element at "mid" is the
        largest in the list.'''

        # Check if mid is the maximum.

        # [17, 40, 42, 2, 6, 11]
        #   0   1   2  3  4   5

        # if lst[2] > lst[3] and lst[2] > lst[1]:
        # if 42 > 2 and 42 > 40:
        if lst[mid] > lst[next] and lst[mid] > lst[prev]:
            # return lst[2] -> 42
            return lst[mid]

        # Decide which half to continue searching.
        # if lst[2] >= lst[0]:
        # if 42 >= 17:
        if lst[mid] >= lst[low]:
            # low = 2 + 1 -> 3
            low = mid + 1
        else:
            # high = 2 - 1 -> 1
            high = mid - 1

    # If the array is fully sorted and not rotated.
    return lst[-1]

# Question 2
def find_pairs(lst, K):
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

            # Make sure "j" is always ahead of "i".
            if i == j:
                j += 1

    return count

# Question 3 Part A
def update_list(lst, value, index=0, removed=False):
    # Base case: reached the end of the list
    if index == len(lst):
        return []

    # If we find the value and haven't removed it yet, skip it once
    if lst[index] == value and not removed:
        return update_list(lst, value, index + 1, True)

    # Otherwise, keep the current element and continue
    return [lst[index]] + update_list(lst, value, index + 1, removed)

# Question 3 Part B
# Has a worst-case time complexity of O(n^2).
# def equal_lists(lst1, lst2):
#     """
#     Recursively checks if two lists contain the same
#     elements with the same frequency, in any order.

#     Parameters:
#         lst1 (list): First list of numerical values.
#         lst2 (list): Second list of numerical values.

#     Returns:
#         bool: True if both lists match in content and count.
#     """
#     # Both lists are empty
#     if not lst1 and not lst2:
#         return True

#     # One list is empty, the other is not
#     if not lst1 or not lst2:
#         return False

#     def update_list(lst, value):
#         """
#         Recursively removes the first occurrence of
#         value from the list lst, if it exists.

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
    Checks if a list of strings is a palindrome.

    Assumes each string in the list is already a palindrome.

    Time complexity: O(n), where n is the length of the list.

    Args:
        lst (list of str): List of strings.

    Returns:
        bool: True if the list reads the same forward and backward.
    """
    def check(start, end):
        if start >= end:
            return True
        if lst[start] != lst[end]:
            return False
        return check(start + 1, end - 1)

    return check(0, len(lst) - 1)