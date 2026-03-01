# Write a continuous program where the user keeps entering
# a number and the program calculates the square root.

# The program exits when the user presses the spacebar.

# Inform the user how to exit the program.
print('Enter spacebar to exit')

# Infinite loop so the program keeps running
# until a break statement is encountered.
while (1):

    # Prompt the user to enter a value.
    a = input("Enter the number: ")

    # Display whether the input consists only of whitespace.
    print("\na.isspace():", a.isspace(), '\n')

    # If the user entered only whitespace (e.g., pressed spacebar),
    # exit the loop and end the program.
    if a.isspace():
        break

    # Convert the input string to an integer.
    n = int(a)

    # Check if the number is non-negative.
    if (n >= 0):
        # Calculate and display the square root.
        print(f'The square root of the number is {n**(0.5)}.')
    else:
        # Handle negative numbers.
        print('The number entered is negative.\n')