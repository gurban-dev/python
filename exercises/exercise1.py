'''
This exercise covers for loops, while loops, data type
conversion, if-elif-else conditionals, and understanding
truthy and falsy values in Python.

Write a Python program that does the following:

Ask the user to input a list of values separated by commas.
The values could be numbers (integers/floats) or strings.

user_input = input("Enter a list of values separated by commas: ")
values = user_input.split(",")

Loop through each value in the list using a for loop:

Strip any extra spaces from the value.

If the value can be converted to an integer, convert it to int.

If the value can be converted to a float, convert it to float.

Otherwise, leave it as a string.

After creating the processed list, use a while loop to iterate
through the list and analyze each element:

If the element is an integer:
Print whether it is even or odd.

Print whether it is truthy or falsy (remember, 0 is falsy).

If the element is a float:
Print whether it is positive, negative, or zero.

Print whether it is truthy or falsy (remember, 0.0 is falsy).

If the element is a string:
Print whether it is empty or non-empty.

Print whether it is truthy or falsy (empty strings are falsy).

E.g.
Input:
0, 3.5, -2, hello, "", 0.0

Output:
0 is an integer and it is even and falsy.
3.5 is a float and it is positive and truthy.
-2 is an integer and it is even and truthy.
'hello' is a string and it is non-empty and truthy.
'' is a string and it is empty and falsy.
0.0 is a float and it is zero and falsy.
'''