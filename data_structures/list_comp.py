nums = [1, 2, 3, 4, 5]

# In this example, a list comprehension will be written to
# iterate through each element inside the 'nums' Python list
# and square it.

# Assign the result to the 'nums_squared' variable.

# Syntax for a list comprehension:
# [<expression> for <variable> in <iterable> if <condition>]

# This is an example of list comprehension.
nums_squared = [num ** 2 for num in nums if num ** 2 < 25]

# Notice how the variable name written in the <expression>
# and in the <condition> must be the same as the variable
# name written in <variable>.

# Line 13 is equivalent to the following commented out source
# code:
# nums_squared = []

# for num in nums:
#   if num ** 2 < 25:
#     # num = num ** 2
#     num **= 2

#     nums_squared.append(num)

print('nums_squared:', nums_squared)