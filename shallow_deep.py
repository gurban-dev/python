import copy

# The original list with a nested list inside.
lst = [[1], 2]

# [1] is called a nested list becaused it's a list inside of a list.
first_item = lst[0]

print('type(first_item):', type(first_item), '\n')

# Make a shallow copy of 'lst' with the .copy() method.
shallow_copy = lst.copy()

# The .copy() method is equivalent to slicing because both perform
# a shallow copy.
print('lst.copy() == lst[:]:', lst.copy() == lst[:])

# Make a deep copy of 'lst' with the deepcopy() function that is
# defined in the 'copy' module (a Python file).
deep_copy = copy.deepcopy(lst)

print('\nBefore assigning anything:')

# hex(id()) will return a hexadecimal representation of an object's identity.

# The term "memory address" is being avoided here since not every implementation
# of Python has them as CPython does.

# Compare the identities of the 'lst', 'shallow_copy' and 'deep_copy'.
print('hex(id(lst)):', hex(id(lst)))
print('hex(id(shallow_copy)):', hex(id(shallow_copy)))
print('hex(id(deep_copy)):', hex(id(deep_copy)))

# Compare the identities of 'lst[0]', 'shallow_copy[0]' and 'deep_copy[0]'.
print('\nhex(id(lst[0])):', hex(id(lst[0])))
print('hex(id(shallow_copy[0])):', hex(id(shallow_copy[0])))
print('hex(id(deep_copy[0])):', hex(id(deep_copy[0])))

# Integers are immutable, so all three indices and the variable 'two' refer
# to the same object.

# Notice how the variable 'two' has the same identity as the above three indices.
two: int = 2
print('\nhex(id(two)):', hex(id(two)))

# Assign a list with the exact same element to the index where the nested
# list is to see whether the identity of lst[0], shallow_copy[0] and deep_copy[0]
# changes.

# Notice how the identity of lst[0] doesn't change when modifying the first item of
# the nested list (lst[0][0]). The shallow_copy's first element will now be [2] as
# well while the deep_copy remain unaffected.
lst[0][0] = 2

print("\nAfter assigning 2 to lst[0][0]:")
print('lst:', lst,
      '\nshallow_copy:', shallow_copy,
      '\ndeep_copy:', deep_copy)

print('\nhex(id(lst[0])):', hex(id(lst[0])))
print('hex(id(shallow_copy[0])):', hex(id(shallow_copy[0])))
print('hex(id(deep_copy[0])):', hex(id(deep_copy[0])))

# Notice how the identity that lst[0] references changes after this.
# This is because assigning a mutable object, will give the first index of
# 'lst' a new identity.

# lst[0] and shallow_copy no longer refer to the same list object.
# At this point, any changes made to the original list at index zero
# will have no effect on the list that shallow_copy[0] refers to.
lst[0] = [2]

print('\nAfter assigning [2] to lst[0]:')
print('hex(id(lst[0])):', hex(id(lst[0])))
print('hex(id(shallow_copy[0])):', hex(id(shallow_copy[0])))
print('hex(id(deep_copy[0])):', hex(id(deep_copy[0])))

# The key takeaway:
# A shallow copy creates a new list, but the items inside still point
# to the same objects.

# A deep copy creates a new list and new copies of all nested objects.