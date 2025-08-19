'''
+=, -=, *=, /*, %= are called augmented
assignment operators.'''

num = 2

# Since the current value of variable "num"
# is equal to 2, num = num + 1 becomes:
# num = 2 + 1
num += 1

print('After num += 1:', num)

# num = num - 1
# num = 3 - 1
num -= 1

print('\nAfter num -= 1:', num)

# num = num * num becomes:
# num = 2 * 2
num *= num

print('\nAfter num *= num:', num)

num = 5

print('\nnum:', num)

# Float division
# num = num / 2 becomes:
# num = 5 / 2
num /= 2

print('\nAfter num /= num:', num)

num = 5

# Integer/floor division
# num = num // 2 becomes:
# num = 5 // 2
num //= 2

print('\nAfter num //= num:', num)

# num = num % 1 becomes:
# num = 2 % 3
num %= 3

print('\nAfter num %= 2:', num)