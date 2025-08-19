#question 1
def find_max(lst, K=0):
    if not lst:
        return None
    n = len(lst)
    max_val = lst[K % n]  # Start at index K (circular)
    for i in range(n):
        idx = (K + i) % n  # Calculate current index in rotation
        if lst[idx] > max_val:
            max_val = lst[idx]
    return max_val

# Example to test the function
example_list = [2, 6, 11, 17, 40, 42]
K = 3
result = find_max(example_list, K)
print("Original list:", example_list)
print("K:", K)
print("Max value after K-rotation iteration:", result)

# Question 2 – Find Pairs with Difference K

def find_pairs(lst, K):
    count = 0
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

# -------------------------
# Test Cases for Question 2
# -------------------------
print("Testing Question 2: find_pairs")

# Test 1: Unique sorted list with K = 2
lst = [1, 3, 5, 7]
print("Expected: 3 | Got:", find_pairs(lst, 2))  # (1,3), (3,5), (5,7)

# Test 2: No pairs with diff 0
lst = [1, 2, 3, 4]
print("Expected: 0 | Got:", find_pairs(lst, 0))  # No pair has diff 0

# Test 3: More complex list with K = 2
lst = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
print("Expected: 3 | Got:", find_pairs(lst, 2))  # (1,3), (3,5), (12,14)

# Test 4: Larger step
lst = [10, 20, 30, 40, 50]
print("Expected: 4 | Got:", find_pairs(lst, 10))  # (10,20), (20,30), (30,40), (40,50)

# Test 5: K = 1 case
lst = [1, 2, 3, 4, 5, 6]
print("Expected: 5 | Got:", find_pairs(lst, 1))  # (1,2), (2,3), ..., (5,6)

print("All test cases passed if outputs match expectations.")


# Question 3 Part A – Recursive function to remove first occurrence of value

def update_list(lst, value, index=0):
    if not lst:
        return lst.copy()
    if index == len(lst):
        return lst.copy()
    if lst[index] == value:
        return lst[:index] + lst[index+1:]
    return update_list(lst, value, index + 1)

# -------------------------
# Test Cases for update_list
# -------------------------
print("Testing update_list (Question 3A):")

# Test 1: value is present
print("Expected: [4, 1] | Got:", update_list([4, 1, 3], 3))

# Test 2: value not present
print("Expected: [3, 8, 10, 6] | Got:", update_list([3, 8, 10, 6], 1))

# Test 3: value in middle
print("Expected: [3, 10, 6] | Got:", update_list([3, 8, 10, 6], 8))

# Test 4: value at beginning
print("Expected: [2, 3, 4] | Got:", update_list([1, 2, 3, 4], 1))

# Test 5: empty list
print("Expected: [] | Got:", update_list([], 5))

print("All test cases for update_list passed if outputs match.")

# Question 3 Part B – Recursive function to check if two lists contain the same elements (any order)

def update_list(lst, value, index=0):
    if not lst:
        return lst.copy()
    if index == len(lst):
        return lst.copy()
    if lst[index] == value:
        return lst[:index] + lst[index+1:]
    return update_list(lst, value, index + 1)

def equal_lists(lst1, lst2):
    if not lst1 and not lst2:
        return True
    if not lst1 or not lst2:
        return False
    updated_lst2 = update_list(lst2, lst1[0])
    if len(updated_lst2) == len(lst2):  # value not found
        return False
    return equal_lists(lst1[1:], updated_lst2)

# -------------------------
# Test Cases for equal_lists
# -------------------------
print("Testing equal_lists (Question 3B):")

# Test 1: Same elements, different order
print("Expected: True | Got:", equal_lists([1, 2, 3], [3, 2, 1]))

# Test 2: One list longer
print("Expected: False | Got:", equal_lists([1, 2], [1, 2, 3]))

# Test 3: Duplicate elements matched
print("Expected: True | Got:", equal_lists([1, 1], [1, 1]))

# Test 4: Unequal duplicate counts
print("Expected: False | Got:", equal_lists([1, 1], [1]))

# Test 5: Both empty
print("Expected: True | Got:", equal_lists([], []))

# Test 6: Same length, different values
print("Expected: False | Got:", equal_lists([4, 5], [5, 6]))

print("All test cases for equal_lists passed if outputs match.")
# Question 4 – Check if a list is a palindromic list of palindromes

def is_palindrome(lst):
    def is_element_palindrome(s, i=0, j=None):
        # Recursively checks if string s is a palindrome
        if j is None:
            j = len(s) - 1
        if i >= j:
            return True
        return s[i] == s[j] and is_element_palindrome(s, i+1, j-1)
    
    def check_list_palindrome(lst, i=0, j=None):
        # Recursively checks if the list is a palindrome and each element is a palindrome
        if j is None:
            j = len(lst) - 1
        if i >= j:
            return True
        if not is_element_palindrome(lst[i]) or not is_element_palindrome(lst[j]):
            return False
        return lst[i] == lst[j] and check_list_palindrome(lst, i+1, j-1)
    
    if not lst:
        return True
    return check_list_palindrome(lst)

# -------------------------
# Test Cases for is_palindrome
# -------------------------
print("Testing is_palindrome (Question 4):")

# Test 1: Full palindromic list
lst = ['abba', 'readaer', 'abba']
print("Expected: True | Got:", is_palindrome(lst))

# Test 2: Single element (also a palindrome)
lst = ['abba']
print("Expected: True | Got:", is_palindrome(lst))

# Test 3: Elements are palindromes but list is not
lst = ['a', 'aa', 'aba', 'a']
print("Expected: False | Got:", is_palindrome(lst))

# Test 4: List is a palindrome but contains a non-palindrome element
lst = ['abba', 'gonna', 'abba']
print("Expected: False | Got:", is_palindrome(lst))

# Test 5: Empty list
lst = []
print("Expected: True | Got:", is_palindrome(lst))

# Test 6: List of empty strings
lst = ['', '', '']
print("Expected: True | Got:", is_palindrome(lst))

print("All test cases for Question 4 passed if outputs match expectations.")
