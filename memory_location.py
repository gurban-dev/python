# The variable "name_of_country" holds a reference to the
# string object 'Liechtenstein'.
name_of_country: str = 'Liechtenstein'

# Assigning "same_country" to "name_of_country" does NOT create a new string object.
# Both variables point to the same string in memory.
same_country: str = name_of_country

# Display the memory location/address of the string object that
# "name_of_country" references.
print('hex(id(name_of_country)):', hex(id(name_of_country)))

print('\nhex(id(same_country)):', hex(id(same_country)))

# Note: In CPython, some strings may be interned automatically.
# The id() of the literal may or may not match the id() of the variable.

# CPython is one of the engines that can run Python code.
# Interning is a technique Python uses to reuse objects in memory to
# save space and improve performance.

# For strings, it means: if two strings have the same value, Python may
# store only one copy in memory and have both variables point to it.
print('\nhex(id(\'Liechtenstein\')):', hex(id('Liechtenstein')))

# Strings are immutable. Their contents can never change
# after creation.

# Because of that, Python can safely let multiple variables
# hold a reference to the same string object in memory.

# There's no risk that changing one variable would
# accidentally affect another because modifying the
# string object in place isn't possible.

# This is how memory is optimised in Python.

# A new list object ([1, 2, 3]) is created in memory.
lst = [1, 2, 3]

# Print the memory address of that list object.
print(f"\nhex(id(lst)): {hex(id(lst))}")

# Since the previous list object was assigned to a
# variable, its memory address remains saved
# throughout the runtime of this program.

# If a new list object is to be created, a new memory
# address must be given to it.
print(f"\nhex(id([1, 2, 3])): {hex(id([1, 2, 3]))}")

# String slicing.
# A new string object is being created because
# strings are immutable in Python.
name_of_country = name_of_country[1:]

print('\nname_of_country:', name_of_country)

print('\nhex(id(name_of_country)):', hex(id(name_of_country)))

lst1 = [1, 2]

# A new object and shallow copy is being created.
lst2 = lst1[1:]

# While a shallow copy will create a new memory
# address for lst2, the indices in lst2 will still
# point to the same memory addresses as in lst1,
# unless a new value is assigned to them.

print('\nhex(id(lst1)):', hex(id(lst1)))

print('\nhex(id(lst2)):', hex(id(lst2)))

print('\nlst1:', lst1)
print('lst2:', lst2)

print('\nhex(id(lst1[1])):', hex(id(lst1[1])))
print('hex(id(lst2[0])):', hex(id(lst2[0])))

# Assigning a new value in index 0 forces that index to
# point to a new memory address.
lst2[0] = 10

print('\nlst1:', lst1)
print('lst2:', lst2)

# Notice how the memory address that lst2[0]
# references changes after a new integer is
# assigned to it.
print('\nhex(id(lst1[1])):', hex(id(lst1[1])))
print('hex(id(lst2[0])):', hex(id(lst2[0])))

# Two-dimensional list.
nested_list = [[0]]

# The return value from slicing a list is a shallow copy.
shallow_copy_of_nested_list = nested_list[:]

# Mutating an item located inside the inner list doesn't
# create a new object with its own distinct memory address.
shallow_copy_of_nested_list[0][0] = 0

print('\nhex(id(nested_list[0][0])):', hex(id(nested_list[0][0])))
print('hex(id(shallow_copy_of_nested_list[0][0])):', hex(id(shallow_copy_of_nested_list[0][0])))

print('\nshallow_copy_of_nested_list:', shallow_copy_of_nested_list)

# Forces the first indice of "shallow_copy_of_nested_list"
# to point to a new memory address. A new list object is
# created in memory.
shallow_copy_of_nested_list[0] = [0]

print('\nhex(id(nested_list[0])):', hex(id(nested_list[0])))
print('hex(id(shallow_copy_of_nested_list[0])):', hex(id(shallow_copy_of_nested_list[0])))