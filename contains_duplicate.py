"""
Given an integer array nums, return true if any
value appears more than once in the array,
otherwise return false.

Algorithm

Input:
An integer array called "nums".

Output:
True or false depending on whether the
array called "nums" contains a duplicate
value.

A set is a data structure in Python that
stores unique values.

1. Declare a container of type "set" called
   "numsUniqueValues".
2. Loop through the elements inside the "nums"
   array.
   a. If the current element is already inside
      "numsUniqueValues", return False.
      Otherwise, add the current element to
      "numsUniqueValues".
   b. Continue to the next iteration.
3. Return true, as a duplicate was never detected
   while looping through the elements of "nums".
"""

# nums = [1, 4, 7, 9]

def contains_duplicate(nums) -> bool:
  # print('Line 35 was reached!')

  # return

  # print('Line  was reached!')

  # Python's built-in set data structure
  # does not permit duplicate values being
  # stored.
  numsUniqueValues = set()

  # For each number in nums:
  for num in nums:
    # 1st iteration:
    # num = 1

    # 2nd iteration:
    # num = 4

    # 3rd iteration:
    # num = 7

    # 4th iteration:
    # num = 9

    # print('num:', num)

    """
    str() is a function that accepts a number and
    converts it to a string. It was necessary to
    convert "num" to a string because it is being
    concatenated to the string literal 'num: '."""
    print('num: ' + str(num))

    if num in numsUniqueValues:
      return True
    else:
      numsUniqueValues.add(num)

  """
  False should not be returned during
  an iteration because then the program
  would return False on the first
  iteration and the remaining iterations
  will not be reached."""
  return False

nums1 = [1, 4, 7, 9]

nums2 = [1, 4, 7, 1]

print(f'\ncontains_duplicate(nums1): {contains_duplicate(nums1)}')

print(f'\ncontains_duplicate(nums2): {contains_duplicate(nums2)}')