# Python List Exercise Solution: Fruits

# Create the list.
# 'fruits' holds a reference to the list object that exists
# in memory.
# Indexes:
#         0 or -5   1 or -4   2 or -3  3 or -2   4 or -1
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Print the first fruit.
print("First fruit:", fruits[0])

# Print the last fruit.
print("Last fruit:", fruits[-1])

# Print all fruits using a for loop.
print("\nAll fruits in the list:")
for fruit in fruits:
  print(fruit)

# Check if the first fruit is "apple".
if fruits[0] == "apple":
  print("The first fruit is apple!")
else:
  print("The first fruit is not apple.")

# Lists are mutable. Changing the first fruit.
fruits[0] = "kiwi"

print("\nAfter changing the first fruit:")

if fruits[0] == "apple":
  print("The first fruit is apple!")
else:
  print("The first fruit is not apple.")