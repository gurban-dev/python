# You are given two sorted lists of integers:

a = [1, 3, 3, 5, 7]
b = [3, 3, 3, 5, 5, 5]

'''
Task:
Write a Python program using a while loop to:

Find all common elements between the two lists,

Return a new sorted list of those elements,

Without using set() or in.


Constraints:
Use a while loop, two pointers (i, j).

Assume a and b are individually sorted.

Don't use in, set, or intersect helpers.


Expected Output:
[3, 5]
'''

# Solution that honours contraints.
def common_elements_sorted(list_a, list_b):
  i = 0
  j = 0
  result = []

  while i < len(list_a) and j < len(list_b):
    if list_a[i] == list_b[j]:
      # To avoid duplicates in the result
      if len(result) == 0 or result[-1] != list_a[i]:
        result.append(list_a[i])
      i += 1
      j += 1
    elif list_a[i] < list_b[j]:
      i += 1
    else:
      j += 1

  return result

# Solution that doesn't honour constraints.
def get_shared_elements(list_a, list_b):
  shared_elements = set()

  for num in list_a:
    if num in list_b:
      shared_elements.add(num)
  return shared_elements

shared_elements = get_shared_elements(a, b)

print('shared_elements:', shared_elements)

common_elements = common_elements_sorted(a, b)

print('common_elements:', common_elements)