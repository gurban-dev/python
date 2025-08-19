# Solution for Question 1 – K-Shift Rotation and
# Maximum Finder
def find_max(lst):
    """
    Return the maximum element in a rotated sorted array.

    Given:
    The input list "lst" is assumed to be a list of numbers
    in strictly ascending order that has been already rotated
    by an unknown number of positions.

    The function runs in O(log n) time using binary search.

    Parameters:
        lst (list): A rotated sorted list of distinct integers.

    Returns:
        int or None: The maximum element in the list, or None
                     if the list is empty.
    """

    if not lst:
        return None

    n = len(lst)
    low = 0
    high = n - 1

    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[high]:
            low = mid + 1
        else:
            high = mid

    # "low" is now the index of the smallest
    # element.
    K = low
    index_of_max_el = (K + n - 1) % n

    return lst[index_of_max_el]

# Solution for Question 2 – Find Pairs with Difference K
def find_pairs(lst, K):
    """
    Return the count of unique index pairs with a given
    difference "K".

    This function assumes the input list "lst" is sorted
    in strictly ascending order and uses the two-pointer
    technique to count the number of unique pairs (i, j) such
    that lst[j] - lst[i] == K and i < j.

    Parameters:
        lst (list): A sorted list of integers.
        K (int): The target difference between pair elements.

    Returns:
        int: The number of pairs with a difference equal to K.
    """

    count = 0

    # Declare and initialise two variables for the
    # two-pointer technique.
    left = 0
    right = 1

    n = len(lst)

    while right < n:
        diff = lst[right] - lst[left]
        if diff == K:
            count += 1
            left += 1
            right += 1
        elif diff < K:
            right += 1
        else:
            left += 1
            if left == right:
                right += 1
    return count

# Solution for Question 3 Part A – Recursive function
# to remove first occurrence of value
def update_list(lst, value):
    """
    Recursively removes the first occurrence of a
    specified value from the list.

    Parameters:
    lst (list): The list of numbers to update.
    value: The value to remove.

    Returns:
    list: A new list with the first occurrence of
          value removed, if found. Otherwise, returns
          the list unchanged.
    """
    def helper(index, element_removed, updated_list):
        if index == len(lst):
            return updated_list
        if lst[index] == value and not element_removed:
            return helper(index + 1, True, updated_list)
        return helper(
            index + 1,
            element_removed,
            updated_list + [lst[index]]
        )

    return helper(0, False, [])


# Solution for Question 3 Part B – Recursive function to
# check if two lists contain the same elements (any order)
def equal_lists(lst1, lst2):
    """
    Recursively checks whether two lists "lst1" and "lst2"
    contain the same elements (in any order), and with the
    same quantity.

    Parameters:
    lst1 (list): The first list of numbers.
    lst2 (list): The second list of numbers.

    Returns:
    bool: True if both lists contain the same elements with
          the same quantities, otherwise False.
    """
    if not lst1 and not lst2:
        return True
    if not lst1 or not lst2:
        return False

    updated_lst2 = update_list(lst2, lst1[0])

    # Value not found.
    if len(updated_lst2) == len(lst2):
        return False

    return equal_lists(lst1[1:], updated_lst2)
    
# Solution for Question 4 – Check if a list is a
# palindromic list of palindromes
def is_palindrome(lst):
    """
    Determine if a list is a "palindromic list".

    A palindromic list is one where the list reads the same
    forward and backward, and each element in the list is
    itself a palindrome string.

    Args:
        lst (list of str): The list of strings to check.

    Returns:
        bool: True if "lst" is a palindromic list. Otherwise, False.
    """
    def is_element_palindrome(s, i=0, j=None):
        """Recursively check if string "s" is a palindrome."""
        if j is None:
            j = len(s) - 1
        if i >= j:
            return True
        return s[i] == s[j] and is_element_palindrome(s, i + 1, j - 1)

    def check_list_palindrome(lst, i=0, j=None):
        """Recursively check if "lst" is a palindrome
           and all elements are palindromes."""
        if j is None:
            j = len(lst) - 1
        if i >= j:
            return True
        if not is_element_palindrome(lst[i]) or not is_element_palindrome(lst[j]):
            return False
        return lst[i] == lst[j] and check_list_palindrome(lst, i + 1, j - 1)

    if not lst:
        return True

    return check_list_palindrome(lst)