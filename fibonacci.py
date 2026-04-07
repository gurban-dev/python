'''
The fibonacci sequence is a Series of numbers.

F(0) = 0
F(1) = 1

F(n) = F(n - 1) + F(n - 2)

0, 1, 1, 2, 3, 5, 8, 13, 21, ..., 610

In order to find the third numbers in the sequence, I simply have
to add the previous two numbers.

Third term:
0 + 1 -> 1

Fourth term:
1 + 1 -> 2

Fifth term:
1 + 2 -> 3
'''

# A function header always begins with the "def" keyword.

# The lines of code that belong to the function are executed
# every time the function is called.

# These lines of code are below the function header and are
# indented. This means that they are positioned four spaces
# to the right of the start of the function header.

# Structure of a function header:
# def <function_name>(<parameter1>, <parameter2>):
def fibonacci(N):
    # This comment is indented just as the lines of code beneath
    # it are.

    # If N is less than or equal to zero, the fibonacci sequence
    # won't have any numbers in it so an empty list will be returned.
    if N <= 0:
        # Returns an empty list back to where this fibonacci() function
        # was invoked.

        # An empty list is simply made up of square brackets with nothing
        # in between them.
        return []
    elif N == 1:
        # The double equal sign (the equality operator) returns True
        # if Python considers the two terms being compared to be equal.
        # If the terms are not equal, the equality operator returns
        # False.
        return [0]
    elif N == 2:
        return [0, 1]
    
    # The variable 'numbers' references the list [0, 1].
    numbers = [0, 1]

    # For loop

    # Since 0 and 1 are already handled, begin looping from
    # the number 2 as opposed to zero.

    # range(start_value, stop_value (excluded), step_value)
    for index in range(2, N):
        # Find the next number in the sequence by computing
        # the sum of the previous two numbers in the sequence.
        next_number = numbers[index - 1] + numbers[index - 2]

        # Take the item in the parentheses and add it to the
        # end of the list referenced by 'numbers'.

        # The .append() method is a function, but it is categorized
        # as a method because it belongs to a list object.

        # In this case, 'numbers' references the list object.
        numbers.append(next_number)

    # Send the list referenced by 'numbers' back to where this
    # fibonacci() function was called.
    return numbers

print(f"fibonacci({5}): {fibonacci(5)}")