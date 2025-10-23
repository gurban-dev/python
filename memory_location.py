name_of_country = 'LLiechtenstein'

# A new object is not being created.
# Likewise, this does not create a shallow copy since
# both variables still point to the same memory address.
same_country = name_of_country

# Display the memory location/address of the variable.
print('hex(id(name_of_country)):', hex(id(name_of_country)))

print('\nhex(id(same_country)):', hex(id(same_country)))

# Reveal the memory location/address of the string
# literal/raw value.
print('\nhex(id(\'LLiechtenstein\')):', hex(id('LLiechtenstein')))

# Strings are immutable. Their contents can never change
# after creation.

# Because of that, Python can safely let multiple variables
# reference the same string object in memory.

# There's no risk that changing one variable would
# accidentally affect another because modifying the
# string in place isn't possible.

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

lst2[0] = 10

print('\nlst1:', lst1)
print('lst2:', lst2)

# Notice how the memory address that lst2[0]
# references changes after a new integer is
# assigned to it.
print('\nhex(id(lst1[1])):', hex(id(lst1[1])))
print('hex(id(lst2[0])):', hex(id(lst2[0])))