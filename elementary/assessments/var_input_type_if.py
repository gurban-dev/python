# Assessment:

# In Visual Studio Code please write a Python program that:
# 1. Prompts the user to enter their name.

# 2. Stores the result in a variable called 'name'.

# 3. Prints the data type of 'name'.

# 4. Prints the number of characters in 'name'.

# 5. If the user entered nothing, print:
#    You entered an empty string.

# Solution:

# Prompt the user to enter their name.
# The input() function always returns a string.
name = input("Enter your name: ")

# Display the data type of the value stored in 'name'.
print(f"Data type: {type(name)}")

# Display the total number of characters in the string.
# The len() function counts every character, including spaces.
print(f"Number of characters: {len(name)}")

# Check whether the user entered an empty string.
# An empty string has a length of 0.
if len(name) == 0:
    print("You entered an empty string.")