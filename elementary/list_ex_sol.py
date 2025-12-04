# Python List Exercise Solution: Fruits

# Create the list.
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Print the first fruit.
print("First fruit:", fruits[0])

# Print the last fruit.

print("Last fruit:", fruits[-1])

# Print all fruits using a for loop.

print("All fruits in the list:")
for fruit in fruits:
  print(fruit)

# Check if the first fruit is "apple".
if fruits[0] == "apple":
  print("The first fruit is apple!")
else:
  print("The first fruit is not apple.")

# Changing the first fruit.
fruits[0] = "kiwi"

print("\nAfter changing the first fruit:")

if fruits[0] == "apple":
  print("The first fruit is apple!")
else:
  print("The first fruit is not apple.")