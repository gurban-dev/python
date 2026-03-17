def fibonacci():
    # Initialise the first two numbers in the Fibonacci sequence.
    current_num = 0
    next_num = 1

    # Create an infinite loop so the generator can
    # produce values on demand.
    while True:
        # Yield the current Fibonacci number and
        # pause the function's execution.
        yield current_num

        # Update both variables simultaneously:
        # - current_num becomes the old next_num
        # - next_num becomes the sum of the previous two numbers
        #
        # This tuple assignment avoids needing temporary variables.
        current_num, next_num = next_num, current_num + next_num


# Ask the user how many Fibonacci numbers to generate.
quantity = int(
    input(
        "How many numbers of the fibonacci sequence would "
        "you like to print?\n"
    )
)

# Calling fibonacci() does NOT run the function immediately.
# It returns a generator object instead.
fib = fibonacci()

# Show that fib is a generator.
print("\ntype(fib):", type(fib))

print("\nThe first", quantity, "fibonacci numbers:")

# Each call to next(fib) resumes execution of the generator
# until it reaches the next yield statement.
for i in range(quantity):
    print(next(fib), end=" ")

print()