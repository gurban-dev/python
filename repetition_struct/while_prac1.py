# Non-entry controlled while loop:
# while True:

# The following is an entry-controlled while loop because
# the condition written in the while statement can potentially
# become False.

n = 5

# While the variable 'n' is greater than zero, the
# the block of source code will be repeatedly executed. 
while n > 0:
    # The following two lines have the same effect.
    # n = n + 1
    n += 1

    if n == 7:
        # Skip the current iteration of the while loop and
        # move on to the next. This means that the remaining
        # lines of source code (24, 27, 29, 30, 31 and 34)
        # will not be executed on this iteration.
        continue

    if n == 10:
        # The below line will terminate the while loop and
        # will have the flow of the program jump to line 39.
        break

    if n != 9:
        print(n, end=', ')
    else:
        # The two instructions below are written differently,
        # but produce the same outcome.
        print(n, end='\n')
        # print(n)

# How is it known that line 39 is not part of the body of
# the while loop?
print("\nWhile loop ended.")