def calculate_average(scores):
	print("DEBUG: calculating average for scores:", scores)

	return sum(scores) / len(scores)

def assign_grade(avg):
	if avg >= 90:
		return "A"
	elif avg >= 80:
		return "B"
	elif avg >= 70:
		return "C"
	elif avg >= 60:
		return "D"
	else:
		return "F"

# Student data (BUG: one student has a string instead of a number)
students = {
	"Alice": [95, 87, 92],
	"Bob": [78, 82, 85],

	# Generates a bug.
	"Charlie": [100, "ninety", 95]
}

for name, scores in students.items():
	print("DEBUG: processing", name)

	print("DEBUG: raw scores =", scores)

	# Throw an error.
	avg = calculate_average(scores)

	print("DEBUG: average =", avg)

	grade = assign_grade(avg)

	print("DEBUG: grade =", grade)