iteration_count = 0

# The outer for loop will loop two times.
for outer in range(2):
    print("outer:", outer)

    # The inner for loop will loop two times for each of the
    # outer loop's iterations.
    for inner in range(1):
        print("inner:", inner)

        iteration_count += 1

    # For the following print statement to be executed on each
    # iteration in the outer loop, it must be indented four
    # spaces to the right of the start of the outer for loop
    # statement.   
    print(f'Outer for loop completed iteration {outer}.\n')

# To determine how many total iterations there are, multiply
# the number of iterations that the outer loop will have by
# the number of iterations that the inner loop will have.

# The total number of iterations:
# 2 * 1 -> 2

print("iteration_count:", iteration_count)