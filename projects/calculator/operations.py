# 'num1' and 'num2' are parameters.
# These are names for the different pieces of data that
# the add() function will accept when it is invoked.

# 'num1' and 'num2' don't have to be defined outside of
# this function.
def add(num1, num2):
    return num1 + num2

# The positional argument 2 is assigned to the parameter
# 'num1'.

# With the keyword argument num2=4, the integer 4 is assigned
# to the parameter 'num2'.
print(f"add(2, 4): {add(2, 4)}")

def subtract(num1: float, num2: float) -> float:
    return num1 - num2