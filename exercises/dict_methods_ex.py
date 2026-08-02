# Concepts:
# Dictionaries
# Dictionary methods
# Loops
# Conditionals

# A dictionary stores students and their exam grades.
students = {
    "alice": 95,
    "bob": 82,
    "charlie": 91,
    "diana": 88
}

# Requirements
# Display the following menu until the user chooses to quit:
# 1. View all students
# 2. Search for a student
# 3. Update a grade
# 4. Show class statistics
# 5. Quit

# Menu option 1
# The student and their grades should be printed in alphabetical order.

# Example:
# Alice: 95
# Bob: 82
# Charlie: 91

# Menu option 2
# Ask the user for the student's name.

# If the student exists:
# Charlie's grade is 91.

# Use the dictionary method .get().

# Otherwise:
# <student_name> not found.

# Menu option 3
# Ask the user for the student's name.

# If the student exists, replace their grade.

# Otherwise:
# Add the student to the dictionary.

# Menu option 4
# Display the:
# • Number of students
# • Average grade
# • Highest grade
# • Lowest grade
# • Honour Roll (student with grades of 90 or above)

# Use the following:
# .values()
# .items()
# sum()
# len()

# Menu Option 5
# Exit the program.