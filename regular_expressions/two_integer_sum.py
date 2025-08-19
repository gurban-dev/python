def twoSum(nums, target):
  differences = {}

  # [3, 4, 5, 6]
  # target = 7

  # Key-value pairs
  # differences: indices

  # 1st iteration:
  # index = 0
  # value = 3
  # difference = 7 - 3 -> 4

  # 2nd iteration:
  # index = 1
  # value = 4
  # difference = 7 - 4 -> 3

  for index, value in enumerate(nums):
    difference = target - value

    # 2nd iteration:
    # if 3 in differences:
    if difference in differences:
      # return [differences[3], 1]
      return [differences[difference], index]

    # 1st iteration:
    # differences[3] = 0
    # differences = {
    #   3: 0
    # }
    differences[value] = index

nums1 = [3,4,5,6]
target = 7
print('twoSum(nums1, target):', twoSum(nums1, target))

nums2 = [4,5,6]
target = 10
print('twoSum(nums2, target):', twoSum(nums2, target))