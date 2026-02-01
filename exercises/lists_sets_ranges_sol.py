"""
Python Fundamentals Exercise Solution
Covers:
- Lists and sets
- Equality and not-equal operators
- range() with start, stop, step
- Iteration and conditionals
- __name__ dunder variable
"""

# ---------------- PART 1: Lists ----------------

def work_with_lists():
  # 1. Create a list of numbers from 1 to 1000
  numbers = list(range(1, 1001))

  # 2. Print the entire list
  print("Numbers list:")
  print(numbers)

  # 3. Loop through the list and check for 5
  for num in numbers:
    print(num)

    if num != 5:
      print(f"{num} is not 5")
    else:
      print("Found 5!")

  # 4. Create a list of even numbers
  even_numbers = []

  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)

  print("Even numbers:")
  print(even_numbers)

  return even_numbers


# ---------------- PART 2: range() ----------------

def work_with_ranges():
  # 5. Numbers from 0 to 20 (inclusive)
  print("Range 0 to 20:")
  for num in range(0, 21):
    print(num)

  # 6. Odd numbers from 1 to 20
  odd_numbers = list(range(1, 21, 2))
  print("Odd numbers from 1 to 20:")
  print(odd_numbers)

  # 7. Count backwards from 10 to 0
  print("Counting backwards from 10 to 0:")
  for num in range(10, -1, -1):
    print(num)

  return odd_numbers


# ---------------- PART 3: Sets ----------------

def work_with_sets():
  # 8. List with duplicates
  duplicate_numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
  print("Duplicate numbers list:")
  print(duplicate_numbers)

  # 9. Convert list to set
  unique_numbers = set(duplicate_numbers)
  print("Unique numbers set:")
  print(unique_numbers)

  # 10. Loop through the set
  for num in unique_numbers:
    if num != 3:
      print(f"{num} is not 3")
    else:
      print("Found the number 3!")

  # Convert back to list (extra practice)
  unique_list = list(unique_numbers)
  print("Set converted back to list:")
  print(unique_list)

  return unique_list


# ---------------- PART 4: Equality vs Not Equality ----------------

def user_input_logic():
  user_numbers = []

  # 11. Ask user for input
  user_value = int(input("Enter a number: "))

  # 12. Compare to 10
  if user_value == 10:
    print("You entered 10.")
  else:
    print("This is not 10.")

  # 13. Check for duplicates
  if user_value in user_numbers:
    print("Duplicate detected.")
  else:
    user_numbers.append(user_value)
    print("Updated user_numbers list:")
    print(user_numbers)

  return user_numbers


# ---------------- PART 5: __name__ ----------------

def main():
  """Main function that runs all parts of the exercise."""
  work_with_lists()
  work_with_ranges()
  work_with_sets()
  user_input_logic()


# This block runs ONLY when the script is executed directly.
if __name__ == "__main__":
  print("This script is being run directly.")
  main()
# This line runs ONLY when the file is imported as a module.
else:
  print("This code was imported as a module.")