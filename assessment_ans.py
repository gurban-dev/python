# In Python, which function do you use to display text and numbers?
print("Hello, world!\n")

# Which keyword do you use to start a function definition?
# def

def greet(first_name, last_name):
    return f"Hello {first_name} {last_name}!\n"

print(greet(first_name="Alexander", last_name="Hamilton"))

# What does the print() function return?
# The print() function returns None.


# What is the name of the standard tool for installing third-party
# Python packages?
# pip (Stands for Pip Installs Packages)

# The name is a recursive acronym, meaning the word itself is used
# inside its own definition.


# Complete the following sentence with the below choices.

# The below choices are limited to the first blank line:
# index, element, number

# In a Python for loop, the loop variable takes each _ from an
# _.

# The below choices are limited to the second blank line:
# boolean, integer, iterable

# In a Python for loop, the loop variable takes each element
# from an iterable.

# Indices:
#       0  1  2  3  4
nums = [1, 2, 3, 4, 5]

# The loop variable 'num' is assigned the elements:
# 1, 2, 3, 4, 5

for num in nums:
    print("num:", num)
print()

# Indices:
#              01234
for letter in "abcde":
    print("letter:", letter)
print()

# Define the correct terms that were used to complete the above
# sentence.

# An element is a single item stored inside a collection that
# can store multiple items.

# An iterable is an object that is capable of returning its
# elements one by one.


# Name a built-in data type that is mutable and one that is
# immutable.

# Mutable: A list
portfolio_projections = [10_500, 11_025, 11_576]

# Valid since lists can be mutated.
portfolio_projections[2] = 11_842

# Immutable: A tuple
date_of_birth = (29, 5, 1917)

# Invalid since tuples cannot be mutated.
try:
    date_of_birth[2] = 1917
except TypeError as err:
    print("Error:", err)

# Which of the following statement are true about dictionaries?
# a. Dictionary keys must be hashable.
# b. A dictionary is automatically sorted by its keys.
# c. Insertion order is preserved.
# d. Dictionary values must be unique.
# e. Dictionary items are accessed by their numeric index.

# Choices a. and c. are correct.

# a. Dictionary keys must be hashable because Python uses their hash values
#    to efficiently store and retrieve dictionary entries. Immutable types
#    such as strings and integers are hashable, while lists are not.

# c. Insertion order is preserved because Python dictionaries maintain
#    entries in the order they were inserted. When iterating over a
#    dictionary, the entries appear in that order unless they are deleted
#    and reinserted.

date_of_birth = {
    # key: value
    "day": 9,
    "month": 9,
    "year": 1917
}

print("\ndate_of_birth[\"year\"]:", date_of_birth["year"])


# numbers = range(5)

# Given the above variable, write a list comprehension that
# generates the following result:
# [0, 1, 4, 9, 16]

# Predict the output of each.

print("\n5 == \"5.0\":", 5 == "5.0", "\n")

print("5 == 5.0:", 5 == 5.0, "\n")

try:
    print("5 > \"5.0\":", 5 > "5.0", "\n")
except TypeError:
    print("The greater-than sign cannot be used to compare "
          "a numeric\ntype and a text type.\n")

print("5 > 5.0:", 5 > 5.0, "\n")