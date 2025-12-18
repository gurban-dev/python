# 1. Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

# 2. Print the first 5 numbers
print("First 5 numbers:", numbers[:5])

# 3. Create a list with different data types
mixed_list = [7, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# 4. Ask the user for a number
user_input = int(input("Enter a number: "))

# 5. Check if the number is in the list
if user_input in numbers:
  print("That number is in the list!")
else:
  print("That number is NOT in the list.")

# 6. Add the user’s number to the list
numbers.append(user_input)

# 7. Print the updated list length
print("Updated length of numbers list:", len(numbers))

# 8. Print even numbers
print("Even numbers:")
for num in numbers:
  if num % 2 == 0:
    print(num, end=" ")

# 9. Print the type of each element in mixed_list.
print("\nTypes in mixed_list:")
for item in mixed_list:
  print(item, "->", type(item))