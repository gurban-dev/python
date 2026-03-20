# Prompt the user to input a value.
prompt_msg = "Enter a value: "

# Notice how the above line is not included in the try block
# because there isn't a possibility that it would raise an
# exception.

try:
    # Attempt to convert the input to an integer.
    num = int(input(prompt_msg))

    # Display the converted integer if successful.
    print("\nYou entered the integer:", num)

    # The print statement is inside this try block because it depends on
    # 'num' being successfully assigned; if the conversion fails, 'num'
    # does not exist, and placing the print statement outside the try
    # block would cause another exception.

# Catch a ValueError if the input cannot be converted to an integer.
except ValueError as err:
    # Inform the user that the input was invalid.
    print(f"\nException raised: {err}")

print()

# Prompt the user again without exception handling.
num = int(input(prompt_msg))

# This demonstrates that when an exception is rasied and not caught,
# a Python program ceases to continue. Whereas when an exception is
# caught with a try / except block, the program continues to the next
# lines of source code.
print("\nProgram continued!")