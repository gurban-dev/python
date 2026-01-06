import copy

# 'lst' has three items.
lst = [1, 2, [3, 4]]

# Make a shallow copy of 'lst' with the .copy() method.
shallow_copy_of_lst = lst.copy()

# Make a deep copy of 'lst' with the deepcopy() function that is
# defined in the 'copy' module.
deep_copy_of_lst = copy.deepcopy(lst)

# Reveal the memory addresses that 'lst', 'shallow_copy_of_lst', and
# 'deep_copy_of_lst' hold a reference to.
print('hex(id(lst)):', hex(id(lst)))
print('hex(id(shallow_copy_of_lst)):', hex(id(shallow_copy_of_lst)))
print('hex(id(deep_copy_of_lst)):', hex(id(deep_copy_of_lst)))

# Reveal the memory addresses that 'lst[0]', 'shallow_copy_of_lst[0]',
# and 'deep_copy_of_lst[0]' hold a reference to.
print('\nhex(id(lst[0])):', hex(id(lst[0])))
print('\nhex(id(shallow_copy_of_lst[0])):', hex(id(shallow_copy_of_lst[0])))
print('hex(id(deep_copy_of_lst[0])):', hex(id(deep_copy_of_lst[0])))

one: int = 1
print('\nhex(id(one)):', hex(id(one)))

# Modify the original list 'lst' to see how it affects the deep copy.
lst[2][0] = []

print('\nlst:', lst,
      '\nshallow_copy_of_lst:', shallow_copy_of_lst,
      '\ndeep_copy_of_lst:', deep_copy_of_lst)