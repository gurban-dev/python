def decrement_list(lst, index=0):
    """
    Recursively decrement each element of a list by 1.
    Demonstrates outdated value issue if we don't return the updated list.
    """
    if index >= len(lst):
      # Base case
      return lst

    # lst[0] -= 1

    # lst[1] -= 1
    lst[index] -= 1  # decrement current element

    # 2nd function call:
    # decrement_list([4, 4, 3], 1)

    # 3rd function call:
    # decrement_list([4, 3, 3], 2)
    decrement_list(lst, index + 1)  # recursive call, but result not captured

    # Returns original list reference, not
    # the updated one from recursion.
    # return lst


my_list = [5, 4, 3]

# 1st function call:
# decrement_list([5, 4, 3])
result = decrement_list(my_list)
print("Result:", result)