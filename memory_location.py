name_of_country = 'Liechtenstein'

# Display the memory location/address of the variable.
print('\nhex(id(name_of_country)):', hex(id(name_of_country)))

# Reveal the memory location/address of the string
# literal/raw value.
print('\nhex(id(\'Liechtenstein\')):', hex(id('Liechtenstein')))

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
# variable, its memory address is remains saved
# throughout the runtime of this program.

# If a new list object is to be created, a new memory
# address must be given to it.
print(f"\nhex(id([1, 2, 3])): {hex(id([1, 2, 3]))}")