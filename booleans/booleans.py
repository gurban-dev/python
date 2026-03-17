# In Python, a Boolean is a data type that can only have two values:
#   True  - represents a true condition
#   False - represents a false condition

# Booleans are often used in:
#   - Conditional statements (if, else)
#   - Loops
#   - Comparison expressions (==, !=, >, <, >=, <=)
#   - Logical expressions using 'and', 'or', and 'not'

# Assign a boolean value to a variable.
raining = True

print('type(True):', type(True))
print('type(raining):', type(raining))

balance = 500

def withdraw(amount):
    balance_after = balance - amount
    
    print('\nbalance-after:', balance_after)

    print('\nbalance_after < 0:', balance_after < 0)

    if balance_after < 0:
        print('Funds are not sufficient!')
        return

withdraw(500)

print('\n500 > 499.9:', 500 > 499.9)

# Equality operator: ==
print('500 == 500:', 500 == 500)

# Not equals operator: !=
print('500 != 500:', 500 != 500)

print('\n10 <= 10:', 10 <= 10)
print('10 >= 10:', 10 >= 10)
print('10.01 >= 10:', 10.01 >= 10)