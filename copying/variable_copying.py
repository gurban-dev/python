# Create an integer object with a value of 10, and
# have "x" point to it.
x = 10

print('Before incrementing variable x:')

# Show the memory location of the integer object.
print('hex(id(x)):', hex(id(x)))

y = x

print('\nhex(id(y)):', hex(id(y)))

print('\ny is x:', y is x)

'''
x = 10 allocates memory on the heap (a section on the RAM) for:
1. The variable name "x" in the namespace.
2. The reference/pointer that links the name "x" to the integer object.
3. The integer object 10 itself (if it's outside the cached range -5 to 256).

Integers are immutable in Python which means that rather than
modifying the value at the same memory location, the program
allocates new memory, but just for the new integer object.

When x += 5 is executed, Python doesn't modify the existing
integer object. Instead, it creates a new integer object with
value 15 and has "x" to point to it, changing the memory
address that "x" references.
'''
x += 5

print('\nAfter incrementing variable x:')

print('hex(id(x)):', hex(id(x)))

print('\nhex(id(y)):', hex(id(y)))

print('\ny is x:', y is x)

print(f'\nx: {x}, y: {y}')