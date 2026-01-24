# A tuple of course names (fixed, cannot be changed).
courses = ("Python", "SQL", "Statistics", "Business Analytics")

# A list of students (can be updated).
students = ["Sara", "Alex", "Jamal", "Priya"]

# A dictionary showing which courses each student has completed.
completed_courses = {
  "Sara": {"Python", "SQL"},
  "Alex": {"Python"},
  "Jamal": {"SQL", "Statistics"},
  "Priya": {"Python", "SQL", "Statistics"}
}

print("TASK 1: TUPLES")

# Print the first course in the tuple.
print("First course:", courses[0])

# Print the last course in the tuple.
print("Last course:", courses[-1])

# Try to change a course in the tuple (this will fail).
try:
  courses[0] = "Java"
except TypeError as e:
  print("Cannot modify tuple:", e)

print("\nTASK 2: LISTS")

# Add a new student to the list.
students.append("Lina")

# Remove a student from the list.
students.remove("Alex")

# Show the updated list of students.
print("Updated students list:", students)

print("\nTASK 3: DICTIONARIES + FOR LOOP")

# Loop through each student and print their completed courses.
for student, course_set in completed_courses.items():
  course_list = ", ".join(course_set)
  print(f"{student} has completed: {course_list}")

  # Print how many courses each student has completed.
  print(f"{student} has completed {len(course_set)} courses.")

print("\nTASK 4: SETS")

# Convert the tuple of courses to a set to make comparisons easier.
all_courses_set = set(courses)

# Check for each student if they completed all courses or not.
for student, course_set in completed_courses.items():
  if course_set == all_courses_set:
    print(f"{student} has completed all courses.")
  else:
    # Show which courses the student is missing.
    
    missing = all_courses_set - course_set

    print(f"{student} is missing: {', '.join(missing)}")

print("\nTASK 5: ILLEGAL OPERATIONS")

# Trying to access a set by index (not allowed).
try:
  completed_courses["Sara"][0]
except TypeError as e:
  print("Cannot index into a set:", e)

# Trying to append to a set (not allowed).
try:
  completed_courses["Alex"].append("SQL")
except AttributeError as e:
  print("Cannot append to a set:", e)

# Trying to use a string key on a list (not allowed).
try:
  students["Sara"] = "Advanced"
except TypeError as e:
  print("Cannot use string key on list:", e)

print("\nOPTIONAL EXTENSION")

# Find all courses that students have completed.
all_completed = set()

for course_set in completed_courses.values():
  all_completed |= course_set  # Union with existing completed courses.

# Find courses that no one has completed
never_completed = all_courses_set - all_completed

# Print courses that no student has completed.
if never_completed:
  print("Courses never completed by any student:", ", ".join(never_completed))
else:
  print("Every course has been completed by at least one student")

# Add the new student Lina with no completed courses yet.
completed_courses["Lina"] = set()

# Show the final dictionary of completed courses.
print("\nFinal completed_courses dictionary:")
print(completed_courses)