"""
Problem to solve:
Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j]
== target and i != j. In other words, i and j cannot
be the same index.

Algorithm

Input:
An array of integers called "nums".

Output:
Indices i and j such that the sum of nums[i] and
nums[j] is equal to the value of the variable "target".

1. Declare a dictionary called "prevMap".
2. Begin iterating through the array of integers
   called "nums".
   a. Get the index and the value of the current
      item in the "nums" array.
   b. Find the difference between the value of "target"
      and the current item.
   
3. 
"""

def twoSum(nums: list[int], target: int) -> list[int]:
  # Hashmap
  # key: element, value: index
  prevMap = {}

  # enumerate() returns the index and value
  # of the current item in the dictionary.
  for index, value in enumerate(nums):
    # First iteration:
    # index = 0
    # value = 9
    # difference = 5 - 9 -> -4

    # Last iteration:
    # index = 3
    # value = 2
    # difference = 5 - 2 -> 3

    difference = target - value

    # Does not belong here because this program
    # would fail with the second example shown
    # below.
    # prevMap[value] = index

    # First iteration:
    # if 9 in prevMap:

    # Last iteration:
    # if 3 in prevMap:
    if difference in prevMap:
      # Last iteration:
      # return [prevMap[3], 3]
      # return [1, 3]

      return [prevMap[difference], index]
    # If we don't find the solution, we have to
    # add the element and index to our hashmap.

    # The value of the element is added here to
    # avoid having a duplicate key.

    """
    Second iteration:
    prevMap[key] = value
    prevMap[3] = 1

    prevMap = {
      9: 0
      3: 1
    }
    """

    # Remember that the only qualification
    # for a dictionary key is immutability.
    prevMap[value] = index

  # Return an empty list if the indices
  # of two elements that sum up to the
  # target do not exist in "nums".
  return []

# Example One
# Indices: 0  1  2  3
nums1 = [9, 3, 8, 2]
target1 = 5

# Example Two
nums2 = [2, 5, 5, 1]
target2 = 10

print(f'twoSum(nums1, target1): {twoSum(nums1, target1)}')

print(f'\ntwoSum(nums2, target2): {twoSum(nums2, target2)}')