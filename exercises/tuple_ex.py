'''
Exercise 3

Write a program that:

Starts with a list of tuples, where each tuple
represents a students_dict's name and grade.

Example:

students = [("Alice", 85), ("Bob", 90), ("Charlie", 72), ("Diana", 95)]

Converts this list into a dictionary where the students_dict's
name is the key and the grade is the value.

Adds a new students_dict "Eve" with a grade of 88.

Updates "Charlie"'s grade to 80.

Prints:

The students_dict with the highest grade

The students_dict with the lowest grade

The class average

💡 Hint: You'll need max(), min(), and sum() with .values() for the dictionary.
'''

def student_grade():
	student_input = input("Enter the list of students separated by commas:\n")

	grade_input = input("\nEnter the grades of the students separated by commas:\n")

	student_list = student_input.strip().split(",")
	grade_list = grade_input.split(",")

	# Cast each grade as a float.
	grade_list = [float(grade) for grade in grade_list]

	students = tuple(zip(student_list, grade_list))

	students_dict = dict(students)

	print('\nstudents_dict:\n', students_dict, sep="")

	# Adding a new students_dict to the dictionary 
	new_name = input("\nEnter the name of the students_dict to be added: ")
	new_grade = float(input("\nEnter the students_dict's grade: "))

	students_dict[new_name] = new_grade

	print('\nstudents_dict:\n', students_dict, sep="")

	# Changing the existing students_dict's grade.
	change_name = input(
		"\nEnter the name of the students_dict " \
		"whose grade has to be changed: ")

	change_grade = float(input("Enter the new grade: "))
	students_dict[change_name] = change_grade

	print('\nstudents_dict:\n', students_dict, end="")

	# Finding the highest grade, lowest grade, and the average.

	# The .values() method returns a dict_values view object.
	# It is not indexable/subscriptable like a Python list.
	values_lst = list(students_dict.values())
	highest = values_lst[0]
	highest_name = ''

	lowest = values_lst[0]
	lowest_name = ''
	c = 0
	s = 0

	print('students_dict.values():', students_dict.values())

	while c < len(students_dict):
		if highest < students_dict.values[c]:
			highest = students_dict.values[c]
			highest_name = students_dict.keys[c]

		if lowest > students_dict.values[c]:
			lowest = students_dict.values[c]
			lowest_name = students_dict.keys[c]
			
		s += students_dict.values[c]
		c += 1

	print(f"\nHighest grade: {highest} by {highest_name}")
	print(f"Lowest grade: {lowest} by {lowest_name}")
	print(f"Average: {s/len(students_dict)}")

student_grade()